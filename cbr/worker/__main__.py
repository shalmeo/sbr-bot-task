import asyncio
import logging
import os
from asyncio import CancelledError

from aiohttp import ClientSession
from redis.asyncio import Redis

from cbr.application.usecases.update_currencies import UpdateCurrencies
from cbr.infrastructure.database.redis.gateway import CurrencyGateway


async def run_worker(redis_client: Redis, client_session: ClientSession) -> None:
    while True:
        await UpdateCurrencies(
            currency_gateway=CurrencyGateway(redis_client=redis_client),
            client_session=client_session,
        ).execute()

        await asyncio.sleep(60 * 60 * 24)  # 24 hours


async def main() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s  %(process)-7s %(module)-20s %(message)s",
    )

    redis_client = Redis.from_url(os.getenv("REDIS_URI"))
    client_session = ClientSession()

    try:
        await run_worker(redis_client=redis_client, client_session=client_session)
    finally:
        await redis_client.aclose()
        await client_session.close()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, CancelledError):
        logging.info("Worker stopped")

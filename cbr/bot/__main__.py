import asyncio
import os

from aiogram import Bot, Dispatcher
from redis.asyncio import Redis

from cbr.application.usecases.exchange_currency import ExchangeCurrency
from cbr.application.usecases.get_currencies import GetCurrencies
from cbr.bot import handlers
from cbr.infrastructure.database.redis.gateway import CurrencyGateway


async def main() -> None:
    bot = Bot(os.getenv("BOT_TOKEN"))
    dispatcher = Dispatcher()
    redis_client = Redis.from_url(os.getenv("REDIS_URI"))

    dispatcher.include_router(handlers.router)

    try:
        await dispatcher.start_polling(
            bot,
            exchange_currency=ExchangeCurrency(CurrencyGateway(redis_client)),
            get_currencies=GetCurrencies(
                CurrencyGateway(redis_client),
            ),
        )
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(main())

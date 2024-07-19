import json

from redis.asyncio import Redis

from cbr.application.dto.currency import Currency


class CurrencyGateway:
    def __init__(self, redis_client: Redis):
        self._redis_client = redis_client

    async def add_currency(self, id: str, name: str, value: float) -> None:
        await self._redis_client.hset(
            "currencies",
            id,
            json.dumps(
                {
                    "id": id,
                    "name": name,
                    "value": value,
                }
            ),
        )

    async def get_currency_by_id(self, id: str) -> Currency:
        currency = await self._redis_client.hget("currencies", id)

        return Currency(**json.loads(currency))

    async def get_currencies(self) -> list[Currency]:
        currencies = await self._redis_client.hgetall("currencies")
        return [Currency(**json.loads(currency)) for currency in currencies.values()]

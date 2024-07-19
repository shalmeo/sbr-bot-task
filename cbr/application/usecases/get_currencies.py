from cbr.infrastructure.database.redis.gateway import CurrencyGateway


class GetCurrencies:
    def __init__(self, currency_gateway: CurrencyGateway):
        self._currency_gateway = currency_gateway

    async def execute(self):
        return await self._currency_gateway.get_currencies()

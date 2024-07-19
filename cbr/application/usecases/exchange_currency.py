from cbr.infrastructure.database.redis.gateway import CurrencyGateway


class ExchangeCurrency:
    def __init__(self, currency_gatway: CurrencyGateway) -> None:
        self._currency_gateway = currency_gatway

    async def execute(self, from_currency: str, quantity: float) -> float:
        currency = await self._currency_gateway.get_currency_by_id(from_currency)

        return currency.value * quantity

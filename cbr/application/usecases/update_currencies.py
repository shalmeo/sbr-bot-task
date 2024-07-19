import logging
from aiohttp import ClientSession

from cbr.infrastructure.cbr.parser import fetch_currency_xml, parse_currency_xml
from cbr.infrastructure.database.redis.gateway import CurrencyGateway

logger = logging.getLogger(__name__)


class UpdateCurrencies:
    def __init__(
        self, currency_gateway: CurrencyGateway, client_session: ClientSession
    ):
        self._currency_gateway = currency_gateway
        self._client_session = client_session

    async def execute(self) -> None:
        currency_xml = await fetch_currency_xml(
            self._client_session, "https://cbr.ru/scripts/XML_daily.asp"
        )
        currencies = parse_currency_xml(currency_xml)

        for currency in currencies:
            await self._currency_gateway.add_currency(
                id=currency.id,
                name=currency.name,
                value=currency.value,
            )

        logger.info("Currencies updated - %s", len(currencies))

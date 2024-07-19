from dataclasses import dataclass

from aiohttp import ClientSession
from xml.etree import ElementTree

from cbr.application.dto.currency import Currency


async def fetch_currency_xml(http_client: ClientSession, url: str) -> str:
    async with http_client.get(url) as response:
        return await response.text()


def parse_currency_xml(currency_xml: str) -> list[Currency]:
    tree = ElementTree.fromstring(currency_xml)
    currencies = []
    for currency in tree.findall(".//Valute"):
        name = currency.find("Name").text
        char_code = currency.find("CharCode").text
        value = currency.find("Value").text
        currencies.append(
            Currency(
                id=char_code,
                name=name,
                value=float(value.replace(",", ".")),
            )
        )

    return currencies

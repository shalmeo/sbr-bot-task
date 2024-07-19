import re

from aiogram import Router
from aiogram.filters import Command, CommandObject
from aiogram.types import Message

from cbr.application.usecases.exchange_currency import ExchangeCurrency
from cbr.application.usecases.get_currencies import GetCurrencies

router = Router()


@router.message(Command("exchange"))
async def exchange(
    message: Message, command: CommandObject, exchange_currency: ExchangeCurrency
) -> None:
    pattern = re.compile(r"(\w{3})\s*(\w{3})\s*(\d+)")

    if not pattern.match(command.args):
        await message.answer("Invalid command format. Example: /exchange USD RUB 100")

    from_currency, to_currency, quantity = command.args.split()
    result = await exchange_currency.execute(from_currency, float(quantity))
    await message.answer(str(result))


@router.message(Command("rates"))
async def rates(message: Message, get_currencies: GetCurrencies) -> None:
    currencies = await get_currencies.execute()

    response = "\n".join(
        f"{currency.name} ({currency.id}): {currency.value}" for currency in currencies
    )

    await message.answer(response)

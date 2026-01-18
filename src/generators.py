from typing import Any, Generator


def filter_by_currency(transactions: list[dict], statute: str) -> Generator[Any, None]:
    """Функцию, которая принимает на вход список транзакции и возвращает поочередно транзакции,
    где валюта операции соответствует заданной."""

    result = filter(lambda x: x["operationAmount"]["currency"]["code"] == statute, transactions)
    for transaction in result:
        yield transaction


def transaction_descriptions(transactions: list[dict]) -> Generator[Any, None]:
    """Функция, которая принимает список словарей с транзакциями и
    возвращает описание каждой операции по очереди."""

    description = list((x["description"] for x in transactions))
    for name_transact in description:
        yield name_transact


def card_number_generator(start: int, finish: int) -> Any:
    """ Функция, которая выдает номера банковских карт в формате XXXX ХХХХ ХХХХХ,
     где X — цифра номера карты. Функция должна принимать начальное
    и конечное значения для генерации диапазона номеров."""

    for num in range(start, finish + 1):
        count_symbol_num = len(str(num))
        card_num = ('0' * (16 - count_symbol_num)) + str(num)

        a = card_num[:4] + ' '
        b = card_num[4:8] + ' '
        c = card_num[8:12] + ' '
        d = card_num[12:]

        card_by_format = a + b + c + d

        yield card_by_format

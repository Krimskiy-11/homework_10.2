import re
from collections import defaultdict


def process_bank_search(data:list[dict], search:str)->list[dict]:
    """ Функцию, которая будет принимать список словарей с данными о
    банковских операциях и строку поиска, а возвращать список словарей,
    у которых в описании есть данная строка. """

    lst_search = []
    for transaction in data:
        if transaction['description']:
            if re.search(search, transaction['description'], flags=re.IGNORECASE):
                lst_search.append(transaction)
    return lst_search


def process_bank_operations(data:list[dict], categories: list)->dict:
    """ Функцию, которая будет принимать список словарей с данными о банковских операциях
     и список категорий операций, а возвращать словарь, в котором ключи — это названия категорий,
     а значения — это количество операций в каждой категории."""

    result_dict = defaultdict(int)
    all_descriptions = [transaction['description'] for transaction in data]
    for description in all_descriptions:
        if description in categories:
            result_dict[description] += 1
    return dict(result_dict)

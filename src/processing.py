from typing import Any


def filter_by_state(my_lists: list[dict], state: str = "EXECUTED") -> Any:
    """Функция возвращает новый список словарей, содержащий словари,
    у которых state соответствует указанному значению"""

    if isinstance(my_lists, list):
        if my_lists != [{}]:
            result_list = list()

            for i in my_lists:
                if i["state"] == state:
                    result_list.append(i)

            return result_list
        else:
            return "Incorrect data entry"
    return "Incorrect data entry"


def sort_by_date(my_lists: list[dict], reverse: bool = True) -> Any:
    """Функция возвращает новый список словарей, отсортированный по дате"""

    if isinstance(my_lists, list):
        if my_lists != [{}]:
            sorted_dict = sorted(my_lists, key=lambda i: i["date"], reverse=reverse)
            return sorted_dict
        else:
            return "Incorrect data entry"
    return "Incorrect data entry"

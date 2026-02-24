import src.import_data
import src.services
import src.utils
from src.widget import get_date, mask_account_card


def main():
    """Функция, которая отвечает за основную логику
    проекта и связывает функциональности между собой."""

    file_selection = input(
        "Привет! Добро пожаловать в программу работы с банковскими транзакциями.\n"
        "Выберите необходимый пункт меню:\n"
        "1. Получить информацию о транзакциях из JSON-файла\n"
        "2. Получить информацию о транзакциях из CSV-файла\n"
        "3. Получить информацию о транзакциях из XLSX-файла\n"
    )
    if file_selection:
        if file_selection.lower() == "1":
            print("Для обработки выбран JSON-файл.\n")
            json_transact = src.utils.get_transactions("operations.json")
            filter_status = input(
                "Введите статус, по которому необходимо выполнить фильтрацию.\n"
                "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n"
            )
            if filter_status:
                if filter_status.upper() == "EXECUTED":
                    executed_list = [
                        transact for transact in json_transact for k, v in transact.items() if v == "EXECUTED"
                    ]
                    sort_date = input("Отсортировать операции по дате?\n" "Да/Нет\n")
                    if sort_date:
                        if sort_date.lower() == "да":
                            sorted_date_list = sorted(executed_list, key=lambda x: x["date"])
                            sorting_order = input("Отсортировать по возрастанию или по убыванию?\n")
                            if sorting_order:
                                if sorting_order.lower() == "по возрастанию":
                                    ascending_sort = sorted(sorted_date_list, key=lambda x: x["date"], reverse=False)
                                    only_RUB_transact = input("Выводить только рублевые транзакции?\n" "Да/Нет\n")
                                    if only_RUB_transact:
                                        if only_RUB_transact.lower() == "да":
                                            RUB_transact = [
                                                x
                                                for x in ascending_sort
                                                if x["operationAmount"]["currency"]["code"] == "RUB"
                                            ]
                                            search_word = input(
                                                "Отфильтровать список транзакций по определенному слову в описании?\n"
                                                "Да/Нет\n"
                                            )
                                            if search_word:
                                                if search_word.lower() == "да":
                                                    my_search_word = input("Введите ключевое слово:\n")
                                                    search_transact = src.services.process_bank_search(
                                                        RUB_transact, my_search_word
                                                    )
                                                    print("Распечатываю итоговый список транзакций...\n")
                                                    print(
                                                        f"Всего банковских операций в выборке:{len(search_transact)}\n"
                                                    )
                                                    for x in search_transact:
                                                        date_and_description = (
                                                            f'{get_date(x['date'])} {x["description"]}\n'
                                                        )
                                                        amount_and_name = f'Сумма: {x["operationAmount"]["amount"]} {x["operationAmount"]["currency"]["name"]}\n'
                                                        if x["description"] == "Открытие вклада":
                                                            from_to = f"{mask_account_card(x['to'])}\n"
                                                        else:
                                                            from_to = f"{mask_account_card(x['from'])} -> {mask_account_card(x['to'])}\n"
                                                        print(
                                                            f"{date_and_description}" f"{from_to}" f"{amount_and_name}"
                                                        )
                                                elif search_word.lower() == "нет":
                                                    print("Распечатываю итоговый список транзакций...\n")
                                                    print(f"Всего банковских операций в выборке:{len(RUB_transact)}\n")
                                                    for x in RUB_transact:
                                                        date_and_description = (
                                                            f'{get_date(x['date'])} {x["description"]}\n'
                                                        )
                                                        amount_and_name = f'Сумма: {x["operationAmount"]["amount"]} {x["operationAmount"]["currency"]["name"]}\n'
                                                        if x["description"] == "Открытие вклада":
                                                            from_to = f"{mask_account_card(x['to'])}\n"
                                                        else:
                                                            from_to = f"{mask_account_card(x['from'])} -> {mask_account_card(x['to'])}\n"
                                                        print(
                                                            f"{date_and_description}" f"{from_to}" f"{amount_and_name}"
                                                        )
                                                else:
                                                    return "Некорректный ввод"
                                            else:
                                                return "Некорректный ввод"
                                        elif only_RUB_transact.lower() == "нет":
                                            search_word = input(
                                                "Отфильтровать список транзакций по определенному слову в описании?\n"
                                                "Да/Нет\n"
                                            )
                                            if search_word:
                                                if search_word.lower() == "да":
                                                    my_search_word = input("Введите ключевое слово:\n")
                                                    search_transact = src.services.process_bank_search(
                                                        ascending_sort, my_search_word
                                                    )
                                                    print("Распечатываю итоговый список транзакций...\n")
                                                    print(
                                                        f"Всего банковских операций в выборке:{len(search_transact)}\n"
                                                    )
                                                    for x in search_transact:
                                                        date_and_description = (
                                                            f'{get_date(x['date'])} {x["description"]}\n'
                                                        )
                                                        amount_and_name = f'Сумма: {x["operationAmount"]["amount"]} {x["operationAmount"]["currency"]["name"]}\n'
                                                        if x["description"] == "Открытие вклада":
                                                            from_to = f"{mask_account_card(x['to'])}\n"
                                                        else:
                                                            from_to = f"{mask_account_card(x['from'])} -> {mask_account_card(x['to'])}\n"
                                                        print(
                                                            f"{date_and_description}" f"{from_to}" f"{amount_and_name}"
                                                        )
                                                elif search_word.lower() == "нет":
                                                    print("Распечатываю итоговый список транзакций...\n")
                                                    print(
                                                        f"Всего банковских операций в выборке:{len(ascending_sort)}\n"
                                                    )
                                                    for x in ascending_sort:
                                                        date_and_description = (
                                                            f'{get_date(x['date'])} {x["description"]}\n'
                                                        )
                                                        amount_and_name = f'Сумма: {x["operationAmount"]["amount"]} {x["operationAmount"]["currency"]["name"]}\n'
                                                        if x["description"] == "Открытие вклада":
                                                            from_to = f"{mask_account_card(x['to'])}\n"
                                                        else:
                                                            from_to = f"{mask_account_card(x['from'])} -> {mask_account_card(x['to'])}\n"
                                                        print(
                                                            f"{date_and_description}" f"{from_to}" f"{amount_and_name}"
                                                        )
                                                else:
                                                    return "Некорректный ввод"
                                            else:
                                                return "Некорректный ввод"
                                        else:
                                            return "Некорректный ввод"
                                    else:
                                        return "Некорректный ввод"
                                elif sorting_order.lower() == "по убыванию":
                                    ascending_sort = sorted(sorted_date_list, key=lambda x: x["date"], reverse=True)
                                    only_RUB_transact = input("Выводить только рублевые транзакции?\n" "Да/Нет\n")
                                    if only_RUB_transact:
                                        if only_RUB_transact.lower() == "да":
                                            RUB_transact = [
                                                x
                                                for x in ascending_sort
                                                if x["operationAmount"]["currency"]["code"] == "RUB"
                                            ]
                                            search_word = input(
                                                "Отфильтровать список транзакций по определенному слову в описании?\n"
                                                "Да/Нет\n"
                                            )
                                            if search_word:
                                                if search_word.lower() == "да":
                                                    my_search_word = input("Введите ключевое слово:\n")
                                                    search_transact = src.services.process_bank_search(
                                                        RUB_transact, my_search_word
                                                    )
                                                    print("Распечатываю итоговый список транзакций...\n")
                                                    print(
                                                        f"Всего банковских операций в выборке:{len(search_transact)}\n"
                                                    )
                                                    for x in search_transact:
                                                        date_and_description = (
                                                            f'{get_date(x['date'])} {x["description"]}\n'
                                                        )
                                                        amount_and_name = f'Сумма: {x["operationAmount"]["amount"]} {x["operationAmount"]["currency"]["name"]}\n'
                                                        if x["description"] == "Открытие вклада":
                                                            from_to = f"{mask_account_card(x['to'])}\n"
                                                        else:
                                                            from_to = f"{mask_account_card(x['from'])} -> {mask_account_card(x['to'])}\n"
                                                        print(
                                                            f"{date_and_description}" f"{from_to}" f"{amount_and_name}"
                                                        )
                                                elif search_word.lower() == "нет":
                                                    print("Распечатываю итоговый список транзакций...\n")
                                                    print(f"Всего банковских операций в выборке:{len(RUB_transact)}\n")
                                                    for x in RUB_transact:
                                                        date_and_description = (
                                                            f'{get_date(x['date'])} {x["description"]}\n'
                                                        )
                                                        amount_and_name = f'Сумма: {x["operationAmount"]["amount"]} {x["operationAmount"]["currency"]["name"]}\n'
                                                        if x["description"] == "Открытие вклада":
                                                            from_to = f"{mask_account_card(x['to'])}\n"
                                                        else:
                                                            from_to = f"{mask_account_card(x['from'])} -> {mask_account_card(x['to'])}\n"
                                                        print(
                                                            f"{date_and_description}" f"{from_to}" f"{amount_and_name}"
                                                        )
                                                else:
                                                    return "Некорректный ввод"
                                            else:
                                                return "Некорректный ввод"
                                        elif only_RUB_transact.lower() == "нет":
                                            search_word = input(
                                                "Отфильтровать список транзакций по определенному слову в описании?\n"
                                                "Да/Нет\n"
                                            )
                                            if search_word:
                                                if search_word.lower() == "да":
                                                    my_search_word = input("Введите ключевое слово:\n")
                                                    search_transact = src.services.process_bank_search(
                                                        ascending_sort, my_search_word
                                                    )
                                                    print("Распечатываю итоговый список транзакций...\n")
                                                    print(
                                                        f"Всего банковских операций в выборке:{len(search_transact)}\n"
                                                    )
                                                    for x in search_transact:
                                                        date_and_description = (
                                                            f'{get_date(x['date'])} {x["description"]}\n'
                                                        )
                                                        amount_and_name = f'Сумма: {x["operationAmount"]["amount"]} {x["operationAmount"]["currency"]["name"]}\n'
                                                        if x["description"] == "Открытие вклада":
                                                            from_to = f"{mask_account_card(x['to'])}\n"
                                                        else:
                                                            from_to = f"{mask_account_card(x['from'])} -> {mask_account_card(x['to'])}\n"
                                                        print(
                                                            f"{date_and_description}" f"{from_to}" f"{amount_and_name}"
                                                        )
                                                elif search_word.lower() == "нет":
                                                    print("Распечатываю итоговый список транзакций...\n")
                                                    print(
                                                        f"Всего банковских операций в выборке:{len(ascending_sort)}\n"
                                                    )
                                                    for x in ascending_sort:
                                                        date_and_description = (
                                                            f'{get_date(x['date'])} {x["description"]}\n'
                                                        )
                                                        amount_and_name = f'Сумма: {x["operationAmount"]["amount"]} {x["operationAmount"]["currency"]["name"]}\n'
                                                        if x["description"] == "Открытие вклада":
                                                            from_to = f"{mask_account_card(x['to'])}\n"
                                                        else:
                                                            from_to = f"{mask_account_card(x['from'])} -> {mask_account_card(x['to'])}\n"
                                                        print(
                                                            f"{date_and_description}" f"{from_to}" f"{amount_and_name}"
                                                        )
                                                else:
                                                    return "Некорректный ввод"
                                            else:
                                                return "Некорректный ввод"
                                        else:
                                            return "Некорректный ввод"
                                    else:
                                        return "Некорректный ввод"
                                else:
                                    return "Некорректный ввод"
                            else:
                                return "Некорректный ввод"
                        elif sort_date.lower() == "нет":
                            only_RUB_transact = input("Выводить только рублевые транзакции?\n" "Да/Нет\n")
                            if only_RUB_transact:
                                if only_RUB_transact.lower() == "да":
                                    RUB_transact = [
                                        x for x in executed_list if x["operationAmount"]["currency"]["code"] == "RUB"
                                    ]
                                    search_word = input(
                                        "Отфильтровать список транзакций по определенному слову в описании?\n"
                                        "Да/Нет\n"
                                    )
                                    if search_word:
                                        if search_word.lower() == "да":
                                            my_search_word = input("Введите ключевое слово:\n")
                                            search_transact = src.services.process_bank_search(
                                                RUB_transact, my_search_word
                                            )
                                            print("Распечатываю итоговый список транзакций...\n")
                                            print(f"Всего банковских операций в выборке:{len(search_transact)}\n")
                                            for x in search_transact:
                                                date_and_description = f'{get_date(x['date'])} {x["description"]}\n'
                                                amount_and_name = f'Сумма: {x["operationAmount"]["amount"]} {x["operationAmount"]["currency"]["name"]}\n'
                                                if x["description"] == "Открытие вклада":
                                                    from_to = f"{mask_account_card(x['to'])}\n"
                                                else:
                                                    from_to = f"{mask_account_card(x['from'])} -> {mask_account_card(x['to'])}\n"
                                                print(f"{date_and_description}" f"{from_to}" f"{amount_and_name}")
                                        elif search_word.lower() == "нет":
                                            print("Распечатываю итоговый список транзакций...\n")
                                            print(f"Всего банковских операций в выборке:{len(RUB_transact)}\n")
                                            for x in RUB_transact:
                                                date_and_description = f'{get_date(x['date'])} {x["description"]}\n'
                                                amount_and_name = f'Сумма: {x["operationAmount"]["amount"]} {x["operationAmount"]["currency"]["name"]}\n'
                                                if x["description"] == "Открытие вклада":
                                                    from_to = f"{mask_account_card(x['to'])}\n"
                                                else:
                                                    from_to = f"{mask_account_card(x['from'])} -> {mask_account_card(x['to'])}\n"
                                                print(f"{date_and_description}" f"{from_to}" f"{amount_and_name}")
                                        else:
                                            return "Некорректный ввод"
                                    else:
                                        return "Некорректный ввод"
                                elif only_RUB_transact.lower() == "нет":
                                    search_word = input(
                                        "Отфильтровать список транзакций по определенному слову в описании?\n"
                                        "Да/Нет\n"
                                    )
                                    if search_word:
                                        if search_word.lower() == "да":
                                            my_search_word = input("Введите ключевое слово:\n")
                                            search_transact = src.services.process_bank_search(
                                                executed_list, my_search_word
                                            )
                                            print("Распечатываю итоговый список транзакций...\n")
                                            print(f"Всего банковских операций в выборке:{len(search_transact)}\n")
                                            for x in search_transact:
                                                date_and_description = f'{get_date(x['date'])} {x["description"]}\n'
                                                amount_and_name = f'Сумма: {x["operationAmount"]["amount"]} {x["operationAmount"]["currency"]["name"]}\n'
                                                if x["description"] == "Открытие вклада":
                                                    from_to = f"{mask_account_card(x['to'])}\n"
                                                else:
                                                    from_to = f"{mask_account_card(x['from'])} -> {mask_account_card(x['to'])}\n"
                                                print(f"{date_and_description}" f"{from_to}" f"{amount_and_name}")
                                        elif search_word.lower() == "нет":
                                            print("Распечатываю итоговый список транзакций...\n")
                                            print(f"Всего банковских операций в выборке:{len(executed_list)}\n")
                                            for x in executed_list:
                                                date_and_description = f'{get_date(x['date'])} {x["description"]}\n'
                                                amount_and_name = f'Сумма: {x["operationAmount"]["amount"]} {x["operationAmount"]["currency"]["name"]}\n'
                                                if x["description"] == "Открытие вклада":
                                                    from_to = f"{mask_account_card(x['to'])}\n"
                                                else:
                                                    from_to = f"{mask_account_card(x['from'])} -> {mask_account_card(x['to'])}\n"
                                                print(f"{date_and_description}" f"{from_to}" f"{amount_and_name}")
                                        else:
                                            return "Некорректный ввод"
                                    else:
                                        return "Некорректный ввод"
                                else:
                                    return "Некорректный ввод"
                            else:
                                return "Некорректный ввод"
                        else:
                            return "Некорректный ввод"
                    else:
                        return "Некорректный ввод"
                elif filter_status.upper() == "CANCELED":
                    canceled_list = [
                        transact for transact in json_transact for k, v in transact.items() if v == "CANCELED"
                    ]
                    sort_date = input("Отсортировать операции по дате?\n" "Да/Нет\n")
                    if sort_date:
                        if sort_date.lower() == "да":
                            sorted_date_list = sorted(canceled_list, key=lambda x: x["date"])
                            sorting_order = input("Отсортировать по возрастанию или по убыванию?\n")
                            if sorting_order:
                                if sorting_order.lower() == "по возрастанию":
                                    ascending_sort = sorted(sorted_date_list, key=lambda x: x["date"], reverse=False)
                                    only_RUB_transact = input("Выводить только рублевые транзакции?\n" "Да/Нет\n")
                                    if only_RUB_transact:
                                        if only_RUB_transact.lower() == "да":
                                            RUB_transact = [
                                                x
                                                for x in ascending_sort
                                                if x["operationAmount"]["currency"]["code"] == "RUB"
                                            ]
                                            search_word = input(
                                                "Отфильтровать список транзакций по определенному слову в описании?\n"
                                                "Да/Нет\n"
                                            )
                                            if search_word:
                                                if search_word.lower() == "да":
                                                    my_search_word = input("Введите ключевое слово:\n")
                                                    search_transact = src.services.process_bank_search(
                                                        RUB_transact, my_search_word
                                                    )
                                                    print("Распечатываю итоговый список транзакций...\n")
                                                    print(
                                                        f"Всего банковских операций в выборке:{len(search_transact)}\n"
                                                    )
                                                    for x in search_transact:
                                                        date_and_description = (
                                                            f'{get_date(x['date'])} {x["description"]}\n'
                                                        )
                                                        amount_and_name = f'Сумма: {x["operationAmount"]["amount"]} {x["operationAmount"]["currency"]["name"]}\n'
                                                        if x["description"] == "Открытие вклада":
                                                            from_to = f"{mask_account_card(x['to'])}\n"
                                                        else:
                                                            from_to = f"{mask_account_card(x['from'])} -> {mask_account_card(x['to'])}\n"
                                                        print(
                                                            f"{date_and_description}" f"{from_to}" f"{amount_and_name}"
                                                        )
                                                elif search_word.lower() == "нет":
                                                    print("Распечатываю итоговый список транзакций...\n")
                                                    print(f"Всего банковских операций в выборке:{len(RUB_transact)}\n")
                                                    for x in RUB_transact:
                                                        date_and_description = (
                                                            f'{get_date(x['date'])} {x["description"]}\n'
                                                        )
                                                        amount_and_name = f'Сумма: {x["operationAmount"]["amount"]} {x["operationAmount"]["currency"]["name"]}\n'
                                                        if x["description"] == "Открытие вклада":
                                                            from_to = f"{mask_account_card(x['to'])}\n"
                                                        else:
                                                            from_to = f"{mask_account_card(x['from'])} -> {mask_account_card(x['to'])}\n"
                                                        print(
                                                            f"{date_and_description}" f"{from_to}" f"{amount_and_name}"
                                                        )
                                                else:
                                                    return "Некорректный ввод"
                                            else:
                                                return "Некорректный ввод"
                                        elif only_RUB_transact.lower() == "нет":
                                            search_word = input(
                                                "Отфильтровать список транзакций по определенному слову в описании?\n"
                                                "Да/Нет\n"
                                            )
                                            if search_word:
                                                if search_word.lower() == "да":
                                                    my_search_word = input("Введите ключевое слово:\n")
                                                    search_transact = src.services.process_bank_search(
                                                        ascending_sort, my_search_word
                                                    )
                                                    print("Распечатываю итоговый список транзакций...\n")
                                                    print(
                                                        f"Всего банковских операций в выборке:{len(search_transact)}\n"
                                                    )
                                                    for x in search_transact:
                                                        date_and_description = (
                                                            f'{get_date(x['date'])} {x["description"]}\n'
                                                        )
                                                        amount_and_name = f'Сумма: {x["operationAmount"]["amount"]} {x["operationAmount"]["currency"]["name"]}\n'
                                                        if x["description"] == "Открытие вклада":
                                                            from_to = f"{mask_account_card(x['to'])}\n"
                                                        else:
                                                            from_to = f"{mask_account_card(x['from'])} -> {mask_account_card(x['to'])}\n"
                                                        print(
                                                            f"{date_and_description}" f"{from_to}" f"{amount_and_name}"
                                                        )
                                                elif search_word.lower() == "нет":
                                                    print("Распечатываю итоговый список транзакций...\n")
                                                    print(
                                                        f"Всего банковских операций в выборке:{len(ascending_sort)}\n"
                                                    )
                                                    for x in ascending_sort:
                                                        date_and_description = (
                                                            f'{get_date(x['date'])} {x["description"]}\n'
                                                        )
                                                        amount_and_name = f'Сумма: {x["operationAmount"]["amount"]} {x["operationAmount"]["currency"]["name"]}\n'
                                                        if x["description"] == "Открытие вклада":
                                                            from_to = f"{mask_account_card(x['to'])}\n"
                                                        else:
                                                            from_to = f"{mask_account_card(x['from'])} -> {mask_account_card(x['to'])}\n"
                                                        print(
                                                            f"{date_and_description}" f"{from_to}" f"{amount_and_name}"
                                                        )
                                                else:
                                                    return "Некорректный ввод"
                                            else:
                                                return "Некорректный ввод"
                                        else:
                                            return "Некорректный ввод"
                                    else:
                                        return "Некорректный ввод"
                                elif sorting_order.lower() == "по убыванию":
                                    ascending_sort = sorted(sorted_date_list, key=lambda x: x["date"], reverse=True)
                                    only_RUB_transact = input("Выводить только рублевые транзакции?\n" "Да/Нет\n")
                                    if only_RUB_transact:
                                        if only_RUB_transact.lower() == "да":
                                            RUB_transact = [
                                                x
                                                for x in ascending_sort
                                                if x["operationAmount"]["currency"]["code"] == "RUB"
                                            ]
                                            search_word = input(
                                                "Отфильтровать список транзакций по определенному слову в описании?\n"
                                                "Да/Нет\n"
                                            )
                                            if search_word:
                                                if search_word.lower() == "да":
                                                    my_search_word = input("Введите ключевое слово:\n")
                                                    search_transact = src.services.process_bank_search(
                                                        RUB_transact, my_search_word
                                                    )
                                                    print("Распечатываю итоговый список транзакций...\n")
                                                    print(
                                                        f"Всего банковских операций в выборке:{len(search_transact)}\n"
                                                    )
                                                    for x in search_transact:
                                                        date_and_description = (
                                                            f'{get_date(x['date'])} {x["description"]}\n'
                                                        )
                                                        amount_and_name = f'Сумма: {x["operationAmount"]["amount"]} {x["operationAmount"]["currency"]["name"]}\n'
                                                        if x["description"] == "Открытие вклада":
                                                            from_to = f"{mask_account_card(x['to'])}\n"
                                                        else:
                                                            from_to = f"{mask_account_card(x['from'])} -> {mask_account_card(x['to'])}\n"
                                                        print(
                                                            f"{date_and_description}" f"{from_to}" f"{amount_and_name}"
                                                        )
                                                elif search_word.lower() == "нет":
                                                    print("Распечатываю итоговый список транзакций...\n")
                                                    print(f"Всего банковских операций в выборке:{len(RUB_transact)}\n")
                                                    for x in RUB_transact:
                                                        date_and_description = (
                                                            f'{get_date(x['date'])} {x["description"]}\n'
                                                        )
                                                        amount_and_name = f'Сумма: {x["operationAmount"]["amount"]} {x["operationAmount"]["currency"]["name"]}\n'
                                                        if x["description"] == "Открытие вклада":
                                                            from_to = f"{mask_account_card(x['to'])}\n"
                                                        else:
                                                            from_to = f"{mask_account_card(x['from'])} -> {mask_account_card(x['to'])}\n"
                                                        print(
                                                            f"{date_and_description}" f"{from_to}" f"{amount_and_name}"
                                                        )
                                                else:
                                                    return "Некорректный ввод"
                                            else:
                                                return "Некорректный ввод"
                                        elif only_RUB_transact.lower() == "нет":
                                            search_word = input(
                                                "Отфильтровать список транзакций по определенному слову в описании?\n"
                                                "Да/Нет\n"
                                            )
                                            if search_word:
                                                if search_word.lower() == "да":
                                                    my_search_word = input("Введите ключевое слово:\n")
                                                    search_transact = src.services.process_bank_search(
                                                        ascending_sort, my_search_word
                                                    )
                                                    print("Распечатываю итоговый список транзакций...\n")
                                                    print(
                                                        f"Всего банковских операций в выборке:{len(search_transact)}\n"
                                                    )
                                                    for x in search_transact:
                                                        date_and_description = (
                                                            f'{get_date(x['date'])} {x["description"]}\n'
                                                        )
                                                        amount_and_name = f'Сумма: {x["operationAmount"]["amount"]} {x["operationAmount"]["currency"]["name"]}\n'
                                                        if x["description"] == "Открытие вклада":
                                                            from_to = f"{mask_account_card(x['to'])}\n"
                                                        else:
                                                            from_to = f"{mask_account_card(x['from'])} -> {mask_account_card(x['to'])}\n"
                                                        print(
                                                            f"{date_and_description}" f"{from_to}" f"{amount_and_name}"
                                                        )
                                                elif search_word.lower() == "нет":
                                                    print("Распечатываю итоговый список транзакций...\n")
                                                    print(
                                                        f"Всего банковских операций в выборке:{len(ascending_sort)}\n"
                                                    )
                                                    for x in ascending_sort:
                                                        date_and_description = (
                                                            f'{get_date(x['date'])} {x["description"]}\n'
                                                        )
                                                        amount_and_name = f'Сумма: {x["operationAmount"]["amount"]} {x["operationAmount"]["currency"]["name"]}\n'
                                                        if x["description"] == "Открытие вклада":
                                                            from_to = f"{mask_account_card(x['to'])}\n"
                                                        else:
                                                            from_to = f"{mask_account_card(x['from'])} -> {mask_account_card(x['to'])}\n"
                                                        print(
                                                            f"{date_and_description}" f"{from_to}" f"{amount_and_name}"
                                                        )
                                                else:
                                                    return "Некорректный ввод"
                                            else:
                                                return "Некорректный ввод"
                                        else:
                                            return "Некорректный ввод"
                                    else:
                                        return "Некорректный ввод"
                                else:
                                    return "Некорректный ввод"
                            else:
                                return "Некорректный ввод"
                        elif sort_date.lower() == "нет":
                            only_RUB_transact = input("Выводить только рублевые транзакции?\n" "Да/Нет\n")
                            if only_RUB_transact:
                                if only_RUB_transact.lower() == "да":
                                    RUB_transact = [
                                        x for x in canceled_list if x["operationAmount"]["currency"]["code"] == "RUB"
                                    ]
                                    search_word = input(
                                        "Отфильтровать список транзакций по определенному слову в описании?\n"
                                        "Да/Нет\n"
                                    )
                                    if search_word:
                                        if search_word.lower() == "да":
                                            my_search_word = input("Введите ключевое слово:\n")
                                            search_transact = src.services.process_bank_search(
                                                RUB_transact, my_search_word
                                            )
                                            print("Распечатываю итоговый список транзакций...\n")
                                            print(f"Всего банковских операций в выборке:{len(search_transact)}\n")
                                            for x in search_transact:
                                                date_and_description = f'{get_date(x['date'])} {x["description"]}\n'
                                                amount_and_name = f'Сумма: {x["operationAmount"]["amount"]} {x["operationAmount"]["currency"]["name"]}\n'
                                                if x["description"] == "Открытие вклада":
                                                    from_to = f"{mask_account_card(x['to'])}\n"
                                                else:
                                                    from_to = f"{mask_account_card(x['from'])} -> {mask_account_card(x['to'])}\n"
                                                print(f"{date_and_description}" f"{from_to}" f"{amount_and_name}")
                                        elif search_word.lower() == "нет":
                                            print("Распечатываю итоговый список транзакций...\n")
                                            print(f"Всего банковских операций в выборке:{len(RUB_transact)}\n")
                                            for x in RUB_transact:
                                                date_and_description = f'{get_date(x['date'])} {x["description"]}\n'
                                                amount_and_name = f'Сумма: {x["operationAmount"]["amount"]} {x["operationAmount"]["currency"]["name"]}\n'
                                                if x["description"] == "Открытие вклада":
                                                    from_to = f"{mask_account_card(x['to'])}\n"
                                                else:
                                                    from_to = f"{mask_account_card(x['from'])} -> {mask_account_card(x['to'])}\n"
                                                print(f"{date_and_description}" f"{from_to}" f"{amount_and_name}")
                                        else:
                                            return "Некорректный ввод"
                                    else:
                                        return "Некорректный ввод"
                                elif only_RUB_transact.lower() == "нет":
                                    search_word = input(
                                        "Отфильтровать список транзакций по определенному слову в описании?\n"
                                        "Да/Нет\n"
                                    )
                                    if search_word:
                                        if search_word.lower() == "да":
                                            my_search_word = input("Введите ключевое слово:\n")
                                            search_transact = src.services.process_bank_search(
                                                canceled_list, my_search_word
                                            )
                                            print("Распечатываю итоговый список транзакций...\n")
                                            print(f"Всего банковских операций в выборке:{len(search_transact)}\n")
                                            for x in search_transact:
                                                date_and_description = f'{get_date(x['date'])} {x["description"]}\n'
                                                amount_and_name = f'Сумма: {x["operationAmount"]["amount"]} {x["operationAmount"]["currency"]["name"]}\n'
                                                if x["description"] == "Открытие вклада":
                                                    from_to = f"{mask_account_card(x['to'])}\n"
                                                else:
                                                    from_to = f"{mask_account_card(x['from'])} -> {mask_account_card(x['to'])}\n"
                                                print(f"{date_and_description}" f"{from_to}" f"{amount_and_name}")
                                        elif search_word.lower() == "нет":
                                            print("Распечатываю итоговый список транзакций...\n")
                                            print(f"Всего банковских операций в выборке:{len(canceled_list)}\n")
                                            for x in canceled_list:
                                                date_and_description = f'{get_date(x['date'])} {x["description"]}\n'
                                                amount_and_name = f'Сумма: {x["operationAmount"]["amount"]} {x["operationAmount"]["currency"]["name"]}\n'
                                                if x["description"] == "Открытие вклада":
                                                    from_to = f"{mask_account_card(x['to'])}\n"
                                                else:
                                                    from_to = f"{mask_account_card(x['from'])} -> {mask_account_card(x['to'])}\n"
                                                print(f"{date_and_description}" f"{from_to}" f"{amount_and_name}")
                                        else:
                                            return "Некорректный ввод"
                                    else:
                                        return "Некорректный ввод"
                                else:
                                    return "Некорректный ввод"
                            else:
                                return "Некорректный ввод"
                        else:
                            return "Некорректный ввод"
                    else:
                        return "Некорректный ввод"
                elif filter_status.upper() == "PENDING":
                    pending_list = [
                        transact for transact in json_transact for k, v in transact.items() if v == "PENDING"
                    ]
                    sort_date = input("Отсортировать операции по дате?\n" "Да/Нет\n")
                    if sort_date:
                        if sort_date.lower() == "да":
                            sorted_date_list = sorted(pending_list, key=lambda x: x["date"])
                            sorting_order = input("Отсортировать по возрастанию или по убыванию?\n")
                            if sorting_order:
                                if sorting_order.lower() == "по возрастанию":
                                    ascending_sort = sorted(sorted_date_list, key=lambda x: x["date"], reverse=False)
                                    only_RUB_transact = input("Выводить только рублевые транзакции?\n" "Да/Нет\n")
                                    if only_RUB_transact:
                                        if only_RUB_transact.lower() == "да":
                                            RUB_transact = [
                                                x
                                                for x in ascending_sort
                                                if x["operationAmount"]["currency"]["code"] == "RUB"
                                            ]
                                            search_word = input(
                                                "Отфильтровать список транзакций по определенному слову в описании?\n"
                                                "Да/Нет\n"
                                            )
                                            if search_word:
                                                if search_word.lower() == "да":
                                                    my_search_word = input("Введите ключевое слово:\n")
                                                    search_transact = src.services.process_bank_search(
                                                        RUB_transact, my_search_word
                                                    )
                                                    print("Распечатываю итоговый список транзакций...\n")
                                                    print(
                                                        f"Всего банковских операций в выборке:{len(search_transact)}\n"
                                                    )
                                                    if len(search_transact) == 0:
                                                        return "Не найдено ни одной транзакции, подходящей под ваши условия фильтрации"
                                                    else:
                                                        for x in search_transact:
                                                            date_and_description = (
                                                                f'{get_date(x['date'])} {x["description"]}\n'
                                                            )
                                                            amount_and_name = f'Сумма: {x["operationAmount"]["amount"]} {x["operationAmount"]["currency"]["name"]}\n'
                                                            if x["description"] == "Открытие вклада":
                                                                from_to = f"{mask_account_card(x['to'])}\n"
                                                            else:
                                                                from_to = f"{mask_account_card(x['from'])} -> {mask_account_card(x['to'])}\n"
                                                            print(
                                                                f"{date_and_description}"
                                                                f"{from_to}"
                                                                f"{amount_and_name}"
                                                            )
                                                elif search_word.lower() == "нет":
                                                    print("Распечатываю итоговый список транзакций...\n")
                                                    print(f"Всего банковских операций в выборке:{len(RUB_transact)}\n")
                                                    if len(RUB_transact) == 0:
                                                        print(
                                                            "Не найдено ни одной транзакции, подходящей под ваши условия фильтрации"
                                                        )
                                                    else:
                                                        for x in RUB_transact:
                                                            date_and_description = (
                                                                f'{get_date(x['date'])} {x["description"]}\n'
                                                            )
                                                            amount_and_name = f'Сумма: {x["operationAmount"]["amount"]} {x["operationAmount"]["currency"]["name"]}\n'
                                                            if x["description"] == "Открытие вклада":
                                                                from_to = f"{mask_account_card(x['to'])}\n"
                                                            else:
                                                                from_to = f"{mask_account_card(x['from'])} -> {mask_account_card(x['to'])}\n"
                                                            print(
                                                                f"{date_and_description}"
                                                                f"{from_to}"
                                                                f"{amount_and_name}"
                                                            )
                                                else:
                                                    return "Некорректный ввод"
                                            else:
                                                return "Некорректный ввод"
                                        elif only_RUB_transact.lower() == "нет":
                                            search_word = input(
                                                "Отфильтровать список транзакций по определенному слову в описании?\n"
                                                "Да/Нет\n"
                                            )
                                            if search_word:
                                                if search_word.lower() == "да":
                                                    my_search_word = input("Введите ключевое слово:\n")
                                                    search_transact = src.services.process_bank_search(
                                                        ascending_sort, my_search_word
                                                    )
                                                    print("Распечатываю итоговый список транзакций...\n")
                                                    print(
                                                        f"Всего банковских операций в выборке:{len(search_transact)}\n"
                                                    )
                                                    if len(search_transact) == 0:
                                                        print(
                                                            "Не найдено ни одной транзакции, подходящей под ваши условия фильтрации"
                                                        )
                                                    else:
                                                        for x in search_transact:
                                                            date_and_description = (
                                                                f'{get_date(x['date'])} {x["description"]}\n'
                                                            )
                                                            amount_and_name = f'Сумма: {x["operationAmount"]["amount"]} {x["operationAmount"]["currency"]["name"]}\n'
                                                            if x["description"] == "Открытие вклада":
                                                                from_to = f"{mask_account_card(x['to'])}\n"
                                                            else:
                                                                from_to = f"{mask_account_card(x['from'])} -> {mask_account_card(x['to'])}\n"
                                                            print(
                                                                f"{date_and_description}"
                                                                f"{from_to}"
                                                                f"{amount_and_name}"
                                                            )
                                                elif search_word.lower() == "нет":
                                                    print("Распечатываю итоговый список транзакций...\n")
                                                    print(
                                                        f"Всего банковских операций в выборке:{len(ascending_sort)}\n"
                                                    )
                                                    if len(ascending_sort) == 0:
                                                        print(
                                                            "Не найдено ни одной транзакции, подходящей под ваши условия фильтрации"
                                                        )
                                                    else:
                                                        for x in ascending_sort:
                                                            date_and_description = (
                                                                f'{get_date(x['date'])} {x["description"]}\n'
                                                            )
                                                            amount_and_name = f'Сумма: {x["operationAmount"]["amount"]} {x["operationAmount"]["currency"]["name"]}\n'
                                                            if x["description"] == "Открытие вклада":
                                                                from_to = f"{mask_account_card(x['to'])}\n"
                                                            else:
                                                                from_to = f"{mask_account_card(x['from'])} -> {mask_account_card(x['to'])}\n"
                                                            print(
                                                                f"{date_and_description}"
                                                                f"{from_to}"
                                                                f"{amount_and_name}"
                                                            )
                                                else:
                                                    return "Некорректный ввод"
                                            else:
                                                return "Некорректный ввод"
                                        else:
                                            return "Некорректный ввод"
                                    else:
                                        return "Некорректный ввод"
                                elif sorting_order.lower() == "по убыванию":
                                    ascending_sort = sorted(sorted_date_list, key=lambda x: x["date"], reverse=True)
                                    only_RUB_transact = input("Выводить только рублевые транзакции?\n" "Да/Нет\n")
                                    if only_RUB_transact:
                                        if only_RUB_transact.lower() == "да":
                                            RUB_transact = [
                                                x
                                                for x in ascending_sort
                                                if x["operationAmount"]["currency"]["code"] == "RUB"
                                            ]
                                            search_word = input(
                                                "Отфильтровать список транзакций по определенному слову в описании?\n"
                                                "Да/Нет\n"
                                            )
                                            if search_word:
                                                if search_word.lower() == "да":
                                                    my_search_word = input("Введите ключевое слово:\n")
                                                    search_transact = src.services.process_bank_search(
                                                        RUB_transact, my_search_word
                                                    )
                                                    print("Распечатываю итоговый список транзакций...\n")
                                                    print(
                                                        f"Всего банковских операций в выборке:{len(search_transact)}\n"
                                                    )
                                                    if len(search_transact) == 0:
                                                        print(
                                                            "Не найдено ни одной транзакции, подходящей под ваши условия фильтрации"
                                                        )
                                                    else:
                                                        for x in search_transact:
                                                            date_and_description = (
                                                                f'{get_date(x['date'])} {x["description"]}\n'
                                                            )
                                                            amount_and_name = f'Сумма: {x["operationAmount"]["amount"]} {x["operationAmount"]["currency"]["name"]}\n'
                                                            if x["description"] == "Открытие вклада":
                                                                from_to = f"{mask_account_card(x['to'])}\n"
                                                            else:
                                                                from_to = f"{mask_account_card(x['from'])} -> {mask_account_card(x['to'])}\n"
                                                            print(
                                                                f"{date_and_description}"
                                                                f"{from_to}"
                                                                f"{amount_and_name}"
                                                            )
                                                elif search_word.lower() == "нет":
                                                    print("Распечатываю итоговый список транзакций...\n")
                                                    print(f"Всего банковских операций в выборке:{len(RUB_transact)}\n")
                                                    if len(RUB_transact) == 0:
                                                        print(
                                                            "Не найдено ни одной транзакции, подходящей под ваши условия фильтрации"
                                                        )
                                                    else:
                                                        for x in RUB_transact:
                                                            date_and_description = (
                                                                f'{get_date(x['date'])} {x["description"]}\n'
                                                            )
                                                            amount_and_name = f'Сумма: {x["operationAmount"]["amount"]} {x["operationAmount"]["currency"]["name"]}\n'
                                                            if x["description"] == "Открытие вклада":
                                                                from_to = f"{mask_account_card(x['to'])}\n"
                                                            else:
                                                                from_to = f"{mask_account_card(x['from'])} -> {mask_account_card(x['to'])}\n"
                                                            print(
                                                                f"{date_and_description}"
                                                                f"{from_to}"
                                                                f"{amount_and_name}"
                                                            )
                                                else:
                                                    return "Некорректный ввод"
                                            else:
                                                return "Некорректный ввод"
                                        elif only_RUB_transact.lower() == "нет":
                                            search_word = input(
                                                "Отфильтровать список транзакций по определенному слову в описании?\n"
                                                "Да/Нет\n"
                                            )
                                            if search_word:
                                                if search_word.lower() == "да":
                                                    my_search_word = input("Введите ключевое слово:\n")
                                                    search_transact = src.services.process_bank_search(
                                                        ascending_sort, my_search_word
                                                    )
                                                    print("Распечатываю итоговый список транзакций...\n")
                                                    print(
                                                        f"Всего банковских операций в выборке:{len(search_transact)}\n"
                                                    )
                                                    if len(search_transact) == 0:
                                                        print(
                                                            "Не найдено ни одной транзакции, подходящей под ваши условия фильтрации"
                                                        )
                                                    else:
                                                        for x in search_transact:
                                                            date_and_description = (
                                                                f'{get_date(x['date'])} {x["description"]}\n'
                                                            )
                                                            amount_and_name = f'Сумма: {x["operationAmount"]["amount"]} {x["operationAmount"]["currency"]["name"]}\n'
                                                            if x["description"] == "Открытие вклада":
                                                                from_to = f"{mask_account_card(x['to'])}\n"
                                                            else:
                                                                from_to = f"{mask_account_card(x['from'])} -> {mask_account_card(x['to'])}\n"
                                                            print(
                                                                f"{date_and_description}"
                                                                f"{from_to}"
                                                                f"{amount_and_name}"
                                                            )
                                                elif search_word.lower() == "нет":
                                                    print("Распечатываю итоговый список транзакций...\n")
                                                    print(
                                                        f"Всего банковских операций в выборке:{len(ascending_sort)}\n"
                                                    )
                                                    if len(ascending_sort) == 0:
                                                        print(
                                                            "Не найдено ни одной транзакции, подходящей под ваши условия фильтрации"
                                                        )
                                                    else:
                                                        for x in ascending_sort:
                                                            date_and_description = (
                                                                f'{get_date(x['date'])} {x["description"]}\n'
                                                            )
                                                            amount_and_name = f'Сумма: {x["operationAmount"]["amount"]} {x["operationAmount"]["currency"]["name"]}\n'
                                                            if x["description"] == "Открытие вклада":
                                                                from_to = f"{mask_account_card(x['to'])}\n"
                                                            else:
                                                                from_to = f"{mask_account_card(x['from'])} -> {mask_account_card(x['to'])}\n"
                                                            print(
                                                                f"{date_and_description}"
                                                                f"{from_to}"
                                                                f"{amount_and_name}"
                                                            )
                                                else:
                                                    return "Некорректный ввод"
                                            else:
                                                return "Некорректный ввод"
                                        else:
                                            return "Некорректный ввод"
                                    else:
                                        return "Некорректный ввод"
                                else:
                                    return "Некорректный ввод"
                            else:
                                return "Некорректный ввод"
                        elif sort_date.lower() == "нет":
                            only_RUB_transact = input("Выводить только рублевые транзакции?\n" "Да/Нет\n")
                            if only_RUB_transact:
                                if only_RUB_transact.lower() == "да":
                                    RUB_transact = [
                                        x for x in pending_list if x["operationAmount"]["currency"]["code"] == "RUB"
                                    ]
                                    search_word = input(
                                        "Отфильтровать список транзакций по определенному слову в описании?\n"
                                        "Да/Нет\n"
                                    )
                                    if search_word:
                                        if search_word.lower() == "да":
                                            my_search_word = input("Введите ключевое слово:\n")
                                            search_transact = src.services.process_bank_search(
                                                RUB_transact, my_search_word
                                            )
                                            print("Распечатываю итоговый список транзакций...\n")
                                            print(f"Всего банковских операций в выборке:{len(search_transact)}\n")
                                            if len(search_transact) == 0:
                                                print(
                                                    "Не найдено ни одной транзакции, подходящей под ваши условия фильтрации"
                                                )
                                            else:
                                                for x in search_transact:
                                                    date_and_description = (
                                                        f'{get_date(x['date'])} {x["description"]}\n'
                                                    )
                                                    amount_and_name = f'Сумма: {x["operationAmount"]["amount"]} {x["operationAmount"]["currency"]["name"]}\n'
                                                    if x["description"] == "Открытие вклада":
                                                        from_to = f"{mask_account_card(x['to'])}\n"
                                                    else:
                                                        from_to = f"{mask_account_card(x['from'])} -> {mask_account_card(x['to'])}\n"
                                                    print(f"{date_and_description}" f"{from_to}" f"{amount_and_name}")
                                        elif search_word.lower() == "нет":
                                            print("Распечатываю итоговый список транзакций...\n")
                                            print(f"Всего банковских операций в выборке:{len(RUB_transact)}\n")
                                            if len(RUB_transact) == 0:
                                                print(
                                                    "Не найдено ни одной транзакции, подходящей под ваши условия фильтрации"
                                                )
                                            else:
                                                for x in RUB_transact:
                                                    date_and_description = (
                                                        f'{get_date(x['date'])} {x["description"]}\n'
                                                    )
                                                    amount_and_name = f'Сумма: {x["operationAmount"]["amount"]} {x["operationAmount"]["currency"]["name"]}\n'
                                                    if x["description"] == "Открытие вклада":
                                                        from_to = f"{mask_account_card(x['to'])}\n"
                                                    else:
                                                        from_to = f"{mask_account_card(x['from'])} -> {mask_account_card(x['to'])}\n"
                                                    print(f"{date_and_description}" f"{from_to}" f"{amount_and_name}")
                                        else:
                                            return "Некорректный ввод"
                                    else:
                                        return "Некорректный ввод"
                                elif only_RUB_transact.lower() == "нет":
                                    search_word = input(
                                        "Отфильтровать список транзакций по определенному слову в описании?\n"
                                        "Да/Нет\n"
                                    )
                                    if search_word:
                                        if search_word.lower() == "да":
                                            my_search_word = input("Введите ключевое слово:\n")
                                            search_transact = src.services.process_bank_search(
                                                pending_list, my_search_word
                                            )
                                            print("Распечатываю итоговый список транзакций...\n")
                                            print(f"Всего банковских операций в выборке:{len(search_transact)}\n")
                                            if len(search_transact) == 0:
                                                print(
                                                    "Не найдено ни одной транзакции, подходящей под ваши условия фильтрации"
                                                )
                                            else:
                                                for x in search_transact:
                                                    date_and_description = (
                                                        f'{get_date(x['date'])} {x["description"]}\n'
                                                    )
                                                    amount_and_name = f'Сумма: {x["operationAmount"]["amount"]} {x["operationAmount"]["currency"]["name"]}\n'
                                                    if x["description"] == "Открытие вклада":
                                                        from_to = f"{mask_account_card(x['to'])}\n"
                                                    else:
                                                        from_to = f"{mask_account_card(x['from'])} -> {mask_account_card(x['to'])}\n"
                                                    print(f"{date_and_description}" f"{from_to}" f"{amount_and_name}")
                                        elif search_word.lower() == "нет":
                                            print("Распечатываю итоговый список транзакций...\n")
                                            print(f"Всего банковских операций в выборке:{len(pending_list)}\n")
                                            if len(pending_list) == 0:
                                                print(
                                                    "Не найдено ни одной транзакции, подходящей под ваши условия фильтрации"
                                                )
                                            else:
                                                for x in pending_list:
                                                    date_and_description = (
                                                        f'{get_date(x['date'])} {x["description"]}\n'
                                                    )
                                                    amount_and_name = f'Сумма: {x["operationAmount"]["amount"]} {x["operationAmount"]["currency"]["name"]}\n'
                                                    if x["description"] == "Открытие вклада":
                                                        from_to = f"{mask_account_card(x['to'])}\n"
                                                    else:
                                                        from_to = f"{mask_account_card(x['from'])} -> {mask_account_card(x['to'])}\n"
                                                    print(f"{date_and_description}" f"{from_to}" f"{amount_and_name}")
                                        else:
                                            return "Некорректный ввод"
                                    else:
                                        return "Некорректный ввод"
                                else:
                                    return "Некорректный ввод"
                            else:
                                return "Некорректный ввод"
                        else:
                            return "Некорректный ввод"
                    else:
                        return "Некорректный ввод"
                else:
                    return "Некорректный ввод"

        elif file_selection.lower() == "2":
            print("Для обработки выбран CSV-файл.\n")
            csv_transact = src.import_data.get_csv_data("transactions.csv")
            filter_status = input(
                "Введите статус, по которому необходимо выполнить фильтрацию.\n"
                "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n"
            )
            if filter_status:
                if filter_status.upper() == "EXECUTED":
                    executed_list = [
                        transact for transact in csv_transact for k, v in transact.items() if v == "EXECUTED"
                    ]
                    sort_date = input("Отсортировать операции по дате?\n" "Да/Нет\n")
                    if sort_date:
                        if sort_date.lower() == "да":
                            sorted_date_list = sorted(executed_list, key=lambda x: x["date"])
                            sorting_order = input("Отсортировать по возрастанию или по убыванию?\n")
                            if sorting_order:
                                if sorting_order.lower() == "по возрастанию":
                                    ascending_sort = sorted(sorted_date_list, key=lambda x: x["date"], reverse=False)
                                    only_RUB_transact = input("Выводить только рублевые транзакции?\n" "Да/Нет\n")
                                    if only_RUB_transact:
                                        if only_RUB_transact.lower() == "да":
                                            RUB_transact = [x for x in ascending_sort if x["currency_code"] == "RUB"]
                                            search_word = input(
                                                "Отфильтровать список транзакций по определенному слову в описании?\n"
                                                "Да/Нет\n"
                                            )
                                            if search_word:
                                                if search_word.lower() == "да":
                                                    my_search_word = input("Введите ключевое слово:\n")
                                                    search_transact = src.services.process_bank_search(
                                                        RUB_transact, my_search_word
                                                    )
                                                    print("Распечатываю итоговый список транзакций...\n")
                                                    print(
                                                        f"Всего банковских операций в выборке:{len(search_transact)}\n"
                                                    )
                                                    for x in search_transact:
                                                        date_and_description = (
                                                            f'{get_date(x['date'])} {x["description"]}\n'
                                                        )
                                                        amount_and_name = (
                                                            f'Сумма: {x["amount"]} {x["currency_name"]}\n'
                                                        )
                                                        if x["description"] == "Открытие вклада":
                                                            from_to = f"{mask_account_card(x['to'])}\n"
                                                        else:
                                                            from_to = f"{mask_account_card(x['from'])} -> {mask_account_card(x['to'])}\n"
                                                        print(
                                                            f"{date_and_description}" f"{from_to}" f"{amount_and_name}"
                                                        )
                                                elif search_word.lower() == "нет":
                                                    print("Распечатываю итоговый список транзакций...\n")
                                                    print(f"Всего банковских операций в выборке:{len(RUB_transact)}\n")
                                                    for x in RUB_transact:
                                                        date_and_description = (
                                                            f'{get_date(x['date'])} {x["description"]}\n'
                                                        )
                                                        amount_and_name = (
                                                            f'Сумма: {x["amount"]} {x["currency_name"]}\n'
                                                        )
                                                        if x["description"] == "Открытие вклада":
                                                            from_to = f"{mask_account_card(x['to'])}\n"
                                                        else:
                                                            from_to = f"{mask_account_card(x['from'])} -> {mask_account_card(x['to'])}\n"
                                                        print(
                                                            f"{date_and_description}" f"{from_to}" f"{amount_and_name}"
                                                        )
                                                else:
                                                    return "Некорректный ввод"
                                            else:
                                                return "Некорректный ввод"
                                        elif only_RUB_transact.lower() == "нет":
                                            search_word = input(
                                                "Отфильтровать список транзакций по определенному слову в описании?\n"
                                                "Да/Нет\n"
                                            )
                                            if search_word:
                                                if search_word.lower() == "да":
                                                    my_search_word = input("Введите ключевое слово:\n")
                                                    search_transact = src.services.process_bank_search(
                                                        ascending_sort, my_search_word
                                                    )
                                                    print("Распечатываю итоговый список транзакций...\n")
                                                    print(
                                                        f"Всего банковских операций в выборке:{len(search_transact)}\n"
                                                    )
                                                    for x in search_transact:
                                                        date_and_description = (
                                                            f'{get_date(x['date'])} {x["description"]}\n'
                                                        )
                                                        amount_and_name = (
                                                            f'Сумма: {x["amount"]} {x["currency_name"]}\n'
                                                        )
                                                        if x["description"] == "Открытие вклада":
                                                            from_to = f"{mask_account_card(x['to'])}\n"
                                                        else:
                                                            from_to = f"{mask_account_card(x['from'])} -> {mask_account_card(x['to'])}\n"
                                                        print(
                                                            f"{date_and_description}" f"{from_to}" f"{amount_and_name}"
                                                        )
                                                elif search_word.lower() == "нет":
                                                    print("Распечатываю итоговый список транзакций...\n")
                                                    print(
                                                        f"Всего банковских операций в выборке:{len(ascending_sort)}\n"
                                                    )
                                                    for x in ascending_sort:
                                                        date_and_description = (
                                                            f'{get_date(x['date'])} {x["description"]}\n'
                                                        )
                                                        amount_and_name = (
                                                            f'Сумма: {x["amount"]} {x["currency_name"]}\n'
                                                        )
                                                        if x["description"] == "Открытие вклада":
                                                            from_to = f"{mask_account_card(x['to'])}\n"
                                                        else:
                                                            from_to = f"{mask_account_card(x['from'])} -> {mask_account_card(x['to'])}\n"
                                                        print(
                                                            f"{date_and_description}" f"{from_to}" f"{amount_and_name}"
                                                        )
                                                else:
                                                    return "Некорректный ввод"
                                            else:
                                                return "Некорректный ввод"
                                        else:
                                            return "Некорректный ввод"
                                    else:
                                        return "Некорректный ввод"
                                elif sorting_order.lower() == "по убыванию":
                                    ascending_sort = sorted(sorted_date_list, key=lambda x: x["date"], reverse=True)
                                    only_RUB_transact = input("Выводить только рублевые транзакции?\n" "Да/Нет\n")
                                    if only_RUB_transact:
                                        if only_RUB_transact.lower() == "да":
                                            RUB_transact = [x for x in ascending_sort if x["currency_code"] == "RUB"]
                                            search_word = input(
                                                "Отфильтровать список транзакций по определенному слову в описании?\n"
                                                "Да/Нет\n"
                                            )
                                            if search_word:
                                                if search_word.lower() == "да":
                                                    my_search_word = input("Введите ключевое слово:\n")
                                                    search_transact = src.services.process_bank_search(
                                                        RUB_transact, my_search_word
                                                    )
                                                    print("Распечатываю итоговый список транзакций...\n")
                                                    print(
                                                        f"Всего банковских операций в выборке:{len(search_transact)}\n"
                                                    )
                                                    for x in search_transact:
                                                        date_and_description = (
                                                            f'{get_date(x['date'])} {x["description"]}\n'
                                                        )
                                                        amount_and_name = (
                                                            f'Сумма: {x["amount"]} {x["currency_name"]}\n'
                                                        )
                                                        if x["description"] == "Открытие вклада":
                                                            from_to = f"{mask_account_card(x['to'])}\n"
                                                        else:
                                                            from_to = f"{mask_account_card(x['from'])} -> {mask_account_card(x['to'])}\n"
                                                        print(
                                                            f"{date_and_description}" f"{from_to}" f"{amount_and_name}"
                                                        )
                                                elif search_word.lower() == "нет":
                                                    print("Распечатываю итоговый список транзакций...\n")
                                                    print(f"Всего банковских операций в выборке:{len(RUB_transact)}\n")
                                                    for x in RUB_transact:
                                                        date_and_description = (
                                                            f'{get_date(x['date'])} {x["description"]}\n'
                                                        )
                                                        amount_and_name = (
                                                            f'Сумма: {x["amount"]} {x["currency_name"]}\n'
                                                        )
                                                        if x["description"] == "Открытие вклада":
                                                            from_to = f"{mask_account_card(x['to'])}\n"
                                                        else:
                                                            from_to = f"{mask_account_card(x['from'])} -> {mask_account_card(x['to'])}\n"
                                                        print(
                                                            f"{date_and_description}" f"{from_to}" f"{amount_and_name}"
                                                        )
                                                else:
                                                    return "Некорректный ввод"
                                            else:
                                                return "Некорректный ввод"
                                        elif only_RUB_transact.lower() == "нет":
                                            search_word = input(
                                                "Отфильтровать список транзакций по определенному слову в описании?\n"
                                                "Да/Нет\n"
                                            )
                                            if search_word:
                                                if search_word.lower() == "да":
                                                    my_search_word = input("Введите ключевое слово:\n")
                                                    search_transact = src.services.process_bank_search(
                                                        ascending_sort, my_search_word
                                                    )
                                                    print("Распечатываю итоговый список транзакций...\n")
                                                    print(
                                                        f"Всего банковских операций в выборке:{len(search_transact)}\n"
                                                    )
                                                    for x in search_transact:
                                                        date_and_description = (
                                                            f'{get_date(x['date'])} {x["description"]}\n'
                                                        )
                                                        amount_and_name = (
                                                            f'Сумма: {x["amount"]} {x["currency_name"]}\n'
                                                        )
                                                        if x["description"] == "Открытие вклада":
                                                            from_to = f"{mask_account_card(x['to'])}\n"
                                                        else:
                                                            from_to = f"{mask_account_card(x['from'])} -> {mask_account_card(x['to'])}\n"
                                                        print(
                                                            f"{date_and_description}" f"{from_to}" f"{amount_and_name}"
                                                        )
                                                elif search_word.lower() == "нет":
                                                    print("Распечатываю итоговый список транзакций...\n")
                                                    print(
                                                        f"Всего банковских операций в выборке:{len(ascending_sort)}\n"
                                                    )
                                                    for x in ascending_sort:
                                                        date_and_description = (
                                                            f'{get_date(x['date'])} {x["description"]}\n'
                                                        )
                                                        amount_and_name = (
                                                            f'Сумма: {x["amount"]} {x["currency_name"]}\n'
                                                        )
                                                        if x["description"] == "Открытие вклада":
                                                            from_to = f"{mask_account_card(x['to'])}\n"
                                                        else:
                                                            from_to = f"{mask_account_card(x['from'])} -> {mask_account_card(x['to'])}\n"
                                                        print(
                                                            f"{date_and_description}" f"{from_to}" f"{amount_and_name}"
                                                        )
                                                else:
                                                    return "Некорректный ввод"
                                            else:
                                                return "Некорректный ввод"
                                        else:
                                            return "Некорректный ввод"
                                    else:
                                        return "Некорректный ввод"
                                else:
                                    return "Некорректный ввод"
                            else:
                                return "Некорректный ввод"
                        elif sort_date.lower() == "нет":
                            only_RUB_transact = input("Выводить только рублевые транзакции?\n" "Да/Нет\n")
                            if only_RUB_transact:
                                if only_RUB_transact.lower() == "да":
                                    RUB_transact = [x for x in executed_list if x["currency_code"] == "RUB"]
                                    search_word = input(
                                        "Отфильтровать список транзакций по определенному слову в описании?\n"
                                        "Да/Нет\n"
                                    )
                                    if search_word:
                                        if search_word.lower() == "да":
                                            my_search_word = input("Введите ключевое слово:\n")
                                            search_transact = src.services.process_bank_search(
                                                RUB_transact, my_search_word
                                            )
                                            print("Распечатываю итоговый список транзакций...\n")
                                            print(f"Всего банковских операций в выборке:{len(search_transact)}\n")
                                            for x in search_transact:
                                                date_and_description = f'{get_date(x['date'])} {x["description"]}\n'
                                                amount_and_name = f'Сумма: {x["amount"]} {x["currency_name"]}\n'
                                                if x["description"] == "Открытие вклада":
                                                    from_to = f"{mask_account_card(x['to'])}\n"
                                                else:
                                                    from_to = f"{mask_account_card(x['from'])} -> {mask_account_card(x['to'])}\n"
                                                print(f"{date_and_description}" f"{from_to}" f"{amount_and_name}")
                                        elif search_word.lower() == "нет":
                                            print("Распечатываю итоговый список транзакций...\n")
                                            print(f"Всего банковских операций в выборке:{len(RUB_transact)}\n")
                                            for x in RUB_transact:
                                                date_and_description = f'{get_date(x['date'])} {x["description"]}\n'
                                                amount_and_name = f'Сумма: {x["amount"]} {x["currency_name"]}\n'
                                                if x["description"] == "Открытие вклада":
                                                    from_to = f"{mask_account_card(x['to'])}\n"
                                                else:
                                                    from_to = f"{mask_account_card(x['from'])} -> {mask_account_card(x['to'])}\n"
                                                print(f"{date_and_description}" f"{from_to}" f"{amount_and_name}")
                                        else:
                                            return "Некорректный ввод"
                                    else:
                                        return "Некорректный ввод"
                                elif only_RUB_transact.lower() == "нет":
                                    search_word = input(
                                        "Отфильтровать список транзакций по определенному слову в описании?\n"
                                        "Да/Нет\n"
                                    )
                                    if search_word:
                                        if search_word.lower() == "да":
                                            my_search_word = input("Введите ключевое слово:\n")
                                            search_transact = src.services.process_bank_search(
                                                executed_list, my_search_word
                                            )
                                            print("Распечатываю итоговый список транзакций...\n")
                                            print(f"Всего банковских операций в выборке:{len(search_transact)}\n")
                                            for x in search_transact:
                                                date_and_description = f'{get_date(x['date'])} {x["description"]}\n'
                                                amount_and_name = f'Сумма: {x["amount"]} {x["currency_name"]}\n'
                                                if x["description"] == "Открытие вклада":
                                                    from_to = f"{mask_account_card(x['to'])}\n"
                                                else:
                                                    from_to = f"{mask_account_card(x['from'])} -> {mask_account_card(x['to'])}\n"
                                                print(f"{date_and_description}" f"{from_to}" f"{amount_and_name}")
                                        elif search_word.lower() == "нет":
                                            print("Распечатываю итоговый список транзакций...\n")
                                            print(f"Всего банковских операций в выборке:{len(executed_list)}\n")
                                            for x in executed_list:
                                                date_and_description = f'{get_date(x['date'])} {x["description"]}\n'
                                                amount_and_name = f'Сумма: {x["amount"]} {x["currency_name"]}\n'
                                                if x["description"] == "Открытие вклада":
                                                    from_to = f"{mask_account_card(x['to'])}\n"
                                                else:
                                                    from_to = f"{mask_account_card(x['from'])} -> {mask_account_card(x['to'])}\n"
                                                print(f"{date_and_description}" f"{from_to}" f"{amount_and_name}")
                                        else:
                                            return "Некорректный ввод"
                                    else:
                                        return "Некорректный ввод"
                                else:
                                    return "Некорректный ввод"
                            else:
                                return "Некорректный ввод"
                        else:
                            return "Некорректный ввод"
                    else:
                        return "Некорректный ввод"
                elif filter_status.upper() == "CANCELED":
                    canceled_list = [
                        transact for transact in csv_transact for k, v in transact.items() if v == "CANCELED"
                    ]
                    sort_date = input("Отсортировать операции по дате?\n" "Да/Нет\n")
                    if sort_date:
                        if sort_date.lower() == "да":
                            sorted_date_list = sorted(canceled_list, key=lambda x: x["date"])
                            sorting_order = input("Отсортировать по возрастанию или по убыванию?\n")
                            if sorting_order:
                                if sorting_order.lower() == "по возрастанию":
                                    ascending_sort = sorted(sorted_date_list, key=lambda x: x["date"], reverse=False)
                                    only_RUB_transact = input("Выводить только рублевые транзакции?\n" "Да/Нет\n")
                                    if only_RUB_transact:
                                        if only_RUB_transact.lower() == "да":
                                            RUB_transact = [x for x in ascending_sort if x["currency_code"] == "RUB"]
                                            search_word = input(
                                                "Отфильтровать список транзакций по определенному слову в описании?\n"
                                                "Да/Нет\n"
                                            )
                                            if search_word:
                                                if search_word.lower() == "да":
                                                    my_search_word = input("Введите ключевое слово:\n")
                                                    search_transact = src.services.process_bank_search(
                                                        RUB_transact, my_search_word
                                                    )
                                                    print("Распечатываю итоговый список транзакций...\n")
                                                    print(
                                                        f"Всего банковских операций в выборке:{len(search_transact)}\n"
                                                    )
                                                    for x in search_transact:
                                                        date_and_description = (
                                                            f'{get_date(x['date'])} {x["description"]}\n'
                                                        )
                                                        amount_and_name = (
                                                            f'Сумма: {x["amount"]} {x["currency_name"]}\n'
                                                        )
                                                        if x["description"] == "Открытие вклада":
                                                            from_to = f"{mask_account_card(x['to'])}\n"
                                                        else:
                                                            from_to = f"{mask_account_card(x['from'])} -> {mask_account_card(x['to'])}\n"
                                                        print(
                                                            f"{date_and_description}" f"{from_to}" f"{amount_and_name}"
                                                        )
                                                elif search_word.lower() == "нет":
                                                    print("Распечатываю итоговый список транзакций...\n")
                                                    print(f"Всего банковских операций в выборке:{len(RUB_transact)}\n")
                                                    for x in RUB_transact:
                                                        date_and_description = (
                                                            f'{get_date(x['date'])} {x["description"]}\n'
                                                        )
                                                        amount_and_name = (
                                                            f'Сумма: {x["amount"]} {x["currency_name"]}\n'
                                                        )
                                                        if x["description"] == "Открытие вклада":
                                                            from_to = f"{mask_account_card(x['to'])}\n"
                                                        else:
                                                            from_to = f"{mask_account_card(x['from'])} -> {mask_account_card(x['to'])}\n"
                                                        print(
                                                            f"{date_and_description}" f"{from_to}" f"{amount_and_name}"
                                                        )
                                                else:
                                                    return "Некорректный ввод"
                                            else:
                                                return "Некорректный ввод"
                                        elif only_RUB_transact.lower() == "нет":
                                            search_word = input(
                                                "Отфильтровать список транзакций по определенному слову в описании?\n"
                                                "Да/Нет\n"
                                            )
                                            if search_word:
                                                if search_word.lower() == "да":
                                                    my_search_word = input("Введите ключевое слово:\n")
                                                    search_transact = src.services.process_bank_search(
                                                        ascending_sort, my_search_word
                                                    )
                                                    print("Распечатываю итоговый список транзакций...\n")
                                                    print(
                                                        f"Всего банковских операций в выборке:{len(search_transact)}\n"
                                                    )
                                                    for x in search_transact:
                                                        date_and_description = (
                                                            f'{get_date(x['date'])} {x["description"]}\n'
                                                        )
                                                        amount_and_name = (
                                                            f'Сумма: {x["amount"]} {x["currency_name"]}\n'
                                                        )
                                                        if x["description"] == "Открытие вклада":
                                                            from_to = f"{mask_account_card(x['to'])}\n"
                                                        else:
                                                            from_to = f"{mask_account_card(x['from'])} -> {mask_account_card(x['to'])}\n"
                                                        print(
                                                            f"{date_and_description}" f"{from_to}" f"{amount_and_name}"
                                                        )
                                                elif search_word.lower() == "нет":
                                                    print("Распечатываю итоговый список транзакций...\n")
                                                    print(
                                                        f"Всего банковских операций в выборке:{len(ascending_sort)}\n"
                                                    )
                                                    for x in ascending_sort:
                                                        date_and_description = (
                                                            f'{get_date(x['date'])} {x["description"]}\n'
                                                        )
                                                        amount_and_name = (
                                                            f'Сумма: {x["amount"]} {x["currency_name"]}\n'
                                                        )
                                                        if x["description"] == "Открытие вклада":
                                                            from_to = f"{mask_account_card(x['to'])}\n"
                                                        else:
                                                            from_to = f"{mask_account_card(x['from'])} -> {mask_account_card(x['to'])}\n"
                                                        print(
                                                            f"{date_and_description}" f"{from_to}" f"{amount_and_name}"
                                                        )
                                                else:
                                                    return "Некорректный ввод"
                                            else:
                                                return "Некорректный ввод"
                                        else:
                                            return "Некорректный ввод"
                                    else:
                                        return "Некорректный ввод"
                                elif sorting_order.lower() == "по убыванию":
                                    ascending_sort = sorted(sorted_date_list, key=lambda x: x["date"], reverse=True)
                                    only_RUB_transact = input("Выводить только рублевые транзакции?\n" "Да/Нет\n")
                                    if only_RUB_transact:
                                        if only_RUB_transact.lower() == "да":
                                            RUB_transact = [x for x in ascending_sort if x["currency_code"] == "RUB"]
                                            search_word = input(
                                                "Отфильтровать список транзакций по определенному слову в описании?\n"
                                                "Да/Нет\n"
                                            )
                                            if search_word:
                                                if search_word.lower() == "да":
                                                    my_search_word = input("Введите ключевое слово:\n")
                                                    search_transact = src.services.process_bank_search(
                                                        RUB_transact, my_search_word
                                                    )
                                                    print("Распечатываю итоговый список транзакций...\n")
                                                    print(
                                                        f"Всего банковских операций в выборке:{len(search_transact)}\n"
                                                    )
                                                    for x in search_transact:
                                                        date_and_description = (
                                                            f'{get_date(x['date'])} {x["description"]}\n'
                                                        )
                                                        amount_and_name = (
                                                            f'Сумма: {x["amount"]} {x["currency_name"]}\n'
                                                        )
                                                        if x["description"] == "Открытие вклада":
                                                            from_to = f"{mask_account_card(x['to'])}\n"
                                                        else:
                                                            from_to = f"{mask_account_card(x['from'])} -> {mask_account_card(x['to'])}\n"
                                                        print(
                                                            f"{date_and_description}" f"{from_to}" f"{amount_and_name}"
                                                        )
                                                elif search_word.lower() == "нет":
                                                    print("Распечатываю итоговый список транзакций...\n")
                                                    print(f"Всего банковских операций в выборке:{len(RUB_transact)}\n")
                                                    for x in RUB_transact:
                                                        date_and_description = (
                                                            f'{get_date(x['date'])} {x["description"]}\n'
                                                        )
                                                        amount_and_name = (
                                                            f'Сумма: {x["amount"]} {x["currency_name"]}\n'
                                                        )
                                                        if x["description"] == "Открытие вклада":
                                                            from_to = f"{mask_account_card(x['to'])}\n"
                                                        else:
                                                            from_to = f"{mask_account_card(x['from'])} -> {mask_account_card(x['to'])}\n"
                                                        print(
                                                            f"{date_and_description}" f"{from_to}" f"{amount_and_name}"
                                                        )
                                                else:
                                                    return "Некорректный ввод"
                                            else:
                                                return "Некорректный ввод"
                                        elif only_RUB_transact.lower() == "нет":
                                            search_word = input(
                                                "Отфильтровать список транзакций по определенному слову в описании?\n"
                                                "Да/Нет\n"
                                            )
                                            if search_word:
                                                if search_word.lower() == "да":
                                                    my_search_word = input("Введите ключевое слово:\n")
                                                    search_transact = src.services.process_bank_search(
                                                        ascending_sort, my_search_word
                                                    )
                                                    print("Распечатываю итоговый список транзакций...\n")
                                                    print(
                                                        f"Всего банковских операций в выборке:{len(search_transact)}\n"
                                                    )
                                                    for x in search_transact:
                                                        date_and_description = (
                                                            f'{get_date(x['date'])} {x["description"]}\n'
                                                        )
                                                        amount_and_name = (
                                                            f'Сумма: {x["amount"]} {x["currency_name"]}\n'
                                                        )
                                                        if x["description"] == "Открытие вклада":
                                                            from_to = f"{mask_account_card(x['to'])}\n"
                                                        else:
                                                            from_to = f"{mask_account_card(x['from'])} -> {mask_account_card(x['to'])}\n"
                                                        print(
                                                            f"{date_and_description}" f"{from_to}" f"{amount_and_name}"
                                                        )
                                                elif search_word.lower() == "нет":
                                                    print("Распечатываю итоговый список транзакций...\n")
                                                    print(
                                                        f"Всего банковских операций в выборке:{len(ascending_sort)}\n"
                                                    )
                                                    for x in ascending_sort:
                                                        date_and_description = (
                                                            f'{get_date(x['date'])} {x["description"]}\n'
                                                        )
                                                        amount_and_name = (
                                                            f'Сумма: {x["amount"]} {x["currency_name"]}\n'
                                                        )
                                                        if x["description"] == "Открытие вклада":
                                                            from_to = f"{mask_account_card(x['to'])}\n"
                                                        else:
                                                            from_to = f"{mask_account_card(x['from'])} -> {mask_account_card(x['to'])}\n"
                                                        print(
                                                            f"{date_and_description}" f"{from_to}" f"{amount_and_name}"
                                                        )
                                                else:
                                                    return "Некорректный ввод"
                                            else:
                                                return "Некорректный ввод"
                                        else:
                                            return "Некорректный ввод"
                                    else:
                                        return "Некорректный ввод"
                                else:
                                    return "Некорректный ввод"
                            else:
                                return "Некорректный ввод"
                        elif sort_date.lower() == "нет":
                            only_RUB_transact = input("Выводить только рублевые транзакции?\n" "Да/Нет\n")
                            if only_RUB_transact:
                                if only_RUB_transact.lower() == "да":
                                    RUB_transact = [x for x in canceled_list if x["currency_code"] == "RUB"]
                                    search_word = input(
                                        "Отфильтровать список транзакций по определенному слову в описании?\n"
                                        "Да/Нет\n"
                                    )
                                    if search_word:
                                        if search_word.lower() == "да":
                                            my_search_word = input("Введите ключевое слово:\n")
                                            search_transact = src.services.process_bank_search(
                                                RUB_transact, my_search_word
                                            )
                                            print("Распечатываю итоговый список транзакций...\n")
                                            print(f"Всего банковских операций в выборке:{len(search_transact)}\n")
                                            for x in search_transact:
                                                date_and_description = f'{get_date(x['date'])} {x["description"]}\n'
                                                amount_and_name = f'Сумма: {x["amount"]} {x["currency_name"]}\n'
                                                if x["description"] == "Открытие вклада":
                                                    from_to = f"{mask_account_card(x['to'])}\n"
                                                else:
                                                    from_to = f"{mask_account_card(x['from'])} -> {mask_account_card(x['to'])}\n"
                                                print(f"{date_and_description}" f"{from_to}" f"{amount_and_name}")
                                        elif search_word.lower() == "нет":
                                            print("Распечатываю итоговый список транзакций...\n")
                                            print(f"Всего банковских операций в выборке:{len(RUB_transact)}\n")
                                            for x in RUB_transact:
                                                date_and_description = f'{get_date(x['date'])} {x["description"]}\n'
                                                amount_and_name = f'Сумма: {x["amount"]} {x["currency_name"]}\n'
                                                if x["description"] == "Открытие вклада":
                                                    from_to = f"{mask_account_card(x['to'])}\n"
                                                else:
                                                    from_to = f"{mask_account_card(x['from'])} -> {mask_account_card(x['to'])}\n"
                                                print(f"{date_and_description}" f"{from_to}" f"{amount_and_name}")
                                        else:
                                            return "Некорректный ввод"
                                    else:
                                        return "Некорректный ввод"
                                elif only_RUB_transact.lower() == "нет":
                                    search_word = input(
                                        "Отфильтровать список транзакций по определенному слову в описании?\n"
                                        "Да/Нет\n"
                                    )
                                    if search_word:
                                        if search_word.lower() == "да":
                                            my_search_word = input("Введите ключевое слово:\n")
                                            search_transact = src.services.process_bank_search(
                                                canceled_list, my_search_word
                                            )
                                            print("Распечатываю итоговый список транзакций...\n")
                                            print(f"Всего банковских операций в выборке:{len(search_transact)}\n")
                                            for x in search_transact:
                                                date_and_description = f'{get_date(x['date'])} {x["description"]}\n'
                                                amount_and_name = f'Сумма: {x["amount"]} {x["currency_name"]}\n'
                                                if x["description"] == "Открытие вклада":
                                                    from_to = f"{mask_account_card(x['to'])}\n"
                                                else:
                                                    from_to = f"{mask_account_card(x['from'])} -> {mask_account_card(x['to'])}\n"
                                                print(f"{date_and_description}" f"{from_to}" f"{amount_and_name}")
                                        elif search_word.lower() == "нет":
                                            print("Распечатываю итоговый список транзакций...\n")
                                            print(f"Всего банковских операций в выборке:{len(canceled_list)}\n")
                                            for x in canceled_list:
                                                date_and_description = f'{get_date(x['date'])} {x["description"]}\n'
                                                amount_and_name = f'Сумма: {x["amount"]} {x["currency_name"]}\n'
                                                if x["description"] == "Открытие вклада":
                                                    from_to = f"{mask_account_card(x['to'])}\n"
                                                else:
                                                    from_to = f"{mask_account_card(x['from'])} -> {mask_account_card(x['to'])}\n"
                                                print(f"{date_and_description}" f"{from_to}" f"{amount_and_name}")
                                        else:
                                            return "Некорректный ввод"
                                    else:
                                        return "Некорректный ввод"
                                else:
                                    return "Некорректный ввод"
                            else:
                                return "Некорректный ввод"
                        else:
                            return "Некорректный ввод"
                    else:
                        return "Некорректный ввод"
                elif filter_status.upper() == "PENDING":
                    pending_list = [
                        transact for transact in csv_transact for k, v in transact.items() if v == "PENDING"
                    ]
                    sort_date = input("Отсортировать операции по дате?\n" "Да/Нет\n")
                    if sort_date:
                        if sort_date.lower() == "да":
                            sorted_date_list = sorted(pending_list, key=lambda x: x["date"])
                            sorting_order = input("Отсортировать по возрастанию или по убыванию?\n")
                            if sorting_order:
                                if sorting_order.lower() == "по возрастанию":
                                    ascending_sort = sorted(sorted_date_list, key=lambda x: x["date"], reverse=False)
                                    only_RUB_transact = input("Выводить только рублевые транзакции?\n" "Да/Нет\n")
                                    if only_RUB_transact:
                                        if only_RUB_transact.lower() == "да":
                                            RUB_transact = [x for x in ascending_sort if x["currency_code"] == "RUB"]
                                            search_word = input(
                                                "Отфильтровать список транзакций по определенному слову в описании?\n"
                                                "Да/Нет\n"
                                            )
                                            if search_word:
                                                if search_word.lower() == "да":
                                                    my_search_word = input("Введите ключевое слово:\n")
                                                    search_transact = src.services.process_bank_search(
                                                        RUB_transact, my_search_word
                                                    )
                                                    print("Распечатываю итоговый список транзакций...\n")
                                                    print(
                                                        f"Всего банковских операций в выборке:{len(search_transact)}\n"
                                                    )
                                                    if len(search_transact) == 0:
                                                        return "Не найдено ни одной транзакции, подходящей под ваши условия фильтрации"
                                                    else:
                                                        for x in search_transact:
                                                            date_and_description = (
                                                                f'{get_date(x['date'])} {x["description"]}\n'
                                                            )
                                                            amount_and_name = (
                                                                f'Сумма: {x["amount"]} {x["currency_name"]}\n'
                                                            )
                                                            if x["description"] == "Открытие вклада":
                                                                from_to = f"{mask_account_card(x['to'])}\n"
                                                            else:
                                                                from_to = f"{mask_account_card(x['from'])} -> {mask_account_card(x['to'])}\n"
                                                            print(
                                                                f"{date_and_description}"
                                                                f"{from_to}"
                                                                f"{amount_and_name}"
                                                            )
                                                elif search_word.lower() == "нет":
                                                    print("Распечатываю итоговый список транзакций...\n")
                                                    print(f"Всего банковских операций в выборке:{len(RUB_transact)}\n")
                                                    if len(RUB_transact) == 0:
                                                        print(
                                                            "Не найдено ни одной транзакции, подходящей под ваши условия фильтрации"
                                                        )
                                                    else:
                                                        for x in RUB_transact:
                                                            date_and_description = (
                                                                f'{get_date(x['date'])} {x["description"]}\n'
                                                            )
                                                            amount_and_name = (
                                                                f'Сумма: {x["amount"]} {x["currency_name"]}\n'
                                                            )
                                                            if x["description"] == "Открытие вклада":
                                                                from_to = f"{mask_account_card(x['to'])}\n"
                                                            else:
                                                                from_to = f"{mask_account_card(x['from'])} -> {mask_account_card(x['to'])}\n"
                                                            print(
                                                                f"{date_and_description}"
                                                                f"{from_to}"
                                                                f"{amount_and_name}"
                                                            )
                                                else:
                                                    return "Некорректный ввод"
                                            else:
                                                return "Некорректный ввод"
                                        elif only_RUB_transact.lower() == "нет":
                                            search_word = input(
                                                "Отфильтровать список транзакций по определенному слову в описании?\n"
                                                "Да/Нет\n"
                                            )
                                            if search_word:
                                                if search_word.lower() == "да":
                                                    my_search_word = input("Введите ключевое слово:\n")
                                                    search_transact = src.services.process_bank_search(
                                                        ascending_sort, my_search_word
                                                    )
                                                    print("Распечатываю итоговый список транзакций...\n")
                                                    print(
                                                        f"Всего банковских операций в выборке:{len(search_transact)}\n"
                                                    )
                                                    if len(search_transact) == 0:
                                                        print(
                                                            "Не найдено ни одной транзакции, подходящей под ваши условия фильтрации"
                                                        )
                                                    else:
                                                        for x in search_transact:
                                                            date_and_description = (
                                                                f'{get_date(x['date'])} {x["description"]}\n'
                                                            )
                                                            amount_and_name = (
                                                                f'Сумма: {x["amount"]} {x["currency_name"]}\n'
                                                            )
                                                            if x["description"] == "Открытие вклада":
                                                                from_to = f"{mask_account_card(x['to'])}\n"
                                                            else:
                                                                from_to = f"{mask_account_card(x['from'])} -> {mask_account_card(x['to'])}\n"
                                                            print(
                                                                f"{date_and_description}"
                                                                f"{from_to}"
                                                                f"{amount_and_name}"
                                                            )
                                                elif search_word.lower() == "нет":
                                                    print("Распечатываю итоговый список транзакций...\n")
                                                    print(
                                                        f"Всего банковских операций в выборке:{len(ascending_sort)}\n"
                                                    )
                                                    if len(ascending_sort) == 0:
                                                        print(
                                                            "Не найдено ни одной транзакции, подходящей под ваши условия фильтрации"
                                                        )
                                                    else:
                                                        for x in ascending_sort:
                                                            date_and_description = (
                                                                f'{get_date(x['date'])} {x["description"]}\n'
                                                            )
                                                            amount_and_name = (
                                                                f'Сумма: {x["amount"]} {x["currency_name"]}\n'
                                                            )
                                                            if x["description"] == "Открытие вклада":
                                                                from_to = f"{mask_account_card(x['to'])}\n"
                                                            else:
                                                                from_to = f"{mask_account_card(x['from'])} -> {mask_account_card(x['to'])}\n"
                                                            print(
                                                                f"{date_and_description}"
                                                                f"{from_to}"
                                                                f"{amount_and_name}"
                                                            )
                                                else:
                                                    return "Некорректный ввод"
                                            else:
                                                return "Некорректный ввод"
                                        else:
                                            return "Некорректный ввод"
                                    else:
                                        return "Некорректный ввод"
                                elif sorting_order.lower() == "по убыванию":
                                    ascending_sort = sorted(sorted_date_list, key=lambda x: x["date"], reverse=True)
                                    only_RUB_transact = input("Выводить только рублевые транзакции?\n" "Да/Нет\n")
                                    if only_RUB_transact:
                                        if only_RUB_transact.lower() == "да":
                                            RUB_transact = [x for x in ascending_sort if x["currency_code"] == "RUB"]
                                            search_word = input(
                                                "Отфильтровать список транзакций по определенному слову в описании?\n"
                                                "Да/Нет\n"
                                            )
                                            if search_word:
                                                if search_word.lower() == "да":
                                                    my_search_word = input("Введите ключевое слово:\n")
                                                    search_transact = src.services.process_bank_search(
                                                        RUB_transact, my_search_word
                                                    )
                                                    print("Распечатываю итоговый список транзакций...\n")
                                                    print(
                                                        f"Всего банковских операций в выборке:{len(search_transact)}\n"
                                                    )
                                                    if len(search_transact) == 0:
                                                        print(
                                                            "Не найдено ни одной транзакции, подходящей под ваши условия фильтрации"
                                                        )
                                                    else:
                                                        for x in search_transact:
                                                            date_and_description = (
                                                                f'{get_date(x['date'])} {x["description"]}\n'
                                                            )
                                                            amount_and_name = (
                                                                f'Сумма: {x["amount"]} {x["currency_name"]}\n'
                                                            )
                                                            if x["description"] == "Открытие вклада":
                                                                from_to = f"{mask_account_card(x['to'])}\n"
                                                            else:
                                                                from_to = f"{mask_account_card(x['from'])} -> {mask_account_card(x['to'])}\n"
                                                            print(
                                                                f"{date_and_description}"
                                                                f"{from_to}"
                                                                f"{amount_and_name}"
                                                            )
                                                elif search_word.lower() == "нет":
                                                    print("Распечатываю итоговый список транзакций...\n")
                                                    print(f"Всего банковских операций в выборке:{len(RUB_transact)}\n")
                                                    if len(RUB_transact) == 0:
                                                        print(
                                                            "Не найдено ни одной транзакции, подходящей под ваши условия фильтрации"
                                                        )
                                                    else:
                                                        for x in RUB_transact:
                                                            date_and_description = (
                                                                f'{get_date(x['date'])} {x["description"]}\n'
                                                            )
                                                            amount_and_name = (
                                                                f'Сумма: {x["amount"]} {x["currency_name"]}\n'
                                                            )
                                                            if x["description"] == "Открытие вклада":
                                                                from_to = f"{mask_account_card(x['to'])}\n"
                                                            else:
                                                                from_to = f"{mask_account_card(x['from'])} -> {mask_account_card(x['to'])}\n"
                                                            print(
                                                                f"{date_and_description}"
                                                                f"{from_to}"
                                                                f"{amount_and_name}"
                                                            )
                                                else:
                                                    return "Некорректный ввод"
                                            else:
                                                return "Некорректный ввод"
                                        elif only_RUB_transact.lower() == "нет":
                                            search_word = input(
                                                "Отфильтровать список транзакций по определенному слову в описании?\n"
                                                "Да/Нет\n"
                                            )
                                            if search_word:
                                                if search_word.lower() == "да":
                                                    my_search_word = input("Введите ключевое слово:\n")
                                                    search_transact = src.services.process_bank_search(
                                                        ascending_sort, my_search_word
                                                    )
                                                    print("Распечатываю итоговый список транзакций...\n")
                                                    print(
                                                        f"Всего банковских операций в выборке:{len(search_transact)}\n"
                                                    )
                                                    if len(search_transact) == 0:
                                                        print(
                                                            "Не найдено ни одной транзакции, подходящей под ваши условия фильтрации"
                                                        )
                                                    else:
                                                        for x in search_transact:
                                                            date_and_description = (
                                                                f'{get_date(x['date'])} {x["description"]}\n'
                                                            )
                                                            amount_and_name = (
                                                                f'Сумма: {x["amount"]} {x["currency_name"]}\n'
                                                            )
                                                            if x["description"] == "Открытие вклада":
                                                                from_to = f"{mask_account_card(x['to'])}\n"
                                                            else:
                                                                from_to = f"{mask_account_card(x['from'])} -> {mask_account_card(x['to'])}\n"
                                                            print(
                                                                f"{date_and_description}"
                                                                f"{from_to}"
                                                                f"{amount_and_name}"
                                                            )
                                                elif search_word.lower() == "нет":
                                                    print("Распечатываю итоговый список транзакций...\n")
                                                    print(
                                                        f"Всего банковских операций в выборке:{len(ascending_sort)}\n"
                                                    )
                                                    if len(ascending_sort) == 0:
                                                        print(
                                                            "Не найдено ни одной транзакции, подходящей под ваши условия фильтрации"
                                                        )
                                                    else:
                                                        for x in ascending_sort:
                                                            date_and_description = (
                                                                f'{get_date(x['date'])} {x["description"]}\n'
                                                            )
                                                            amount_and_name = (
                                                                f'Сумма: {x["amount"]} {x["currency_name"]}\n'
                                                            )
                                                            if x["description"] == "Открытие вклада":
                                                                from_to = f"{mask_account_card(x['to'])}\n"
                                                            else:
                                                                from_to = f"{mask_account_card(x['from'])} -> {mask_account_card(x['to'])}\n"
                                                            print(
                                                                f"{date_and_description}"
                                                                f"{from_to}"
                                                                f"{amount_and_name}"
                                                            )
                                                else:
                                                    return "Некорректный ввод"
                                            else:
                                                return "Некорректный ввод"
                                        else:
                                            return "Некорректный ввод"
                                    else:
                                        return "Некорректный ввод"
                                else:
                                    return "Некорректный ввод"
                            else:
                                return "Некорректный ввод"
                        elif sort_date.lower() == "нет":
                            only_RUB_transact = input("Выводить только рублевые транзакции?\n" "Да/Нет\n")
                            if only_RUB_transact:
                                if only_RUB_transact.lower() == "да":
                                    RUB_transact = [x for x in pending_list if x["currency_code"] == "RUB"]
                                    search_word = input(
                                        "Отфильтровать список транзакций по определенному слову в описании?\n"
                                        "Да/Нет\n"
                                    )
                                    if search_word:
                                        if search_word.lower() == "да":
                                            my_search_word = input("Введите ключевое слово:\n")
                                            search_transact = src.services.process_bank_search(
                                                RUB_transact, my_search_word
                                            )
                                            print("Распечатываю итоговый список транзакций...\n")
                                            print(f"Всего банковских операций в выборке:{len(search_transact)}\n")
                                            if len(search_transact) == 0:
                                                print(
                                                    "Не найдено ни одной транзакции, подходящей под ваши условия фильтрации"
                                                )
                                            else:
                                                for x in search_transact:
                                                    date_and_description = (
                                                        f'{get_date(x['date'])} {x["description"]}\n'
                                                    )
                                                    amount_and_name = f'Сумма: {x["amount"]} {x["currency_name"]}\n'
                                                    if x["description"] == "Открытие вклада":
                                                        from_to = f"{mask_account_card(x['to'])}\n"
                                                    else:
                                                        from_to = f"{mask_account_card(x['from'])} -> {mask_account_card(x['to'])}\n"
                                                    print(f"{date_and_description}" f"{from_to}" f"{amount_and_name}")
                                        elif search_word.lower() == "нет":
                                            print("Распечатываю итоговый список транзакций...\n")
                                            print(f"Всего банковских операций в выборке:{len(RUB_transact)}\n")
                                            if len(RUB_transact) == 0:
                                                print(
                                                    "Не найдено ни одной транзакции, подходящей под ваши условия фильтрации"
                                                )
                                            else:
                                                for x in RUB_transact:
                                                    date_and_description = (
                                                        f'{get_date(x['date'])} {x["description"]}\n'
                                                    )
                                                    amount_and_name = f'Сумма: {x["amount"]} {x["currency_name"]}\n'
                                                    if x["description"] == "Открытие вклада":
                                                        from_to = f"{mask_account_card(x['to'])}\n"
                                                    else:
                                                        from_to = f"{mask_account_card(x['from'])} -> {mask_account_card(x['to'])}\n"
                                                    print(f"{date_and_description}" f"{from_to}" f"{amount_and_name}")
                                        else:
                                            return "Некорректный ввод"
                                    else:
                                        return "Некорректный ввод"
                                elif only_RUB_transact.lower() == "нет":
                                    search_word = input(
                                        "Отфильтровать список транзакций по определенному слову в описании?\n"
                                        "Да/Нет\n"
                                    )
                                    if search_word:
                                        if search_word.lower() == "да":
                                            my_search_word = input("Введите ключевое слово:\n")
                                            search_transact = src.services.process_bank_search(
                                                pending_list, my_search_word
                                            )
                                            print("Распечатываю итоговый список транзакций...\n")
                                            print(f"Всего банковских операций в выборке:{len(search_transact)}\n")
                                            if len(search_transact) == 0:
                                                print(
                                                    "Не найдено ни одной транзакции, подходящей под ваши условия фильтрации"
                                                )
                                            else:
                                                for x in search_transact:
                                                    date_and_description = (
                                                        f'{get_date(x['date'])} {x["description"]}\n'
                                                    )
                                                    amount_and_name = f'Сумма: {x["amount"]} {x["currency_name"]}\n'
                                                    if x["description"] == "Открытие вклада":
                                                        from_to = f"{mask_account_card(x['to'])}\n"
                                                    else:
                                                        from_to = f"{mask_account_card(x['from'])} -> {mask_account_card(x['to'])}\n"
                                                    print(f"{date_and_description}" f"{from_to}" f"{amount_and_name}")
                                        elif search_word.lower() == "нет":
                                            print("Распечатываю итоговый список транзакций...\n")
                                            print(f"Всего банковских операций в выборке:{len(pending_list)}\n")
                                            if len(pending_list) == 0:
                                                print(
                                                    "Не найдено ни одной транзакции, подходящей под ваши условия фильтрации"
                                                )
                                            else:
                                                for x in pending_list:
                                                    date_and_description = (
                                                        f'{get_date(x['date'])} {x["description"]}\n'
                                                    )
                                                    amount_and_name = f'Сумма: {x["amount"]} {x["currency_name"]}\n'
                                                    if x["description"] == "Открытие вклада":
                                                        from_to = f"{mask_account_card(x['to'])}\n"
                                                    else:
                                                        from_to = f"{mask_account_card(x['from'])} -> {mask_account_card(x['to'])}\n"
                                                    print(f"{date_and_description}" f"{from_to}" f"{amount_and_name}")
                                        else:
                                            return "Некорректный ввод"
                                    else:
                                        return "Некорректный ввод"
                                else:
                                    return "Некорректный ввод"
                            else:
                                return "Некорректный ввод"
                        else:
                            return "Некорректный ввод"
                    else:
                        return "Некорректный ввод"
                else:
                    return "Некорректный ввод"
        elif file_selection.lower() == "3":
            print("Для обработки выбран XLSX-файл.\n")
            excel_transact = src.import_data.get_excel_data("transactions_excel.xlsx")
            filter_status = input(
                "Введите статус, по которому необходимо выполнить фильтрацию.\n"
                "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n"
            )
            if filter_status:
                if filter_status.upper() == "EXECUTED":
                    executed_list = [
                        transact for transact in excel_transact for k, v in transact.items() if v == "EXECUTED"
                    ]
                    sort_date = input("Отсортировать операции по дате?\n" "Да/Нет\n")
                    if sort_date:
                        if sort_date.lower() == "да":
                            sorted_date_list = sorted(executed_list, key=lambda x: x["date"])
                            sorting_order = input("Отсортировать по возрастанию или по убыванию?\n")
                            if sorting_order:
                                if sorting_order.lower() == "по возрастанию":
                                    ascending_sort = sorted(sorted_date_list, key=lambda x: x["date"], reverse=False)
                                    only_RUB_transact = input("Выводить только рублевые транзакции?\n" "Да/Нет\n")
                                    if only_RUB_transact:
                                        if only_RUB_transact.lower() == "да":
                                            RUB_transact = [x for x in ascending_sort if x["currency_code"] == "RUB"]
                                            search_word = input(
                                                "Отфильтровать список транзакций по определенному слову в описании?\n"
                                                "Да/Нет\n"
                                            )
                                            if search_word:
                                                if search_word.lower() == "да":
                                                    my_search_word = input("Введите ключевое слово:\n")
                                                    search_transact = src.services.process_bank_search(
                                                        RUB_transact, my_search_word
                                                    )
                                                    print("Распечатываю итоговый список транзакций...\n")
                                                    print(
                                                        f"Всего банковских операций в выборке:{len(search_transact)}\n"
                                                    )
                                                    for x in search_transact:
                                                        date_and_description = (
                                                            f'{get_date(x['date'])} {x["description"]}\n'
                                                        )
                                                        amount_and_name = (
                                                            f'Сумма: {x["amount"]} {x["currency_name"]}\n'
                                                        )
                                                        if x["description"] == "Открытие вклада":
                                                            from_to = f"{mask_account_card(x['to'])}\n"
                                                        else:
                                                            from_to = f"{mask_account_card(x['from'])} -> {mask_account_card(x['to'])}\n"
                                                        print(
                                                            f"{date_and_description}" f"{from_to}" f"{amount_and_name}"
                                                        )
                                                elif search_word.lower() == "нет":
                                                    print("Распечатываю итоговый список транзакций...\n")
                                                    print(f"Всего банковских операций в выборке:{len(RUB_transact)}\n")
                                                    for x in RUB_transact:
                                                        date_and_description = (
                                                            f'{get_date(x['date'])} {x["description"]}\n'
                                                        )
                                                        amount_and_name = (
                                                            f'Сумма: {x["amount"]} {x["currency_name"]}\n'
                                                        )
                                                        if x["description"] == "Открытие вклада":
                                                            from_to = f"{mask_account_card(x['to'])}\n"
                                                        else:
                                                            from_to = f"{mask_account_card(x['from'])} -> {mask_account_card(x['to'])}\n"
                                                        print(
                                                            f"{date_and_description}" f"{from_to}" f"{amount_and_name}"
                                                        )
                                                else:
                                                    return "Некорректный ввод"
                                            else:
                                                return "Некорректный ввод"
                                        elif only_RUB_transact.lower() == "нет":
                                            search_word = input(
                                                "Отфильтровать список транзакций по определенному слову в описании?\n"
                                                "Да/Нет\n"
                                            )
                                            if search_word:
                                                if search_word.lower() == "да":
                                                    my_search_word = input("Введите ключевое слово:\n")
                                                    search_transact = src.services.process_bank_search(
                                                        ascending_sort, my_search_word
                                                    )
                                                    print("Распечатываю итоговый список транзакций...\n")
                                                    print(
                                                        f"Всего банковских операций в выборке:{len(search_transact)}\n"
                                                    )
                                                    for x in search_transact:
                                                        date_and_description = (
                                                            f'{get_date(x['date'])} {x["description"]}\n'
                                                        )
                                                        amount_and_name = (
                                                            f'Сумма: {x["amount"]} {x["currency_name"]}\n'
                                                        )
                                                        if x["description"] == "Открытие вклада":
                                                            from_to = f"{mask_account_card(x['to'])}\n"
                                                        else:
                                                            from_to = f"{mask_account_card(x['from'])} -> {mask_account_card(x['to'])}\n"
                                                        print(
                                                            f"{date_and_description}" f"{from_to}" f"{amount_and_name}"
                                                        )
                                                elif search_word.lower() == "нет":
                                                    print("Распечатываю итоговый список транзакций...\n")
                                                    print(
                                                        f"Всего банковских операций в выборке:{len(ascending_sort)}\n"
                                                    )
                                                    for x in ascending_sort:
                                                        date_and_description = (
                                                            f'{get_date(x['date'])} {x["description"]}\n'
                                                        )
                                                        amount_and_name = (
                                                            f'Сумма: {x["amount"]} {x["currency_name"]}\n'
                                                        )
                                                        if x["description"] == "Открытие вклада":
                                                            from_to = f"{mask_account_card(x['to'])}\n"
                                                        else:
                                                            from_to = f"{mask_account_card(x['from'])} -> {mask_account_card(x['to'])}\n"
                                                        print(
                                                            f"{date_and_description}" f"{from_to}" f"{amount_and_name}"
                                                        )
                                                else:
                                                    return "Некорректный ввод"
                                            else:
                                                return "Некорректный ввод"
                                        else:
                                            return "Некорректный ввод"
                                    else:
                                        return "Некорректный ввод"
                                elif sorting_order.lower() == "по убыванию":
                                    ascending_sort = sorted(sorted_date_list, key=lambda x: x["date"], reverse=True)
                                    only_RUB_transact = input("Выводить только рублевые транзакции?\n" "Да/Нет\n")
                                    if only_RUB_transact:
                                        if only_RUB_transact.lower() == "да":
                                            RUB_transact = [x for x in ascending_sort if x["currency_code"] == "RUB"]
                                            search_word = input(
                                                "Отфильтровать список транзакций по определенному слову в описании?\n"
                                                "Да/Нет\n"
                                            )
                                            if search_word:
                                                if search_word.lower() == "да":
                                                    my_search_word = input("Введите ключевое слово:\n")
                                                    search_transact = src.services.process_bank_search(
                                                        RUB_transact, my_search_word
                                                    )
                                                    print("Распечатываю итоговый список транзакций...\n")
                                                    print(
                                                        f"Всего банковских операций в выборке:{len(search_transact)}\n"
                                                    )
                                                    for x in search_transact:
                                                        date_and_description = (
                                                            f'{get_date(x['date'])} {x["description"]}\n'
                                                        )
                                                        amount_and_name = (
                                                            f'Сумма: {x["amount"]} {x["currency_name"]}\n'
                                                        )
                                                        if x["description"] == "Открытие вклада":
                                                            from_to = f"{mask_account_card(x['to'])}\n"
                                                        else:
                                                            from_to = f"{mask_account_card(x['from'])} -> {mask_account_card(x['to'])}\n"
                                                        print(
                                                            f"{date_and_description}" f"{from_to}" f"{amount_and_name}"
                                                        )
                                                elif search_word.lower() == "нет":
                                                    print("Распечатываю итоговый список транзакций...\n")
                                                    print(f"Всего банковских операций в выборке:{len(RUB_transact)}\n")
                                                    for x in RUB_transact:
                                                        date_and_description = (
                                                            f'{get_date(x['date'])} {x["description"]}\n'
                                                        )
                                                        amount_and_name = (
                                                            f'Сумма: {x["amount"]} {x["currency_name"]}\n'
                                                        )
                                                        if x["description"] == "Открытие вклада":
                                                            from_to = f"{mask_account_card(x['to'])}\n"
                                                        else:
                                                            from_to = f"{mask_account_card(x['from'])} -> {mask_account_card(x['to'])}\n"
                                                        print(
                                                            f"{date_and_description}" f"{from_to}" f"{amount_and_name}"
                                                        )
                                                else:
                                                    return "Некорректный ввод"
                                            else:
                                                return "Некорректный ввод"
                                        elif only_RUB_transact.lower() == "нет":
                                            search_word = input(
                                                "Отфильтровать список транзакций по определенному слову в описании?\n"
                                                "Да/Нет\n"
                                            )
                                            if search_word:
                                                if search_word.lower() == "да":
                                                    my_search_word = input("Введите ключевое слово:\n")
                                                    search_transact = src.services.process_bank_search(
                                                        ascending_sort, my_search_word
                                                    )
                                                    print("Распечатываю итоговый список транзакций...\n")
                                                    print(
                                                        f"Всего банковских операций в выборке:{len(search_transact)}\n"
                                                    )
                                                    for x in search_transact:
                                                        date_and_description = (
                                                            f'{get_date(x['date'])} {x["description"]}\n'
                                                        )
                                                        amount_and_name = (
                                                            f'Сумма: {x["amount"]} {x["currency_name"]}\n'
                                                        )
                                                        if x["description"] == "Открытие вклада":
                                                            from_to = f"{mask_account_card(x['to'])}\n"
                                                        else:
                                                            from_to = f"{mask_account_card(x['from'])} -> {mask_account_card(x['to'])}\n"
                                                        print(
                                                            f"{date_and_description}" f"{from_to}" f"{amount_and_name}"
                                                        )
                                                elif search_word.lower() == "нет":
                                                    print("Распечатываю итоговый список транзакций...\n")
                                                    print(
                                                        f"Всего банковских операций в выборке:{len(ascending_sort)}\n"
                                                    )
                                                    for x in ascending_sort:
                                                        date_and_description = (
                                                            f'{get_date(x['date'])} {x["description"]}\n'
                                                        )
                                                        amount_and_name = (
                                                            f'Сумма: {x["amount"]} {x["currency_name"]}\n'
                                                        )
                                                        if x["description"] == "Открытие вклада":
                                                            from_to = f"{mask_account_card(x['to'])}\n"
                                                        else:
                                                            from_to = f"{mask_account_card(x['from'])} -> {mask_account_card(x['to'])}\n"
                                                        print(
                                                            f"{date_and_description}" f"{from_to}" f"{amount_and_name}"
                                                        )
                                                else:
                                                    return "Некорректный ввод"
                                            else:
                                                return "Некорректный ввод"
                                        else:
                                            return "Некорректный ввод"
                                    else:
                                        return "Некорректный ввод"
                                else:
                                    return "Некорректный ввод"
                            else:
                                return "Некорректный ввод"
                        elif sort_date.lower() == "нет":
                            only_RUB_transact = input("Выводить только рублевые транзакции?\n" "Да/Нет\n")
                            if only_RUB_transact:
                                if only_RUB_transact.lower() == "да":
                                    RUB_transact = [x for x in executed_list if x["currency_code"] == "RUB"]
                                    search_word = input(
                                        "Отфильтровать список транзакций по определенному слову в описании?\n"
                                        "Да/Нет\n"
                                    )
                                    if search_word:
                                        if search_word.lower() == "да":
                                            my_search_word = input("Введите ключевое слово:\n")
                                            search_transact = src.services.process_bank_search(
                                                RUB_transact, my_search_word
                                            )
                                            print("Распечатываю итоговый список транзакций...\n")
                                            print(f"Всего банковских операций в выборке:{len(search_transact)}\n")
                                            for x in search_transact:
                                                date_and_description = f'{get_date(x['date'])} {x["description"]}\n'
                                                amount_and_name = f'Сумма: {x["amount"]} {x["currency_name"]}\n'
                                                if x["description"] == "Открытие вклада":
                                                    from_to = f"{mask_account_card(x['to'])}\n"
                                                else:
                                                    from_to = f"{mask_account_card(x['from'])} -> {mask_account_card(x['to'])}\n"
                                                print(f"{date_and_description}" f"{from_to}" f"{amount_and_name}")
                                        elif search_word.lower() == "нет":
                                            print("Распечатываю итоговый список транзакций...\n")
                                            print(f"Всего банковских операций в выборке:{len(RUB_transact)}\n")
                                            for x in RUB_transact:
                                                date_and_description = f'{get_date(x['date'])} {x["description"]}\n'
                                                amount_and_name = f'Сумма: {x["amount"]} {x["currency_name"]}\n'
                                                if x["description"] == "Открытие вклада":
                                                    from_to = f"{mask_account_card(x['to'])}\n"
                                                else:
                                                    from_to = f"{mask_account_card(x['from'])} -> {mask_account_card(x['to'])}\n"
                                                print(f"{date_and_description}" f"{from_to}" f"{amount_and_name}")
                                        else:
                                            return "Некорректный ввод"
                                    else:
                                        return "Некорректный ввод"
                                elif only_RUB_transact.lower() == "нет":
                                    search_word = input(
                                        "Отфильтровать список транзакций по определенному слову в описании?\n"
                                        "Да/Нет\n"
                                    )
                                    if search_word:
                                        if search_word.lower() == "да":
                                            my_search_word = input("Введите ключевое слово:\n")
                                            search_transact = src.services.process_bank_search(
                                                executed_list, my_search_word
                                            )
                                            print("Распечатываю итоговый список транзакций...\n")
                                            print(f"Всего банковских операций в выборке:{len(search_transact)}\n")
                                            for x in search_transact:
                                                date_and_description = f'{get_date(x['date'])} {x["description"]}\n'
                                                amount_and_name = f'Сумма: {x["amount"]} {x["currency_name"]}\n'
                                                if x["description"] == "Открытие вклада":
                                                    from_to = f"{mask_account_card(x['to'])}\n"
                                                else:
                                                    from_to = f"{mask_account_card(x['from'])} -> {mask_account_card(x['to'])}\n"
                                                print(f"{date_and_description}" f"{from_to}" f"{amount_and_name}")
                                        elif search_word.lower() == "нет":
                                            print("Распечатываю итоговый список транзакций...\n")
                                            print(f"Всего банковских операций в выборке:{len(executed_list)}\n")
                                            for x in executed_list:
                                                date_and_description = f'{get_date(x['date'])} {x["description"]}\n'
                                                amount_and_name = f'Сумма: {x["amount"]} {x["currency_name"]}\n'
                                                if x["description"] == "Открытие вклада":
                                                    from_to = f"{mask_account_card(x['to'])}\n"
                                                else:
                                                    from_to = f"{mask_account_card(x['from'])} -> {mask_account_card(x['to'])}\n"
                                                print(f"{date_and_description}" f"{from_to}" f"{amount_and_name}")
                                        else:
                                            return "Некорректный ввод"
                                    else:
                                        return "Некорректный ввод"
                                else:
                                    return "Некорректный ввод"
                            else:
                                return "Некорректный ввод"
                        else:
                            return "Некорректный ввод"
                    else:
                        return "Некорректный ввод"
                elif filter_status.upper() == "CANCELED":
                    canceled_list = [
                        transact for transact in excel_transact for k, v in transact.items() if v == "CANCELED"
                    ]
                    sort_date = input("Отсортировать операции по дате?\n" "Да/Нет\n")
                    if sort_date:
                        if sort_date.lower() == "да":
                            sorted_date_list = sorted(canceled_list, key=lambda x: x["date"])
                            sorting_order = input("Отсортировать по возрастанию или по убыванию?\n")
                            if sorting_order:
                                if sorting_order.lower() == "по возрастанию":
                                    ascending_sort = sorted(sorted_date_list, key=lambda x: x["date"], reverse=False)
                                    only_RUB_transact = input("Выводить только рублевые транзакции?\n" "Да/Нет\n")
                                    if only_RUB_transact:
                                        if only_RUB_transact.lower() == "да":
                                            RUB_transact = [x for x in ascending_sort if x["currency_code"] == "RUB"]
                                            search_word = input(
                                                "Отфильтровать список транзакций по определенному слову в описании?\n"
                                                "Да/Нет\n"
                                            )
                                            if search_word:
                                                if search_word.lower() == "да":
                                                    my_search_word = input("Введите ключевое слово:\n")
                                                    search_transact = src.services.process_bank_search(
                                                        RUB_transact, my_search_word
                                                    )
                                                    print("Распечатываю итоговый список транзакций...\n")
                                                    print(
                                                        f"Всего банковских операций в выборке:{len(search_transact)}\n"
                                                    )
                                                    for x in search_transact:
                                                        date_and_description = (
                                                            f'{get_date(x['date'])} {x["description"]}\n'
                                                        )
                                                        amount_and_name = (
                                                            f'Сумма: {x["amount"]} {x["currency_name"]}\n'
                                                        )
                                                        if x["description"] == "Открытие вклада":
                                                            from_to = f"{mask_account_card(x['to'])}\n"
                                                        else:
                                                            from_to = f"{mask_account_card(x['from'])} -> {mask_account_card(x['to'])}\n"
                                                        print(
                                                            f"{date_and_description}" f"{from_to}" f"{amount_and_name}"
                                                        )
                                                elif search_word.lower() == "нет":
                                                    print("Распечатываю итоговый список транзакций...\n")
                                                    print(f"Всего банковских операций в выборке:{len(RUB_transact)}\n")
                                                    for x in RUB_transact:
                                                        date_and_description = (
                                                            f'{get_date(x['date'])} {x["description"]}\n'
                                                        )
                                                        amount_and_name = (
                                                            f'Сумма: {x["amount"]} {x["currency_name"]}\n'
                                                        )
                                                        if x["description"] == "Открытие вклада":
                                                            from_to = f"{mask_account_card(x['to'])}\n"
                                                        else:
                                                            from_to = f"{mask_account_card(x['from'])} -> {mask_account_card(x['to'])}\n"
                                                        print(
                                                            f"{date_and_description}" f"{from_to}" f"{amount_and_name}"
                                                        )
                                                else:
                                                    return "Некорректный ввод"
                                            else:
                                                return "Некорректный ввод"
                                        elif only_RUB_transact.lower() == "нет":
                                            search_word = input(
                                                "Отфильтровать список транзакций по определенному слову в описании?\n"
                                                "Да/Нет\n"
                                            )
                                            if search_word:
                                                if search_word.lower() == "да":
                                                    my_search_word = input("Введите ключевое слово:\n")
                                                    search_transact = src.services.process_bank_search(
                                                        ascending_sort, my_search_word
                                                    )
                                                    print("Распечатываю итоговый список транзакций...\n")
                                                    print(
                                                        f"Всего банковских операций в выборке:{len(search_transact)}\n"
                                                    )
                                                    for x in search_transact:
                                                        date_and_description = (
                                                            f'{get_date(x['date'])} {x["description"]}\n'
                                                        )
                                                        amount_and_name = (
                                                            f'Сумма: {x["amount"]} {x["currency_name"]}\n'
                                                        )
                                                        if x["description"] == "Открытие вклада":
                                                            from_to = f"{mask_account_card(x['to'])}\n"
                                                        else:
                                                            from_to = f"{mask_account_card(x['from'])} -> {mask_account_card(x['to'])}\n"
                                                        print(
                                                            f"{date_and_description}" f"{from_to}" f"{amount_and_name}"
                                                        )
                                                elif search_word.lower() == "нет":
                                                    print("Распечатываю итоговый список транзакций...\n")
                                                    print(
                                                        f"Всего банковских операций в выборке:{len(ascending_sort)}\n"
                                                    )
                                                    for x in ascending_sort:
                                                        date_and_description = (
                                                            f'{get_date(x['date'])} {x["description"]}\n'
                                                        )
                                                        amount_and_name = (
                                                            f'Сумма: {x["amount"]} {x["currency_name"]}\n'
                                                        )
                                                        if x["description"] == "Открытие вклада":
                                                            from_to = f"{mask_account_card(x['to'])}\n"
                                                        else:
                                                            from_to = f"{mask_account_card(x['from'])} -> {mask_account_card(x['to'])}\n"
                                                        print(
                                                            f"{date_and_description}" f"{from_to}" f"{amount_and_name}"
                                                        )
                                                else:
                                                    return "Некорректный ввод"
                                            else:
                                                return "Некорректный ввод"
                                        else:
                                            return "Некорректный ввод"
                                    else:
                                        return "Некорректный ввод"
                                elif sorting_order.lower() == "по убыванию":
                                    ascending_sort = sorted(sorted_date_list, key=lambda x: x["date"], reverse=True)
                                    only_RUB_transact = input("Выводить только рублевые транзакции?\n" "Да/Нет\n")
                                    if only_RUB_transact:
                                        if only_RUB_transact.lower() == "да":
                                            RUB_transact = [x for x in ascending_sort if x["currency_code"] == "RUB"]
                                            search_word = input(
                                                "Отфильтровать список транзакций по определенному слову в описании?\n"
                                                "Да/Нет\n"
                                            )
                                            if search_word:
                                                if search_word.lower() == "да":
                                                    my_search_word = input("Введите ключевое слово:\n")
                                                    search_transact = src.services.process_bank_search(
                                                        RUB_transact, my_search_word
                                                    )
                                                    print("Распечатываю итоговый список транзакций...\n")
                                                    print(
                                                        f"Всего банковских операций в выборке:{len(search_transact)}\n"
                                                    )
                                                    for x in search_transact:
                                                        date_and_description = (
                                                            f'{get_date(x['date'])} {x["description"]}\n'
                                                        )
                                                        amount_and_name = (
                                                            f'Сумма: {x["amount"]} {x["currency_name"]}\n'
                                                        )
                                                        if x["description"] == "Открытие вклада":
                                                            from_to = f"{mask_account_card(x['to'])}\n"
                                                        else:
                                                            from_to = f"{mask_account_card(x['from'])} -> {mask_account_card(x['to'])}\n"
                                                        print(
                                                            f"{date_and_description}" f"{from_to}" f"{amount_and_name}"
                                                        )
                                                elif search_word.lower() == "нет":
                                                    print("Распечатываю итоговый список транзакций...\n")
                                                    print(f"Всего банковских операций в выборке:{len(RUB_transact)}\n")
                                                    for x in RUB_transact:
                                                        date_and_description = (
                                                            f'{get_date(x['date'])} {x["description"]}\n'
                                                        )
                                                        amount_and_name = (
                                                            f'Сумма: {x["amount"]} {x["currency_name"]}\n'
                                                        )
                                                        if x["description"] == "Открытие вклада":
                                                            from_to = f"{mask_account_card(x['to'])}\n"
                                                        else:
                                                            from_to = f"{mask_account_card(x['from'])} -> {mask_account_card(x['to'])}\n"
                                                        print(
                                                            f"{date_and_description}" f"{from_to}" f"{amount_and_name}"
                                                        )
                                                else:
                                                    return "Некорректный ввод"
                                            else:
                                                return "Некорректный ввод"
                                        elif only_RUB_transact.lower() == "нет":
                                            search_word = input(
                                                "Отфильтровать список транзакций по определенному слову в описании?\n"
                                                "Да/Нет\n"
                                            )
                                            if search_word:
                                                if search_word.lower() == "да":
                                                    my_search_word = input("Введите ключевое слово:\n")
                                                    search_transact = src.services.process_bank_search(
                                                        ascending_sort, my_search_word
                                                    )
                                                    print("Распечатываю итоговый список транзакций...\n")
                                                    print(
                                                        f"Всего банковских операций в выборке:{len(search_transact)}\n"
                                                    )
                                                    for x in search_transact:
                                                        date_and_description = (
                                                            f'{get_date(x['date'])} {x["description"]}\n'
                                                        )
                                                        amount_and_name = (
                                                            f'Сумма: {x["amount"]} {x["currency_name"]}\n'
                                                        )
                                                        if x["description"] == "Открытие вклада":
                                                            from_to = f"{mask_account_card(x['to'])}\n"
                                                        else:
                                                            from_to = f"{mask_account_card(x['from'])} -> {mask_account_card(x['to'])}\n"
                                                        print(
                                                            f"{date_and_description}" f"{from_to}" f"{amount_and_name}"
                                                        )
                                                elif search_word.lower() == "нет":
                                                    print("Распечатываю итоговый список транзакций...\n")
                                                    print(
                                                        f"Всего банковских операций в выборке:{len(ascending_sort)}\n"
                                                    )
                                                    for x in ascending_sort:
                                                        date_and_description = (
                                                            f'{get_date(x['date'])} {x["description"]}\n'
                                                        )
                                                        amount_and_name = (
                                                            f'Сумма: {x["amount"]} {x["currency_name"]}\n'
                                                        )
                                                        if x["description"] == "Открытие вклада":
                                                            from_to = f"{mask_account_card(x['to'])}\n"
                                                        else:
                                                            from_to = f"{mask_account_card(x['from'])} -> {mask_account_card(x['to'])}\n"
                                                        print(
                                                            f"{date_and_description}" f"{from_to}" f"{amount_and_name}"
                                                        )
                                                else:
                                                    return "Некорректный ввод"
                                            else:
                                                return "Некорректный ввод"
                                        else:
                                            return "Некорректный ввод"
                                    else:
                                        return "Некорректный ввод"
                                else:
                                    return "Некорректный ввод"
                            else:
                                return "Некорректный ввод"
                        elif sort_date.lower() == "нет":
                            only_RUB_transact = input("Выводить только рублевые транзакции?\n" "Да/Нет\n")
                            if only_RUB_transact:
                                if only_RUB_transact.lower() == "да":
                                    RUB_transact = [x for x in canceled_list if x["currency_code"] == "RUB"]
                                    search_word = input(
                                        "Отфильтровать список транзакций по определенному слову в описании?\n"
                                        "Да/Нет\n"
                                    )
                                    if search_word:
                                        if search_word.lower() == "да":
                                            my_search_word = input("Введите ключевое слово:\n")
                                            search_transact = src.services.process_bank_search(
                                                RUB_transact, my_search_word
                                            )
                                            print("Распечатываю итоговый список транзакций...\n")
                                            print(f"Всего банковских операций в выборке:{len(search_transact)}\n")
                                            for x in search_transact:
                                                date_and_description = f'{get_date(x['date'])} {x["description"]}\n'
                                                amount_and_name = f'Сумма: {x["amount"]} {x["currency_name"]}\n'
                                                if x["description"] == "Открытие вклада":
                                                    from_to = f"{mask_account_card(x['to'])}\n"
                                                else:
                                                    from_to = f"{mask_account_card(x['from'])} -> {mask_account_card(x['to'])}\n"
                                                print(f"{date_and_description}" f"{from_to}" f"{amount_and_name}")
                                        elif search_word.lower() == "нет":
                                            print("Распечатываю итоговый список транзакций...\n")
                                            print(f"Всего банковских операций в выборке:{len(RUB_transact)}\n")
                                            for x in RUB_transact:
                                                date_and_description = f'{get_date(x['date'])} {x["description"]}\n'
                                                amount_and_name = f'Сумма: {x["amount"]} {x["currency_name"]}\n'
                                                if x["description"] == "Открытие вклада":
                                                    from_to = f"{mask_account_card(x['to'])}\n"
                                                else:
                                                    from_to = f"{mask_account_card(x['from'])} -> {mask_account_card(x['to'])}\n"
                                                print(f"{date_and_description}" f"{from_to}" f"{amount_and_name}")
                                        else:
                                            return "Некорректный ввод"
                                    else:
                                        return "Некорректный ввод"
                                elif only_RUB_transact.lower() == "нет":
                                    search_word = input(
                                        "Отфильтровать список транзакций по определенному слову в описании?\n"
                                        "Да/Нет\n"
                                    )
                                    if search_word:
                                        if search_word.lower() == "да":
                                            my_search_word = input("Введите ключевое слово:\n")
                                            search_transact = src.services.process_bank_search(
                                                canceled_list, my_search_word
                                            )
                                            print("Распечатываю итоговый список транзакций...\n")
                                            print(f"Всего банковских операций в выборке:{len(search_transact)}\n")
                                            for x in search_transact:
                                                date_and_description = f'{get_date(x['date'])} {x["description"]}\n'
                                                amount_and_name = f'Сумма: {x["amount"]} {x["currency_name"]}\n'
                                                if x["description"] == "Открытие вклада":
                                                    from_to = f"{mask_account_card(x['to'])}\n"
                                                else:
                                                    from_to = f"{mask_account_card(x['from'])} -> {mask_account_card(x['to'])}\n"
                                                print(f"{date_and_description}" f"{from_to}" f"{amount_and_name}")
                                        elif search_word.lower() == "нет":
                                            print("Распечатываю итоговый список транзакций...\n")
                                            print(f"Всего банковских операций в выборке:{len(canceled_list)}\n")
                                            for x in canceled_list:
                                                date_and_description = f'{get_date(x['date'])} {x["description"]}\n'
                                                amount_and_name = f'Сумма: {x["amount"]} {x["currency_name"]}\n'
                                                if x["description"] == "Открытие вклада":
                                                    from_to = f"{mask_account_card(x['to'])}\n"
                                                else:
                                                    from_to = f"{mask_account_card(x['from'])} -> {mask_account_card(x['to'])}\n"
                                                print(f"{date_and_description}" f"{from_to}" f"{amount_and_name}")
                                        else:
                                            return "Некорректный ввод"
                                    else:
                                        return "Некорректный ввод"
                                else:
                                    return "Некорректный ввод"
                            else:
                                return "Некорректный ввод"
                        else:
                            return "Некорректный ввод"
                    else:
                        return "Некорректный ввод"
                elif filter_status.upper() == "PENDING":
                    pending_list = [
                        transact for transact in excel_transact for k, v in transact.items() if v == "PENDING"
                    ]
                    sort_date = input("Отсортировать операции по дате?\n" "Да/Нет\n")
                    if sort_date:
                        if sort_date.lower() == "да":
                            sorted_date_list = sorted(pending_list, key=lambda x: x["date"])
                            sorting_order = input("Отсортировать по возрастанию или по убыванию?\n")
                            if sorting_order:
                                if sorting_order.lower() == "по возрастанию":
                                    ascending_sort = sorted(sorted_date_list, key=lambda x: x["date"], reverse=False)
                                    only_RUB_transact = input("Выводить только рублевые транзакции?\n" "Да/Нет\n")
                                    if only_RUB_transact:
                                        if only_RUB_transact.lower() == "да":
                                            RUB_transact = [x for x in ascending_sort if x["currency_code"] == "RUB"]
                                            search_word = input(
                                                "Отфильтровать список транзакций по определенному слову в описании?\n"
                                                "Да/Нет\n"
                                            )
                                            if search_word:
                                                if search_word.lower() == "да":
                                                    my_search_word = input("Введите ключевое слово:\n")
                                                    search_transact = src.services.process_bank_search(
                                                        RUB_transact, my_search_word
                                                    )
                                                    print("Распечатываю итоговый список транзакций...\n")
                                                    print(
                                                        f"Всего банковских операций в выборке:{len(search_transact)}\n"
                                                    )
                                                    if len(search_transact) == 0:
                                                        return "Не найдено ни одной транзакции, подходящей под ваши условия фильтрации"
                                                    else:
                                                        for x in search_transact:
                                                            date_and_description = (
                                                                f'{get_date(x['date'])} {x["description"]}\n'
                                                            )
                                                            amount_and_name = (
                                                                f'Сумма: {x["amount"]} {x["currency_name"]}\n'
                                                            )
                                                            if x["description"] == "Открытие вклада":
                                                                from_to = f"{mask_account_card(x['to'])}\n"
                                                            else:
                                                                from_to = f"{mask_account_card(x['from'])} -> {mask_account_card(x['to'])}\n"
                                                            print(
                                                                f"{date_and_description}"
                                                                f"{from_to}"
                                                                f"{amount_and_name}"
                                                            )
                                                elif search_word.lower() == "нет":
                                                    print("Распечатываю итоговый список транзакций...\n")
                                                    print(f"Всего банковских операций в выборке:{len(RUB_transact)}\n")
                                                    if len(RUB_transact) == 0:
                                                        print(
                                                            "Не найдено ни одной транзакции, подходящей под ваши условия фильтрации"
                                                        )
                                                    else:
                                                        for x in RUB_transact:
                                                            date_and_description = (
                                                                f'{get_date(x['date'])} {x["description"]}\n'
                                                            )
                                                            amount_and_name = (
                                                                f'Сумма: {x["amount"]} {x["currency_name"]}\n'
                                                            )
                                                            if x["description"] == "Открытие вклада":
                                                                from_to = f"{mask_account_card(x['to'])}\n"
                                                            else:
                                                                from_to = f"{mask_account_card(x['from'])} -> {mask_account_card(x['to'])}\n"
                                                            print(
                                                                f"{date_and_description}"
                                                                f"{from_to}"
                                                                f"{amount_and_name}"
                                                            )
                                                else:
                                                    return "Некорректный ввод"
                                            else:
                                                return "Некорректный ввод"
                                        elif only_RUB_transact.lower() == "нет":
                                            search_word = input(
                                                "Отфильтровать список транзакций по определенному слову в описании?\n"
                                                "Да/Нет\n"
                                            )
                                            if search_word:
                                                if search_word.lower() == "да":
                                                    my_search_word = input("Введите ключевое слово:\n")
                                                    search_transact = src.services.process_bank_search(
                                                        ascending_sort, my_search_word
                                                    )
                                                    print("Распечатываю итоговый список транзакций...\n")
                                                    print(
                                                        f"Всего банковских операций в выборке:{len(search_transact)}\n"
                                                    )
                                                    if len(search_transact) == 0:
                                                        print(
                                                            "Не найдено ни одной транзакции, подходящей под ваши условия фильтрации"
                                                        )
                                                    else:
                                                        for x in search_transact:
                                                            date_and_description = (
                                                                f'{get_date(x['date'])} {x["description"]}\n'
                                                            )
                                                            amount_and_name = (
                                                                f'Сумма: {x["amount"]} {x["currency_name"]}\n'
                                                            )
                                                            if x["description"] == "Открытие вклада":
                                                                from_to = f"{mask_account_card(x['to'])}\n"
                                                            else:
                                                                from_to = f"{mask_account_card(x['from'])} -> {mask_account_card(x['to'])}\n"
                                                            print(
                                                                f"{date_and_description}"
                                                                f"{from_to}"
                                                                f"{amount_and_name}"
                                                            )
                                                elif search_word.lower() == "нет":
                                                    print("Распечатываю итоговый список транзакций...\n")
                                                    print(
                                                        f"Всего банковских операций в выборке:{len(ascending_sort)}\n"
                                                    )
                                                    if len(ascending_sort) == 0:
                                                        print(
                                                            "Не найдено ни одной транзакции, подходящей под ваши условия фильтрации"
                                                        )
                                                    else:
                                                        for x in ascending_sort:
                                                            date_and_description = (
                                                                f'{get_date(x['date'])} {x["description"]}\n'
                                                            )
                                                            amount_and_name = (
                                                                f'Сумма: {x["amount"]} {x["currency_name"]}\n'
                                                            )
                                                            if x["description"] == "Открытие вклада":
                                                                from_to = f"{mask_account_card(x['to'])}\n"
                                                            else:
                                                                from_to = f"{mask_account_card(x['from'])} -> {mask_account_card(x['to'])}\n"
                                                            print(
                                                                f"{date_and_description}"
                                                                f"{from_to}"
                                                                f"{amount_and_name}"
                                                            )
                                                else:
                                                    return "Некорректный ввод"
                                            else:
                                                return "Некорректный ввод"
                                        else:
                                            return "Некорректный ввод"
                                    else:
                                        return "Некорректный ввод"
                                elif sorting_order.lower() == "по убыванию":
                                    ascending_sort = sorted(sorted_date_list, key=lambda x: x["date"], reverse=True)
                                    only_RUB_transact = input("Выводить только рублевые транзакции?\n" "Да/Нет\n")
                                    if only_RUB_transact:
                                        if only_RUB_transact.lower() == "да":
                                            RUB_transact = [x for x in ascending_sort if x["currency_code"] == "RUB"]
                                            search_word = input(
                                                "Отфильтровать список транзакций по определенному слову в описании?\n"
                                                "Да/Нет\n"
                                            )
                                            if search_word:
                                                if search_word.lower() == "да":
                                                    my_search_word = input("Введите ключевое слово:\n")
                                                    search_transact = src.services.process_bank_search(
                                                        RUB_transact, my_search_word
                                                    )
                                                    print("Распечатываю итоговый список транзакций...\n")
                                                    print(
                                                        f"Всего банковских операций в выборке:{len(search_transact)}\n"
                                                    )
                                                    if len(search_transact) == 0:
                                                        print(
                                                            "Не найдено ни одной транзакции, подходящей под ваши условия фильтрации"
                                                        )
                                                    else:
                                                        for x in search_transact:
                                                            date_and_description = (
                                                                f'{get_date(x['date'])} {x["description"]}\n'
                                                            )
                                                            amount_and_name = (
                                                                f'Сумма: {x["amount"]} {x["currency_name"]}\n'
                                                            )
                                                            if x["description"] == "Открытие вклада":
                                                                from_to = f"{mask_account_card(x['to'])}\n"
                                                            else:
                                                                from_to = f"{mask_account_card(x['from'])} -> {mask_account_card(x['to'])}\n"
                                                            print(
                                                                f"{date_and_description}"
                                                                f"{from_to}"
                                                                f"{amount_and_name}"
                                                            )
                                                elif search_word.lower() == "нет":
                                                    print("Распечатываю итоговый список транзакций...\n")
                                                    print(f"Всего банковских операций в выборке:{len(RUB_transact)}\n")
                                                    if len(RUB_transact) == 0:
                                                        print(
                                                            "Не найдено ни одной транзакции, подходящей под ваши условия фильтрации"
                                                        )
                                                    else:
                                                        for x in RUB_transact:
                                                            date_and_description = (
                                                                f'{get_date(x['date'])} {x["description"]}\n'
                                                            )
                                                            amount_and_name = (
                                                                f'Сумма: {x["amount"]} {x["currency_name"]}\n'
                                                            )
                                                            if x["description"] == "Открытие вклада":
                                                                from_to = f"{mask_account_card(x['to'])}\n"
                                                            else:
                                                                from_to = f"{mask_account_card(x['from'])} -> {mask_account_card(x['to'])}\n"
                                                            print(
                                                                f"{date_and_description}"
                                                                f"{from_to}"
                                                                f"{amount_and_name}"
                                                            )
                                                else:
                                                    return "Некорректный ввод"
                                            else:
                                                return "Некорректный ввод"
                                        elif only_RUB_transact.lower() == "нет":
                                            search_word = input(
                                                "Отфильтровать список транзакций по определенному слову в описании?\n"
                                                "Да/Нет\n"
                                            )
                                            if search_word:
                                                if search_word.lower() == "да":
                                                    my_search_word = input("Введите ключевое слово:\n")
                                                    search_transact = src.services.process_bank_search(
                                                        ascending_sort, my_search_word
                                                    )
                                                    print("Распечатываю итоговый список транзакций...\n")
                                                    print(
                                                        f"Всего банковских операций в выборке:{len(search_transact)}\n"
                                                    )
                                                    if len(search_transact) == 0:
                                                        print(
                                                            "Не найдено ни одной транзакции, подходящей под ваши условия фильтрации"
                                                        )
                                                    else:
                                                        for x in search_transact:
                                                            date_and_description = (
                                                                f'{get_date(x['date'])} {x["description"]}\n'
                                                            )
                                                            amount_and_name = (
                                                                f'Сумма: {x["amount"]} {x["currency_name"]}\n'
                                                            )
                                                            if x["description"] == "Открытие вклада":
                                                                from_to = f"{mask_account_card(x['to'])}\n"
                                                            else:
                                                                from_to = f"{mask_account_card(x['from'])} -> {mask_account_card(x['to'])}\n"
                                                            print(
                                                                f"{date_and_description}"
                                                                f"{from_to}"
                                                                f"{amount_and_name}"
                                                            )
                                                elif search_word.lower() == "нет":
                                                    print("Распечатываю итоговый список транзакций...\n")
                                                    print(
                                                        f"Всего банковских операций в выборке:{len(ascending_sort)}\n"
                                                    )
                                                    if len(ascending_sort) == 0:
                                                        print(
                                                            "Не найдено ни одной транзакции, подходящей под ваши условия фильтрации"
                                                        )
                                                    else:
                                                        for x in ascending_sort:
                                                            date_and_description = (
                                                                f'{get_date(x['date'])} {x["description"]}\n'
                                                            )
                                                            amount_and_name = (
                                                                f'Сумма: {x["amount"]} {x["currency_name"]}\n'
                                                            )
                                                            if x["description"] == "Открытие вклада":
                                                                from_to = f"{mask_account_card(x['to'])}\n"
                                                            else:
                                                                from_to = f"{mask_account_card(x['from'])} -> {mask_account_card(x['to'])}\n"
                                                            print(
                                                                f"{date_and_description}"
                                                                f"{from_to}"
                                                                f"{amount_and_name}"
                                                            )
                                                else:
                                                    return "Некорректный ввод"
                                            else:
                                                return "Некорректный ввод"
                                        else:
                                            return "Некорректный ввод"
                                    else:
                                        return "Некорректный ввод"
                                else:
                                    return "Некорректный ввод"
                            else:
                                return "Некорректный ввод"
                        elif sort_date.lower() == "нет":
                            only_RUB_transact = input("Выводить только рублевые транзакции?\n" "Да/Нет\n")
                            if only_RUB_transact:
                                if only_RUB_transact.lower() == "да":
                                    RUB_transact = [x for x in pending_list if x["currency_code"] == "RUB"]
                                    search_word = input(
                                        "Отфильтровать список транзакций по определенному слову в описании?\n"
                                        "Да/Нет\n"
                                    )
                                    if search_word:
                                        if search_word.lower() == "да":
                                            my_search_word = input("Введите ключевое слово:\n")
                                            search_transact = src.services.process_bank_search(
                                                RUB_transact, my_search_word
                                            )
                                            print("Распечатываю итоговый список транзакций...\n")
                                            print(f"Всего банковских операций в выборке:{len(search_transact)}\n")
                                            if len(search_transact) == 0:
                                                print(
                                                    "Не найдено ни одной транзакции, подходящей под ваши условия фильтрации"
                                                )
                                            else:
                                                for x in search_transact:
                                                    date_and_description = (
                                                        f'{get_date(x['date'])} {x["description"]}\n'
                                                    )
                                                    amount_and_name = f'Сумма: {x["amount"]} {x["currency_name"]}\n'
                                                    if x["description"] == "Открытие вклада":
                                                        from_to = f"{mask_account_card(x['to'])}\n"
                                                    else:
                                                        from_to = f"{mask_account_card(x['from'])} -> {mask_account_card(x['to'])}\n"
                                                    print(f"{date_and_description}" f"{from_to}" f"{amount_and_name}")
                                        elif search_word.lower() == "нет":
                                            print("Распечатываю итоговый список транзакций...\n")
                                            print(f"Всего банковских операций в выборке:{len(RUB_transact)}\n")
                                            if len(RUB_transact) == 0:
                                                print(
                                                    "Не найдено ни одной транзакции, подходящей под ваши условия фильтрации"
                                                )
                                            else:
                                                for x in RUB_transact:
                                                    date_and_description = (
                                                        f'{get_date(x['date'])} {x["description"]}\n'
                                                    )
                                                    amount_and_name = f'Сумма: {x["amount"]} {x["currency_name"]}\n'
                                                    if x["description"] == "Открытие вклада":
                                                        from_to = f"{mask_account_card(x['to'])}\n"
                                                    else:
                                                        from_to = f"{mask_account_card(x['from'])} -> {mask_account_card(x['to'])}\n"
                                                    print(f"{date_and_description}" f"{from_to}" f"{amount_and_name}")
                                        else:
                                            return "Некорректный ввод"
                                    else:
                                        return "Некорректный ввод"
                                elif only_RUB_transact.lower() == "нет":
                                    search_word = input(
                                        "Отфильтровать список транзакций по определенному слову в описании?\n"
                                        "Да/Нет\n"
                                    )
                                    if search_word:
                                        if search_word.lower() == "да":
                                            my_search_word = input("Введите ключевое слово:\n")
                                            search_transact = src.services.process_bank_search(
                                                pending_list, my_search_word
                                            )
                                            print("Распечатываю итоговый список транзакций...\n")
                                            print(f"Всего банковских операций в выборке:{len(search_transact)}\n")
                                            if len(search_transact) == 0:
                                                print(
                                                    "Не найдено ни одной транзакции, подходящей под ваши условия фильтрации"
                                                )
                                            else:
                                                for x in search_transact:
                                                    date_and_description = (
                                                        f'{get_date(x['date'])} {x["description"]}\n'
                                                    )
                                                    amount_and_name = f'Сумма: {x["amount"]} {x["currency_name"]}\n'
                                                    if x["description"] == "Открытие вклада":
                                                        from_to = f"{mask_account_card(x['to'])}\n"
                                                    else:
                                                        from_to = f"{mask_account_card(x['from'])} -> {mask_account_card(x['to'])}\n"
                                                    print(f"{date_and_description}" f"{from_to}" f"{amount_and_name}")
                                        elif search_word.lower() == "нет":
                                            print("Распечатываю итоговый список транзакций...\n")
                                            print(f"Всего банковских операций в выборке:{len(pending_list)}\n")
                                            if len(pending_list) == 0:
                                                print(
                                                    "Не найдено ни одной транзакции, подходящей под ваши условия фильтрации"
                                                )
                                            else:
                                                for x in pending_list:
                                                    date_and_description = (
                                                        f'{get_date(x['date'])} {x["description"]}\n'
                                                    )
                                                    amount_and_name = f'Сумма: {x["amount"]} {x["currency_name"]}\n'
                                                    if x["description"] == "Открытие вклада":
                                                        from_to = f"{mask_account_card(x['to'])}\n"
                                                    else:
                                                        from_to = f"{mask_account_card(x['from'])} -> {mask_account_card(x['to'])}\n"
                                                    print(f"{date_and_description}" f"{from_to}" f"{amount_and_name}")
                                        else:
                                            return "Некорректный ввод"
                                    else:
                                        return "Некорректный ввод"
                                else:
                                    return "Некорректный ввод"
                            else:
                                return "Некорректный ввод"
                        else:
                            return "Некорректный ввод"
                    else:
                        return "Некорректный ввод"
                else:
                    return "Некорректный ввод"
            else:
                return "Некорректный ввод"
        else:
            return "Некорректный ввод"
    return "Всё!"


print(main())

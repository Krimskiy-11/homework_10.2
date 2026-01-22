from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(card_account: str) -> str:
    """Функция принимает тип и номер карты или счета, и возвращает строку с
    замаскированным номером"""

    if card_account is None or card_account == '':
        return 'Incorrect data entry'
    else:
        list_str_account = card_account.split()

        mask = []
        for i in list_str_account:
            if i.isalpha():
                mask.append(i)

            if i.isdigit():
                len_num = len(i)
                if len_num == 20:
                    mask_card = get_mask_account(i)
                    mask.append(mask_card)
                elif len_num == 16:
                    mask_account = get_mask_card_number(i)
                    mask.append(mask_account)
                else:
                    return 'Incorrect data entry'

        ending_mask = ' '.join(mask)

        return ending_mask


def get_date(date: str) -> str:
    """Функция принимает исходную форму даты и возвращает более привычную"""

    if date is None or date == '':
        return 'Incorrect data entry'
    else:
        normal_date = date[:10]
        list_normal_date = normal_date.split("-")
        date = f"{list_normal_date[2]}.{list_normal_date[1]}.{list_normal_date[0]}"

        if date[:5] == '30.02' or date[:5] == '31.02':
            return 'There is no such date'
        elif int(date[:2]) > 31:
            return 'There is no such date'

        return date

import pytest

from src.widget import mask_account_card, get_date


@pytest.mark.parametrize('account_num, result', [
    ('Visa Platinum 7000792289606361', 'Visa Platinum 7000 79** **** 6361'),
    ('Счет 64686473678894779589', 'Счет **9589'),
    (None, 'Incorrect data entry'),
    ('', 'Incorrect data entry'),
    ('Счет 82357934359238957235732', 'Incorrect data entry')
])
def test_mask_account_card(account_num, result):
    assert mask_account_card(account_num) == result


@pytest.mark.parametrize('date, result', [
    ('2024-03-11T02:26:18.671407', '11.03.2024'),
    ('2025-01-21T05:44:20.373434', '21.01.2025'),
    (None, 'Incorrect data entry'),
    ('', 'Incorrect data entry'),
    ('2025-02-30T05:44:20.373434', 'There is no such date'),
    ('2004-05-44T02:26:18.671407', 'There is no such date')
])
def test_get_date(date, result):
    assert get_date(date) == result

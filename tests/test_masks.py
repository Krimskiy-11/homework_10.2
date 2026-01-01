import pytest

from src.masks import get_mask_card_number, get_mask_account
from tests.conftest import cards, account


@pytest.mark.parametrize('card, result', [
    ('5000892289605566', '5000 89** **** 5566'),
    (None, 'Incorrect data entry'),
    (5000892289605566, '5000 89** **** 5566'),
    ('500089228960556623465', 'Incorrect data entry')
])
def test_get_mask_card_number(card, result):
    assert get_mask_card_number(card) == result

def test_get_mask_card_number_1(cards):
    assert get_mask_card_number(cards) == '7000 79** **** 6361'


@pytest.mark.parametrize('account_num, result', [
    ('23593520050864052040', '**2040'),
    (None, 'Incorrect data entry'),
    (23593520050864052040, '**2040'),
    ('82357934359238957235732', 'Incorrect data entry')
])
def test_get_mask_account(account_num, result):
    assert get_mask_account(account_num) == result

def test_get_mask_account_1(account):
    assert get_mask_account(account) == '**4305'
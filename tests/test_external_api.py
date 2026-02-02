from unittest.mock import Mock, patch

from src.external_api import sum_transaction


def test_sum_transaction_with_RUB(transaction_RUB):
    assert sum_transaction(transaction_RUB) == "31957.58"


@patch("requests.get")
def test_sum_transaction_with_USD(mock_get):
    mock_response = Mock()
    mock_response.json.return_value = {"result": 74.5}
    mock_get.return_value = mock_response

    transaction = {"operationAmount": {"amount": "1", "currency": {"code": "USD"}}}

    result = sum_transaction(transaction)
    assert result == 74.5


@patch("requests.get")
def test_sum_transaction_with_EUR(mock_get):
    mock_response = Mock()
    mock_response.json.return_value = {"result": 88.5}
    mock_get.return_value = mock_response

    transaction = {"operationAmount": {"amount": "2", "currency": {"code": "EUR"}}}

    result = sum_transaction(transaction)
    assert result == 88.5


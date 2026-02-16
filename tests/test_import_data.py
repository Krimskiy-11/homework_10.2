from unittest.mock import patch

import pandas as pd

from src import import_data


@patch('src.import_data.pd.read_csv')
def test_csv_data(mock_get):
    fake_df = pd.DataFrame([
        {"id": 1, "amount": 100},
        {"id": 2, "amount": 200}
    ])

    mock_get.return_value = fake_df
    result = import_data.get_csv_data("transactions.csv")
    expected = fake_df.to_json(orient='records', indent=4, force_ascii=False)

    assert result == expected


@patch('src.import_data.pd.read_excel')
def test_excel_data(mock_get):
    fake_df = pd.DataFrame([
        {"id": 1, "amount": 500},
        {"id": 2, "amount": 700}
    ])

    mock_get.return_value = fake_df
    result = import_data.get_excel_data("transactions_excel.xlsx")
    expected = fake_df.to_json(orient='records', indent=4, force_ascii=False)

    assert result == expected

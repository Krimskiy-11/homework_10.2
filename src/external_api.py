import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('API_KEY')


def sum_transaction(transaction):
    path_code = transaction['operationAmount']['currency']['code']

    if path_code == "RUB":
        return transaction['operationAmount']['amount']

    elif path_code == "USD":
        to = "RUB"
        from_ = "USD"
        amount = transaction['operationAmount']['amount']
        url = f"https://api.apilayer.com/exchangerates_data/convert?to={to}&from={from_}&amount={amount}"
        headers = {"apikey": API_KEY}

        response = requests.get(url, headers=headers)
        result = response.json()
        return result['result']

    elif path_code == "EUR":
        to = "RUB"
        from_ = "EUR"
        amount = transaction['operationAmount']['amount']

        url = f"https://api.apilayer.com/exchangerates_data/convert?to={to}&from={from_}&amount={amount}"

        headers = {"apikey": API_KEY}

        response = requests.get(url, headers=headers)
        result = response.json()
        return result['result']

    else:
        return None

# def random_transact(transactions: list):
#     return random.choice(transactions)
#
#
# tr = random_transact(get_transactions('operations.json'))
# print(sum_transaction(tr))


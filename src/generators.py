def filter_by_currency(transactions: list[dict], statute):
    """Функцию, которая принимает на вход список транзакции и возвращает поочередно транзакции,
    где валюта операции соответствует заданной."""

    count = 0
    result = list(filter(lambda x: x["operationAmount"]["currency"]["name"] == statute, transactions))
    while count < len(result):
        yield result[count]
        count += 1
    return 'Ending...'



def transaction_descriptions(transactions: list[dict]):
    """Функция, которая принимает список словарей с транзакциями и
    возвращает описание каждой операции по очереди."""

    count = 0

    while count < len(transactions):
        description = list((x["description"] for x in transactions))
        yield description[count]
        count += 1
    else:
        return 'Ending...'


def card_number_generator():
    pass


transact = [{
          "id": 939719570,
          "state": "EXECUTED",
          "date": "2018-06-30T02:08:58.425572",
          "operationAmount": {
              "amount": "9824.07",
              "currency": {
                  "name": "USD",
                  "code": "USD"
              }
          },
          "description": "Перевод организации",
          "from": "Счет 75106830613657916952",
          "to": "Счет 11776614605963066702"
      },
      {
              "id": 142264268,
              "state": "EXECUTED",
              "date": "2019-04-04T23:20:05.206878",
              "operationAmount": {
                  "amount": "79114.93",
                  "currency": {
                      "name": "USD",
                      "code": "USD"
                  }
              },
              "description": "Перевод со счета на счет",
              "from": "Счет 19708645243227258542",
              "to": "Счет 75651667383060284188"
       },
      {
              "id": 142222222,
              "state": "EXECUTED",
              "date": "2019-04-04T23:20:05.206878",
              "operationAmount": {
                  "amount": "79114.93",
                  "currency": {
                      "name": "USDT",
                      "code": "USDT"
                  }
              },
              "description": "Перевод со счета на счет",
              "from": "Счет 19708645243227258542",
              "to": "Счет 75651667383060284188"
       },
      {
              "id": 142555568,
              "state": "EXECUTED",
              "date": "2019-04-04T23:20:05.206878",
              "operationAmount": {
                  "amount": "79114.93",
                  "currency": {
                      "name": "RUB",
                      "code": "RUB"
                  }
              },
              "description": "Перевод организации",
              "from": "Счет 19708645243227258542",
              "to": "Счет 75651667383060284188"
       },
]

usd_transactions = filter_by_currency(transact, "USD")
for _ in range(3):
    print(next(usd_transactions))


descriptions = transaction_descriptions(transact)
for _ in range(10):
    print(next(descriptions))
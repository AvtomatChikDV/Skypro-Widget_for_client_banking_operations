import random


def filter_by_currency(transactions: list, currency: str):
    """
    Функция возвращает итератор, который поочередно выдает транзакции,
    где валюта операции соответствует
    заданной (например, USD).
    """

    for transaction in transactions:
        try:
            if transaction["operationAmount"]["currency"]["code"] == currency:
                yield transaction
        except (KeyError, TypeError):
            continue


transactions=[{
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
          "id": 000000000,
          "state": "EXECUTED",
          "date": "2018-06-30T02:08:58.425572",
          "operationAmount": {
              "amount": "9824.07",
              "currency": {
                  "name": "RUS",
                  "code": "RUS"
              }
          },
          "description": "Перевод организации",
          "from": "Счет 75106830613657916952",
          "to": "Счет 11776614605963066702"
      }
]
usd_transactions = filter_by_currency(transactions, "RUS")
for _ in range(2):
    try:
        print(next(usd_transactions))
    except StopIteration:
        print("Больше нет транзакций")
        break


def transaction_descriptions(transactions: list):
    for transaction in transactions:
        try:
            yield transaction["description"]
        except (KeyError, TypeError):
            continue


descriptions = transaction_descriptions(transactions)
for _ in range(5):
    try:
        print(next(descriptions))
    except StopIteration:
        print("Больше нет транзакций")
        break


def card_number_generator(start: int, end: int):

    for number in range(start, end + 1):
        # Форматируем число в 16 цифр с ведущими нулями
        card_str = f"{number:016d}"
        # Разбиваем на группы по 4 цифры
        formatted_card = ' '.join([card_str[i:i + 4] for i in range(0, 16, 4)])
        yield formatted_card


for card_number in card_number_generator(100, 150):
    print(card_number)





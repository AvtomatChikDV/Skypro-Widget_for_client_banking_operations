def filter_by_currency(transactions: list, currency: str):
    """
    Генератор возвращает итератор для фильтрации транзакций по валюте.
    Отбирает только те транзакции, валюта которых соответствует заданной.
    """

    for transaction in transactions:

        if transaction["operationAmount"]["currency"]["code"] == currency:
            yield transaction


def transaction_descriptions(transactions: list):
    """
    Генератор принимает список словарей с транзакциями и
    генерирует текстовые описания для каждой операции.
    """

    for transaction in transactions:
        yield transaction["description"]


def card_number_generator(start: int, end: int):
    """
    Генератор номеров банковских карт в формате ХХХХ ХХХХ ХХХХ ХХХХ.
    Диапазон: от 0000 0000 0000 0001 до 9999 9999 9999 9999.
    """
    for number in range(start, end + 1):
        # Форматируем число в 16 цифр с ведущими нулями
        card_str = f"{number:016d}"
        # Разбиваем на группы по 4 цифры
        formatted_card = " ".join([card_str[i : i + 4] for i in range(0, 16, 4)])
        yield formatted_card

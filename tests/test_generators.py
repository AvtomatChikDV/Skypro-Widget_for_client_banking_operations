import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_by_currency(transactions: list[dict], currency: str = "RUB"):
    """Тест правильного фильтра транзакций по типу валюты, пример currency_code = 'RUB'"""
    generator = filter_by_currency(transactions, currency)
    assert next(generator) == {
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160",
    }


def test_filter_absent_currency(transactions: list[dict], currency: str = "EUR"):
    """
    Тест отсутствия списка транзакций, если нет типа валюты,
    пример currency_code = 'EUR'
    """
    generator = filter_by_currency(transactions, currency)
    with pytest.raises(StopIteration):
        next(generator)


def test_filter_empty_currency(currency: str = "EUR"):
    """Тест отработки генератора, при пустом списке транзакций"""
    generator = filter_by_currency([], currency)
    # Ожидаем отработки исключения StopIteration
    with pytest.raises(StopIteration):
        next(generator)


def test_transaction_descriptions(transactions: list[dict]):
    """Тест правильного вывода типа операций"""
    generator = transaction_descriptions(transactions)
    assert next(generator) == "Перевод организации"
    assert next(generator) == "Перевод со счета на счет"
    assert next(generator) == "Перевод со счета на счет"


def test_transaction_end_descriptions(transactions: list[dict]):
    """Тест вывода типа операций, если список окончен"""
    descriptions = transaction_descriptions(transactions)
    # Длина списка фикстуры transactions = 5
    # Ожидаем отработки исключения StopIteration
    with pytest.raises(StopIteration):
        for _ in range(7):
            next(descriptions)


def test_transaction_empty_descriptions():
    """Тест вывода типа операций, если список транзакций на входе пустой"""
    descriptions = transaction_descriptions([])
    # Ожидаем отработки исключения StopIteration
    with pytest.raises(StopIteration):
        next(descriptions)


def test_card_number_generator_correct_value():
    """Тест корректного вывода, при нормальном диапазоне"""
    generator = card_number_generator(100, 111111)
    numbers = list(generator)
    assert numbers[0] == "0000 0000 0000 0100"
    assert numbers[1] == "0000 0000 0000 0101"
    assert numbers[2] == "0000 0000 0000 0102"
    assert numbers[3] == "0000 0000 0000 0103"
    assert numbers[111011] == "0000 0000 0011 1111"


def test_format_correctness():
    """Тест корректности форматирования"""
    generator = card_number_generator(1234567890123456, 1234567890123456)
    number = next(generator)
    # Проверка формата
    assert len(number) == 19  # 16 цифр + 3 пробела
    parts = number.split(" ")
    assert len(parts) == 4
    # Проверка конкретного значения
    assert number == "1234 5678 9012 3456"


def test_edge_cases():
    """Тест крайних случаев"""
    # Минимальное значение
    gen_min = card_number_generator(1, 1)
    assert next(gen_min) == "0000 0000 0000 0001"

    # Максимальное значение
    gen_max = card_number_generator(9999999999999999, 9999999999999999)
    assert next(gen_max) == "9999 9999 9999 9999"


def test_reverse_range():
    """Тест обратного диапазона (start > end)"""
    generator = card_number_generator(5, 3)
    numbers = list(generator)
    assert numbers == []  # Должен вернуть пустой список

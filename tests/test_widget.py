import pytest

from src.widget import mask_account_card, get_date


@pytest.mark.parametrize(
    "input_data, expected",
    [
        ("Счет 12345678901234567890", "Счет **7890"),
        ("Visa 4111111111111111", "Visa 4111 11** **** 1111"),
        ("MasterCard 5555555555554444", "MasterCard 5555 55** **** 4444"),
        ("Maestro 1234-5678-1234-5678", "Maestro 1234 56** **** 5678"),  # С разделителем
        ("Счет 40817810099910004312", "Счет **4312"),
        ("  Счет   40817810099910004312 ", "Счет **4312"),  # С пробелами
    ],
)
def test_account_card_masking(input_data, expected):
    """Тестирование маскирования стандартных карт и счетов"""
    assert mask_account_card(input_data) == expected


def test_no_input():
    """Тестирование пустых данных"""
    with pytest.raises(ValueError):
        mask_account_card("")


@pytest.mark.parametrize(
    "invalid_data",
    [
        ("12345678901234567890"),  # Нет определителя счёт/карта
        ("Visa 41111"),  # Короткий номер
        ("MasterCard"),  # Нет номера
        ("Maestro 123dsfsd4#5678-45678"),  # Левые символы
    ],
)
def test_invalid_input(invalid_data):
    """Тестирование некорректных входных данных, ожидаемый вывод ошибки ValueError """
    with pytest.raises(ValueError):
        mask_account_card(invalid_data)


@pytest.mark.parametrize(
    "input_date, expected",
    [
        # Стандартный формат
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2019-07-03T18:35:29.512364", "03.07.2019"),
        ("2024-03-11T02:26:18", "11.03.2024"),
        ("2019-07-03T18:35:29", "03.07.2019"),
        # Только дата (без времени)
        ("2024-03-11", "11.03.2024"),
        ("2019-07-03", "03.07.2019"),
        ("2018-06-30", "30.06.2018"),
        # Граничные даты
        ("2023-12-31T23:59:59.999999", "31.12.2023"),
        ("2023-01-01T00:00:00.000000", "01.01.2023"),
        ("2000-02-29T12:00:00.000000", "29.02.2000"),  # Високосный год
    ],
)
def test_valid_iso_dates(input_date, expected):
    """Тестирование стандартных форматов дат"""
    assert get_date(input_date) == expected


@pytest.mark.parametrize(
    "input_date",
    [
        # Случаи когда дата отсутствует или не распознается
        "",
        "   ",
        "invalid_date",
        "not-a-date",
        "hello world",
        "1234567890",
        "2024/03/11",  # Другой формат разделителей
        "11.03.2024",  # Уже в нужном формате
        "03-11-2024",  # Американский формат
        "2024-13-45",  # Невалидная дата (13 месяц)
        "2024-02-30",  # Невалидная дата (30 февраля)
    ],
)
def test_invalid_or_unsupported_formats(input_date):
    """Тестирование невалидных или неподдерживаемых форматов"""
    assert get_date(input_date) == "Неправильная дата!!!"

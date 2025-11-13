import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "card_number, expected",
    [
        ("4111111111111111", "4111 11** **** 1111"),  # Visa
        ("5555555555554444", "5555 55** **** 4444"),  # Mastercard
        ("3782822463100057", "3782 82** **** 0057"),  # American Express
        ("1234567812345674", "1234 56** **** 5674"),  # Другой номер
        ("1234-2134-4567-9865", "1234 21** **** 9865"),  # Номер со специальными символами
        ("5346 3643 2354 8798", "5346 36** **** 8798"),  # Номер с пробелами
    ],
)
def test_get_mask_card_number(card_number: str, expected: str) -> None:
    """Функция проверки стандартных номеров карт"""
    assert get_mask_card_number(card_number) == expected


@pytest.mark.parametrize(
    "invalid_cards",
    [
        "4111",  # Короткий номер
        "5sh555vb55hdhs44",  # Номер с буквами
        "",  # Номер не введён
        "1234567812345674645645646465",  # Длинный номер
        "757 097#@)?8 5",  # Номер со специальными знаками, пробелами
    ],
)
def test_get_mask_card_invalid_number(invalid_cards: str) -> None:
    """
    Функция проверки неправильных номеров карт,
    пропускаются номера стандартного размера 16 чисел.
    Программа выводит ошибку Value Error(f"Номер карты должен содержать 16 цифр, получено: {len(digits)}")
    """
    with pytest.raises(ValueError):
        get_mask_card_number(invalid_cards)


@pytest.mark.parametrize(
    "account_number, expected",
    [
        ("12345678901234567890", "**7890"),  # Стандартный счет
        ("40817810099910004312", "**4312"),
        ("40898794646910004378", "**4378"),
        ("06730710099910002452", "**2452"),
        ("0673 0710099910-002452", "**2452"),  # Номер со специальными символами
    ],
)
def test_get_mask_account(account_number: str, expected: str) -> None:
    """Функция проверки стандартных номеров счетов"""
    assert get_mask_account(account_number) == expected


@pytest.mark.parametrize(
    "invalid_accounts",
    [
        "1jkghkshg78901234567890",  # Номер с буквами
        "408178 1009№%_-)(№004312",  # Номер со специальными символами
        "408987946469100",  # Короткий номер
        "06730710099910474453002452",  # Длинный номер
        "",
    ],
)
def test_get_mask_invalid_account(invalid_accounts) -> None:
    """
    Функция проверки неправильных номеров счетов,
    пропускаются номера стандартного размера 20 чисел.
    Программа выводит ошибку Value Error(f"Номер счёта должен содержать 20 цифр, получено: {len(digits)}")
    """
    with pytest.raises(ValueError):
        get_mask_account(invalid_accounts)

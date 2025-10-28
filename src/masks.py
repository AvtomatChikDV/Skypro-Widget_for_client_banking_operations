def get_mask_card_number(card_number: str) -> str:
    """
    Маскирует номер карты в формате XXXX XX** **** XXXX

    card_number - Номер карты (16 цифр, может быть с разделителями)

    Returns - Маскированный номер в формате XXXX XX** **** XXXX
    Примеры:
           7000792289606361 --> 7000 79** **** 6361
        7000 7922_8960-6361 --> 7000 79** **** 6361
    """
    # Оставляем только цифры
    digits = ''.join(char for char in card_number if char.isdigit())

    # Проверяем что номер карты содержит 16 цифр
    if len(digits) != 16:
        raise ValueError(f"Номер карты должен содержать 16 цифр, получено: {len(digits)}")

    # Разбиваем на части и формируем маску
    part1 = digits[:4]  # Первые 4 цифры
    part2 = digits[4:6]  # Следующие 2 цифры (видимые)
    part3 = "**"  # Маскируем следующие 2 цифр
    part4 = "****"  # Маскируем еще 4 цифры
    part5 = digits[-4:]  # Последние 4 цифры

    return f"{part1} {part2}{part3} {part4} {part5}"


def get_mask_account(account_number: str) -> str:
    """
        Маскирует номер счёта в формате **XXXX

        account_number - Номер счёта (8 цифр)

        Returns - Маскированный номер в формате **XXXX
        """
    # Оставляем только цифры
    digits = ''.join(char for char in account_number if char.isdigit())
    # Проверяем что номер счёта содержит 8 цифр
    if len(digits) != 8:
        raise ValueError(f"Номер счёта должен содержать 8 цифр, получено: {len(digits)}")

    return f"**{digits[-4:]}"
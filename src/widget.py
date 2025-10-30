from src.masks import get_mask_account, get_mask_card_number
import re


def mask_account_card(card_or_account_data: str) -> str:
    """Определяет что на входе карта или счёт и выводит соответствующую маску"""
    new_list = card_or_account_data.split()

    if "Счет" in new_list[0]:
        new_list[-1] = get_mask_account(new_list[-1])
    else:
        new_list[-1] = get_mask_card_number(new_list[-1])
    return " ".join(new_list)


def get_date(data_info: str) -> str:
    """Функция берёт данные даты и времени в формате "2024-03-11T02:26:18.671407"
    и возвращает только дату в формате 'ДД.ММ.ГГГГ'"""
    # new_list = data_info[:10]
    pattern = r"(\d{4})-(\d{2})-(\d{2})"
    match = re.search(pattern, data_info)
    return ".".join(match.group().split("-")[::-1]) if match else "Нет даты!!!"

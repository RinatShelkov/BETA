import datetime
import re

from masks import return_mask_bank_account, return_mask_cards


def return_mask_card_account(information_on_card: str) -> str:
    """Принимает на вход строку с информацией типа карты/счета и номера карты/счета
    возвращает эту строку с замаскированным номером карты/счета.
    :param
    information_on_card: Тип карты/счета
    :return: Маскированный по правилу номер карты/счета"""
    number_card_or_count = " ".join(re.findall(r"\d+", information_on_card))
    information_on_card = information_on_card.replace(number_card_or_count, "")
    if len(number_card_or_count) == 16:
        number_card_or_count = return_mask_cards(number_card_or_count)
    elif len(number_card_or_count) == 20:
        number_card_or_count = return_mask_bank_account(number_card_or_count)
    else:
        return f"{'Неправильно введены данные номер карты/счета'}"
    return f"{information_on_card.title()} {number_card_or_count}"


def return_date_from_str(string_with_date: str) -> str:
    """Принимает на вход строку (формат вида: 2018-07-11T02:26:18.671407) и возвращает строку вида: 11.07.2018
    :param string_with_date: Строка
    :return дата в формате - 11.07.2018"""
    string_with_date = string_with_date.replace("T" or "t" or "Т" or "т", " ")
    string_date = datetime.datetime.strptime(string_with_date, "%Y-%m-%d %H:%M:%S.%f")
    return string_date.strftime("%d.%m.%Y")

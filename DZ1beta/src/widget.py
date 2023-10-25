import datetime


def return_mask_card_account(type_card_or_account: str, number_card_or_account: str) -> str:
    """Принимает на вход строку с информацией типа карты/счета и номера карты/счета
    возвращает эту строку с замаскированным номером карты/счета.
    :param
    type_card_or_account: Тип карты/счета
    number_card_or_account: Номер карты/счета
        :return: Маскированный по правилу номер карты/счета"""
    if len(number_card_or_account.replace(" ", "")) == 16:
        number_card_or_account = number_card_or_account.replace(" ", "")
        number_card_or_account = (
            number_card_or_account[:6] + (len(number_card_or_account[6:-4]) * "*") + number_card_or_account[-4:]
        )
        part_of_number_card_or_account = len(number_card_or_account)
        number_of_parts = len(number_card_or_account) // 4
        mask_card_or_account = " ".join(
            [
                number_card_or_account[i : i + number_of_parts]
                for i in range(0, part_of_number_card_or_account, number_of_parts)
            ]
        )
    elif len(number_card_or_account.replace(" ", "")) == 20:
        number_card_or_account = number_card_or_account.replace(" ", "")
        mask_card_or_account = len(number_card_or_account[14:16]) * "*" + number_card_or_account[-4:]

    else:
        return f"{'Неправильно введен номер карты/счета'}"
    return f"{type_card_or_account.title()} {mask_card_or_account}"


def return_date_from_str(string_with_date: str) -> str:
    """Принимает на вход строку (формат вида: 2018-07-11T02:26:18.671407) и возвращает строку вида: 11.07.2018
    :param string_with_date: Строка
    :return дата в формате - 11.07.2018"""
    string_with_date = string_with_date.replace("T" or "t" or "Т" or "т", " ")
    string_date = datetime.datetime.strptime(string_with_date, "%Y-%m-%d %H:%M:%S.%f")
    return string_date.strftime("%d.%m.%Y")

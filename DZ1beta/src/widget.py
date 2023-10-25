def return_mask_card_account(type_card_or_account: str, number_card_or_account: str) -> str:
    """Принимает на вход строку с информацией типа карты/счета и номера карты/счета
возвращает эту строку с замаскированным номером карты/счета.
:param
type_card_or_account: Тип карты/счета
number_card_or_account: Номер карты/счета
    :return: Маскированный по правилу номер карты/счета"""
    if len(number_card_or_account.replace(" ", "")) == 16:
        number_card_or_account = number_card_or_account.replace(" ", "")
        number_card_or_account = number_card_or_account[:6] + (
                len(number_card_or_account[6:-4]) * "*") + number_card_or_account[-4:]
        part_of_number_card_or_account = len(number_card_or_account)
        number_of_parts = len(number_card_or_account) // 4
        mask_card_or_account = " ".join(
            [number_card_or_account[i: i + number_of_parts] for i in
             range(0, part_of_number_card_or_account, number_of_parts)]
        )
    elif len(number_card_or_account.replace(" ", "")) == 20:
        number_card_or_account = number_card_or_account.replace(" ", "")
        mask_card_or_account = len(number_card_or_account[14:16]) * "*" + number_card_or_account[-4:]

    else:
        return f"{'Неправильно введен номер карты/счета'}"
    return f"{type_card_or_account.title()} {mask_card_or_account}"




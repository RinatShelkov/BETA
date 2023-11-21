from src.logger import logging_masks


def return_mask_cards(numbers_card: str) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску
    :param numbers_card: Номер для маскирования
    :return: Маскированный по правилу номер
    """
    logger_masks = logging_masks()

    if len(numbers_card.replace(" ", "")) == 16:
        numbers_card = numbers_card.replace(" ", "")
        numbers_card = numbers_card[:6] + (len(numbers_card[6:-4]) * "*") + numbers_card[-4:]
        part_of_numbers_card = len(numbers_card)
        number_of_parts = len(numbers_card) // 4
        logger_masks.info("Номер карты успешно замаскирован")
        return " ".join(
            [numbers_card[i: i + number_of_parts] for i in range(0, part_of_numbers_card, number_of_parts)]
        )

    else:
        logger_masks.error("Неправильно введен номер карты")
        return f"{'Неправильно введен номер карты'}"


def return_mask_bank_account(number_account: str) -> str:
    """Функция принимает на вход номер счёта и возвращает его маску
    :param number_account: Номер для маскирования
    :return: Маскированный по правилу номер счета
    """
    logger_masks = logging_masks()

    if len(number_account.replace(" ", "")) == 20:
        number_account = number_account.replace(" ", "")
        number_account = len(number_account[14:16]) * "*" + number_account[-4:]
        logger_masks.info("Номер счета успешно замаскирован")
        return number_account
    else:
        logger_masks.error("Неправильно введен номер счета")
        return f"{'Неправильно введен номер счета'}"

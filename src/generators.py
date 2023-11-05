from collections.abc import Iterator


def filter_by_currency(transactions: list, currency: str) -> Iterator[int]:
    """Функция, которая принимает список словарей и возвращает итератор, который выдает по очереди операции, в которых
    указана заданная валюта.
    :param
    transactions: список словарей с транзакциями
    currency: валюта(ключ) по которой происходит отбор транзакций
    :return выдает по очереди операции, в которых указана заданная валюта"""
    for code in transactions:
        if code["operationAmount"]["currency"]["code"] == currency.upper():
            yield code


def transaction_descriptions(transactions: list) -> Iterator[str]:
    """Функция принимает список словарей и возвращает описание каждой операции по очереди
    :param transactions: список словарей
    :return операции по очереди"""
    for description in transactions:
        yield description["description"]

from collections.abc import Iterator

def filter_by_currency(transactions: list, currency: str) -> Iterator[int]:
    """Функция, которая принимает список словарей и возвращает итератор, который выдает по очереди операции, в которых
    указана заданная валюта.
    :param
    transactions: список словарей с транзакциями
    currency: валюта(ключ) по которой происходит отбор транзакций"""
    for code in transactions:
        if code["operationAmount"]["currency"]["code"] == currency.upper():
            yield code

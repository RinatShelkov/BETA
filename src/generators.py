import textwrap
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


def card_number_generator(bottom_range: int, up_range: int) -> Iterator | str:
    """Генератор номеров банковских карт, генерирует номера карт в формате "XXXX XXXX XXXX XXXX"
    :param
    bottom_range: Нижний диапозон номеров карт
    up_range: Верхний диапозон номеров карт
    :return Генератор номера банковских карт"""
    if len(str(up_range)) > 16:
        return f'{"Укажите корректно нижний и верхний диапозон"}'
    elif bottom_range > up_range:
        return f'{"Укажите корректно нижний и верхний диапозон"}'
    elif bottom_range <= 0:
        return f'{"Укажите корректно нижний и верхний диапозон"}'

    generator_numbers = map(
        lambda x: " ".join(textwrap.wrap(x, 4)), [str(i).zfill(16) for i in range(bottom_range, up_range + 1)]
    )
    return generator_numbers

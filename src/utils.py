import json
from os import PathLike
from typing import Any


def get_list_dict_json(path_json: PathLike) -> Any:
    """Принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях
    :param path_json: путь до JSON-файла
    :return file_json список словарей с данными о финансовых транзакциях
    (Если файл пустой, содержит не список или не найден, функция возвращает пустой список)
    """
    try:
        with open(path_json, encoding="utf-8") as file:
            file_json = json.load(file)

    except FileNotFoundError:
        file_json = []

    except json.JSONDecodeError:
        file_json = []

    return file_json


def get_summ_transaction_rub(transaction: dict) -> float | Any:
    """Функция принимает на вход одну транзакцию и возвращает:
    сумму транзакции (amount) в рублях, возвращает тип float,
    если транзация совершалась в рублях ошибку ValueError с сообщением
    "Транзация выполнена не в рублях. Укажите транзакцию в рублях",
    если транзакция была совершена в другой валюте.
    :param transaction: Словарь с транзакцией
    :return rub_amount: сумма транзакции в рублях"""
    if bool(transaction) is False:
        raise ValueError("Транзакция повреждена")
    elif transaction["operationAmount"]["currency"]["code"] == "RUB":
        rub_amount = transaction["operationAmount"]["amount"]
        return float(rub_amount)
    else:
        raise ValueError("Транзация выполнена не в рублях. Укажите транзакцию в рублях")

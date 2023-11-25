import pprint
import re
from collections import Counter

import numpy as np

from data.config import OPERATIONS
from src.utils import get_list_dict_json


def get_dict_with_key_state(list_dict: list, key: str = "EXECUTED") -> list:
    """Функция принимает список словарей и возвращает список словарей с ключом state = EXECUTED
    :param
    list_dict: Список словарей с операцийми для фильтрации
    key: Ключ для фильтрации
    :return
    list_executed Список словарей отфильтрованный ключом key"""

    list_comrehantions = []
    for dictionary in list_dict:
        if dictionary["state"] == key:
            list_comrehantions.append(dictionary)
    return list_comrehantions


def get_sorted_list(list_dict: list, revers: bool = True) -> list:
    """Функция принимает список словарей и возвращает новый список в котором исходные словари
    отсортированы по убыванию даты(ключ date). Функция принмиает два аргумента, второй необязательный
    задает порядок сортировки(убывание, возраcтание)
    :param
    list_dict: Список словарей с операциями для фильтрации по дате
    revers: bool значение для выбора сортировки(убывание/возрастание)
    :return
    sorted_list Список словарей отсоритированных по атрибуту revers"""

    sorted_list = sorted(list_dict, key=lambda date: date["date"], reverse=revers)
    return sorted_list


def get_list_dict_search_string(list_dict: list, search_string: str) -> list:
    """Функция принимает список словарей с данными о банковских операциях и строку поиска и
    возвращает список словарей, у которых в описании есть данная строка
    param list_dict: Список словарей с данными о операции
    param search_string: Строка поиска
    return Список словарей, у которых в описании есть данная строка"""

    list_dict_with_description = []
    for dictionary in list_dict:
        if bool(dictionary) is True and type(dictionary) is not str:
            value = dictionary.get("description")
            search = re.search(search_string, str(value), flags=re.IGNORECASE)
            if search is not None:
                list_dict_with_description.append(dictionary)

    return list_dict_with_description


def get_dict_description_amount(
    list_dict_operation: list[dict],
    dict_description: dict,
) -> dict:
    keys = dict_description.keys()
    result = list(
        np.concatenate(
            [[des.get("description") for des in get_list_dict_search_string(list_dict_operation, key)] for key in keys]
        )
    )
    counted = Counter(result)
    return dict(counted)


list_dict_op = get_list_dict_json(OPERATIONS)
list_description = {
    "Перевод организации": 0,
    "Перевод с карты на карту": 0,
    "Открытие вклада": 0,
    "Перевод со счета на счет": 0,
}

pprint.pprint(get_dict_description_amount(list_dict_op, list_description))

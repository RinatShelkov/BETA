def get_dict_with_key_state(list_dict: list) -> list:
    """Функция принимает список словарей и возвращает список словарей с ключом state = EXECUTED
    :param list_dict
    :return list_executed"""

    list_executed = []
    for dictionary in list_dict:
        if dictionary["state"] == "EXECUTED":
            list_executed.append(dictionary)
    return list_executed


def get_sorted_list(list_dict: list, revers: bool = True) -> list:
    """Функция принимает список словарей и возвращает новый список в котором исходные словари
    отсортированы по убыванию даты(ключ date). Функция принмиает два аргумента, второй необязательный
    задает порядок сортировки(убывание, возраcтание)
    :param
    list_dict
    revers
    :return sorted_list"""

    sorted_list = sorted(list_dict, key=lambda date: date["date"], reverse=revers)
    return sorted_list

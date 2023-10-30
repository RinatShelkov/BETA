def get_dict_with_key_state(list_dict: list) -> list:
    """Функция принимает список словарей и возвращает список словарей с ключом state = EXECUTED
    :param list_dict
    :return list_executed"""

    list_executed = []
    for dictionary in list_dict:
        if dictionary["state"] == "EXECUTED":
            list_executed.append(dictionary)
    return list_executed

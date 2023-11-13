import json
from os import PathLike


def get_list_dict_json(path_json: PathLike) -> object:
    try:
        with open(path_json, encoding="utf-8") as file:
            file_json = json.load(file)

    except FileNotFoundError:
        file_json = []

    except json.JSONDecodeError:
        file_json = []

    return file_json

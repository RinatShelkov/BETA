from unittest.mock import patch

import pytest

from data.config import OPERATIONS
from src.processing import (get_dict_description_amount, get_dict_with_key_state, get_list_dict_search_string,
                            get_sorted_list)
from src.utils import get_list_dict_json


@pytest.fixture
def list_dict():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.mark.parametrize(
    "key, expected",
    [
        (
            "EXECUTED",
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
        ),
        (
            "CANCELED",
            [
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
        ),
    ],
)
def test_get_dict_with_key_state(list_dict, key, expected):
    assert get_dict_with_key_state(list_dict, key) == expected


@pytest.mark.parametrize(
    "revers, expected",
    [
        (
            True,
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
        ),
        (
            False,
            [
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            ],
        ),
    ],
)
def test_get_sorted_list(list_dict, revers, expected):
    assert get_sorted_list(list_dict, revers) == expected


def test_get_list_dict_search_string():
    with patch("src.processing.get_list_dict_search_string") as mock_get:
        mock_get(get_list_dict_json(OPERATIONS), "Перевод организации").return_value = {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589",
        }

        assert get_list_dict_search_string(get_list_dict_json(OPERATIONS), "Перевод организации")[0] == {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589",
        }
        mock_get.assert_called_once_with(get_list_dict_json(OPERATIONS), "Перевод организации")


def test_get_dict_description_amount():
    with patch("src.processing.get_dict_description_amount") as mock_get:
        mock_get(get_list_dict_json(OPERATIONS), {"Перевод организации": ""}).return_value = {
            "Перевод организации": 40
        }

        assert get_dict_description_amount(get_list_dict_json(OPERATIONS), {"Перевод организации": ""}) == {
            "Перевод организации": 40
        }
        mock_get.assert_called_once_with(get_list_dict_json(OPERATIONS), {"Перевод организации": ""})

import pytest

from data.config import TEST_UTILS_FileNotFoundError, TEST_UTILS_JSONDecodeError, OPERATIONS
from src.utils import get_list_dict_json, get_summ_transaction_rub


@pytest.fixture()
def expected_list_dict_json():
    return "<class 'list'>"


@pytest.mark.parametrize(
    "path_json", [OPERATIONS,
                  TEST_UTILS_FileNotFoundError,
                  TEST_UTILS_JSONDecodeError])
def test_get_list_dict_json(path_json, expected_list_dict_json):
    assert f"{type(get_list_dict_json(path_json))}" == expected_list_dict_json


@pytest.fixture()
def list_dict_json():
    list_dict_json = get_list_dict_json(OPERATIONS)
    return list_dict_json


def test_get_summ_transaction_not_rub(list_dict_json):
    with pytest.raises(ValueError):
        get_summ_transaction_rub(list_dict_json[1])


def test_get_summ_transaction_rub(list_dict_json):
    rub_amount = get_summ_transaction_rub(list_dict_json[0])
    assert rub_amount == 31957.58


def test_get_summ_transaction_rub_error(list_dict_json):
    with pytest.raises(ValueError):
        get_summ_transaction_rub(list_dict_json[74])

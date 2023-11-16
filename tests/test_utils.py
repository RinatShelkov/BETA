import pytest

from data.config import TEST_UTILS_FileNotFoundError, TEST_UTILS_JSONDecodeError, OPERATIONS
from src.utils import get_list_dict_json


@pytest.fixture()
def expected_list_dict_jsom():
    return "<class 'list'>"


@pytest.mark.parametrize(
    "path_json", [OPERATIONS,
                  TEST_UTILS_FileNotFoundError,
                  TEST_UTILS_JSONDecodeError])
def test_get_list_dict_json(path_json, expected_list_dict_jsom):
    assert f"{type(get_list_dict_json(path_json))}" == expected_list_dict_jsom

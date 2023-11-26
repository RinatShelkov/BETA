from unittest.mock import patch

import pytest

from data.config import TEST_UTILS_FileNotFoundError, TEST_UTILS_JSONDecodeError, OPERATIONS
from data.config import TRANSACTION_PATH_XLSX, TRANSACTION_PATH_CSV
from src.utils import get_list_dict_json, get_summ_transaction_rub, reading_csv_xlsx_file


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


def test_reading_xlsx_file():
    with patch('src.utils.reading_csv_xlsx_file') as mock_get:
        mock_get(TRANSACTION_PATH_XLSX).return_value = 650703.0

        assert reading_csv_xlsx_file(TRANSACTION_PATH_XLSX)[0]['id'] == 650703.0
        mock_get.assert_called_once_with(TRANSACTION_PATH_XLSX)


def test_reading_csv_file():
    with patch('src.utils.reading_csv_xlsx_file') as mock_get:
        mock_get(TRANSACTION_PATH_CSV).return_value = 650703.0

        assert reading_csv_xlsx_file(TRANSACTION_PATH_CSV)[0]['id'] == 650703.0
        mock_get.assert_called_once_with(TRANSACTION_PATH_CSV)


def test_reading_file_invalid():
    with patch('src.utils.reading_csv_xlsx_file') as mock_get:
        mock_get(OPERATIONS).return_value = "Неверное расширение файла, задан неправильный путь"

        assert reading_csv_xlsx_file(OPERATIONS) == "Неверное расширение файла, задан неправильный путь"
        mock_get.assert_called_once_with(OPERATIONS)

from pathlib import Path

ROOT_PATH = Path(__file__).resolve().parent.parent
SRC_PATH = ROOT_PATH.joinpath("src")
LOG_PATH = ROOT_PATH.joinpath("log")
OPERATIONS = ROOT_PATH.joinpath("data").joinpath("operations.json")
TEST_UTILS_JSONDecodeError = ROOT_PATH.joinpath("data").joinpath("test_get_list_dict_json.json")
TEST_UTILS_FileNotFoundError = ROOT_PATH.joinpath("data").joinpath("test_get_list_dict_invalid")
LOG_MASKS_PATH = ROOT_PATH.joinpath("log").joinpath("masks.log")
LOG_UTILS_PATH = ROOT_PATH.joinpath("log").joinpath("utils.log")
TRANSACTION_PATH_CSV = ROOT_PATH.joinpath("data").joinpath("transactions.csv")
TRANSACTION_PATH_XLSX = ROOT_PATH.joinpath("data").joinpath("transactions_excel.xlsx")
import datetime
import os.path

import pytest

from data.config import LOG_PATH
from src.decorators import log


@pytest.mark.parametrize(
    "arg_1, arg_2, expected", [(1, 2, " test_func ok"), (1, "2", " test_func error: TypeError. Inputs: (1, '2'), {}")]
)
def test_log_decorator_filename(arg_1, arg_2, expected):
    filename = "test.txt"
    if os.path.exists(os.path.join(LOG_PATH, filename)):
        os.remove(os.path.join(LOG_PATH, filename))

    @log(filename)
    def test_func(x, y):
        return x + y

    time_func = datetime.datetime.now().strftime("%Y-%m-%d %X")
    test_func(arg_1, arg_2)

    with open(os.path.join(LOG_PATH, filename)) as file:
        log_text = file.read().strip()

    expected_log_text = time_func + expected

    assert log_text == expected_log_text


@pytest.mark.parametrize(
    "arg_1, arg_2, expected", [(1, 2, " test_func ok"), (1, "2", " test_func error: TypeError. Inputs: (1, '2'), {}")]
)
def test_log_decorator_not_filename(capsys, arg_1, arg_2, expected):
    @log()
    def test_func(x, y):
        return x + y

    time_func = datetime.datetime.now().strftime("%Y-%m-%d %X")
    test_func(arg_1, arg_2)

    log_text = capsys.readouterr()
    expected_log_text = time_func + expected

    assert log_text.out.strip() == expected_log_text

import datetime
import os
from functools import wraps
from typing import Any, Callable

from data.config import LOG_PATH


def log(filename: Any = None) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Callable | Any:
            time_func = datetime.datetime.now().strftime("%Y-%m-%d %X")

            try:
                result_func = func(*args, **kwargs)
                log_text = f"{time_func} {func.__name__} ok\n"

            except Exception as error:
                log_text = f"{time_func} {func.__name__} error: {type(error).__name__}. Inputs: {args}, {kwargs}\n"
                result_func = None

            if filename is not None:
                with open(os.path.join(LOG_PATH, filename), "a", encoding="utf-8") as f:
                    f.write(log_text)
            else:
                print(log_text)

            return result_func

        return wrapper

    return decorator

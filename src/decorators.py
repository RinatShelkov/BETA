import datetime
import os
from functools import wraps
from typing import Any, Callable

from data.config import ROOT_PATH


def log(filename: Any = None) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            time_func = datetime.datetime.now().strftime("%Y-%m-%d %X")
            result = "ok"
            text_error = None

            try:
                # Код, в котором может возникнуть ошибка
                func(*args, **kwargs)

            except Exception as e:  # Сохранение ошибки в переменную
                result = "error"
                text_error = e
            if filename is not None:
                if result == "error":
                    with open(os.path.join(ROOT_PATH, filename), "a", encoding="utf-8") as f:
                        f.write(f"{time_func} {func.__name__} {result}: {text_error}. Inputs: {*args, *kwargs}\n")
                else:
                    with open(os.path.join(ROOT_PATH, filename), "a", encoding="utf-8") as f:
                        f.write(f"{time_func} {func.__name__} {result}\n")
            else:
                if result == "error":
                    print(f"{time_func} {func.__name__} {result}: {text_error}. Inputs: {*args, *kwargs}")
                else:
                    print(f"{time_func} {func.__name__} {result}")

        return wrapper

    return decorator

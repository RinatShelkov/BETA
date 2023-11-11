import datetime
from functools import wraps
from typing import Any, Callable


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
                    with open(filename, "a", encoding="utf-8") as f:
                        f.write(f"{time_func} {func.__name__} {result}: {text_error}. Inputs: {*args, *kwargs}\n")
                else:
                    with open(filename, "a", encoding="utf-8") as f:
                        f.write(f"{time_func} {func.__name__} {result}\n")
            else:
                if result == "error":
                    print(f"{time_func} {func.__name__} {result}: {text_error}. Inputs: {*args, *kwargs}")
                else:
                    print(f"{time_func} {func.__name__} {result}")

        return wrapper

    return decorator

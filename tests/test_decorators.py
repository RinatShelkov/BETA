from src.decorators import log


def test_log_decorator_not_filename():
    @log()
    def test_func(x, y):
        return x + y

    test_func(1, 2)
    test_func(1, "2")


def test_log_decorator_filename():
    @log("test.txt")
    def test_func(x, y):
        return x + y

    test_func(1, 2)
    test_func(1, "2")

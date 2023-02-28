import time


def speed(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        end = time.time()

        print(f"Func speed: {end - start} sec.")

        return res
    return wrapper


class Speed:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        start = time.time()
        res = self.func(*args, **kwargs)
        end = time.time()

        print(f"Func speed: {end - start} sec.")

        return res


@Speed
def test_func():
    time.sleep(1)


test_func()
# speed(test_func)()

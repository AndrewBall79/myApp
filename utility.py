from time import time


def performance(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = fn(*args, **kwargs)
        t2 = time()
        print(f'took {t2-t1} ms')
        return result
    return wrapper


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    return num1 / num2

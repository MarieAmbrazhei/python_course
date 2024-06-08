"""Homework11_3:Decorations Writing and implementing programs."""

from functools import wraps


# Декоратор типов
# Напишите декоратор, который проверял бы тип параметров функции,
# конвертировал их если надо и складывал:

def typed(r_type):
    """Checks the input of a function parameters ,
    converts them if necessary, and then adds them up
    """

    def decorator_type(func):
        @wraps(func)
        def wrapper(*args):
            args = list(map(r_type, args))
            return func(*args)

        return wrapper

    return decorator_type


@typed(r_type=str)
def add_str(a, b):
    """returns the sum of all arguments"""
    return a + b


assert add_str("3", 5) == '35'
assert add_str(5, 5) == '55'
assert add_str('a', 'b') == 'ab'


@typed(r_type=int)
def add_int(a, b, c):
    """returns the sum of all arguments"""
    return a + b + c


assert add_int(5, 6, 7) == 18


@typed(r_type=float)
def add_float(a, b, c):
    """returns the sum of all arguments"""
    return a + b + c


assert add_float(0.1, 0.2, 0.4) == 0.7000000000000001

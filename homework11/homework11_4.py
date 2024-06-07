"""Homework11_4:Decorators. Writing and implementing programs."""

from typing import Dict

# Функция кэширования *
# Напишите декоратор @cache, который кэширует результаты вызова функции и
# возвращает закэшированное значение при повторных вызовах с теми же
# аргументами. Это поможет избежать повторных вычислений для одинаковых
# входных данных и ускорит работу программы.
# Подсказки:
# Используйте словарь для хранения закэшированных значений. Ключом словаря
# будет набор аргументов функции, а значением - результат вызова функции
# с этими аргументами.
# Внутри декоратора, передайте аргументы функции в качестве ключа для доступа
# к закэшированным значениям.
# Если ключ уже есть в словаре, верните соответствующее значение. Если ключа
# нет, вызовите функцию, сохраните результат в словаре и верните его.

cached_results: Dict[str, int] = {}


def cache(func):
    """ Decorator to cache the results of a function.
    When the function is called with the same arguments,
    it returns the cached result, avoiding repeated computations.
   """

    def wrapper(n):
        if cached_results.get(n) is not None:
            return cached_results[n]
        result = func(n)
        cached_results[n] = result
        return result

    return wrapper


@cache
def fibonacci(n):
    """Calculats Fibonacci numbers"""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


assert fibonacci(5) == 5
assert fibonacci(10) == 55
assert fibonacci(5) == 5
assert fibonacci(10) == 55

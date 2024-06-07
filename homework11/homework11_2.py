"""Homework11_2:Decorators. Writing and implementing programs."""


# Вернуть число
# Создайте декоратор, который проверяет, является ли результат функции числом и
# выводит сообщение об ошибке, если это не так. Вот некоторые подсказки:
# Внутри декоратора, после вызова функции, проверьте тип результата с помощью
# функции isinstance().
# Если тип не является числом, выведите сообщение об ошибке с помощью функции
# print().

def is_number(func):
    """Checks if the result of the function is a number."""

    def wrapper(*args):
        result = func(*args)
        if not isinstance(result, (int, float)):
            print(f'{result} is not a number.')
            return None
        return func(*args)

    return wrapper


@is_number
def returned_number(a):
    """"Returns the values that were provided as arguments"""
    return a


assert returned_number('a') is None
assert returned_number(1) == 1
assert returned_number(1.2) == 1.2

"""Homework11_1:Decorators. Writing and implementing programs."""


# Положительные аргументы функции
# Напишите декоратор @validate_arguments, который проверяет, что все
# аргументы функции являются положительными числами. Если встречается
# аргумент, не соответствующий этому условию, функция должна вывести сообщение
# об ошибке. Вот некоторые подсказки:
# Внутри декоратора, используйте цикл for для перебора аргументов функции.
# Используйте оператор if для проверки,
# является ли аргумент положительным числом.
# Если аргумент не соответствует условию, используйте оператор raise для вызова
# исключения ValueError.

def validate_arguments(func):
    """Returns ValueError if function argument is
       not a positive number"""

    def wrapper(*args):
        for arg in args:
            if arg <= 0:
                raise ValueError(f'Arg {arg} is not a positive number')
        return func(*args)

    return wrapper


@validate_arguments
def result_of_validate(a, b):
    """Prints the passed arguments"""
    print(a, b)


try:
    result_of_validate(2, 4)
except ValueError as e:
    print(e)

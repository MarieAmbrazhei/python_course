""" Homework9_3: Functions. Writing and implementing programs
in Python """


# Число на против
# Рассмотрим целые числа от 0 до n-1, записанные по окружности так, чтобы
# расстояние между любыми двумя соседними числами было одинаковым (обратите
# внимание, что 0 и n-1 тоже являются соседними).
# Учитывая n и first_number, найдите число, которое написано в радиально
# противоположной позиции от first_number.
# Для n = 10 и first_number = 2 вывод должен быть (n, first_number) = 7.

def find_opposite_number(n: int, first_number: int) -> int:
    """
    Find the the radially opposite number.
    """
    degree_between_numbers = 360 / n
    opposite_number = (180 / degree_between_numbers + first_number) % n
    return int(opposite_number)


assert find_opposite_number(10, 9)

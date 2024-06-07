""" Homework9_2: Functions. Writing and implementing programs
in Python """


# Последовательность
# Дана последовательность целых чисел в виде массива. Определите, можно ли
# получить строго возрастающую последовательность, удалив из массива не более
# одного элемента.
# Примечание: последовательность a0, a1, ..., an считается строго возрастающей,
# если a0 < a1 < ... < an. Последовательность, содержащая только один элемент,
# также считается строго возрастающей.
# Примеры
# Для последовательности = [1, 3, 2, 1], вывод должен быть решение = False.
# В этом массиве нет ни одного элемента, который можно было бы удалить, чтобы
# получить строго возрастающую последовательность.
# Для последовательности = [1, 3, 2] вывод должен быть = True.
# Вы можете удалить 3 из массива, чтобы получить строго возрастающую
# последовательность [1, 2]. Альтернативно можно убрать 2, чтобы получить
# строго возрастающую последовательность [1, 3].

def can_be_ascending_by_removing_one(seq_int: list) -> bool:
    """
    Get a strictly ascending sequence by removing only one element.
    """
    if len(seq_int) - len(set(seq_int)) > 1:
        print(f'Duplicate count is: {len(seq_int) - len(set(seq_int))}')
        return False
    count = 0

    for i in range(len(seq_int) - 1):
        if seq_int[i] >= seq_int[i + 1]:
            count += 1
            if count > 1:
                return False

            if i > 0 and seq_int[i - 1] >= seq_int[i + 1] and i + 2 < len(
                    seq_int) and seq_int[i] >= seq_int[i + 2]:
                return False

    return True


assert can_be_ascending_by_removing_one([1, 2, 3])
assert can_be_ascending_by_removing_one([1, 2, 1, 2])
assert can_be_ascending_by_removing_one([1, 3, 2, 1])
assert can_be_ascending_by_removing_one([1, 2, 3, 4, 5, 3, 5, 6])
assert can_be_ascending_by_removing_one([40, 50, 60, 10, 20, 30])

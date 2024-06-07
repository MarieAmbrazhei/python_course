""" Homework9_1: Functions. Writing and implementing programs
in Python """


# Validate
# Ваша задача написать программу, принимающее число - номер кредитной карты
# (число может быть четным или не четным).
# И проверяющей может ли такая карта существовать. Предусмотреть защиту от
# ввода букв, пустой строки и т.д. Примечания Алгоритм Луна.

def validate_card(card_number: int) -> bool:
    """
    Validate a credit card number using the Luhn algorithm.
    """
    if isinstance(card_number, int):
        card_number_str = str(card_number)
        even = []
        odd = []
        card_number_reverted = card_number_str[::-1]
        for elem in range(len(card_number_str)):
            if (elem + 1) % 2 == 0:
                odd_number = int(card_number_reverted[elem]) * 2
                if odd_number > 9:
                    odd_number -= 9
                odd.append(odd_number)

            else:
                even.append(int(card_number_reverted[elem]))

        final_sum = sum(odd + even)
        if final_sum % 10 == 0:
            return True
        return False
    print(f'Card number should have datatype int '
          f'current type is {type(card_number)}')
    return False


assert validate_card(4561261212345464), 'Please provide correct card number'
assert validate_card(4561261212345467)

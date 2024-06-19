"""Homework10_3:Functions. Writing and implementing programs."""


# Подсчет количества букв
# На вход подается строка, например, "cccbba" результат работы
# программы - строка “c3b2a"

def count_letters(given_string: str) -> str:
    """
     Returns a string with
     unique characters and their quantity.
     """
    result_string = ''
    letters = {}

    def count_and_remove(cut_string: str) -> str:
        nonlocal result_string, letters
        for idx, letter in enumerate(cut_string):
            if letter not in letters:
                letters[letter] = 1
            else:
                letters[letter] += 1
            if len(cut_string) == 1 or len(set(cut_string)) == 1:
                result_string += (letter + str(len(cut_string)))
                return result_string.replace('1', '')
            if cut_string[idx] != cut_string[idx + 1]:
                result_string += (letter + str(letters.get(letter)))
                cut_string = cut_string[idx + 1:]
                letters = {}
                return count_and_remove(cut_string)
        # to pass pylint R1710
        return ''

    return count_and_remove(given_string)


assert count_letters('cccbba') == "c3b2a"
assert count_letters('abeehhhhhccced') == "abe2h5c3ed"
assert count_letters('aaabbceedd') == "a3b2ce2d2"
assert count_letters('abcde') == "abcde"
assert count_letters('aaabbdefffff') == "a3b2def5"

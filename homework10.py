"""Homework10:Functions. Writing and implementing programs."""


# Строки с заданным символом
# Напишите программу, которая бы работала следующим образом - находила символ
# "#" и если этот символ найден - удаляла предыдущий символ из строки. Ваша
# задача обработать строки с "#" символом

def remove_excessive_symbols(str_with_hash: str) -> str:
    """
    Removes the character preceding each '#' in the string.
    """
    while True:
        try:
            index = str_with_hash.index('#')
            if index > 0:
                str_with_hash = str_with_hash[:index - 1] + str_with_hash[
                                                            index + 1:]
            else:
                str_with_hash = str_with_hash[index + 1:]
        except ValueError:
            break
    return str_with_hash


assert remove_excessive_symbols("a#bc#d") == "bd"
assert remove_excessive_symbols("abc#d##c") == "ac"
assert remove_excessive_symbols("abc##d######") == ""
assert remove_excessive_symbols("#######") == ""
assert remove_excessive_symbols("") == ""


# Свечи
# Когда свеча догорает, остается остаток. Остатки можно объединить, чтобы
# создать новую свечу, которая при догорании, в свою очередь, оставит
# еще один остаток. У вас есть количество свечей. Какое общее количество
# свечей вы можете сжечь, если предположить, что вы создадите
# новые свечи, как только у вас останется достаточно остатков?

def solution(candles_number: int, make_new: int) -> int:
    """
    Calculates total candles burned, including those made from remainders.
    """
    total_burned = 0
    candle_stubs = 0

    while candles_number > 0:
        total_burned += candles_number
        candle_stubs += candles_number
        candles_number = candle_stubs // make_new
        candle_stubs = candle_stubs % make_new
    return total_burned


assert solution(5, 2) == 9
assert solution(1, 2) == 1
assert solution(15, 5) == 18
assert solution(12, 2) == 23
assert solution(6, 4) == 7
assert solution(13, 5) == 16
assert solution(2, 3) == 2


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

"""Homework10._1:Functions. Writing and implementing programs."""


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

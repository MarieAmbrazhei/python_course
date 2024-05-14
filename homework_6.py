"""Homework#6; Python data types: creating lists and using basic methods."""

# Перевести строку в список 'Robin Singh' => ['Robin”, “Singh']
NAME = 'Robin Singh'
split_name = NAME.split()
print(split_name)

# 'I love arrays they are my favorite' =>
# ['I', 'love', 'arrays', 'they', 'are', 'my', 'favorite']
LONG_STRING = 'I love arrays they are my favorite'
split_long_string = LONG_STRING.split()
print(split_long_string)

# Дан список: [Ivan, Ivanou], и 2 строки: Minsk, Belarus
# Напечатайте текст: “Привет, Ivan Ivanou! Добро пожаловать в Minsk Belarus”
fullname_in_list = ['Ivan', 'Ivanou']
CITY = 'Minsk'
COUNTRY = 'Belarus'
print(f'Привет, {" ".join(fullname_in_list)}! Добро пожаловать'
      f' в {CITY} {COUNTRY}')

# Дан список ['I', 'love', 'arrays', 'they', 'are', 'my', 'favorite']
# сделайте из него строку => 'I love arrays they are my favorite'
list_of_words = ['I', 'love', 'arrays', 'they', 'are', 'my', 'favorite']
STR_OF_WORDS = ' '.join(list_of_words)
print(STR_OF_WORDS)

# Создайте список из 10 элементов, вставьте на 3-ю позицию новое значение,
# удалите элемент из списка под индексом 6
given_list = ['one', 2, 0.5, {'a': 'b'}, 'python', [3, 6], 3,
              'THE BEST', 8, '5g']
print(f'Initial length is: {len(given_list)}')
given_list.insert(3, 'Awesome_python')
print(f'updated list after inserting "Awesome_python": '
      f'{given_list} with length: {len(given_list)}')
del given_list[6]
print(f'updated list after deleting element at index 6: '
      f'{given_list} with length: {len(given_list)}')

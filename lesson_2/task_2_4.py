"""
Задание 4.
Пользователь вводит строку из нескольких слов, разделённых пробелами.
Вывести каждое слово с новой строки. Строки нужно пронумеровать.
Если слово длинное, выводить только первые 10 букв в слове.
"""


list_words = [str(i) for i in input('Введите слова  пробел: ').split()]
i = 1
for word in list_words:
    print(f'{i}: {word[0:10]}')
    i += 1

"""
Панграмма - предложение, которое использует каждую букву алфавита (в нашем случае - английского алфавита).
Необходимо реализовать код, который скажет, является предложение панграммой или нет.
Буквы в верхнем и нижнем регистрах считаются эквивалентными.
Предложения содержат только буквы английского алфавита, без пробелов и т.п.
Проверка:
pytest ./2_sentence_is_pangram/test.py
"""


def is_sentence_is_pangram(sentence: str) -> bool:
    # создадим словарь алфавита из строки с алфавитом
    letters = "abcdefghijklmnopqrstuvwxyz"
    alphabet = {letter: 0 for letter in letters}
    # предполагаем, что на вход у нас только буквы
    # прибавляем к ключу-букве значение 1, если ее встретили
    for letter in sentence:
        alphabet[letter.lower()] += 1
    # после этого смотрим, есть ли нули
    return not (0 in alphabet.values())

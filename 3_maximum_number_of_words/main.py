"""
Вам дан список предложений.
предложения содержит только слова, которые разделены единичными пробелами.
Необзодимо вернуть максимальное количество слов, которое содержится в одном предложении.
sentences[i] - это одно предложение.
Если ни одно из предложений не содержит слов, то нужно вернуть 0
Проверка:
pytest ./3_maximum_number_of_words/test.py
"""


def get_max_number_of_words_from_sentences(sentences: list[str]) -> bool:
    list_of_number_of_words = [len(sentence.split(' ')) if (sentence) else 0 for sentence in sentences]
    return (max(list_of_number_of_words))

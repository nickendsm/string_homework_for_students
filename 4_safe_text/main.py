"""
Вы - начинающий журналист. Накануне вечером вы написали статью про кошек для ветеринарного журнала,
но забыли заблокировать компьютер. На утро вы обнаружили, что вашей собаке не понравилось, что пишете вы про кошек,
а не про собак.
Она испортила вам статью и оставила следующую записку:
1) я заменила все слова "cat" в статье на "woof-woof"
2) я развернула каждое предложение и добавила в его конец, перед точкой, строку, состояющую из символа "!".
Длина этой строки восклицательных знаков равна длине предложения (без учета точки).
3) я перевела все предложения в верхний регистр

Попробуй вернуть все назад, woof-woof!

Ваша задача вернуть текст в первозданный вид.
Ограничения:
1) В результате предложения разделены символом '.\n'.
2) В результате все предложения начинаются с буквы верхнего регистра. Это единственная буква в верхнем регистре
в предложении.

Исходный текст представлен в файле correct_article.txt.
Испорченный текст представлен в файле wrong_article.txt.

Реализуйте код, который восстановит статью и вернет ее в качестве результата работы функции.

Проверка результата:
pytest ./4_safe_text/text.py
"""
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SPLIT_SYMBOL = '.\n'


def get_article(path: str) -> str:
    with open(path, 'r') as file:
        file_article = file.read()
    return file_article


def get_correct_article() -> str:
    return get_article(os.path.join(BASE_DIR, '4_safe_text', 'articles', 'correct_article.txt'))


def get_wrong_article() -> str:
    return get_article(os.path.join(BASE_DIR, '4_safe_text', 'articles', 'wrong_article.txt'))


def recover_article() -> str:
    wrong_article = get_wrong_article()
    # сначала делим на предложения, убираем восклицательные знаки
    correct_article = wrong_article.split('.\n')
    correct_article = [sentence[:sentence.find("!")] for sentence in correct_article]
    # потом переворачиваем и переводим в нижний регистр
    correct_article = [(sentence[::-1]).lower() for sentence in correct_article]
    # заменяем слова
    correct_article = [sentence.replace("woof-woof", "cat") for sentence in correct_article]
    # заглавные буквы
    correct_article = [sentence[0].upper()+sentence[1:] if sentence else "" for sentence in correct_article]
    return ".\n".join(correct_article)

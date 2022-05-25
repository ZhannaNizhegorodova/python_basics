"""
6. Реализовать функцию int_func(), принимающую слово из маленьких
латинских букв и возвращающую его же, но с прописной первой буквой.
Например, print(int_func(‘text’)) -> Text.

Продолжить работу над заданием. В программу должна попадать строка из слов,
разделенных пробелом. Каждое слово состоит из латинских букв в нижнем регистре.
Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
Необходимо использовать написанную ранее функцию int_func().
"""


def int_func(word):
    return word.title()


print(int_func('text word list'))


def my_tittle(words):
    list_words = str(words).split()
    new_list = []
    for i in list_words:
        i = i[0].upper() + i[1:]  # Либо i = i.capitalize()
        new_list.append(i)
    return ' '.join(new_list)


print(my_tittle('text word list'))

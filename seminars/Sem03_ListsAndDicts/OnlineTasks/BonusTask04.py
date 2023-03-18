"""
Напишите программу, которая принимает на вход строку,
и отслеживает, сколько раз каждый символ уже встречался.
Количество повторов добавляется к символам с помощью постфикса формата _n.
Пример ввода:
a a a b c a a d c d d

Пример вывода:
a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
"""


def transfer(source_list: list):

    for el in source_list:
        if el not in count_dict:
            count_dict[el] = 0
            yield el
            continue
        count_dict[el] += 1
        yield f'{el}_{count_dict[el]}'


source = 'a a a b c a a d c d d'.split()
count_dict = {}
print(' '.join(_ for _ in transfer(source)))

"""
Напишите программу, которая принимает на вход строку,
и отслеживает, сколько раз каждый символ уже встречался.
Количество повторов добавляется к символам с помощью постфикса формата _n.
Пример ввода:
- "a a a b c a a d c d d"

Пример вывода:
a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
"""


def using_dict(source: str) -> None:

    count_dict = {}
    stack = []
    for el in source:
        if not el.isalnum():
            continue
        elif el not in count_dict:
            count_dict[el] = 0
            stack.append(el)
            continue
        count_dict[el] += 1
        stack.append(f'{el}_{count_dict[el]}')

    print('From using_dict\t->', ' '.join(stack))


def using_str(sequence: str):

    stack = []
    for index in range(len(sequence)):
        char = sequence[index]
        if not char.isalnum():
            continue
        counter = sequence[:index].count(char)
        stack.append(char if counter == 0 else f'{char}_{counter}')
    print('From using_str\t->', ' '.join(stack))


def main() -> None:
    queue = 'a a a b c a a d c d d'
    using_str(queue)
    using_dict(queue)


if __name__ == '__main__':
    main()

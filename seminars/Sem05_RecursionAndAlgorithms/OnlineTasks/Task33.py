""" Задача №33:
Хакер Василий получил доступ к классному журналу и хочет заменить все свои
минимальные оценки на максимальные. Напишите программу, которая заменяет оценки
Василия, но наоборот: все максимальные – на минимальные.

Input:
 -  5 -> [1, 3, 3, 3, 4]
Output:
-   [1, 3, 3, 3, 1]
"""


from random import randint


def change_marks(marks: list) -> None:
    """ Заменяет все максимальные значения в списке чисел, на минимальное значение списка

    :param marks: Список чисел, <class 'list'>
    :return: None
    """
    min_mark, max_mark = min(marks), max(marks)
    while max_mark in marks:
        index = marks.index(max_mark)
        marks[index] = min_mark


def main() -> None:
    """ Главная функция.

    :return: None
    """
    jornal_length = int(input('Введите кол-во оценок ученика:\n>>> '))
    print(jornal := [randint(1, 5) for _ in range(jornal_length)])
    change_marks(jornal)
    print(jornal)


if __name__ == '__main__':
    main()

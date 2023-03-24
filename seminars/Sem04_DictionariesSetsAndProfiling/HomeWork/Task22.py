""" Задача №22:
Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений
в порядке возрастания все те числа, которые встречаются в обоих наборах.
Пользователь вводит 2 числа.
    N - кол-во элементов первого множества.
    M - кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

11 6
2 4 6 8 10 12 10 8 6 4 2
3 6 9 12 15 18
6 12
"""


def get_intersection_of_sets(*args) -> list:
    """ Функция возвращает пересечения переданных последовательностей.

    :param args: Переданные последовательности.
    :return: Список из элементов пересечения последовательностей, <class 'int'>
    """
    if len(args) == 1:
        result_of_intersection = list(*args)
        result_of_intersection.sort()
        return result_of_intersection
    try:
        temp_tuple = tuple(map(set, args))
    except TypeError as ex:
        print(ex)
        return list()
    else:
        length = len(temp_tuple)
        intersection = lambda index: temp_tuple[index - 1] & temp_tuple[index]
        temp_intersections = map(intersection, range(1, length))

        return get_intersection_of_sets(*temp_intersections)


# [ ] Добавить функционал ввода последовательностей пользователем.
def user_input():
    pass


def main() -> None:
    """ Главная функция.

    :return: None
    """
    fst, sec = [2, 4, 6, 8, 10, 12, 10, 8, 6, 4, 2], [3, 6, 9, 12, 15, 18]
    print(get_intersection_of_sets(fst, sec))


if __name__ == '__main__':
    main()

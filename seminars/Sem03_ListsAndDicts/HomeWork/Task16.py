"""Задача №16:
 Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1&..N]. Пользователь
в первой строке вводит натуральное число N – количество элементов в массиве. В последующих строках
записаны N целых чисел Ai. Последняя строка содержит число X

5
[1, 2, 3, 4, 5]
3
-> 1
"""


from random import randint


def get_count_value_in_list(list_of_values: list, value) -> int:
    """ Считает, сколько раз значение (value) встретилось в списке (list_of_values).

    :param list_of_values: Список со значениями, <class 'list'>.
    :param value: Искомое значение, <class 'int'>.
    :return: Сколько раз значение встретилось в списке, <class 'int'>.
    """
    return sum([1 for _ in list_of_values if _ == value])


def get_list_of_values(upper_bound: int, min_value: int = 0, max_value: int = 9) -> list:
    """ Инициализирует и возвращает список длинной upper_bound заполненный
    случайными целыми числами от min_value до max_value.

    :param upper_bound: Длина генерируемого списка, <class 'int'>.
    :param min_value: Минимальное значение для заполнения списка, <class 'int'>.
    :param max_value: Максимальное значение для заполнения списка, <class 'int'>.
    :return: Список заполненный случайными целыми числами,<class 'list'>.
    """
    return [randint(min_value, max_value) for _ in range(upper_bound)]


def get_user_values(list_length=None, search_value=None) -> tuple:
    """ Обрабатывает 2 пользовательских ввода. Пользователь вводит:
     - длину списка;
     - искомое значение.

     Если введенные пользователем данные не удалось преобразовать к целому числу, вызывается рекуррентный случай с
     передачей валидных значений.

    :param list_length: Валидное значение длины списка, <class 'int'>.
    :param search_value: Валидное искомое значение, <class 'int'>.
    :return: Длину списка для инициализации списка значений, искомое значение для поиска в списке, <class 'tuple'>.
    """
    if list_length is None:
        list_length = input('Введите длину списка:\n>>> ')
    try:
        list_length = int(list_length)
    except ValueError:
        print('Не удалось преобразовать строку к числу. Повторите ввод.')
        return get_user_values()
    except Exception as ex:
        print('Произошла непредвиденная ошибка:', ex)
        return get_user_values()

    if search_value is None:
        search_value = input('Введите искомое значение:\n>>> ')
    try:
        search_value = int(search_value)
    except ValueError:
        print('Не удалось преобразовать строку к числу. Повторите ввод.')
        return get_user_values(list_length=list_length)
    except Exception as ex:
        print('Произошла непредвиденная ошибка:', ex)
        return get_user_values()

    return list_length, search_value


def main() -> None:
    """ Главная функция.

    :return: None.
    """
    length, desired_value = get_user_values()
    list_with_randint = get_list_of_values(length)
    count = get_count_value_in_list(list_with_randint, desired_value)
    print(f'{list_with_randint}\nЗначение "{desired_value}" встретилось {count} раз.')


if __name__ == '__main__':
    main()

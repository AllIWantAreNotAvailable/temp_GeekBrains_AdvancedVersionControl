"""Задача №18:
Требуется найти в массиве A[1...N] самый близкий по величине элемент к заданному числу X. Пользователь
 в первой строке вводит натуральное число N – количество элементов в массиве. В последующих строках записаны
N целых чисел Ai. Последняя строка содержит число X

5
[1, 2, 3, 4, 5]
6
-> 5
"""


def get_value_close_to_desired(list_of_values: list, searching_value: int) -> int:
    """ Возвращает значение наиболее близкое или равное переданному (searching_value) из списка (list_of_values).

    :param list_of_values: Список значений, в котором ведется поиск, <class 'list'>.
    :param searching_value: Значение, которое ищем в списке, <class 'list'>.
    :return: Значение наиболее близкое к искомому, <class 'int'>.
    """
    value = 0  # Будет 100% работать только с данным условием задачи -> [1...N]
    for el in list_of_values:
        if value < el <= searching_value:
            value = el
    return value


def get_list_of_values(length: int, min_value: int = 1) -> list:
    """ Возвращает числовой ряд (список) от min_value до length включительно.

    :param length: Длина списка, <class 'int'>
    :param min_value: Первое значение в списке, <class 'int'>
    :return: Список значений [min_value...length], <class 'int'>
    """
    return [x for x in range(min_value, length + 1)]


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
    """ Главная функция

    :return: None
    """
    length_of_list,  desired_value = get_user_values()
    list_of_randint = get_list_of_values(length_of_list)
    print(list_of_randint, f'\nСамое близкое значение к "{desired_value}" ->',
          get_value_close_to_desired(list_of_randint, desired_value))


if __name__ == '__main__':
    main()

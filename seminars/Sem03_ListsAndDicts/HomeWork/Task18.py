"""Задача №18:
Требуется найти в массиве A[1...N] самый близкий по величине элемент к заданному числу X. Пользователь
 в первой строке вводит натуральное число N – количество элементов в массиве. В последующих строках записаны
N целых чисел Ai. Последняя строка содержит число X

5
[1, 2, 3, 4, 5]
6
-> 5
"""


from random import randint


def get_value_close_to_desired(list_of_values: list, searching_value: int) -> tuple:
    """ Возвращает значения наиболее близкое или равное переданному (searching_value) из списка (list_of_values).

    :param list_of_values: Список значений, в котором ведется поиск, <class 'list'>.
    :param searching_value: Значение, которое ищем в списке, <class 'list'>.
    :return: Значения наиболее близкое к искомому, <class 'tuple'>.
    """
    sorted_values = sorted(list_of_values)
    nearest_lower = sorted_values[0]
    nearest_bigger = sorted_values[-1]

    if searching_value < nearest_lower:
        return nearest_lower,
    elif nearest_bigger < searching_value:
        return nearest_bigger,

    for index in range(1, len(sorted_values[1:-1])):
        current_element = sorted_values[index]

        if current_element == searching_value:
            return current_element,
        if nearest_lower < current_element < searching_value:
            nearest_lower = current_element
        if searching_value < current_element < nearest_bigger:
            nearest_bigger = current_element

    if abs(nearest_lower - searching_value) < abs(nearest_bigger - searching_value):
        return nearest_lower,
    elif abs(nearest_lower - searching_value) > abs(nearest_bigger - searching_value):
        return nearest_bigger,
    else:
        return nearest_lower, nearest_bigger


def get_list_of_values(upper_bound: int, min_value: int = -10, max_value: int = 10) -> list:
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
    """ Главная функция

    :return: None
    """
    length_of_list,  desired_value = get_user_values()
    list_of_randint = get_list_of_values(length_of_list)
    values = get_value_close_to_desired(list_of_randint, desired_value)
    temp_text = 'Наиболее близкое(ие) по величине: '
    print(sorted(list_of_randint), f'\nСамое близкое значение к "{desired_value}" ->',
          f'{temp_text}{values[0]}' if len(values) == 1 else f'{temp_text} {values[0]} и {values[1]}')


if __name__ == '__main__':
    main()

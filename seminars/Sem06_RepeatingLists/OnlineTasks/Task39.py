"""Задача №39:
Даны два массива чисел. Требуется вывести те элементы первого массива (в том порядке,
в каком они идут в первом массиве), которых нет во втором массиве. Пользователь вводит
число N - количество элементов в первом массиве, затем N чисел - элементы массива.
Затем число M - количество элементов во втором массиве. Затем элементы второго массива

Input:
-   7 -> [3, 1, 3, 4, 2, 4, 12]
-   6 -> [4, 15, 43, 1, 15, 1]
Output:
- [3, 3, 2, 12]

(каждое число вводится с новой строки)
"""


def get_difference_of_arrays(decrement: tuple, subtraction: tuple) -> tuple:
    return tuple(el for el in decrement if el not in subtraction)


def stop_input(element: str, stop_chars: tuple) -> bool:
    return element not in stop_chars


def get_invitation(ordinal_number: int) -> str:
    return f'Введите {ordinal_number}-й элемент массива:\n>>> '


def get_array() -> tuple:
    counter = 1
    stop_chars = ('-', 'stop')
    elements = list()
    pretty_text = '", "'.join(x for x in stop_chars)
    print('Заполните массив целочисленными значениями. Чтобы остановить ввод элементов',
          f'введите один из символов: "{pretty_text}".')

    while stop_input(new_element := input(get_invitation(counter)), stop_chars):
        try:
            element = int(new_element)
        except ValueError:
            print(f'Не удалось преобразовать строку "{new_element}" к числу. Повторите ввод {counter}-го элемента.')
            continue
        else:
            elements.append(element)
            counter += 1

    return tuple(elements)


def main() -> None:
    first_array, second_array = get_array(), get_array()
    difference = get_difference_of_arrays(decrement=first_array,
                                          subtraction=second_array)
    print(f'{first_array} - {second_array} = {difference}')


if __name__ == '__main__':
    main()

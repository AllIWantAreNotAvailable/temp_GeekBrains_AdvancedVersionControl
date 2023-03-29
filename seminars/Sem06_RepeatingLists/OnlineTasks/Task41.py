"""Задача №41:
Дан массив, состоящий из целых чисел. Сначала вводится число N — количество элементов в массиве
Далее записаны N чисел — элементы массива. Массив состоит из целых чисел. Напишите
программу, которая в данном массиве определит количество элементов, у которых два соседних и, при
этом, оба соседних элемента меньше данного.

Input:
-   5 -> [1, 2, 3, 4, 5]
Output:
-   0

Input:
-   5 -> [1, 5, 1, 5, 1]
Output:
-   2

(каждое число вводится с новой строки)
"""


def count_elements_with_smaller_neighbors(array: tuple) -> int:
    if 2 < len(array):
        return sum(1 for index in range(1, len(array) - 1) if array[index - 1] < array[index] > array[index + 1])
    return 0


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
    user_array = get_array()
    elements_with_smaller_neighbors = count_elements_with_smaller_neighbors(user_array)

    pretty_text = ', '.join(map(str, user_array))
    print(f'[{pretty_text}] -> {elements_with_smaller_neighbors}')


if __name__ == '__main__':
    main()

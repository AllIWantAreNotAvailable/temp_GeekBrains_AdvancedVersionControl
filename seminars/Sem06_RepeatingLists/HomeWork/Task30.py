"""Задача №30:
Заполните массив элементами арифметической прогрессии. Её первый элемент,
разность и количество элементов нужно ввести с клавиатуры. Формула для
получения n-го члена прогрессии: an = a1 + (n-1) * d.
Каждое число вводится с новой строки.

Input:
-   (first_element := 7, difference := 2, length := 5)
Out[ut:
- [7, 9, 11, 13, 15]
"""


def get_arithmetic_progression(start: int, step: int, length: int) -> tuple:
    stop = start + step * length
    return tuple(el for el in range(start, stop, step))


def main() -> None:
    pretty_text = 'арифметической прогрессии:\n>>> '
    first_element = int(input(f'Укажите первый элемент {pretty_text}'))
    difference = int(input(f'Введите шаг {pretty_text}'))
    length = int(input(f'Укажите длину {pretty_text}'))
    print(get_arithmetic_progression(first_element, difference, length))


if __name__ == '__main__':
    main()

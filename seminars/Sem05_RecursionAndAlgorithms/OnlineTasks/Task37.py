""" Задача №37:
Дано натуральное число N и последовательность из N элементов. Требуется вывести эту
последовательность в обратном порядке.
Input:
-   2 -> 3 4
Output:
-   4 3

Примечание. В программе запрещается объявлять массивы и использовать циклы (даже для ввода и вывода).
"""


def get_reversed_sequence(length: int) -> str:
    temp = input(f'Введите член последовательности №{length}:\n>>> ')
    if length - 1:
        return get_reversed_sequence(length - 1) + temp
    return temp


def main() -> None:
    sequence_length = int(input('Укажите длину последовательности:\n>>> '))
    sequence = get_reversed_sequence(sequence_length)
    print(sequence)


if __name__ == '__main__':
    main()

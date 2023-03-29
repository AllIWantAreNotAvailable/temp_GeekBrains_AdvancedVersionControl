"""Задача №32:
Определить индексы элементов массива (списка), значения которых принадлежат
заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)

Input:
-   [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7];
-   Диапазон от 6 до 12.
Output:
-   [1, 9, 13, 14, 19]
"""


def get_indices_of_elements_in_range(elements, lower_bound, upper_bound):
    return [i for i in range(len(elements)) if elements[i] in range(lower_bound, upper_bound + 1)]


def main():
    array = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
    l_bound = 6
    u_bound = 12
    result = get_indices_of_elements_in_range(array, l_bound, u_bound)
    print(result)


if __name__ == '__main__':
    main()

""" Задача №28:
Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

Input:
-   2 2
Output:
-   4
"""


def get_sum_recursion(first_summand: int, second_summand: int) -> int:
    """ Рекурсивная функция суммирования 2-х чисел.

    :param first_summand: Первое слагаемое, <class 'int'>.
    :param second_summand: Второе слагаемое, <class 'int'>.
    :return: Сумма чисел, <class 'int'>.
    """
    if first_summand:
        return 1 + get_sum_recursion(first_summand - 1, second_summand)
    elif second_summand:
        return 1 + get_sum_recursion(first_summand, second_summand - 1)
    else:
        return 0


def main() -> None:
    """ Главная функция.

    :return: None.
    """
    first_number = int(input('Введите первое слагаемое:\n>>> '))
    second_number = int(input('Введите второе слагаемое:\n>>> '))
    sum_of_numbers = get_sum_recursion(first_number, second_number)
    print(f'Сумма {first_number} и {second_number} -> {sum_of_numbers}')


if __name__ == '__main__':
    main()

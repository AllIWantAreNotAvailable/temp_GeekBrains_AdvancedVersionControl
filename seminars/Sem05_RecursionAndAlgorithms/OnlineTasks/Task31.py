""" Задача №31:
Последовательностью Фибоначчи называется последовательность чисел a0, a1, ..., an, ..., где
a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1). Требуется найти N-е число Фибоначчи

Input:
-   7
Output:
-   21

Задание необходимо решать через рекурсию
"""


def fibonacci_sequence(member: int) -> int:
    """ Возвращает значение N-ого по порядку члена последовательности Фибоначчи.
    Рекурсивная функция. Считаем, что 0 является 1-м по порядку элементом последовательности.

    :param member: Номер члена последовательности., <class 'int'>.
    :return: Значение N-ого по порядку члена последовательности Фибоначчи, <class 'int'>.
    """
    if member in (1, 2):
        return member - 1
    return fibonacci_sequence(member - 2) + fibonacci_sequence(member - 1)


def main() -> None:
    """ Главная функция.

    :return: None
    """
    order_number_of_member = int(input('Порядковый номер члена последовательности Фибоначчи:\n>>> '))
    value_of_member = fibonacci_sequence(order_number_of_member)
    print(f'Член последовательности Фибоначчи №{order_number_of_member} -> {value_of_member}')


if __name__ == '__main__':
    main()

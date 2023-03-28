""" Задача со звёздочкой №6:
Даны натуральные числа k и s. Определите, сколько существует k-значных натуральных чисел, сумма цифр
которых равна s. Запись натурального числа не может начинаться с цифры 0.
В этой задаче можно использовать цикл для перебора всех цифр, стоящих на какой-либо позиции.
3 15 -> 69
4 16 -> 564
2 3 -> 3
6, 40 -> 10746
"""


def get_numbers_sum_of_digits_equals_value(digits: int, sum_of_digits: int) -> tuple:
    """ Функция находит числа с указанной разрядностью, сумма цифр которого равна заданному значению.

    :param digits: Разрядность чисел, <class 'int'>.
    :param sum_of_digits: Сумма цифр числа, <class 'int'>.
    :return: Кортеж из валидных чисел и количество валидных чисел, <class 'tuple'>.
    """
    start = digits - 1
    results = list()
    for value in range(10 ** start, 10 ** digits):
        if sum(value // 10 ** exponent % 10 for exponent in range(start, -1, -1)) == sum_of_digits:
            results.append(value)
    return results, len(results)


def main() -> None:
    """ Главная функция.

    :return: None.
    """
    digits_of_number = int(input('Введите разрядность числа:\n>>> '))
    desired_sum_of_digits = int(input('Желаемая сумма цифр числа:\n>>> '))
    numbers_tuple, numbers_count = get_numbers_sum_of_digits_equals_value(digits_of_number, desired_sum_of_digits)
    print(f'В диапазоне [{10 ** (digits_of_number - 1)}...{10 ** digits_of_number}) всего {numbers_count} чисел, '
          f'сумма цифр которых равна {desired_sum_of_digits}:\n{", ".join(map(str, numbers_tuple))}')


if __name__ == '__main__':
    main()

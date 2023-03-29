"""Задача №45:
Два различных натуральных числа n и m называются дружественными, если сумма делителей
числа n (включая 1, но исключая само n) равна числу m и наоборот.
Например, 220 и 284 – дружественные числа. По данному числу k выведите все пары
дружественных чисел, каждое из которых не превосходит k. Программа получает на вход
одно натуральное число k, не превосходящее 105. Программа должна вывести все пары
дружественных чисел, каждое из которых не превосходит k. Пары необходимо выводить по
одной в строке, разделяя пробелами. Каждая пара должна быть выведена только один раз
(перестановка чисел новую пару не дает).

Input:
-   300
Output:
-   [220, 284]
"""


def is_simple(number: int, cross_check: int, divisor: int = 2) -> bool:
    """ Функция проверяет, является ли переданное число простым, рекурсивно проверяет делители от 2 до number // 2 + 1.

    :param number: Число, которое проверяется, <class 'int'>.
    :param cross_check: Встречный делитель числа, <class 'int'>.
    :param divisor: Делитель числа, <class 'int'>.
    :return: True если число простое, False если не является простым, <class 'bool'>.
    """
    condition = number % cross_check != 0 and number % divisor != 0

    next_divisor = divisor + 1
    next_cross_check = cross_check - 1

    if next_divisor <= next_cross_check:
        return condition and is_simple(number, next_divisor, next_cross_check)
    return condition


def get_sum_of_divisors(number: int) -> int:
    return sum(divisor for divisor in range(number // 2 + 1, 0, -1) if not number % divisor)


def find_friendly(k: int):
    pairs = dict()
    for i in [x for x in range(1, k + 1) if not is_simple(x, x // 2 + 1)]:
        sum_of_divisors = get_sum_of_divisors(i)
        if i != sum_of_divisors and sum_of_divisors <= k:
            pairs[i] = sum_of_divisors

    temp = set()
    for key, value in pairs.items():
        if value in pairs and pairs[value] == key:
            temp.add(tuple(sorted([key, value])))

    return temp


def main() -> None:
    """ Главная функция.

    :return: None.
    """
    upper_bound = int(input('Введите верхнюю границу поиска пар дружественных числе:\n>>> '))
    pairs = find_friendly(upper_bound)
    print('\n'.join(f'{el}' for el in pairs))


if __name__ == '__main__':
    main()

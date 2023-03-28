""" Задача №35:
Напишите функцию, которая принимает одно число и проверяет, является ли оно простым.

Input:
-   5
Output:
-   yes

Напоминание: Простое число - это число, которое имеет 2 делителя: 1 и n(само число)
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


def recursion_wrapper(number: int):
    """ Функция обертка для рекурсивной функции is_simple(), призвана сократить кол-во операций в рекуррентных вызовах.

    :param number: Число, которое проверяется, <class 'int'>.
    :return: True если число простое, False если не является простым, <class 'bool'>.
    """
    if number == 1:  # не является простым числом
        return False
    elif number == 2:  # исключение из метода
        return True

    return is_simple(number, number // 2 + 1)


def main() -> None:
    user_number = int(input('Введите число:\n>>> '))
    print(f'Число {user_number} {"" if recursion_wrapper(user_number) else "не "}является простым числом!')


if __name__ == '__main__':
    main()

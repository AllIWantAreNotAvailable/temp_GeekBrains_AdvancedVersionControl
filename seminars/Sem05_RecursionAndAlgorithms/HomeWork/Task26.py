""" Задача №26:
Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

Input:

-   A = 3; B = 5
-   A = 2; B = 3
Output:
-   243
-   8
"""


def get_number_to_power(base: int, exponent: int) -> int:
    """ Возвращает значение числа возведенного в степень.

    :param base: Основание степени, <class 'int'>.
    :param exponent: Показатель степени, <class 'int'>.
    :return: Значение числа возведенного в степень, <class 'int'>.
    """
    if exponent == 0:
        return 1
    elif exponent == 1:
        return base
    else:
        return base * get_number_to_power(base, exponent - 1)


def main() -> None:
    """ Главная функция.

    :return: None.
    """
    number = int(input('Введите основание степени:\n>>> '))
    exponent = int(input('Введите показатель степени:\n>>> '))
    power_of_number = get_number_to_power(number, exponent)
    print(f'{number} в степени {exponent} -> {power_of_number}')


if __name__ == '__main__':
    main()

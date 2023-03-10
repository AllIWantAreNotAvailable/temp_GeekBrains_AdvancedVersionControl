"""Задача 2:
Найдите сумму цифр трехзначного числа.

Примеры:
-   123 -> 6 (1 + 2 + 3)
-   100 -> 1 (1 + 0 + 0)
"""


def get_sum_of_digits_in_string(number: str) -> int:
    """ Принимает строку и возвращает сумму цифр в строке.

    :param number: Строка, цифры в которой суммируются, <class 'str'>.
    :return: Сумма цифр в строке, <class 'int'>.
    """
    result = 0
    for char in number:
        result += int(char) if char.isdigit() else 0
    return result


def main() -> None:
    """ Главная функция.

    :return: None
    """
    number = input('Введите число, цифры которого будут просуммированы:\n>>> ')
    sum_of_digits = get_sum_of_digits_in_string(number)
    print('Сумма цифр в строке:', number, '->', sum_of_digits)


if __name__ == '__main__':
    main()

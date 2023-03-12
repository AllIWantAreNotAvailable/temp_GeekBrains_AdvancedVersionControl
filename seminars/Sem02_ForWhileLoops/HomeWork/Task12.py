"""Задача 12:
Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. Он
задумывает два натуральных числа X и Y (X, Y ≤ 1000), а Катя должна их отгадать. Для этого Петя делает две
подсказки. Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.

Например:
Input:
1. 4 4 ->
2. 5 6 ->
Output:
1. -> 2 2
2. -> 2 3
"""


def get_numbers(sum_of_numbers: int, product_of_numbers: int) -> tuple:
    first_temp, second_temp = 0, sum_of_numbers

    while first_temp + second_temp == sum_of_numbers and first_temp * second_temp != product_of_numbers:
        first_temp += 1
        second_temp -= 1

    return first_temp, second_temp


def is_input_valid(product_of_numbers, sum_of_numbers):
    is_sum_valid = sum_of_numbers is None or isinstance(sum_of_numbers, int) or sum_of_numbers.isdigit()
    is_product_valid = product_of_numbers is None or isinstance(product_of_numbers, int) or product_of_numbers.isdigit()
    return is_product_valid, is_sum_valid


def user_input(sum_of_numbers=None, product_of_numbers=None) -> tuple:
    """ Функция обрабатывает ввод пользователя, если введенные данные не удалось преобразовать к числу, либо
    преобразованное число меньше 1, будет вызван рекуррентный случай.

    :return: Возвращает только натуральные числа, <class 'tuple'>
    """
    is_product_valid, is_sum_valid = is_input_valid(product_of_numbers, sum_of_numbers)

    sum_of_numbers = input(f'Введите сумму чисел:\n>>> ') if is_sum_valid else sum_of_numbers
    product_of_numbers = input(f'Введите произведение чисел:\n>>> ') if is_product_valid else product_of_numbers

    is_product_valid, is_sum_valid = is_input_valid(product_of_numbers, sum_of_numbers)
    sum_of_numbers = int(sum_of_numbers) if is_sum_valid else sum_of_numbers
    product_of_numbers = int(product_of_numbers) if is_product_valid else product_of_numbers

    if (is_sum_valid and 1 < sum_of_numbers) and (is_product_valid and 0 < product_of_numbers):
        return sum_of_numbers, product_of_numbers
    else:
        print('Непредвиденная ошибка. Проверьте введенные данные и повторите ввод:\n'
              '* Допускается ввод только натуральных чисел.\n'
              '** Минимальная сумма 2-х натуральных чисел - это 2')
        return user_input(sum_of_numbers, product_of_numbers)


def main() -> None:
    """  Главная функция.

    Ввод пользователя и вычисления вынесены в отдельные методы.

    :return: None
    """
    sum_of_numbers, product_of_numbers = user_input()
    print(get_numbers(sum_of_numbers, product_of_numbers))


if __name__ == '__main__':
    main()

""" Задача со звёздочкой №4:
Напишите функцию, которая будет возвращать переданное в качестве параметра n число словами
Input -> 435467
Output -> четыреста тридцать пять тысяч четыреста шестьдесят семь
"""
import random


def get_sorted_keys_list(structure: dict) -> list:
    """ Преобразует генератор ключей в список и возвращает отсортированный список ключей.

    :param structure: Структура числа, <class 'dict'>.
    :return: Отсортированный список ключей, <class 'list'>.
    """
    return sorted(structure, key=lambda el: structure[el][1], reverse=True)


def get_string_number_representation(**kwargs) -> str:
    """ Формирует из структуры разрядов числа прописное представление числа.

    :param kwargs: Структура разрядов числа.
    :return: Число прописью, <class 'str'>
    """
    output = ' '.join(get_number_in_words(key, kwargs[key][0]) for key in get_sorted_keys_list(kwargs))
    return output


def get_number_in_words(key: str, value: int) -> str:
    """ Функция возвращает число прописью. Правила склонения слов игнорируются.

    Если передан ключ структуры состоящей из 3-х числовых разрядов, то:

    - сначала, кол-во разрядов будет разложено на структуру числа;
    - после, на основании новой структуры будет вызвано 3 рекуррентных случая.

    :param key: Разряд числа, <class 'str'>.
    :param value: Кол-во разрядов, <class 'int'>.
    :return: Число прописью, <class 'str'>.
    """
    exceptions_from_main_logic = dict(
        billion='миллиардов',
        millions='миллионов',
        thousands='тысяч'
    )

    if key in exceptions_from_main_logic:
        new_struct = get_number_structure(value)
        output = ' '.join(get_number_in_words(key, new_struct[key][0]) for key in get_sorted_keys_list(new_struct))
        return f'{output} {exceptions_from_main_logic[key]}'

    number_in_words = dict(
        hundreds=[
            '',
            'сто',
            'двести',
            'триста',
            'четыреста',
            'пятьсот',
            'шестьсот',
            'семьсот',
            'восемьсот',
            'девятьсот'
        ],
        tens=[
            '',
            'десять',
            'двадцать',
            'тридцать',
            'сорок',
            'пятьдесят',
            'шестьдесят',
            'семьдесят',
            'восемьдесят',
            'девяносто'
        ],
        ones=[
            '',
            'один',
            'два',
            'три',
            'четыре',
            'пять',
            'шесть',
            'семь',
            'восемь',
            'девять'
        ],
        tens_ex=[
            '',
            'одиннадцать',
            'двенадцать',
            'тринадцать',
            'четырнадцать',
            'пятнадцать',
            'шестнадцать',
            'семнадцать',
            'восемнадцать',
            'девятнадцать'
        ]
    )
    return number_in_words[key][value]


def is_zero_value(value: int) -> bool:
    """ Данная функция используется для формирования словаря функцией get_number_structure().

    :param value: Кол-во разрядов числа, <class 'int'>.
    :return: Если кол-во разрядов ('value') больше 0 – True, иначе False, <class 'bool'>.
    """
    return bool(value)


def get_ones(number: int) -> tuple:
    """ Данная функция используется для формирования словаря функцией get_number_structure().

    :param number:  Число от 1 до 999 999 999 999, <class 'int'>.
    :return: Кортеж состоящий из ('ключ словаря' 'кол-во единиц' 'число единиц'), <class 'tuple'>.
    """
    temp = number % 10
    return 'ones', temp, temp


def get_tens(number: int) -> tuple:
    """ Данная функция используется для формирования словаря функцией get_number_structure().
    Может вернуть 2 варианта кортежа, в зависимости от того, заканчивается ли число ('number') на значения от 11 до 20.

    Если число ('number') заканчивается на значения от 11 до 20, то:

    - кортеж состоящий из ('ключ словаря' 'кол-во единиц' 'число десятков');

    иначе:

    - кортеж состоящий из ('ключ словаря' 'кол-во десятков' 'число десятков').

    :param number:  Число от 1 до 999 999 999 999, <class 'int'>.
    :return: Кортеж для формирования элемента словаря, <class 'tuple'>.
    """
    ten = 10
    temp = number // ten % 10
    if 10 < number % 100 < 20:
        return 'tens_ex', number % 10, temp * ten
    else:
        return 'tens', temp, temp * ten


def get_hundreds(number: int) -> tuple:
    """ Данная функция используется для формирования словаря функцией get_number_structure().

    :param number:  Число от 1 до 999 999 999 999, <class 'int'>.
    :return: Кортеж состоящий из ('ключ словаря' 'кол-во сотен' 'число сотен'), <class 'tuple'>.
    """
    hundred = 100
    temp = number // hundred % 10
    return 'hundreds', temp, temp * hundred


def get_number_structure(number: int) -> dict:

    functions = [
        get_ones,
        get_tens,
        get_hundreds
    ]
    structure = dict()

    for f in functions:
        key, count, value = f(number)

        if key == 'ones' and 'tens_ex' in structure:
            continue

        if is_zero_value(value):  # Возможно это рудимент...
            structure[key] = (count, value)

    return structure


def get_number_from_user() -> int:
    """ Функция считывает ввод пользователя и преобразует его в целое число.

    Правила:

    - допускается ввод только положительных чисел;
    - допускается использовать единичный пробел или символ '_' в качестве разделителя разрядов.

    :return: Положительное целое число, которое ввел пользователь, <class 'int'>.
    """
    user_input = input('Введите число:\n')
    try:
        input_without_spaces = user_input.replace(' ', '_')
        user_number = int(input_without_spaces)
        if user_number < 0:
            raise ValueError(f'Программа преобразует только положительное числа и 0. '
                             f'Вы ввели: {user_number} -> {user_number} < 0.')
    except ValueError as ex:
        print(ex, 'Повторите ввод.')
        return get_number_from_user()
    return user_number


def divide_number_into_groups_of_digits(number: int) -> tuple:
    groups = ('hundreds', 'thousands', 'millions', 'billions')


def main() -> None:
    """ Главная функция.

    :return: None
    """
    source = get_number_from_user()

    if source:
        number_structure = get_number_structure(source)
        print(source, '->', get_string_number_representation(**number_structure))
    else:
        print(source, '->', 0)


if __name__ == '__main__':
    main()

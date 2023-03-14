""" Дополнительное задание №3:
Валентина прогуляла лекцию по математике.
Преподаватель решил подшутить над нерадивой студенткой и
попросил ее на практическом занятии перечислить все положительные делители некоторых целых чисел.
Для несложных примеров студентка быстро нашла решения (для числа 6 это: 1, 2, 3, 6; а для числа 16 это: 1, 2, 4, 8, 16),
но этим все не закончилось.
На домашнее задание ей дали варианты посложнее: 23436, 190187200, 380457890232.

Решить такое вручную, как вы понимаете, практически нереально.
Вот Валентина и обратилась к вам за помощью.
Помогите ей (при помощи функции all_divisors(number)).

* Вывести только делители, которые являются простыми числами (делится на себя и на 1)
"""


def divider(number: int) -> list:
    """ Возвращает положительные целые делители переданного числа.

    :param number: Число, делители которого ищем, <class 'int'>.
    :return: Список положительных целых делителей, <class 'list'>.
    """
    return [x for x in range(1, number + 1) if number % x == 0]


def simple_divisor(number_dividers: list) -> list:
    """ Возвращает только простые числа из переданного списка.

    :param number_dividers: Список положительных целых чисел, <class 'list'>
    :return: Список простых чисел, <class 'list'>
    """
    return [x for x in number_dividers if len([y for y in range(2, x) if x % y == 0]) == 0 and x != 1]


def show_result(number: int, dividers_list: list, only_simple: bool = False) -> None:
    """ Выводит результат в консоль.

    :param number: Число делители которого искали, <class 'int'>.
    :param dividers_list: Список делителей числа, <class 'list'>.
    :param only_simple: Добавить в вывод уточнение "простые делители", <class 'bool'>.
    :return: None
    """
    pretty_text = ';\n'.join([f'{x[0]}) {x[1]}' for x in enumerate(dividers_list, 1)])
    print(f'Положительные {"простые " if only_simple else ""}делители числа {number}:\n{pretty_text}.\n')


def math() -> None:
    """ Главная функция.

    :return:
    """
    user_number = int(input('Введите целое число:\n>>> '))
    all_divisors = divider(user_number)
    show_result(number=user_number,
                dividers_list=all_divisors)
    show_result(number=user_number,
                dividers_list=simple_divisor(all_divisors),
                only_simple=True)


if __name__ == '__main__':
    math()


"""Задача 6:
Вы пользуетесь общественным транспортом? Вероятно, вы
расплачивались за проезд и получали билет с номером. Счастливым
билетом называют такой билет с шестизначным номером, где сумма
первых трех цифр равна сумме последних трех. Т.е. билет с номером
385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать
программу, которая проверяет, является ли билет счастливым.

Например:
-   385916 -> yes
-   123456 -> no
"""


def is_lucky_ticket(number: str) -> bool:
    """ Функция проверяет, является ли переданное число (последовательность цифр) счастливой по следующему принципу:

    - если суммы цифр левой и правой половины последовательности равны, то число считается счастливым.

    :param number: Число (последовательность цифр), <class 'str'>
    :return: True – если счастливое, False – не соответствует условию, <class 'bool'>.
    """
    if isinstance(number, type(str())):
        length = len(number)
        middle = length // 2
        if length % 2 == 0:
            left_side, right_side = number[:middle], number[middle:]
        else:
            left_side, right_side = number[:middle], number[middle + 1:]  # Середину не считаем, не влияет на результат
        return sum([int(x) for x in left_side]) == sum([int(x) for x in right_side])


def get_digits_from_user(message='') -> str:
    """ Вызывается для получения того, чтобы получить от пользователя число (последовательность цифр).
    Если введены не цифры, вызывается рекуррентный случай.

    :param message: По умолчанию 'Пустая строка', принимает значение в рекуррентном вызове.
    :return: Строка пользователя, которая состоит только из цифр, <class 'str'>.
    """
    user_strint = input(f'{message}Введите номер билета:\n>>> ')
    return user_strint if user_strint.isdigit() else get_digits_from_user('Ошибка ввода! ')


def main() -> None:
    """ Главная функция.

    :return: None.
    """
    ticket_number = get_digits_from_user()
    is_lucky = is_lucky_ticket(ticket_number)  # None -> неявно преобразуется внутри тернарного оператора
    print(f'Билет №{ticket_number} -> {"Счастливый билет ^_^" if is_lucky else "Не повезло..."}')


if __name__ == '__main__':
    main()

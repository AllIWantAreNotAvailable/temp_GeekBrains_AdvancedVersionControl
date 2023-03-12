"""Задача 14:
Требуется вывести все целые степени 2 (т.е. числа вида 2^k), не превосходящие числа N.

Например:
Input:
10
Output:
1 2 4 8
"""


def user_input() -> tuple:
    """ Обрабатывает ввод пользователя.

    При возникновении исключительной ситуации, будет вызван рекуррентный случай.

    Доступно 3 параметра, один из которых обязательный:

    - input: STOP – 'STOP' -> последняя степень 2, обязательный параметр.
    - input: START, STOP - 'START' -> начальная степень, а 'STOP' –> последняя степень 2.
    - input: START, STOP, STEP - 'START' -> начальная степень, 'STOP' –> последняя степень 2, 'STEP' -> шаг степени.

    :return: (START, STOP, STEP) - 'START' по умолчанию 0; 'STOP' не имеет значения по умолчанию; 'STEP' по умолчанию 1.
    """
    doc = user_input.__doc__[38:338]
    params = input(f'Программа выводит степени числа 2. {doc}\nПараметры вводятся через запятую "," или запятую +'
                   'пробел ", ".\nВведите показатель степени:\n>>> ')
    params_list = params.split(',')
    try:
        params_list = [int(x.strip()) for x in params_list]
    except Exception as ex:
        print(f'Произошла непредвиденная ошибка: "{ex}"')
        return user_input()
    else:
        if len(params_list) == 1:
            params_list.insert(0, 0)
            params_list.append(1)
            return tuple(params_list)
        elif len(params_list) == 2:
            params_list.append(1)
            return tuple(params_list)
        elif len(params_list) == 3:
            return tuple(params_list)
        else:
            print('Введено недопустимое количество параметров. Повторите ввод.')
            return user_input()


def main() -> None:
    """ Главная функция
    Программа выводит все степени двойки до N включительно.
    Ввод пользователя вынесен в отдельный метод для валидации введенных значений.
    :return: None
    """

    start_with, end_with, with_step = user_input()
    # Не удалось быстро найти способ вывода символа в верхнем индексе, для показателя степени, поэтому указываем
    # традиционным образом 'основание^показатель'
    print('\n'.join([f'2^{x} = {2 ** x}' for x in range(start_with, end_with + 1, with_step)]))


if __name__ == '__main__':
    main()

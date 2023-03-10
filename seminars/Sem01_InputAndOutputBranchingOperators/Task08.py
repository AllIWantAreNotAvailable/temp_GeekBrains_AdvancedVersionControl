"""Задача 8:
Требуется определить, можно ли от шоколадки размером n × m
долек отломить k долек, если разрешается сделать один разлом по
прямой между дольками (то есть разломить шоколадку на два
прямоугольника).

Например:
-   3 2 4 -> yes
-   3 2 1 -> no
"""


def user_input(width=None, length=None, pieces=None) -> tuple:
    """ Функция считывает ввод пользователя и получает следующие данные:

    - ширина шоколадки;
    - длина шоколадки;
    - количество долек.

    После чего, осуществляется попытка перевода строковых данных к типу int. В случае возникновения исключения,
    производится рекуррентный вызов функции с передачей аргументов: width, length, pieces; для повторной инициализации
    переменных с сохранением предыдущих значений не вызвавших исключение.

    :param width: По умолчанию - None. Получает входящее значение при рекуррентном вызове в исключительной ситуации.
    :param length: По умолчанию - None. Получает входящее значение при рекуррентном вызове в исключительной ситуации.
    :param pieces: По умолчанию - None. Получает входящее значение при рекуррентном вызове в исключительной ситуации.
    :return: Кортеж содержащий значения типа int (ширина_шоколадки, длина_шоколадки, количество_долек), <class 'tuple'>
    """
    width = input('Какой ширины у шоколадки?\n>>> ') if width is None or not width.isdigit() else width
    length = input('Какой длины шоколадка?\n>>> ') if length is None or not length.isdigit() else length
    pieces = input('Сколько долек отломить?\n>>> ') if pieces is None or not pieces.isdigit() else pieces

    try:
        width, length, pieces = int(width), int(length), int(pieces)
    except ValueError:
        print('Ошибка обработки данных!',
              'Повторите ввод:')
        width, length, pieces = user_input(width, length, pieces)
    except Exception as ex:
        print('Непредвиденная ошибка ->\n', ex)
        print('Повторите ввод:')
        width, length, pieces = user_input(width, length, pieces)
    finally:
        return width, length, pieces


def main() -> None:
    """ Главная функция.

    :return: None.
    """
    chocolate_width, chocolate_length, pieces = user_input()
    condition = pieces % chocolate_width == 0 or pieces % chocolate_length == 0
    print(f'От шоколадки шириной {chocolate_width} кусочков и длиной {chocolate_length} кусочков',
          f'{"можно".upper() if condition else "нельзя".upper()} отломить {pieces} кусочков за один разлом')


if __name__ == '__main__':
    main()

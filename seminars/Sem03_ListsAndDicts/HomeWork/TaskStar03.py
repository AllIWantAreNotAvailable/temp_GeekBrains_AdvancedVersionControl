""" Задача со звёздочкой №3:
Напишите функцию, которая принимает словарь с параметрами и возвращает строку запроса,
сформированную из отсортированных в лексикографическом порядке параметров.

Пример:
Код print(query({'course': 'python', 'lesson': 2, 'challenge': 17})) должен возвращать строку:

challenge=17&course=python&lesson=2
"""


def query(**kwargs) -> str:
    """ Преобразуем переданный словарь в строку запроса, сформированную из отсортированных
     в лексикографическом порядке параметров.

     Подход к решению:
     - генерируем список кортежей из ключей и значений;
     - сортируем список по первому элементу кортежа ("ключу словаря");
     - генерируем список и из отсортированного с форматированием элементов по ф-строке и
     сливаем все в строку с разделителем.

    :param kwargs: Словарь с параметрами, <class 'dict'>
    :return: Строка запроса, <class 'str'>
    """
    key_value_list = [(key, value) for key, value in kwargs.items()]
    key_value_list.sort(key=lambda el: el[0])
    return '&'.join(f'{k}={v}' for k, v in key_value_list)


def main() -> None:
    """ Гласная функция

    :return: None
    """
    output = query(course='python', lesson=2, challenge=17)
    print({'course': 'python', 'lesson': 2, 'challenge': 17}, output, sep='\n')


if __name__ == '__main__':
    main()

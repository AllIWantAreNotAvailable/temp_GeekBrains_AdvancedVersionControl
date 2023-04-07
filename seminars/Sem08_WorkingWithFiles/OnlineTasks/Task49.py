""" Задача №49:
Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. Фамилия, имя, отчество, номер
телефона - данные, которые должны находиться в файле.
1. Программа должна выводить данные
2. Программа должна сохранять данные в текстовом файле
3. Пользователь может ввести одну из характеристик для поиска определенной записи (Например имя или фамилию человека)
4. Использование функций. Ваша программа не должна быть линейной
"""

import os
import json


def find_contact(contacts: list) -> None:
    """ Функция осуществляет поиск по справочнику и выводит найденные записи на экран.

    :param contacts: Справочник, <class 'list'>.
    :return: None
    """
    what = input('Кого ищем?\n>>> ')
    found = list(filter(lambda el: what in el['first_name'] or what in el['second_name'], contacts))
    if found:
        show_on_screen(found)
    else:
        print('Никого не нашли ;(')


def file_path(file_name='contact_list') -> str:
    """ Функция возвращает путь к файлу справочника.

    :param file_name: Имя файла справочника, <class 'str'>.
    :return: Путь к файлу справочника, <class 'str'>.
    """
    return os.path.join(os.path.dirname(__file__), f'{file_name}.txt')


def load_from_file() -> list:
    """ Функция загружает справочник из файла.

    :return: Справочник контактов, <class 'list'>.
    """
    path = file_path()

    with open(path, 'r', encoding='UTF-8') as file:
        data = json.load(file)

    return data


def save_to_file(contacts: list) -> None:
    """ Функция сохраняет справочник в файл.

    :param contacts: Справочник, <class 'list'>.
    :return: None
    """
    path = file_path()

    with open(path, 'w', encoding='UTF-8') as file:
        json.dump(contacts, file, ensure_ascii=False)


def show_on_screen(contacts: list) -> None:
    """ Функция выводит переданные записи справочника на экран.

    :param contacts: Записи справочника, <class 'list'>.
    :return: None
    """
    decode_keys = dict(
        first_name='Имя:',
        second_name='Фамилия:',
        contacts='Телефон:'
    )
    pretty_text = str()
    for num, elem in enumerate(contacts, 1):
        pretty_text += f'Контакт №{num}:\n'
        pretty_text += '\n'.join(f'{decode_keys[k]} {v}' for k, v in elem.items())
        pretty_text += '\n________\n'
    print(pretty_text)


def new_contact(contacts: list) -> None:
    """ Функция создает новую запись справочника.

    :param contacts: Список записей справочника, <class 'list'>.
    :return: None
    """
    contacts.append(
        dict(
            first_name=input('Введите имя контакта:\n>>> '),
            second_name=input('Введите фамилию контакта:\n>>> '),
            contacts=input('Введите номер телефона:\n>>> ')
        )
    )


def menu() -> int:
    """ Функция реализует функционал "меню" программы.

    :return: Индекс команды программы, <class 'int'>.
    """
    commands = [
        'Показать все контакты',
        'Найти контакт',
        'Создать контакт'
    ]
    print('Укажите номер команды:')
    print('\n'.join(f'{n}. {v}' for n, v in enumerate(commands, 1)))
    choice = input('>>> ')

    try:
        choice = int(choice)
        if choice < 0 or len(commands) < choice:
            raise Exception('Такой команды пока нет ;(')
        choice -= 1
    except ValueError as ex:
        print('Я вас не понял, повторите...')
        menu()
    except Exception as ex:
        print(ex)
        menu()
    else:
        return choice


def main() -> None:
    """ Главная функция.

    :return: None
    """
    print('Программа запущена...')
    data = load_from_file()

    command = menu()
    if command == 0:
        show_on_screen(data)
    elif command == 1:
        find_contact(data)
    elif command == 2:
        new_contact(data)

    save_to_file(data)
    print('Конец программы!')


if __name__ == '__main__':
    main()

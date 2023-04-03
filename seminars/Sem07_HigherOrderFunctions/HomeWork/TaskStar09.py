""" Задача со звёздочкой №9:
Чтобы лучше разобраться в типах параметров функций Инна создала inspect_function(), которая
в качестве аргумента принимает другую функцию (главное, не встроенную, built-in).
В результате работы она выводит следующие данные: название анализируемой функции,
наименование всех принимаемых ею параметров и их типы (позиционные, ключевые и т.п.).
Попробуйте повторить результат девушки.

def my_func(a, b, /, c, d, *args, e, f, **kwargs):
    pass

def my_func(a, b, c, d, *args):
    pass

"""


import inspect


def my_func_demo(a, b, c, d, *args):
    pass


def my_func_full(a, b, /, c, d, *args, e, f, **kwargs):
    pass


def get_parameter_type(param):
    description = dict(
        POSITIONAL_ONLY="Значение должно быть указано как позиционный аргумент. Позиционными являются только те "
                        "параметры, которые появляются перед записью / (если она присутствует) в определении "
                        "функции Python.",
        POSITIONAL_OR_KEYWORD="Значение может быть представлено в виде ключевого или позиционного аргумента (это "
                              "стандартное поведение биндинга для функций, реализованных в Python.)",
        VAR_POSITIONAL="Кортеж позиционных аргументов, не связанных ни с одним другим параметром. Это соответствует "
                       "параметру *args в определении функции Python.",
        KEYWORD_ONLY="Значение должно быть указано в качестве ключевого аргумента. Только ключевых параметры - это "
                     "параметры, которые появляются после записи * или *args в определении функции Python.",
        VAR_KEYWORD="Словарь ключевых аргументов, которые не привязаны к какому-либо другому параметру. Это "
                    "соответствует параметру **kwargs в определении функции Python."
    )
    return f'{param.kind.description} - {description[str(param.kind)]}'


def inspect_function(function_object):
    function_signature = inspect.signature(function_object)
    function_parameters = function_signature.parameters.values()
    declaration = dict(
        name_and_signature=f'Имя функции: "{function_object.__name__}", сигнатура: {function_signature}',
        parameters=[f'Параметр "{v.name}", тип параметра: {get_parameter_type(v)}.' for v in function_parameters]
    )
    print(declaration['name_and_signature'],
          '\n'.join(f'\t{num}. {val}' for num, val in enumerate(declaration['parameters'], 1)), sep='\n', end='\n\n')


def main() -> None:
    inspect_function(my_func_demo)
    inspect_function(my_func_full)


if __name__ == '__main__':
    main()

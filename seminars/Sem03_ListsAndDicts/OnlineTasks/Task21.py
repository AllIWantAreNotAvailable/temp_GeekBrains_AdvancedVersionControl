""" Задача №21:
Напишите программу для печати всех уникальных значений в словаре.

Input:
-   [
        {"V": "S001"},
        {"V": "S002"},
        {"VI": "S001"},
        {"VI": "S005"},
        {"VII": "S005"},
        {"V": "S009"},
        {"VIII": "S007"}
    ]
Output:
-   {'S005', 'S002', 'S007', 'S001', 'S009'}

Примечание: Список словарей задан изначально. Пользователь его не вводит
"""

list_of_dicts = [
                 {"V": "S001"},
                 {"V": "S002"},
                 {"VI": "S001"},
                 {"VI": "S005"},
                 {"VII": "S005"},
                 {"V": "S009"},
                 {"VIII": "S007"}
                ]

values = list(map(lambda el: tuple(el.values())[0], list_of_dicts))
unique_values = [x for x in values if values.count(x) == 1]

print('Значения без повторений ->', set(values))
print('Уникальные значения ->', unique_values)

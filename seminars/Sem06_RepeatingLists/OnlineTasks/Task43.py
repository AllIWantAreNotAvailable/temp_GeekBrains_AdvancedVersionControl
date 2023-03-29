"""Задача №43:
Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу. Считается,
что любые два элемента, равные друг другу образуют одну пару, которую необходимо посчитать.
Вводится список чисел. Все числа списка находятся на разных строках.

Input:
-   [1, 2, 3, 2, 3]
Output:
-   2
"""


from math import factorial

numbers_list = [1, 2, 3, 2, 3]
group = 2
pairs = dict()
for el in numbers_list:
    if (el_count := numbers_list.count(el)) - 1:
        pairs[el] = factorial(el_count) / (factorial(group) * factorial(el_count - group))

print(sum(pairs.values()))


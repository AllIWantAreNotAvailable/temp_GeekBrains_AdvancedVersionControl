"""Задача №9:
По данному целому неотрицательному n вычислите значение n!.
N! = 1 * 2 * 3 * ... * N (произведение всех чисел от 1 до N) 0! = 1
Решить задачу используя цикл while

Input:
-   5
Output:
-   120
"""


factorial = int(input('Введите число для вычисления факториала:\n>>> '))
if factorial == 0 or factorial == 1:
    print(f'{factorial}! = 1')
else:
    result = 1
    for number in range(2, factorial + 1):
        result *= number
    print(f'{factorial}! = {result}')

"""Задача №11:
Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи оно является,
то есть выведите такое число n, что φ(n)=A.
Если А не является числом Фибоначчи, выведите число -1.

Input:
-   5
Output:
-   6
"""


fibonacci_number = int(input('Введите число из последовательности Фибоначчи:\n>>> '))
fibonacci_numbers = [0, 1]
if fibonacci_number == 0:
    print(f'φ(1) = {" + ".join([str(x) for x in fibonacci_numbers[:1]])}')
elif fibonacci_number == 1:
    print(f'φ(2) = {" + ".join([str(x) for x in fibonacci_numbers])}')
else:
    while fibonacci_numbers[-1] < fibonacci_number:
        fibonacci_numbers.append(fibonacci_numbers[-1] + fibonacci_numbers[-2])
    if fibonacci_numbers[-1] == fibonacci_number:
        print(f'φ({len(fibonacci_numbers)}) = {" + ".join([str(x) for x in fibonacci_numbers])}')
    else:
        print(f'φ(-1)')

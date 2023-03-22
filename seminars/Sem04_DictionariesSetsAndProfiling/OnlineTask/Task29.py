"""Задача №29:
Ваня и Петя поспорили, кто быстрее решит следующую задачу: “Задана последовательность неотрицательных
целых чисел. Требуется определить значение наибольшего элемента последовательности, которая завершается
первым встретившимся нулем (число 0 не входит в последовательность)”. Однако 2 друга оказались не такими
смышлеными. Никто из ребят не смог до конца сделать это задание. Они решили так: у кого будет меньше ошибок
в коде, тот и выиграл спор. За помощью товарищи обратились к Вам, студентам.

Ваня:
```
n = int(input())
max_number = 1000
while n != 0:
    n = int(input())
        if max_number > n:
            max_number = n
print(max_number)
```

Петя:
```
n = int(input())
max_number = -1
while n < 0:
    n = int(input())
        if max_number < n:
            n = max_number
print(n)
```
"""


from random import randint


def vanya_method(sequence: list) -> None:
    """ Заходит в цикл while, проходит по нему, пока number != 0, но возвращает 0.

    :return:
    """
    index = 0
    n = sequence[index]

    # n = int(input())
    max_number = 1000
    while n != 0:
        # n = int(input())
        index += 1
        n = sequence[index]

        if max_number > n:
            max_number = n
    print('Метод Ивана -> ', max_number)


def petya_method(sequence: list) -> None:
    """ Не входит в while при положительном number, возвращает введенное число.

    :return:
    """
    index = 0
    n = sequence[index]

    max_number = -1
    while n < 0:
        index += 1
        n = sequence[index]

        if max_number < n:
            n = max_number
    print('Метод Петра -> ', n)


def ours_method(sequence):
    index = 0
    max_el = sequence[index]
    while sequence[index] != 0:
        if max_el < sequence[index]:
            max_el = sequence[index]
        index += 1
    print(f'Наш метод -> {max_el if max_el else "Пустая последовательность..."}')


def main():
    sequence = list(randint(0, 20) for _ in range(20))
    sequence.append(0)
    print(sequence)

    vanya_method(sequence)
    petya_method(sequence)
    ours_method(sequence)


if __name__ == '__main__':
    main()

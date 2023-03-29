"""   Задача со звёздочкой №8:
Дано 20+ значное целое число, проверить его на делимость на 7.

Input:
-   234_523_642_345_789_812_354_678_654_323_454_919_865
Output:
-   Делится
"""


def is_divisible_by_seven(number: int) -> bool:
    groups = list()
    while number != 0:
        groups.append(number % 1_000)
        number //= 1_000

    # Так как мы идем от 0, то инвертируем условие сложения групп разрядов 2-го признака делимости на 7
    digits = [-groups[i] if i % 2 else groups[i] for i in range(len(groups))]
    sum_of_groups = abs(sum(digits))

    # Если сумма групп разрядов больше 99_999, то сократим число еще раз
    if 99 < sum_of_groups // 1_000:
        return is_divisible_by_seven(sum_of_groups)

    return (sum_of_groups // 10 * 3 + sum_of_groups % 10) % 7 == 0


def main():
    number = 234_523_642_345_789_812_354_678_654_323_454_919_865
    # ?! Условие в лоб
    #    ->          ->          ->          ->          ->          ->          ->   VVV
    print(f'Делится' if number % 7 == 0 else 'Не делится')
    # ?! Условие а-ля математик, типа что-то пытаюсь оптимизировать,
    # при этом не обращаю внимание на увеличение сложности алгоритма
    #                           VVV
    print(f'Делится' if is_divisible_by_seven(number) else 'Не делится')


if __name__ == '__main__':
    main()

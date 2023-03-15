"""
У вас есть девять цифр: 1, 2, …, 9. Именно в таком порядке.
Вы можете вставлять между ними знаки '+', '-' или ничего. У вас будут получаться выражения вида 123+45-6+7+89.
Найдите все из них, которые равны 100.

"""


def solve_expression(sequence: tuple, expression: str = '') -> None:
    if len(sequence) == 1:
        expression += f'{sequence[0]}'
        if eval(expression) == 100:
            print(f'{expression} == 100')
    else:
        solve_expression(sequence[1:], expression + f'{sequence[0]}')
        solve_expression(sequence[1:], expression + f'{sequence[0]} + ')
        solve_expression(sequence[1:], expression + f'{sequence[0]} - ')


def main():
    sequence_of_digits = (1, 2, 3, 4, 5, 6, 7, 8, 9)
    solve_expression(sequence_of_digits)


if __name__ == '__main__':
    main()

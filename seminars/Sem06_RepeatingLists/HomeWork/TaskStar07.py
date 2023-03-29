"""  Задача со звёздочкой №7:
Даны числа a и b. Определите, сколько существует последовательностей из a нулей и b единиц, в которых никакие
два нуля не стоят рядом.
Input:
-   5, 8
Output:
-   126
"""


def get_sequences(zeroes: int, ones: int, sequences: list, sequence: str = '') -> tuple:
    if ones == zeroes == 0:
        if sequence.find('00') == -1:
            sequences.append(sequence)
    if ones:
        get_sequences(zeroes, ones - 1, sequences, sequence + '1')
    if zeroes:
        get_sequences(zeroes - 1, ones, sequences, sequence + '0')
    return tuple(sequences)


def main() -> None:
    zeroes, ones = int(input('Введите кол-во нулей:\n>>> ')), int(input('Введите кол-во единиц:\n>>> '))
    sequences = get_sequences(zeroes, ones, list())
    pretty_text = ';\n'.join(f'{n}. {v}' for n, v in enumerate(sequences, 1)) + '.'
    print(pretty_text)


if __name__ == '__main__':
    main()

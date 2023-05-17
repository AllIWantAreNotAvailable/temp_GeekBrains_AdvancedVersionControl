def tests():
    romans = {'III': 3, 'LVIII': 58, 'MCMXCIV': 1994}
    print(list(romans.keys()))
    case = 1
    for roman in romans.keys():
        print(f'{case} {romans[roman] == roman_to_Int(roman)}')
        case += 1


def roman_to_Int(s: str) -> int:
    convert = dict(
        I=1,
        V=5,
        X=10,
        L=50,
        C=100,
        D=500,
        M=1000
    )
    integers = list()
    for i in range(len(s) - 1):
        integers.append(arabic if convert[s[i + 1]] <= (arabic := convert[s[i]]) else -arabic)
    integers.append(convert[s[-1]])
    return sum(integers)


def main():
    tests()


if __name__ == '__main__':
    main()

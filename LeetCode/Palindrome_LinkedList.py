def tests():
    cases = {(1, 2, 2, 1): True, (1, 2): False}
    case = 1
    for palindrome in cases:
        print(f"{case} => {cases[palindrome] == is_palindrome(list(palindrome))}")


def is_palindrome(source: list) -> bool:
    return source == source[::-1]


def main():
    tests()


if __name__ == '__main__':
    main()

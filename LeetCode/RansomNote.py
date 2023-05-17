def tests():
    cases = [
             dict(case={'ransomNote': 'a', 'magazine': 'b'}, output=False),
             dict(case={'ransomNote': 'aa', 'magazine': 'ab'}, output=False),
             dict(case={'ransomNote': 'aa', 'magazine': 'aab'}, output=True)
            ]
    for case in cases:
        print(case['output'] == can_construct(**case['case']))


def can_construct(ransomNote: str, magazine: str) -> bool:
    char_set = set(ransomNote)
    if not char_set.issubset(set(magazine)):
        return False

    flag = True
    for letter in list(char_set):
        flag = ransomNote.count(letter) <= magazine.count(letter)
        if not flag:
            break
    return flag


def main():
    tests()


if __name__ == '__main__':
    main()

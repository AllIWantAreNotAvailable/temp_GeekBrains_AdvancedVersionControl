def test():
    mat = [[1, 0, 0, 0],
           [1, 1, 1, 1],
           [1, 0, 0, 0],
           [1, 0, 0, 0]]
    print(kWeakestRows(mat, 3))


def kWeakestRows(mat: list, k: int):
    return sorted(range(len(mat)), key=lambda el: sum(mat[el]))[:k]


def main():
    test()


if __name__ == '__main__':
    main()

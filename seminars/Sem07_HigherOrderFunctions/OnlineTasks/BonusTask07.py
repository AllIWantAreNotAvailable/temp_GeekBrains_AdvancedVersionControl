import time


def main(func):

    def wrapper(*args):
        start = time.time()
        result = func(*args)
        print('Время работы:', time.time() - start)
        return result

    return wrapper


@main
def get_nod(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a


if __name__ == '__main__':
    print(get_nod(1000, 50))

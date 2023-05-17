def fizzBuzz(n: int):
    # answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
    # answer[i] == "Fizz" if i is divisible by 3.
    # answer[i] == "Buzz" if i is divisible by 5.
    # answer[i] == i (as a string) if none of the above conditions are true.
    return list(map(condition, range(1, n + 1)))


def condition(index: int) -> str:
    if not index % 15:
        return 'FizzBuzz'
    elif not index % 3:
        return 'Fizz'
    elif not index % 5:
        return 'Buzz'
    else:
        return str(index)


def main():
    print(fizzBuzz(15))


if __name__ == '__main__':
    main()

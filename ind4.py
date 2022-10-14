def obr():
    n = int(input(">>> "))
    if n != 0:
        obr()
        print(n)
    else:
        print(n)


def fib(x):
    if x in {0, 1}:
        return x
    else:
        return fib(x - 1) + fib(x - 2)


if __name__ == '__main__':
    obr()
    k = int(input("введите число до которого показать ряд фибоначчи "))
    print([fib(x) for x in range(k)])

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import timeit


code1 = '''
def factorial(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return n * factorial(n - 1)
'''


code2 = '''
def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n - 2) + fib(n - 1)
'''


code3 = '''
def factorial(n):
    product = 1
    while n > 1:
        product *= n
        n -= 1
    return product
'''


code4 = '''
def fib(n):
    a, b = 0, 1
    while n > 0:
        a, b = b, a + b
        n -= 1
    return a
'''


code5 = '''
from functools import lru_cache
@lru_cache
def factorial(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return n * factorial(n - 1)
'''


code6 = '''
from functools import lru_cache
@lru_cache
def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n - 2) + fib(n - 1)
'''


if __name__ == '__main__':
    print('Результат рекурсивного факториала:', timeit.timeit(setup=code1, number=1000))
    print('Результат рекурсивного числа Фибоначи:', timeit.timeit(setup=code2, number=1000))
    print('Результат итеративного факториала:', timeit.timeit(setup=code3, number=1000))
    print('Результат итеративного числа Фибоначи:', timeit.timeit(setup=code4, number=1000))
    print('Результат факториала с декоратором:', timeit.timeit(setup=code5, number=1000))
    print('Результат числа Фибоначи с декоратором:', timeit.timeit(setup=code6, number=1000))
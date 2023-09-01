"""
Требуется найти N-е число Фибоначчи
1, 1, 2, 3, 5, 8, 13, 21
Input: 7
Output: 13 / 21
"""


def fibon(n):
    if n < 2:
        return n
    return fibon(n - 2) + fibon(n - 1)
print(fibon(7))


def fib(n):
    if n in [0, 1]:
        return 1
    return fib(n - 2) + fib(n - 1)

print(fib(7))
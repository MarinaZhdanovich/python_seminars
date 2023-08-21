"""
Дано натуральное число A > 1. Определите, каким по
счету числом Фибоначчи оно является, то есть
выведите такое число n, что φ(n)=A. Если А не
является числом Фибоначчи, выведите число -1
"""
number = int(input("Введите число A: "))

fib_1 = 0
fib_2 = 1
index = 2  # два номера внесены

while fib_2 < number:
    # temp = fib_2
    # fib_2 = fib_1 + fib_2
    # fib_1 = temp
    fib_1, fib_2 = fib_2, fib_1 + fib_2
    index += 1

if fib_2 == number:
    print(f"{number} по счету {index}")
else:
    print(-1)



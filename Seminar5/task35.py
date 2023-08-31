"""Напишите функцию, которая принимает одно число и
проверяет, является ли оно простым
Напоминание: Простое число - это число, которое
имеет 2 делителя: 1 и n(само число)
Input: 5
Output: yes
"""

a = int(input("Введите число: "))
count = 0

for el in range(2, a):
    if a % el == 0:
        count += 1

if count == 0:
    print("Число простое")
else:
    print("Число составное")


def recur(a, count=0, el=2):
    if el == a:
        if count == 0:
            print("Число простое")
        else:
            print("Число составное")
        return
    if a % el == 0:
        count += 1
    return recur(a, count, el+1)
recur(a)

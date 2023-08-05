"""
Найдите сумму цифр трехзначного числа n.
"""

number = int(input("Введите трехзначное число: "))
sum_digit = 0
while number > 0:
    sum_digit += number % 10  # sum_digit = sum_digit + number % 10 сложение с присваиванием
    number //= 10   #number = number // 10 деление с присваиванием

print(sum_digit)

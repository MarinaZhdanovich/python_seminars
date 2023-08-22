"""По данному целому неотрицательному n вычислите
значение n!. N! = 1 * 2 * 3 * … * N (произведение всех
чисел от 1 до N) 0! = 1 Решить задачу используя цикл
while"""

n = int(input("Enter a number: "))
factorial = 1

while n > 1: # while n > 0, лишнее умножение на 1 в случае n = 0, поэтому 1
    factorial = factorial * n  # factorial *= n
    n -= 1
print(factorial)






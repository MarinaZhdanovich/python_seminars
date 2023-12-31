"""
Определите, можно ли от шоколадки размером a × b долек отломить c долек, если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).

Выведите yes или no соответственно.
a, b, c = 3, 2, 4 -> yes
a, b, c = 3, 2, 1 -> no
"""
a = 3
b = 2
c = 4

result = 'yes' if c < a * b and (c % a == 0 or c % b == 0) else 'no'
print(result)

# проверяем, что количество долек делится нацело на одну из сторон шоколадки a или b.
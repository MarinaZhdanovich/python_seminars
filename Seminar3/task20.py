"""Требуется найти в массиве list_1 самый близкий по величине элемент к заданному числу k и вывести его.
"""
list_1 = [1, 2, 3, 4, 5]
k = 6
c = []
for i in list_1:
    c.append(abs(k - i))
d = c.index(min(c))
print(list_1[d])
"""
Хакер Василий получил доступ к классному журналу и
хочет заменить все свои минимальные оценки на
максимальные. Напишите программу, которая
заменяет оценки Василия, но наоборот: все
максимальные – на минимальные.
Input: 5 -> 1 3 3 3 4
Output: 1 3 3 3 1
"""

lst = [1, 3, 3, 3, 4]
min_el = min(lst)
max_el = max(lst)
res = []
for el in lst:
    if el == max_el:
        res.append(min_el)
    else:
        res.append(el)

print(res)


def recur(lst, res=[], min_el=min(lst), max_el=max(lst)):
    if len(lst) == 0:
        return res
    if lst[0] == max_el:
        res.append(min_el)
    else:
        res.append(lst[0])

    return recur(lst[1:])

print(recur(lst))

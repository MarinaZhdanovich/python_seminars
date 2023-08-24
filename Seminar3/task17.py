"""Дан список чисел. Определите, сколько в нем
встречается различных чисел.
Input: [1, 1, 2, 0, -1, 3, 4, 4]
Output: 6
"""
# 1)
list_numbers = [1, 1, 2, 0, -1, 3, 4, 4]
result = set(list_numbers)
print(len(result))


# 2)
lst = [1, 1, 2, 0, -1, 3, 4, 4]

count_unic = []
for i in lst:
    if i not in count_unic:
        count_unic.append(i)

print(len(count_unic))
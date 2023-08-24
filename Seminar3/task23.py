"""
Дан массив, состоящий из целых чисел. Напишите
программу, которая подсчитает количество
элементов массива, больших предыдущего (элемента
с предыдущим номером)
Input: [0, -1, 5, 2, 3]
Output: 2 (-1 < 5, 2 < 3)
"""
lst_obj = [0, -1, 5, 2, 3]
counter = 0
prev_el = lst_obj[0]
for i in range(1, len(lst_obj)):
    if lst_obj[i] > prev_el:
        counter += 1
    prev_el = lst_obj[i]
print(counter)


lst_obj = [1, 1, 0, -1, 5, 2, 3, 2, 6]

counter = 0
for i in range(1, len(lst_obj)):
    if lst_obj[i] > lst_obj[i-1]:
        counter += 1
print(counter)

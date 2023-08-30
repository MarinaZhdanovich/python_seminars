"""
Быстрая сортировка
"""


def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)


print(quicksort([10, 5, 2, 3]))


# 1-е повторение рекурсии:
#  array = [10, 5, 2, 3]
#  pivot = 10
#  less = [5, 2, 3]
#  greater = []
#  return quicksort([5, 2, 3]) + [10] + quicksort([])
# 2-е повторение рекурсии:
#  array = [5, 2, 3]
#  pivot = 5
#  less = [2, 3]
#  greater = []
#  return quicksort([2, 3]) + [5] + quicksort([]) # Важно! Не забывайте, что
# здесь помимо вызова рекурсии добавляется список [10]
#  3-е повторение рекурсии:
#  array = [2, 3]
#  return [2, 3] # Сработал базовый случай рекурсии
#  На этом работа рекурсии завершилась и итоговый список будет выглядеть таким
#  образом: [2, 3] + [5] + [10] = [2, 3, 5, 10]

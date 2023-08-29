"""
Напишите программу, которая принимает на вход
строку, и отслеживает, сколько раз каждый символ
уже встречался. Количество повторов добавляется к
символам с помощью постфикса формата _n.
Input: a a a b c a a d c d d
Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
Для решения данной задачи используйте функцию
.split()
"""

lst = input("Введите символы через пробел: ").split()
res = {}   # СЛОВАРЬ, отслеживает количество повторений каждой буквы
for i in lst:
    if i in res:
        print(f"{i}_{res[i]}", end=' ')
    else:
        print(i, end=' ')
    res[i] = res.get(i, 0) + 1  #oбновляется ЗНАЧЕНИЕ словаря, ключ прежний


# dictionary.get(key, default_value)
# key: ключ, default_value: значение, которое будет возвращено, если ключ key не найден в словаре.
# по умолчанию, если этот аргумент не указан, метод вернет None, поэтому мы поставили 0

# метод get() словаря, получает значение по заданному ключу i.
# Если ключ i существует, то get вернет значение,если ключ i отсутствует в словаре, метод вернет значение по умолчанию,
# указанное вторым аргументом (в данном случае, это 0).

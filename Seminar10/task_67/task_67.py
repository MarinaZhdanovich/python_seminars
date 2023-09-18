"""
Создать новый столбец в таблице с
пингвинами, который будет отвечать за
показатель длины клюва пингвина.
high - длинный(от 42)
middle - средний(от 35 до 42)
low - маленький(до 35)
"""
import random
import seaborn as sns

penguins = sns.load_dataset("penguins")


def f(row):
    val = ''
    res = random.randint(1, 60)

    if res < 35:
        val = 'low'
    elif 35 < res < 42:
        val = 'middle'
    elif res > 42:
        val = 'high'

    return val


# 1 or ‘columns’: apply function to each row.
penguins['len'] = penguins.apply(f, axis=1)

# view DataFrame
print(penguins)

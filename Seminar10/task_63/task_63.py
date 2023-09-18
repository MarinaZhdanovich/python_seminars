"""
1. Изобразите отношение households к population с
помощью точечного графика
2. Визуализировать longitude по отношения к
median_house_value, используя линейный график
3. Представить гистограмму по housing_median_age
4. Изобразить гистограмму по median_house_value с
оттенком housing_median_age
"""

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data = pd.read_csv('california_housing_test.csv')


# 1
def first():
    households = list(data.households)
    population = list(data.population)

    plt.scatter(households, population)

    plt.xlabel("households")
    plt.ylabel("population")

    plt.title("Scatter plot for households and population")
    plt.show()


# first()

# 2
def second():
    longitude = list(data.longitude)
    median_house_value = list(data.median_house_value)

    plt.plot(longitude, median_house_value)

    plt.xlabel("longitude")
    plt.ylabel("median_house_value")

    plt.title("Line plot for longitude and median_house_value")

    plt.show()


# Гистограммы агрегируют числовые данные по группам с равными интервалами,
# которые называют бинами, и отображают частоту
# встречаемости значений в каждом из бинов
# second()
def third():
    housing_median_age = list(data.housing_median_age)

    plt.hist(housing_median_age, bins=7, edgecolor='black')

    plt.title("Hist plot for housing_median_age")

    plt.show()


# third()

# fourth
def fourth():
    median_house_value = list(data.median_house_value)
    housing_median_age = list(data.housing_median_age)

    plt.hist(housing_median_age, bins=7, edgecolor='black')

    plt.hist(median_house_value, bins=7)
    plt.hist(housing_median_age, bins=7)

    plt.show()

# fourth()

def fourth_():
    sns.histplot(data=data, x="median_house_value", hue="housing_median_age")
    plt.show()


fourth_()


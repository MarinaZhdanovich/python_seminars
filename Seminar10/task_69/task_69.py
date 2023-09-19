"""
Изобразить гистограмму по flipper_length_mm
с оттенком height_group - колонку создали в 67 задаче.
"""

import seaborn as sns
import matplotlib.pyplot as plt

penguins = sns.load_dataset("penguins")
def first():
    sns.histplot(data=penguins, x="flipper_length_mm", hue="sex")
    plt.show()

first()
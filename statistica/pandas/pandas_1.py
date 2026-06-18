import csv

import matplotlib.pyplot as plt
import pandas as pd

import numpy_es as np

plt.style.use("fivethirtyeight")
plt.rc("figure", figsize=(5.0, 2.0))

with open("heroes.csv", "r") as heroes_file:
    heroes_reader = csv.reader(heroes_file, delimiter=";", quotechar='"')
    heroes = list(heroes_reader)[1:]

years = [int(h[7]) if h[7] else None for h in heroes]
names = [h[0] for h in heroes]
first_appearance = pd.Series(years, index=names)

print(first_appearance)

print("\n")

print(int(first_appearance["A-Bomb"]))

first_app_freq = first_appearance[first_appearance < 2090].value_counts().sort_index()
first_app_freq.head(10)

years_labels = np.arange(1945, 2010, 10)
index_pos = []
valid_labels = []
for year in years_labels:
    try:
        index_pos.append(first_app_freq.index.get_loc(year))
        valid_labels.append(year)
    except KeyError:
        pass

first_app_freq.plot.bar()
plt.xticks(index_pos, valid_labels)
plt.ylim((0, 18.5))
plt.show()

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import csv

names = ['Aquaman', 'Ant-Man', 'Batman', 'Black Widow',
         'Captain America', 'Daredavil', 'Elektra', 'Flash',
         'Green Arrow', 'Human Torch', 'Hancock', 'Iron Man',
         'Mystique', 'Professor X', 'Rogue', 'Superman',
         'Spider-Man', 'Thor', 'Northstar']

years = [1941, 1962, None, None, 1941,
         1964, None, 1940, 1941, 1961,
         None, 1963, None, 1963, 1981,
         None, None, 1962, 1979]

def find_hero(name):
    if name in names:
        print('Found')
    else:
        print('Not Found')

def print_names():
    print(names)

def get_sorted_counts(sequence):
    counts = {}

    for x in sequence:
        if x in counts:
            counts[x] += 1
        else:
            counts[x] = 1

    pairs = counts.items()
    return sorted(pairs, key=lambda p:p[1], reverse=True)


find_hero('Aquaman')

del names[0]

find_hero('Aquaman')

print_names()

names.sort(key=len)

print_names()

# Filtra i valori None
# years_clean = [y for y in years if y is not None]
# x , y = np.array(get_sorted_counts(years_clean)).transpose()
# x = x.astype(int)
# plt.rc('figure', figsize=(5.0, 2.0))
# plt.bar(x, y)
# plt.show()

with open('heroes.csv', 'r') as heroes_file:
    heroes_reader = csv.reader(heroes_file, delimiter=';', quotechar='"')
    heroes = list(heroes_reader)[1:]

years = [int(h[7]) for h in heroes if h[7]]

print(years)

counts = get_sorted_counts(years)
x, y = np.array(counts).transpose()
plt.bar(x, y)
plt.xlim((1900, 2100))
plt.ylim((0, 18.5))
plt.show()
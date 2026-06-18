import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.stats as stats
from scipy.stats import binom, mode, norm

x = np.arange(-5, 5, 0.01)
y = 1 / (np.sqrt(1 * np.pi)) * np.exp(-(x**2) / 2)

plt.plot(x, y)
plt.show()

y = norm.pdf(x)

plt.plot(x, y)
plt.show()

y = 4 * np.exp(-4 * x)
plt.plot(x, y)
plt.show()

y = 1 - np.exp(-4 * x)
plt.plot(x, y)
plt.show()

print((163 - 167) / (27 / (np.sqrt(144))), (171 - 167) / (27 / (np.sqrt(144))))

print((2 * (0.9616)) - 1)

print(1 - stats.chi2.cdf(18.67, df=14))

array = np.array([284, 280, 277, 282, 279, 285, 281, 283, 278, 277])
print(np.mean(array))

print((15 * 2 + 16 * 5 + 7 * 11 + 18 * 9 + 19 * 14 + 20 * 13) / 54)

dati = np.array([15, 16, 17, 18, 19, 20])
freq = np.array([2, 5, 11, 9, 14, 13])

print(np.average(dati, weights=freq))
campione = np.repeat(dati, freq)
print(np.median(campione))
print(dati[np.argmax(freq)])
plt.bar(dati, freq)
plt.show()

dati = np.array([1, 2, 3, 4, 5, 6])
freq = np.array([9, 8, 5, 5, 6, 7])
print(np.average(dati, weights=freq))
campione = np.repeat(dati, freq)
print(np.median(campione))
print(dati[np.argmax(freq)])

dati = np.array([22, 22, 26, 28, 27, 25, 30, 29, 24])
anno = np.array([1985, 1986, 1987, 1988, 1989, 1990, 1991, 1992, 1993])

print(np.var(dati, ddof=1))

dati = np.array([12, 16, 13, 18, 19, 12, 18, 19, 12, 14])
fc = np.array([73, 67, 74, 63, 73, 84, 60, 62, 76, 71])

print(np.corrcoef(dati, fc)[0, 1])
plt.scatter(dati, fc)
plt.show()

dati_pd = pd.Series([137, 139, 141, 137, 144, 141, 139, 137, 144, 141, 143, 143, 141])
dati_np = np.array([137, 139, 141, 137, 144, 141, 139, 137, 144, 141, 143, 143, 141])
conta_valori = dati_pd.value_counts()

print(conta_valori)

plt.bar(conta_valori.index, conta_valori.values)
plt.show()

plt.pie(conta_valori.values, labels=conta_valori.index)
plt.show()

riserve_petrolio = np.array([38.7, 22.6, 8.8, 60.0])
stati = np.array(["Stati Uniti", "Sud America", "Canada", "Messico"])

plt.pie(riserve_petrolio, labels=stati)
plt.show()

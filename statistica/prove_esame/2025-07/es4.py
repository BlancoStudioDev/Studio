import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.stats as stats
from scipy.special import binom

dati = pd.read_csv("stelle_marine.csv")

print(dati.head())


braccia_freq_cum = (
    dati["num_braccia"].value_counts(normalize=True).sort_index().cumsum()
)
print(braccia_freq_cum)
n = braccia_freq_cum[braccia_freq_cum >= 0.95].index[0]

stelle_ridotto = dati[dati["num_braccia"] < n]

print(stelle_ridotto.head())

print("Stimatore per m: ", dati.profondita.mean() * 3)
m = dati.profondita.mean() * 3
plt.hist(stelle_ridotto.profondita, bins=30, density=True)
x = np.linspace(0, m, 200)
y = (2 / m) - (2 * x) / (m**2)
plt.plot(x, y)
plt.show()

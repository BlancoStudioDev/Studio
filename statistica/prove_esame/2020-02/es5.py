## ----------------------
#  Esercizio 5
## ----------------------
#
#
# 1. Calcolate la media del carattere cilindrata.
#

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.stats as stats

car = pd.read_csv("mtcars.csv")

print(car.cilindrata.mean())

# 2. Calcolate la deviazione standard del carattere cilindrata.
#

print(car.cilindrata.std())

# 3. Generate un campione casuale di 32 elementi estratto da una popolazione normale di
# valore atteso e deviazione standard uguali alla media e alla deviazione standard trovati
# nei due punti precedenti. Salvate tale campione nella variabile chiamata valoriSimulati
# (suggerimento: per generare un campione casuale di una popolazione normale si può usare
# il metodo rvs su un oggetto della classe norm in python e la funzione rnorm in R).

mu = car.cilindrata.mean()
sigma = car.cilindrata.std()

valoriSimulati = stats.norm.rvs(loc=mu, scale=sigma, size=32)
print(valoriSimulati)

car.cilindrata.value_counts().sort_index().plot(kind="bar")
plt.show()

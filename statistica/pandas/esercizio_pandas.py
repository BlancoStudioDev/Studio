import pandas as pd

dati = pd.read_csv("banking.csv")

print(dati.shape)  ## mostra le dimensioni del dataframe per riga e colonna
print(dati.head())  ## mostra le prime 5 righe
print(dati.dtypes)  ## mi fa vedere i tipi di dati divisi per colonna
print(dati.isnull().sum())  ## trova il numero di elementi che sono nulli
print(
    dati["utente"].nunique()
)  ## trova il numero di valori unici nella colonna "utente" 1752
print(
    (dati[dati["illecito"] == 1]), (dati[dati["illecito"] == 1]).shape
)  ## trova tutte quelle righe che hanno come valore, della colonna illecito, 1
print(
    (dati[dati["illecito"] == 0]), (dati[dati["illecito"] == 0]).shape
)  ## trova tutte quelle righe che hanno come valore, della colonna illecito, 0

print(
    "\n\n\nTENTATIVI:", dati["tentativi"].describe()
)  ## descrive le statistiche della colonna "tentativi", come media, deviazione standerd, minimo, massimo e 25%, 50% e 75% che sono i quartili

print(
    dati["tentativi"].value_counts()
)  ## numero di volte che si ripete un valore nella colonna "tentativi", per tutti i valori

print(
    dati["tentativi"].value_counts(normalize=True)
)  ## fa la stessa cosa solo che crea le frequenze relative

import matplotlib.pyplot as plt
from statsmodels.api import qqplot

qqplot(dati["minuti"])
plt.show()

dati.plot.scatter("minuti", "illecito")
plt.show()

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import statsmodels.api as sm


dati = pd.read_csv("punteggi.csv", sep=";")

print(dati.isnull().sum())

print("l'attributo dispositivo è un: ", dati["dispositivo"].dtypes)

print(dati.dispositivo.value_counts())

plt.hist(dati.dispositivo, bins = 30)
plt.show()

plt.pie(dati.dispositivo.value_counts(), labels=["mobile", "TV"])
plt.legend()
plt.show()

print(dati.minuto.head())
plt.hist(dati.minuto, bins=100)
plt.show()

plt.scatter(dati.minuto, dati.pubblicita)
plt.show()

print(dati.minuto.corr(dati.pubblicita))

dati_puliti = dati[dati.pubblicita/60 <= dati.minuto]
print(len(dati), len(dati_puliti))

plt.hist(dati_puliti.minuto, bins=286)
plt.show()

sm.qqplot(dati_puliti.minuto.dropna(), line="s")
plt.show()

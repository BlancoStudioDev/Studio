import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.stats as stats
from scipy.special import binom, factorial

dati = pd.read_csv("accessi.csv")

print(dati.head())
print(dati.iloc[1, :].isnull().sum())
richieste_mancanti = dati["richieste"].isnull().sum()
allarme_mancanti = dati["allarme"].isnull().sum()
carico_mancanti = dati["carico"].isnull().sum()
timestamp_mancanti = dati["timestamp"].isnull().sum()

print("Dati mancanti in timestamp:", timestamp_mancanti)
print("Dati mancanti in richieste:", richieste_mancanti)
print("Dati mancanti in allarme:", allarme_mancanti)
print("Dati mancanti in carico:", carico_mancanti)

mancanti = np.array(
    [timestamp_mancanti, richieste_mancanti, allarme_mancanti, carico_mancanti]
)
for i, valori in enumerate(mancanti):
    if valori != 0:
        print(f"Colonna {i} ha dati mancanti")

plt.pie(dati["allarme"].value_counts(), labels=[0, 1])
plt.legend([0, 1])
plt.show()

print("correlazione tra carico e allarme: ", dati["carico"].corr(dati["allarme"]))
x = dati["carico"]
y = dati["allarme"]
plt.scatter(x, y)
plt.show()

##non c'è correlazione tra le due cose

rich = dati["richieste"].dropna().sort_values()
cdf = np.arange(1, len(rich) + 1) / len(rich) * 100
plt.axhline(y=95, color="red")
plt.axvline(x=rich.quantile(0.95), color="red", linestyle="--")
plt.step(rich, cdf)
plt.show()

print("95esimo percentile: ", rich.quantile(0.95))

# modo 1: crostab
freqrel = pd.crosstab(dati.richieste, dati.allarme, normalize=True, margins=True)
print(freqrel)

# esercizio 9

stats.probplot(dati["richieste"], dist="norm", plot=plt)
plt.show()

plt.bar(dati["richieste"].value_counts().index, dati["richieste"].value_counts())
plt.show()

print("varianza: ", np.var(dati["richieste"], ddof=1))
print("media: ", np.mean(dati["richieste"]))

allarme_si = dati[dati["allarme"] == 1]["richieste"]
print("varianza allarme attivo: ", np.var(allarme_si, ddof=1))
print("media allarme attivo: ", np.mean(allarme_si))

print("lambda = ", np.mean(allarme_si))
print(allarme_si.mean(), allarme_si.var())
stats.probplot(
    allarme_si, dist=stats.poisson(np.mean(allarme_si)), sparams=(), plot=plt
)
plt.show()

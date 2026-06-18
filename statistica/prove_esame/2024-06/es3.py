## -----------------------
#  Esercizio 3
## -----------------------

# 1. Scrivete ed eseguite del codice che visualizzi su righe differenti il nome di ogni attributo unitamente al
# corrispondente numero di valori mancanti.
#

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import statsmodels.api as sm

risultati = pd.read_csv("risultati.csv")

print(risultati.isnull().sum())

# 2. Di che tipo è l'attributo genere? Sulla base della risposta data, visualizzate la distribuzione di questo
# attributo fornendo sia una formulazione tabulare, sia un grafica, motivando le vostre scelte.
#

print("il tipo dell'attributo genere è: ", risultati.genere.dtype)

print(risultati.genere.value_counts())

plt.pie(risultati.genere.value_counts(), labels=risultati.genere.value_counts().index)
plt.legend(["Femmine", "Maschi"])
plt.show()

# 3. Considerate l'attributo punteggio, e ripetete l'analisi svolta al punto precedente, valutando se debba
# essere fatta nello stesso modo oppure se debbano essere utilizzati strumenti diversi.
#

print(risultati.punteggio.head())
print(risultati.head())

plt.hist(risultati.punteggio, bins=30)
plt.show()

# 4. Valutate l'ipotesi che vi sia una relazione tra gli attributi punteggio e tempo, specificando
# eventualmente il tipo e la forza della relazione determinata. Quali strumenti avete utilizzato
# per valutare questa ipotesi? Perché?
#

print(risultati.punteggio.corr(risultati.tempo))

plt.scatter(risultati.punteggio, risultati.tempo)
plt.show()

# 5. Gli esperti del centro di formazione sospettano che l'attributo punteggio dovrebbe sia ben descritto
# da una distribuzione analoga a quella studiata nell'Esercizio 1. Scegliete uno strumento che ha senso
# utilizzare per validare questa ipotesi e applicatelo, commentando i risultati ottenuti.
#

a = risultati.punteggio.mean() * 2
ecdf = sm.distributions.empirical_distribution.ECDF(risultati.punteggio)
x = np.linspace(0, a)
Fx = (3 / a**2) * x**2 - (2 / a**3) * x**3

plt.plot(x, ecdf(x))
plt.plot(x, Fx)
plt.show()

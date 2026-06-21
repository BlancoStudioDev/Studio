# Inizio 15:05
#
## ----------------------
#  Esercizio 4
## ----------------------
#
#
# 1. Scrivete ed eseguite del codice che calcoli la percentuale di casi del dataset che
# contengono almeno un valore mancante
#

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.stats as stats
import statsmodels.api as sm
from scipy.special import binom

acquisti = pd.read_csv("acquisti.csv")

print(
    "Percentuale di dati mancanti in tutto il db",
    acquisti.isnull().sum().sum() / (3 * len(acquisti.temperatura)),
)

print(
    "Percentuale di dati mancanti per colonna\n",
    acquisti.isnull().sum() / len(acquisti),
)

# 2. Descrivete l'attributo bottiglie_acquistate utilizzando la rappresentazione grafica che
# ritenete più adeguata, motivando la scelta fatta e commentando i risultati ottenuti.

print(acquisti.head())

plt.boxplot(acquisti.bottiglie_acquistate.dropna(), vert=False)
plt.show()

# 3.  L'ipotesi fatta all'inizio dell'esercizio 3 dovrebbe consentire di utilizzare un istogramma
# in alternativa alla rappresentazione del punto precedente; perchè? Visualizzate tale
# istogramma, scegliendo opportunamente il numero di intervalli da considerare.
#
# B(n*n_C, p_C)
#
# essendo la supposizione fatta precedentemente all'esercizio 3, una supposizione per una distribuzione
# binomiale allora possiamo andare semplicemente a descriverla come tale, quindi con un grafico a barre
# o un grafico a istogramma o ancora vlines, per semplicità useremo un istogramma.
#

plt.hist(acquisti.bottiglie_acquistate, bins=30)
plt.show()

# siamo tra l'altro in grado di vedere che questa distribuzione segue una normale anche
#
# valore atteso = mean()
#

print(acquisti.bottiglie_acquistate.mean())

# il valore atteso è infatti 3450.124124124124 che si posizione precisamente al centro della campana nella
# visualizzazione dell'istogramma, confermando la possibilità dell'approssimazione tramite normale
#

sm.qqplot(acquisti.bottiglie_acquistate.dropna(), fit=True, line="45")
plt.show()

# anche questo test ci permette di vedere con precisione che segue una distribuzione normale.
#

# 4. Valutate l'ipotesi che vi sia una relazione di tipo diretto tra gli attributi
# bottiglie_acquistate e temperatura, utilizzando in modo opportuno sia un metodo grafico
# sia un indice numerico. Commentate i risultati ottenuti.
#

print(acquisti.bottiglie_acquistate.corr(acquisti.temperatura))

plt.scatter(acquisti.temperatura, acquisti.bottiglie_acquistate)
plt.show()

# non c'è nessun tipo di relazione, le bottiglie vengono acquistate sempre, a guardare dal grafico sono
# ben distribuite e anche con la formula di pearson, vediamo che la correlazine non esiste: -0.00618051
#

# 5. Una bottiglia d'acqua costa 1€, e il distributore sconta 10 centesimi per ogni bottiglia
# resa. Aggiungete al dataset una colonna dal nome ricavo che contenga il ricavo settimanale
# per ogni caso.
#

acquisti["ricavo"] = acquisti.bottiglie_acquistate * 1 - acquisti.bottiglie_rese * 0.1

print(acquisti.ricavo)

# 6. Valutate l'ipotesi che il ricavo settimanale di ogni acquisto sia ben descritto da un
# modello normale, commentando i risultati ottenuti.
#
# facciamo le stesse analisi di prima:
#

sm.qqplot(acquisti.ricavo.dropna(), fit=True, line="45")
plt.show()

plt.hist(acquisti.ricavo.dropna())
plt.show()

print(acquisti.ricavo.dropna().mean())

# si è descritto perfettamente da una normale.
#

# 7. Alla luce dei risultati ottenuti al punto precedente, è opportuno rivedere le ipotesi fatte
# all'inizio dell'esercizio 3? Perchè? E quali ipotesi devono essere riesaminate?
#
# Che cazzo di ipotesi devo rifare, prima ho detto tutto, poisson, normale e binomiale e spiegato tutto
# ora sappiamo che possiamo approssimare sta roba con una normale...
#

# 8. Valutate l'ipotesi che il numero di bottiglie acquistate sia ben descritto da un modello
# normale, commentando i risultati ottenuti.
#
# Porca troia ce l'ha su con il modello normale, l'analisi l'abbiamo fatta prima, quindi si attacca al
# cazzo.
#

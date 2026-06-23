## ----------------
#  Esercizio 3
## ----------------
#
#
# Gli esperti ritengono che la distribuzione del numero di richieste segua una distribuzione di Poisson
# (di parametro ignoto) se si considerano solamente i casi nei quali è stato emesso un allarme.
#
# 1. Memorizzate in una variabile `allarme_si` i valori dell'attributo richieste che si riferiscono
# a tutti e soli i casi nei quali è stato emesso un allarme.
#

import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

import pandas as pd

accessi = pd.read_csv("accessi.csv")

allarme_si = accessi[accessi["allarme"] == 1]

# 2. Ripetete l'analisi fatta all'ultimo punto dell'esercizio 3, considerando solo i casi
# contenuti in `allarme_si`.
#

print(allarme_si.richieste.mean())
print(allarme_si.richieste.var())

# beh adesso siamo un po' lontani.... non seguono molto bene poisson
#

# 3. Nel resto di questo esercizio, supporremo che i valori contenuti in `allarme_si` siano
# assimilabili a un campione estratto da una popolazione $X$ che segue una distribuzione di
# Poisson di parametro $\lambda$. Stimate questo parametro.
#

lambda_valore = allarme_si.richieste.mean()

print(lambda_valore)

# 4. Utilizzando la stima ottenuta al punto precedente, confermate ulteriormente l'ipotesi che i
# valori contenuti in `allarme_si` siano descritti da una distribuzione appartenente al modello
# di Poisson.
#

# 5. Con quale probabilità potete garantire che la stima fatta al punto 3 disti in valore
# assoluto dal valore sconosciuto più di 0.05?
#

print(
    2
    * stats.norm.cdf(
        0.05 * np.sqrt(len(allarme_si)) / np.sqrt(allarme_si.richieste.std())
    )
    - 1
)

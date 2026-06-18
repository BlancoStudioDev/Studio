## -----------------------
#  Esercizio 4
## -----------------------

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.stats as stats
import statsmodels.api as sm

risultati = pd.read_csv("risultati.csv")

# 1. Sulla base della soluzione che avete proposto per l'Esercizio 2, calcolate una stima per a
#
# Uno stimatore per a, come visto nell'esercizio 2 è: 2\bar(Z_n), quindi andiamo a calcolarlo:
#

a = 2 * risultati.punteggio.mean()
print(a)

# 2. Utilizzare il risultato dell'Esercizio 2.7 per stimare la probabilità che la stima ottenuta
# al punto precedente comporti un errore (in valore assoluto) minore o uguale di 1
#
# Per farlo dobbiamo semplicemente andare a calcolare il valore precedentemente analizzato in maniera
# matematica, ovvero 2\phi(\sqrt(5n)/a) - 1
#

print(2 * stats.norm.cdf(np.sqrt(5 * len(risultati.punteggio)) / a) - 1)

# 3. Indichiamo con X  la variabile aleatoria che descrive il punteggio ottenuto. Il test si
# considera sostenuto con successo se si ottiene un punteggio superiore a 21. Calcolate la
# frequenza di questo evento nel dataset considerato e confrontatela con la probabilità P (X > 21) a,
# calcolata sostituendo al parametro la corrispondente stima ottenuta nel punto 1 di questo
# esercizio, commentando i risultati ottenuti.
#

maggiori_21 = risultati[risultati.punteggio > 21]

print(len(maggiori_21) / len(risultati.punteggio))

# per calcolare P(X > 21) devo andare a scriverla come P(X<=21) e per calcolarla basta usare la cdf
# della normale per calcolarla:
#

x = 21
print((3 / a**2) * x**2 - (2 / a**3) * x**3)

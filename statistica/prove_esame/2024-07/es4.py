## ----------------------
#  Esercizio 4
## ----------------------
#
#
# I valori dell'attributo cui valore massimo a punteggio nel dataset considerato al punto precedente sono espressi in una scala il
# non è stato reso noto, e il centro di formazione vuole stimare questo valore.
#
# 1. Sulla base della soluzione che avete proposto per l'Esercizio 2, calcolate una stima per a
#
# Per risolvere questo problema basta semplicemente andare ad applicare la funzione P(X -\mu <= epsilon)
#

import numpy as np
import pandas as pd
import scipy.stats as stats

risultati = pd.read_csv("risultati.csv")

print((3 * risultati.punteggio.mean() - 1) / 2)

a = (3 * risultati.punteggio.mean() - 1) / 2

# 2. Utilizzare il risultato dell'Esercizio 2.7 per stimare la probabilità che la stima ottenuta al punto
# precedente comporti un errore (in valore assoluto) minore o uguale di 1.

print(
    "formula:",
    2 * stats.norm.cdf(1 / (np.sqrt((a**2 + a - 2) / (8 * len(risultati.punteggio)))))
    - 1,
)

# 3. Indichiamo con X la variabile aleatoria che descrive il punteggio ottenuto. Il test si considera sostenuto
# con successo se si ottiene un punteggio superiore a 35. Calcolate la frequenza di questo evento nel
# dataset considerato e confrontatela con la probabilità p = P(X > 35), calcolata sostituendo al
# parametro a la corrispondente stima ottenuta nel punto 1 di questo esercizio, commentando i risultati ottenuti.
#

x = 35

print(1 - ((x * (x + 1)) / (a * (a + 1))))

print(risultati.punteggio.dtype)

print((risultati.punteggio > 35).mean())

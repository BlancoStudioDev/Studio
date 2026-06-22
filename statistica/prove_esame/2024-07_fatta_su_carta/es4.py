## --------------------
#  Esercizio 4
## --------------------
#
#
# I valori dell'attributo cui valore massimo a punteggio nel dataset considerato al punto
# precedente sono espressi in una scala il non è stato reso noto, e il centro di formazione
# vuole stimare questo valore.
#
# 1. Sulla base della soluzione che avete proposto per l'Esercizio 2, calcolate una stima per a
#
# per fare questo utilizziamo lo stimatore T che abbiamo creato nell'esercizio 2, ovvero T = (3X - 1)/2
#

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.stats as stats
from scipy.special import binom

risultati = pd.read_csv("risultati.csv")

print((3 * risultati.punteggio.mean() - 1) / 2)

a = (3 * risultati.punteggio.mean() - 1) / 2
# 2. Utilizzare il risultato dell'Esercizio 2.7 per stimare la probabilità che la stima ottenuta al punto
# precedente comporti un errore (in valore assoluto) minore o uguale di 1.
#
# Applichiamo semplicemente la formula ottenuta prima, ma dobbiamo anche andare a considerare che siamo
# con n = len(risultati.punteggio.dropna()) e sigma = risultati.punteggio.std()
#

epsilon = 1
sigma = risultati.punteggio.std()
n = len(risultati.punteggio)

print(2 * stats.norm.cdf(epsilon / (sigma / np.sqrt(n))) - 1)

# questo è come lo faremmo se fosse normalmente, se invece vogliamo calcolarlo con la sua deviazione
# standard che è np.sqrt((a**2 + a - 2)/(8*n)) allora bisogna scomposse la cdf e sigma in modo più esteso
#

sigma = np.sqrt((a**2 + a - 2) / (8 * n))

print(2 * stats.norm.cdf(epsilon / (sigma)) - 1)

# 3. Indichiamo con X la variabile aleatoria che descrive il punteggio ottenuto. Il test si
# considera sostenuto con successo se si ottiene un punteggio superiore a 35. Calcolate la frequenza
# di questo evento nel dataset considerato e confrontatela con la probabilità p = P(X > 35), calcolata
# sostituendo al parametro a la corrispondente stima ottenuta nel punto 1 di questo esercizio,
# commentando i risultati ottenuti.
#
# x = 35
#
# P(X > 35) = 1 - P(X <= 35) = 1 - (x*(x + 1))/(a *(a+1))
#

x = 18

p = 1 - (x * (x + 1)) / (a * (a + 1))

print("Probabilità P(X > 25): ", p)

print(len(risultati[risultati["punteggio"] > 35]) / len(risultati.punteggio.dropna()))

# 4. Ipotizzando che sussista indipendenza tra i punteggi ottenuti nel test da persone diverse che lo
# sostengono, supponiamo che cinque studenti o studentesse del centro svolgano il test in una stessa
# tornata, e indichiamo con Y la variabile aleatoria che indica il numero di test superati. Dite quale
# distribuzione segue questa variabile aleatoria. Considerate poi gli eventi seguenti, esprimendo ognuno
# di essi in termini di Y a e calcolate la corrispondente probabilità, sostituendo al parametro la stima che
# avete precedentemente ottenuto:
# A. nessuna persona supera il test;
# B. esattamente due persone superano il test;
# C. almeno una persona supera il test.
#
# Beh allora p un po' difficile dire che tipo di distribuzione è presente all'interno di questo campione se
# ho solamente 5 dati all'interno del campione, potrebbe benissimo essere falsata in qualsiasi modo.
#
# Posso solamente dire che questa distribuzione potrebbe essere binomiale data dal testo, poichè so per esempio
# p e n. Quindi B(5, p)
#
# A. nessuna persona è P(X = 0) = binom(5, 0) * p^0 * (1 - p)^5
#

print("A: ", binom(5, 0) * p**0 * (1 - p) ** 5)

# B. Esattamente due persone superano il test P(X = 2)
#

print("B: ", binom(5, 2) * p**2 * (1 - p) ** 3)

# C. almeno una persona supera il test P(X >= 1) = 1 - P(X = 0)
#

print("C: ", 1 - binom(5, 0) * p**0 * (1 - p) ** 5)

# Nelle stesse ipotesi del punto precedente, supponiamo che a livello nazionale vi siano 3000 persone
# che hanno svolto il test in una stessa giornata, e indichiamo con Z la variabile aleatoria che indica il
# numero di test superati. Dite quale distribuzione segue Z. Considerate poi gli eventi seguenti,
# esprimete ognuno di essi in termini di Z e calcolate la corrispondente probabilità, sostituendo al
# parametro a la stima che avete precedentemente ottenuto:
#
# A. tra il 50% e il 60% dei partecipanti superano il test;
# B. al più il 50% dei partecipanti supera il test.
#
# Siccome ci troviamo in un caso in cui la probabilità è molto bassa ovvero: 0.1043144884419328, almeno
# nell'esercizio iniziale con X > 35,  e il numero è molto alto, allora possiamo approssimare, quella che
# era la nostra distribuzione binomiale come una variabile di distribuzione poissoniana. Ancora meglio
# al posto della distribuzione di Poisson possiamo utilizzare una distribuzione come quella normale, andando
# a stimare i grandi numeri come: 2 * phi((valore - mu) /(sigma)) - 1
#
# P((3000/100) * 50 < X < (3000/100) * 60) = P(X < (3000/100) * 60) - P(X < (3000/100) * 50)
#
# Arrivati a questo punto calcoliamo però il nostro valore atteso e la nostra deviazione standard come:
# E[T] = a = 26.44 e sigma = np.sqrt((a**2 + a - 2) / 8*n)
#
# Arrivando alla formula finale possiamo dire che
#

n = 3000

sigma = np.sqrt((a**2 + a - 2) / (8 * n))
print(sigma)
mu = a

magg = 3000 / 100 * 60
min = 3000 / 100 * 50

print(stats.norm.cdf((magg - mu) / sigma) - stats.norm.cdf((min - mu) / sigma))

# per il punto B quello che ci serve fare è andare a calcolare P(X <= 0.5 * n) quindi andando a svolgere
# i calcoli si ottiene che la probabilità è uguale a phi((0.5*n - \mu)/ \sigma)
#

print(stats.norm.cdf((0.5 * 3000 - mu) / sigma))

# questa risoluzione porta alla nostra risoluzione un problema principale, ovvero che la probabilità degli
# eventi è o 0 o 1. Per farla in un altro modo, modo che nel testo non è detto di applicare, posso scrivere
# che N(np, np(1-p)) data direttamente dalla binomiale, i quali sono valore atteso e varianza, quindi nel nostro
# caso avremmo: N(np, np.sqrt(np*(1-p)))
#

mu = n * p
sigma = np.sqrt(n * p * (1 - p))

print(stats.norm.cdf((magg - mu) / sigma) - stats.norm.cdf((min - mu) / sigma))

print(stats.norm.cdf((0.5 * 3000 - mu) / sigma))

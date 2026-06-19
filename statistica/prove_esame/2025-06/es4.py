# Inizio 9:23
## --------------------
#  Esercizio 4
## --------------------
#
#
# Un ex dipendente del centro medico vuole aprire una sua struttura ed entrare in concorrenza con il suo precedente datore
# di lavoro. È già a conoscenza del fatto che o = 400 e p = 0.2, ma non conosce il valore r rimborsato dal sistema sanitario
# pubblico. Avendo trafugato il dataset che abbiamo studiato nell'esercizio precedente, decide di utilizzarlo per stimare r,
# lavorando esclusivamente sui dati relativi ai mesi invernali, che considereremo come un campione aleatorio R1,...,Rn estratto
# dalla variabile aleatoria R introdotta nell'Esercizio 2.

# 1. Sulla base della soluzione che avete proposto per l'Esercizio 2, calcolate una stima adeguata per r.
#

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.stats as stats
import statsmodels.api as sm

o = 400
p = 0.2

esami = pd.read_csv("esami.csv")

esami["inverno"] = (
    (esami["mese"] == 1) | (esami["mese"] == 1) | (esami["mese"] == 1)
).astype(int)

print(esami[esami["inverno"] == 1].tot_rimborsato.mean() / (o * p))

r = esami[esami["inverno"] == 1].tot_rimborsato.mean() / (o * p)

# 2. Come potete adattare il risultato dell'Esercizio 2.7 per ottenere la probabilità che la stima ottenuta al
# punto precedente comporti un errore (in valore assoluto) minore o uguale di mezzo euro? Calcolate questa probabilità.
#
# Per farlo dobbiamo andare intanto a ricordare come era fatta la nostra probabilità, ovvero: 2*phi(\epsilon/(sigma)) - 1
# con sigma = r * np.sqrt( p * o * (1-p) / (n*o*p) ) e \epsilon = 1/2
#

epsilon = 0.5
n = len(esami)

print(2 * stats.norm.cdf(epsilon / (r * np.sqrt(p * o * (1 - p) / (n * o * p)))) - 1)

# 3. Indichiamo con P la variabile aleatoria che indica l'introito mensile dovuto ai clienti paganti. Stimate il valore
# atteso e la deviazione standard di P dal campione considerato, e memorizzateli in due variabili mu pe sigma p. Memorizzate
# poi nelle variabili mu r e sigma_r le stime di valore atteso e deviazione standard della variabile aleatoria R, ottenute
# considerando i risultati dell'Esercizio 1.6 e sostituendo a r la stima precedentemente ricavata. Nel resto dell'esercizio,
# approssimeremo le distribuzioni di Re di P con delle opportune leggi gaussiane.
#

mu_P = esami.tot_pagato.mean()
sigma_P = esami.tot_pagato.std()

mu_R = r * o * p
sigma_R = r**2 * o * p * (1 - p)

print("Valore atteso di P: ", mu_P, "\nDeviazione Standard di P: ", sigma_P)
print("Valore atteso di R: ", mu_R, "\nDeviazione Standard di R: ", sigma_R)

# 4. Il centro medico che l'ex dipendente si appresta ad aprire dovrà sostenere delle spese fisse mensili di 25000 Euro.
# Indichiamo con F l'evento che si verifica se in un mese i soldi ottenuti dai clienti paganti e dal sistema sanitario
# non sono sufficienti a coprire queste spese. Esprimete F in termini delle variabili aleatorie R e P, e calcolate poi P(F).
#

Npr = stats.norm(mu_P + mu_R, sigma_P + sigma_R)
print(Npr.cdf(25000))

# Fine 9:42

# Inizio 17:00
#
## -------------------
#  Esercizio 4
## -------------------
#
# Prendendo in considerazione che `differenza` sia distribuito come $Z$
#
# 1. Sapendo che $\mu_X = 5$ calcolare una stima di $\mu_Y$
#
# Prendondo da prima devo semplicemente fare: 2 - E[\bar(Z)] e posso usare mean() per il calcolo del
# valore atteso da differenza
#

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.stats as stats

punteggi = pd.read_csv("punteggi.csv")

print(5 - punteggi.differenza.mean())

# 2. Calcolare una stima per $\sigma_X^2$ evidenziando le proprietà dello stimatore
#
# se come nell'esercizio prima consideriamo che sigma_X = sigma_Y allora possiamo anche dire che:
# \sigma_X ^ 2 = var(Z)/2

print(punteggi.differenza.var() / 2)

# 3. Calcolare $\sqrt{\sigma_X^2 + \sigma_Y^2}$
#

print(np.sqrt(punteggi.differenza.var()))

# 4. Calcolare la probabilità che si verifichi un errore al più di 0.2 nella stima di $\mu_Y$
#
# bisogna applicare semplicemente la formula ricavata precedentemente:
# 2*\phi(\epsilonsqrt(n)/\sqrt(\sigma_x^2 + \sigma_Y^2))
#

print(
    2
    * stats.norm.cdf(
        (0.2 * np.sqrt(len(punteggi.differenza)) / (np.sqrt(25 + 8.377036**2)))
    )
    - 1
)

# 5. Determinare se sono presenti valori nulli in `differenza`
#

if punteggi.differenza.isnull().sum() == 0:
    print("Non ci sono valori nulli")
else:
    print("Ci sono: ", punteggi.differenza.isnull().sum(), " valori nulli")

# FINO A QUI -> 17:39

# 6. Utilizzando le stime fatte negli esercizi precedenti per sostituire i valori nulli, calcolare le seguenti probabilità
#    1. Che X vinca contro Y
#    2. Che X batta Y almeno 3 volte su 10
#    3. Che X batta Y almeno 3 volte sapendo che X ne ha vinte almeno 2
#    4. Che X vinca dopo almeno 3 sconfitte
#    5. Che X vinca dopo almeno 3 sconfitte sapendo che Y ha vinto la prima

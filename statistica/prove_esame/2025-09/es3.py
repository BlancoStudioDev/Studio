# Inizio 17:00
#
## -------------------
#  Esercizio 3
## -------------------
#
# 1. Descrivere i dati e determinarne i tipi
#

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import statsmodels.api as sm

punteggi = pd.read_csv("punteggi.csv")

print(punteggi.head())

print(punteggi.dtypes)

# 2. Si ha il sospetto che l'arbitro A abbia un pregiudizio sul giocatore $X$,
# determinare un indice che consenta di confermare o confutare questa ipotesi
#

print(punteggi.groupby("arbitro")["differenza"].mean())


# 3. Determinare se è presente un qualche tipo di influenza tra la temperatura
# e la differenza dei punteggi
#

plt.scatter(punteggi.temperatura, punteggi.differenza)
plt.show()

# non particolarmente, ma verifichiamolo anche con un indice di correlazione

print(punteggi.temperatura.corr(punteggi.differenza))

# correlazione di -0.02999 quindi praticamente nulla, se fosse vicino a 1 la correlazione di pearson
# allora avremmo una correlazione, questo non accade.

# 4. Stabilire se temperatura segue una distribuzione normale
#
# Per farlo dobbiamo inanzitutto disegnare il grafo per vedere che tipo di grafo è, e lo farei con un qqplot
#

sm.qqplot(punteggi.temperatura, fit=True, line="45")
plt.show()

# direi di si a parte qualche outliers

# 5. I punteggi dati dagli arbitri sono disomogenei, trovare un indice che consenta di confermare
# o confutare questa ipotesi (?)
#
# Questa cosa si può fare con un indice di gini andando a prendere le frequenze relative degli arbitri
# per poi farne la media e dividerla per il numero totale di casi.
#

frequenze_relative = punteggi.groupby("arbitro")["differenza"].std()

print(frequenze_relative)

## Fine 17:22

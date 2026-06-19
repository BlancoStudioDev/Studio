## ----------------------
#  Esercizio 5
## ----------------------
#
#
# In questo esercizio ci concentreremo sui valori dell'attributo _tentativi_ relativi __ai soli accessi illeciti__
# al sito di home banking, e li interpreteremo come i valori assunti da un campione estratto da una popolazione
# distribuita come una variabile aleatoria $Y$.
#
# 1. Ci sono valori mancanti per l'attributo in questione? Se sì, quanti sono?
#

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.stats as stats
import statsmodels.api as sm

banking = pd.read_csv("banking.csv")

dati_illeciti = banking[banking["illecito"] == 1]

print(dati_illeciti.tentativi.isnull().sum())

# 2. Stimate il valore atteso $\mathbb E(Y)$, specificando la dimensione del campione utilizzato e indicando
# eventuali proprietà dello stimatore utilizzato.
#

print(dati_illeciti.tentativi.mean())

print(len(dati_illeciti.tentativi.dropna()))

# 3. I dati a disposizione permettono di garantire, con probabilità maggiore o uguale a 0.99, che la stima fatta
# al punto precedente comporti un errore (in valore assoluto) grande al più $\epsilon = 0.1$?
#
# 2*\phi(epsilon/sigma) - 1
#
# sigma = np.sqrt(1 - h / h^2)
#

epsilon = 0.1
p = 0.99

sigma = np.sqrt((1 - p) / p**2)

print(2 * stats.norm.cdf(epsilon / sigma) - 1)

# 6. Applicate lo stimatore proposto al punto 4 per ottenere una stima $\hat h$ del parametro sconosciuto $h$.
#

h_hat = 1 / (1 + dati_illeciti["tentativi"].mean())
print(h_hat)

# 7. Calcolate la probabilità $\mathbb P(3 < X < 8)$ che il numero di tentativi di autenticazione durante un
# accesso illecito sia strettamente compreso tra 3 e 8.
#

Y = stats.geom(h_hat)

print(Y.cdf(7) - Y.cdf(3))

# 8. Un malintenzionato ha effettuato due tentativi di accesso andati a vuoto. Calcolate la probabilità
# che siano necessari più di due ulteriori tentativi di accesso.
#

print(1 - Y.cdf(1))

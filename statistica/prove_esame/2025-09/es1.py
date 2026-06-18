# Inizio 16:06
#
## -------------------
#  Esercizio 1
## -------------------
#
# 1. $Z$ è una variabile aleatoria? Se sì, è discreta o continua? Motivare adeguatamente la risposta
#
# Certo che è una variabile continua, deriva dalla sottrazione, operazione continua, di due variabili
# aleatorie continue, quindi è continua
#
#
# 2. Calcolare il valore atteso di $Z$ esprimendolo in funzione di $\mu_X$ e $\mu_Y$, mostrando i passaggi
#
# Per calcolare il valore atteso di Z basta semplicemente andare ad applicare le trasformazioni del valore
# atteso: E[Z] = E[X - Y] = E[X] - E[Y] = \mu_x - \mu_y
#
#
# 3. Calcolare la varianza di $Z$ esprimendola in funzione di $\sigma_X$ e $\sigma_Y$, mostrando i passaggi
#
# Facciamo la stessa identica cosa del valore atteso: Var(X - Y) = Var(X) - Var(Y) = (\sigma_X)^2 - (\sigma_Y)^2
#
#
# 4. La variabile aleatoria $Z$ segue una distribuzione normale? Motivare la risposta
#
# La variabile aleatoria Z segue una distribuzione normale in quanto è la differenza, operazione continua,
# tra due variabili aleatorie di distribuzioni normali
#
#
# 5. Calcolare la funzione di ripartizione $F_Z(x)$ esprimendola in funzione dei parametri citati sopra
# e utilizzando $\phi$
#
# N(\mu, \sigma) = N(\mu_X - \mu_Y, sqrt((\sigma_X)^2 + (\sigma_Y)^2))
# P(Z) = ((X - \mu_X + \mu_Y)/sqrt((\sigma_X)^2 + (\sigma_Y)^2))
#
#
# 6. Tenendo conto che $\mu_X = 2$, $\mu_Y = 1$, $\sigma_X = 1$ e $\sigma_Y = 2$, disegnare il
# grafico della funzione di ripartizione di $Z$
#

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.stats as stats
import statsmodels.api as sm

mu_X = 2
mu_Y = 1
sigma_X = 1
sigma_Y = 2

mu_Z = mu_X - mu_Y
sigma_Z = np.sqrt((sigma_X) ** 2 + (sigma_Y) ** 2)

x = np.linspace(mu_Z - 3 * sigma_Z, mu_Z + 3 * sigma_Z, 500)
y = stats.norm.cdf(x, mu_Z, sigma_Z)
plt.scatter(x, y)
plt.show()

# 7. Calcolare la funzione di densità di probabilità $f_Z(x)$ esprimendola
# in funzione dei parametri sopracitati e utilizzando $\phi$
#
# per farlo normalmente si userebbe la funzione: 1/(sqrt(2)\pi\sigma)np.exp(-(x-\mu)^2/2*\sigma**2)
# ma siccome dobbiamo passare alla forma standardizzata andiamo a farla normalmente con \phi e poi a
# standardizzarla dividendo per la varianza.
#
# 1/\sigma_Z * \phi((1-\mu_Z)/\sigma_Z) andando poi a sostituire i valori precedentemente calcolati
#


x = np.linspace(mu_Z - 3 * sigma_Z, mu_Z + 3 * sigma_Z, 500)
f_x = 1 / sigma_Z * stats.norm.cdf(x, mu_Z, sigma_Z)

# 8. Tenendo conto che $\mu_X = 2$, $\mu_Y = 1$, $\sigma_X = 2$ e $\sigma_Y = 2$, disegnare il
# grafico della funzione di densità di probabilità di $Z$

mu_X = 2
mu_Y = 1
sigma_X = 2
sigma_Y = 2

mu_Z = mu_X - mu_Y
sigma_Z = np.sqrt((sigma_X) ** 2 + (sigma_Y) ** 2)

x = np.linspace(mu_Z - 3 * sigma_Z, mu_Z + 3 * sigma_Z, 500)
f_x = 1 / sigma_Z * stats.norm.pdf(x, mu_Z, sigma_Z)

plt.scatter(x, f_x)
plt.show()

## fine 16:35

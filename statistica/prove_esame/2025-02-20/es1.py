# Inizio 9:45
#
## ----------------------
#  Esercizio 1
## ----------------------
#
#
# Sia $X$ una variabile aleatoria distribuita secondo un modello di Poisson di parametro $\lambda$.
#
# 1. Considerate le seguenti affermazioni e, per ognuna, dite se è vera o falsa, motivando le vostre risposte:
#
#   * $\lambda$ può assumere un valore maggiore di 1;
#   * $\lambda$ deve sempre assumere valori interi;
#   * $\lambda$ non può mai essere negativo;
#   * $X$ può sempre assumere specificazioni maggiori di $\lambda$.
#
# 1 -> si lambda può assumere qualsiasi valore, non è una probabilità
# 2 -> lambda è un valore continuo, quindi non è vero
# 3 -> vero lambda non può essere negativo
# 4 -> falso la maggior parte delle volte poichè X è data da e^-lambda*(lambda^i/i!)
#

# 2. Fissato $n \in \mathbb{N}$ siano $X_1, ..., X_n$ variabili aleatorie indipendenti e identicamente distribuite
# come $X$. Indichiamo con $S$ la somma $\sum_{i=1}^{n} X_i$. Che distribuzione segue $S$? Perché?
#
# Può essere visto in due modi, poichè quando n cresce tanto possiamo dire che la distribuzione è una binomiale approssimabile
# a una Poissiana
#

# 3. Dato un generico numero naturale $z$, esprimete $\mathbb{P}(S=z)$ in funzione di $\lambda$, $n$ e $z$.
#
# P(S = z) = e^-n*lambda* ((n*lambda)**z/z!

# 4. Sia $\bar{S} = \frac{1}{n} \sum_{i=1}^{n} X_i$. Indicate quali sono i valori che può assumere $\bar{S}$ ed
# esprimete $\mathbb{P}(\bar{S} = x)$ in funzione di $\lambda$, $n$ e $x$.
#
# P(S/n = x) = P(S = n*x) = e^-n*lambda * ((n*lambda**(n*x))/((n*x)!))
#

# 5. Fissiamo, solo in questo punto, $\lambda = 0.9$ e $n = 15$. Utilizzando il computer visualizzate il grafico della funzione
# di massa di probabilità di $\bar{S}$, motivando la scelta fatta. Se non avete risposto alla domanda 4, potete visualizzare
# l'analogo grafico per $S$.
#

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.stats as stats
import statsmodels.api as st
from scipy.special import binom, factorial

lambda_valore = 0.9
n = 15

z_valori = np.arange(0, 25)
x = z_valori / n

y = np.exp((-n) * lambda_valore) * (
    ((n * lambda_valore) ** z_valori) / factorial(z_valori)
)
z = np.exp((-n) * lambda_valore) * (((n * lambda_valore) ** (n * x)) / factorial(n * x))

plt.bar(z_valori, z)
plt.show()

plt.bar(x, y, width=0.05)
plt.show()

# fine 10:11

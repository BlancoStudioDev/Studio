# Inizio 14:09
#
## ----------------------
#  Esercizio 1
## ----------------------
#
#
# Sia C una variabile aleatoria distribuita secondo unun modello binomiale di parametri n_C e
# p_C ∈ [ 0 , 1). Nel resto del tema d'esame C modellerà il numero di bottiglie d'acqua minerale
# di una certa marca che un nucleo familiare acquista nell'arco di una settimana.
#
# 1. Quali valori può assumere il parametro nC ? e quali valori può assumere C? Giustificate la risposta
#
# N_c è il numero delle bottiglie massimo che vengono assunte dalla famiglia.
# La variabile aleatoria C può assumere diversi valori con risultati 1,2,3,4,....n_C
#

# 2. Indichiamo con f_C la funzione di massa di probabilità della variabile aleatoria C. Scrivete
# la forma analitica di f_C in dipendenza dai parametri indicati al punto precedente e di una
# generica specificazione x della variabile aleatoria C.
#
# La pmf o funzione di massa di probabilità per le distribuzioni discrete è delineata nel sequente
# modo: P(C = x) = binom(n_c, x) * p_C^x * (1-p_C)**(n_c-x)
#

# 3. Fissiamo, solo in questo punto,
# n_C = 20 e p_C = 0.8. Utilizzando il computer visualizzate
# graficamente l'andamento di f C(x) al variare di x, nella zona in cui questa funzione
# assume valori sensibilmente diversi da zero. Come avete scelto i valori minimo e
# massimo per x?
#

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.stats as stats
from scipy.special import binom

n_C = 20
p_C = 0.8

# scelgo questi valori per includere il [media - 3*std, media + 3*std]

media = n_C * p_C
std = np.sqrt(n_C * p_C * (1 - p_C))

x = np.arange(np.floor(media - 3 * std), np.floor(media + 3 * std))
y = binom(n_C, x) * p_C**x * (1 - p_C) ** (n_C - x)

plt.bar(x, y)
plt.show()

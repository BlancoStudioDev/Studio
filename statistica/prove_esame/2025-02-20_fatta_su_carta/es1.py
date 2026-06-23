## -------------------
#  Esercizio 1
## -------------------
#
#
# 5. Fissiamo, solo in questo punto, $\lambda = 0.9$ e $n = 15$. Utilizzando il computer visualizzate il grafico della
# funzione di massa di probabilità di $\bar{S}$, motivando la scelta fatta. Se non avete risposto alla domanda 4, potete
# visualizzare l'analogo grafico per $S$.
#

import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
from scipy.special import factorial

import pandas as pd

lambda_valore = 0.9
n = 15

x = np.arange(0, 30) / 15
y = np.exp(-n * lambda_valore) * (((n * lambda_valore) ** (n * x)) / (factorial(n * x)))

plt.vlines(x, 0, y)
plt.show()

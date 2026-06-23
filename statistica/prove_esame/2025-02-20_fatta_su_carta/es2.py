## ------------------
#  Esercizio 2
## ------------------
#
#
# 5. Fissando, solo in questo punto, $\lambda = 0.9$ ed $\epsilon = 0.05$, scrivete ed eseguite del codice che mostra come la
# probabilità calcolata al punto precedente tenda a 1 all'aumentare della dimensione del campione. Commentate il risultato ottenuto,
# spiegando il comportamento dell'andamento per i valori estremi considerati per $n$.
#

import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

lambda_valore = 0.9
epsilon = 0.05

n = np.arange(0, 50)
y = 2 * stats.norm.cdf(epsilon / (np.sqrt(lambda_valore / n)) - 1)

plt.plot(n, y)
plt.show()

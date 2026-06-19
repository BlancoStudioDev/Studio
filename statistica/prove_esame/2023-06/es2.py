## ----------------------
#  Esercizio 2
## ----------------------
#
#
# Sia $X \sim \mathrm G(h)$ una variabile aleatoria distribuita secondo un modello geometrico di parametro $h$.
#
# 1. Quali sono i valori $x$ per i quali ha senso calcolare la probabilità $\mathbb P(X > x)$?
#
# per x <= 0
#

# 2. Per un generico $x \in \mathbb N$, calcolate la probabilità $\mathbb P(X > x)$, esprimendola in funzione del parametro $h$.
#
# P(X > x) = (1-h)**(n+1)
#

# 3. Esprimete in funzione di $x$ e $h$ il valore $F_X(x)$ restituito dalla funzione di ripartizione di $X$.
#
# P(X > x) = (1-h)**(\floor[x]+1)
#

# 4. Disegnate il grafico della fuzione $F_X$ ottenuta al punto precedente, fissando $h = \frac{4}{10}$.
#

import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

h = 4 / 10

x = np.arange(0, 50)
y = 1 - (1 - h) ** (np.floor(x) + 1)

plt.plot(x, y)
plt.show()

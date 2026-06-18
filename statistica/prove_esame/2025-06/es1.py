## --------------------
#  Esercizio 1
## --------------------
#
# In questo esercizio ipotizzeremo che sia fisso il numero di volte, nell'arco di un mese, che in
# un centro medico viene eseguito un dato esame. Indicato con oЄN tale numero, sia pЄ[0, 1] la
# probabilità che un utente che effettua l'esame non debba pagare la prestazione medica, perché
# è coperto dal sistema sanitario pubblico. Siano, infine, $X1,... Xo$ delle variabili aleatorie,
# ognuna delle quali assume le seguenti specificazioni:

# - 1 quando la prestazione per l'i-esimo esame è riconosciuta dal sistema sanitario
# - 0 altrimenti

# 1. Che distribuzione segue $X$, indipendentemente dal valore di i?
#
# Una singola variabile aleatoria, X_i, anche se non prendiamo come rilevante la presenza di i
# è un avariabile aleatoria con distribuzione Bernoulliana, poichè si tratta come un singolo
# evento indipendente.
#

# 2. Che motivazioni utilizzereste per sostenere che le variabili aleatorie $X1,..., Xo$ sono i.i.d.?
#
# Le prestazioni di un singolo cliente, ovvero i suoi esami, non influenzano gli esami delle altre
# persone, e pertanto non devono essere viste come variabili che dipendono da altre, ma completamente
# indipendati
#

# 3. Sia $M$ la somma da i a o di $Xi$. Quando si verifica l'evento $M$=m?
#
# L'evento M si verifica nel momento che viene verificato m, quindi che M = m effettivamente.
#

# 4. Che distribuzione segue $M$?
#
# Distribuzione Binomiale, in quanto è una successione di diverse Bernoulliane, pertanto, se mette insieme
# diverse Bernoulliane ottengo una Binomiale.
#

# 5. Indichiamo con $R$ la variabile aleatoria che indica il rimborso totale ottenuto dal centro medico in
# un mese. Esprimete $R$ in funzione r e di una o più tra le variabili aleatorie introdotte, scegliendole
# opportunamente. Esprimete poi la probabilità P(R) in funzione di o, p, r e x.
#
# R = r*M
#
# P(R) -> R = r*m -> P(R = x) = P(r*M = x) = P(M = x/r) = binom(o x/r) * p**(x/r) * (1-p)**(o - (x/r))
#

# 6. Calcolate il valore atteso e la varianza di R, esprimendoli in funzione di r, o e p
#
# Il valore atteso è definito come E[R] = r*E[M] = r * o * p, mentre la varianza è Var(R) = r**2Var(M) =
# = r**2 * o * p *(1-p)
#

# 7. Solo in questo punto fissiamo r = 35, o = 40 e p=0.2. Disegnate il grafico della funzione di
# massa di probabilità di R e commentate il risultato ottenuto
#

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.stats as stats
from scipy.special import binom

o = 40
p = 0.2
r = 35

x = np.arange(0, o * r)
y = binom(o, (x / r)) * p ** (x / r) * (1 - p) ** (o - (x / r))

plt.bar(x, y)
plt.show()

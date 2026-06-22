## ----------------------
#  Esercizio 1
## ----------------------
#
#
# Sia X una variabile casuale che segue una legge bernoulliana di parametro p.
#
# 1. Quali valori può assumere X?
#
# La variabile aleatoria X può assumere qualsiasi valore, è la probabilità che può
# assumere solamente valori tra 0 e 1. Per esempio il lancio di una moneta è descritto
# da una bernoulliana, solo se questo avviene per una volta, non per n volte. QUindi assume
# valori o successo o insuccesso, o valori di vero falso, in generale 1 o 0.
#

# 2. Quali valori può assumere il parametro p?
#
# Il parametro p, che immagino stia a descrivere la probabilità di avventimento di un determinato
# evento, assume valori tra 0 e 1, in particolare p o 1-p
#

# 3. Esprimete, in funzione di p, il valore ateso E(X).
#
# Il valore atteso di una bernoulliana è esattamente p
#

# 4. Completate la Figura 77(a) con il grafico di E(X) al variare di p, evidenziando in tale
# grafico tutte le informazioni che ritenete rilevanti.
#

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 1, 0.01)
y = x
plt.plot(x, y)
plt.show()

# 5. Quali valori può assumere E(X)? Giustificate la risposta
#
# gli stessi di p, siccome E[X] = p allora i valori che assume sono tra 0 e 1
#

# 6. Esprimete, in funzione di p, la varianza Var (X).
#
# Var(X) = p(1-p)
#

# 7. Completate la Figura 77(b) con il grafico di Var(X) al variare di p, evidenziando in tale
# grafico tutte le informazioni che ritenete rilevanti
#

x = np.arange(0, 1, 0.01)
y = x * (1 - x)

plt.plot(x, y)
plt.xlabel("p")
plt.axvline(x=0.5, color="r", linestyle="--")
plt.text(0.55, 0.1, "p/2", ha="center", color="r")
plt.text(1, 0, "p", ha="center", color="r")
plt.show()

# 8. Quali valori può assumere Var(X)? Giustificate la risposta.
#
# Var(X) può assumere dei valori fino a 1/4 come massimo, uno perchè lo vediamo dal grafico
#

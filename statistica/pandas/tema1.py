# Esercizio 1.1
#
# D_10_5 = 10^5
#
#
# Esercizio 1.2
#
# Estratta a caso all'interno del dataframe
# P(uniforme) = 1 / (10^5) = 0.00001 perchè ha uno spazio equiprobabile
#
#
# Esercizio 1.3
#
# Esempio: 111 23 o 222 75 ...
# Questa è una combinazione che viene calcolata come: per le prime 3 cifre è 10 combinazioni
# mentre per le ultime due ho 10^2, quindi in titale ho 10 * 10^2 = 10^3
#
#
# Esercizio 1.4
#
# P(password) = 1 / (10^3) = 0.001
#
#
# Esercizio 1.5
#
# 2800 password uscendo da:
# A = aaa--
# B = -aaa-
# C = --aaa
# 3*10^3
#
# A int B = aaaa-
# B int C = -aaaa
# 2*10^2
#
# A int C = aaaaa
# 10
#
# A int B int C = aaaaa
# 10
#
# n_password = 3*10^3 + 2*10^2 + 10 - 10 = 2800
#
#
# Esercizio 1.6
#
# P(uguali) = 1/2800 = 0.000357
#
#
# Esercizio 2.1
#
# Per x appartenente a R con due "condizioni", se la probabilità è negativa allora
# la probabilità deve essere fatta come 1-probabilità e se invece avessi un numero
# positivo ma con la virgola allora la probabilità deve esserne fatto il floor
#
#
# Esercizio 2.2
#
# Nel modello geometrico sappiamo che la funzione di ripartizione è:
# 1 - (1-p)^{floor{x} + 1}
#
# la funzione di ripartizione calcola quindi il numero di tentativi necessari prima
# di ottenere un successo. Mettiamo il x + 1 perchè ci consente di trovare tutti i fallimenti
# se lo togliessimo troveremmo il primo successo, non l'ultimo fallimento.
#
# Esercizio 2.3
#
# F_X(x) = 1 - (1-p)^{floor{x} + 1} se x >= 1
# F_X(x) = 0 se x < 1
#
# Esercizio 2.4

import matplotlib.pyplot as plt
import numpy_es as np

def F(x, h):
    return 1 - ( 1 - h ) ** (np.floor(x) + 1)

x = np.linspace(0, 50)
y = F(x, 4/10)

plt.step(x, y)
plt.show()

# Esercizio 3.1
#
# Il valore atteso è sempre uno stimatore non distorto per la media campionaria

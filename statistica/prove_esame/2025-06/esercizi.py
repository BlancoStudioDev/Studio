# Esercizio 1
#
# 1.1 La distribuzione è descritta da un modello bernoulliano
#
# 1.2 gli esami sono identicamente indipendenti distribuiti perchè l'esame di un utente non determina l'esito dell'esame di un altro
#
# 1.3 esito =
#    \begin{cases}
#    0 & P(X=1) = p\\
#    1 & P(X=0) = 1-p\\
#    \end{cases}
#    somma di tutti gli esiti = m
#    ovvero che lo stato riconosce esattamente m=M esami
#
# 1.4 M segue la distribuzione binomiale poichè andiamo solamente a ripetere il processo di un esame su m esami
#
# 1.5 R = r*m
#    C(o, x/r) * p^(x/r) * (1-p)^(o-(x/r))
#
# 1.6 E(R) = r*o*p,   Var(R) = r^2 o*p(1-p)
#
# 1.7 p^i(1-p)^(o-i)

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.special import binom

r = 35
o = 40
p = 0.2

x = np.arange(0, o * r, r)
y = binom(o, (x / r)) * p ** (x / r) * (1 - p) ** (o - (x / r))

# plt.vlines(x, 0, y)
# plt.show()


# Esercizio 2
#
# 2.1 il valore atteso è lo stesso di prima...
#
# 2.2 con il metodo plugin vado a scrivere il valore atteso precedente e escludere la variabile che non conosco per chiamarla stimatore
#     E(R) = r*o*p quindi r è uguale a r = E(R)/(o*p) sostituisco E(R) con R' quindi T = R'/(o*p) quindi posso dire che T = (r*o*p)/(o*p) = r
#
# 2.3 per applicare il metodo plugin anche con la varianza, basta che applico lo stesso ragionamento: Var(R) = r^2*o*p*(1-p), quindi
#     r = radice (Var(R)/(o*p*(1-p))). Non si può dire senza calcolare l'MSE
#
# 2.4 MSE(T) = Var(T) + bias^2. Il bias è uguale a 0


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

dati = pd.read_csv("esami.csv")

print(dati.head())

print(dati["mese"].dtype)

print("mese missing: " + str(dati["mese"].isnull().sum()))
print("tot_pagato missing: " + str(dati["tot_pagato"].isnull().sum()))
print("tot_rimborsato missing: " + str(dati["tot_rimborsato"].isnull().sum()))

plt.bar(dati["mese"].unique(), dati["mese"].value_counts())
plt.show()

print(dati["mese"].value_counts())

plt.scatter(dati["mese"], dati["tot_rimborsato"])
plt.show()

print(dati["tot_rimborsato"].corr(dati["mese"]))

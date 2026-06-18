import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats
from scipy.special import factorial, binom

# 3 incidenti settimanali
# prossima settimana almeno un incidente

# P(X >= 1) = 1 - P(X = 0) = e ^ (-lambda) * (lambda^x/x!)

lambda_valore = 3
print(1 - np.exp(-lambda_valore) * (lambda_valore**0 / factorial(0)))

# probabilità di essere difettosi pari a 0.1
#
# variabile aleatoria binomiale perchè ha una probabilità di successo fissata
# Possiamo però utilizzare poisson come approssimazione della binomiale
#
# P(X <= 1) = P(X = 0) + P(X = 1) = binom(n, 0)*p^0*(1-p)^10 + binom(n,1)*p^1*(1-p)^9
#

n = 10
p = 0.1
print(binom(n, 0)*p**0*(1-p)**10 + binom(n,1)*p**1*(1-p)**9)

# se lo faccio con poisson
# P(X <= 1) = e^(-lambda_valore)*(lambda_valore**x/x!) + np.exp(-lambda_valore)*(lambda_valore**x/x!)
#

lambda_valore = 1
print(np.exp(-lambda_valore)*(lambda_valore**0/factorial(0)) + np.exp(-lambda_valore)*(lambda_valore**1/factorial(1)))


# valore medio della variabile aleatoria è = 3.2
# non vengano emesse più di 2 particelle
# lambda = 3.2
# la probabilità è quindi data da una semplice formula di poisson:
# P(X<=2)= P(X=0) + P(X = 1) + P(X = 2)
#

lambda_valore = 3.2
print(np.exp(-lambda_valore)*(lambda_valore**0/factorial(0))+np.exp(-lambda_valore)*(lambda_valore**1/factorial(1))+np.exp(-lambda_valore)*(lambda_valore**2/factorial(2)))


lambda_valore = 5
print(np.exp(-lambda_valore)*(lambda_valore**0/factorial(0))+np.exp(-lambda_valore)*(lambda_valore**1/factorial(1))+np.exp(-lambda_valore)*(lambda_valore**2/factorial(2)))

lambda_valore = 5
n = 5
p_x_4 = np.exp(-lambda_valore)*(lambda_valore**4/factorial(4))
print(p_x_4)
print(binom(n, 3)*p_x_4**3*(1-p_x_4)**(n-3))

import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
from scipy.special import binom, factorial
from scipy.stats import binom as binom_dist
from scipy.stats import norm, poisson

## ---------------------------
#  Esercizio 11
## ---------------------------
#
# In questo esercizio viene utilizzato il teorema di Bayes, perchè l'esercizio chiede
# data una popolazione con \lambda = 3, viene sviluppato un nuovo farmaco che abbassa
# lambda da 3 a 2, con probabilità del 75%, qual'è la probabilità che se non ho preso
# il raffreddore in un anno allora il farmaco ha fatto effetto?
#
# Per farlo bisogna fare ricorso alla probabilità condizionata e al teorema di Bayes
# che dice che la probabilità di A condizionata su B è P(A|B) = P(A) * P(B|A) / P(B)
#
# Nel nostro caso abbiamo che P(E|S) = (P(S|E) * P(E))/ (P(S|E) * P(E) + P(S|N) * P(N))
# Dove P(S|E) = P(X = 0|\lambda = 2)
# Dove P(S|N) = P(X = 0|\lambda = 3)
# Dove P(E) = 0.75
# Dove P(N) = 0.25
# quindi resta solo che calcolare il tutto come:
#

print(poisson.pmf(0, 2) * 0.75 / (poisson.pmf(0, 2) * 0.75 + poisson.pmf(0, 3) * 0.25))

## ---------------------------
#  Esercizio 12
## ---------------------------
#
# In questo esercizio viene chiesto, sulla base dei morti annuali degli 80 anni
# del secolo scorso di capire le settimane in cui il numero di morti è maggiore
# o uguale a 130 morti e un'altra richiesta minore o uguale a 100 morti.
#
# Per farlo bisogna utilizzare la stima tramite Phi
#
# P(X >=130) = 1 - Phi(0.684)
#
print(1 - norm.cdf(0.684))

# P(X <= 100) = Phi(0.684)

Z = (99.5 - 121.95) / 11.04
print("Z =", Z)
print(norm.cdf(Z))

## ---------------------------
#  Esercizio 12
## ---------------------------
#
# Un semplice esercizio di applicazione della distribuzione normale
#
# \sigma = 6
# \mu = 10

print(1 - norm.cdf((-(5 / 6))))
print(norm.cdf(1) - norm.cdf(-1))
print(norm.cdf(-1 / 3))
print(norm.cdf(5 / 3))
print(1 - norm.cdf(1))
print(norm.cdf(0.0050 / 0.0030) - norm.cdf(-0.0050 / 0.0030))

print(2000 + norm.ppf(0.05) * 85)

print(1 - stats.norm.cdf((25 - 22) / 12.869))

## ---------------------------
#  Esercizio 12
## ---------------------------
#
# Uno stabilimento ha 6 macchinari che usano in media energia elettrica per 20 minuti ogni ora.
# Se i macchinari vengono usati indipendentemente, mostrare che la probabilit`a che 4 o pi`u mac-
# chinari usino energia elettrica contemporaneamente `e 0.1.

prob = 20 / 60
n = 60

print(binom(6, 4) * prob**4 * (1 - prob) ** 2)
print(binom(6, 5) * prob**5 * (1 - prob) ** 1)
print(prob**6)
print(
    binom(6, 4) * prob**4 * (1 - prob) ** 2
    + binom(6, 5) * prob**5 * (1 - prob) ** 1
    + prob**6
)

# Se lo stabilimento avesse 60 macchinari, quale sarebbe la probabilit`a di avere al massimo 30
# macchinari in funzione contemporaneamente?

print(np.exp(-20) * (20**30 / factorial(30)))  # -> molto impreciso

# al posto di usare l'approssimazione di poisson uso quella normale

sigma = np.sqrt((prob * n) * (1 - prob))
mu = n * prob
print(norm.cdf(30, mu, sigma))

# Sempre considerando 60 macchinari trovare un numero approssimato r, tale che la probabilit`a
# che pi`u di r macchinari usino energia elettrica allo stesso tempo sia 0.1.

print(19.5 + 3.65 * (norm.ppf(0.90)))

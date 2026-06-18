import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.stats as stats
from scipy.special import binom, factorial
from scipy.stats import binom as binom_dist
from scipy.stats import poisson

## ---------------------------
#  Esercizio 1
## ---------------------------

# autobus passa ogni 15 minuti, il tipo arriva alla fermata
# tra le 7 e le 7:30, con quanta probabilità l'autobus arriva
# tra 5 minuti?
#
# per farlo bisogna sapere che l'autobus passa ogni 15 minuti, quindi
# 7 - 7:15 - 7:30, quindi i periodi di tempo in cui mettersi ad aspettarlo
# sono 7:10 < x < 7:15 e 7:25 < x < 7:30, per questo motivo con il modello
# uniforme possiamo calcolare questa probabilità, come:
#
# P(7:10 < x < 7:15) + P(7:25 < x < 7:30) = 5/30 + 5/30 = 10/30 = 1/3
#
# poi chiede almeno di 12 minuti, quindi basta fare:
# P(7:00 < x < 7:03) + P(7:15 < x < 7:18) = 3/30 + 3/30 = 6/30 = 1/5

print(10 ** (-7) * (np.exp(15) - np.exp(5)) - 10 ** (-6))
print(1 - stats.norm.cdf(-1))
print(stats.norm.cdf(1) - stats.norm.cdf(-(1 / 4)))
print(1 - stats.norm.cdf(1.5))
print(1 - stats.norm.cdf(2.5))
print(np.sqrt(40))
print(1 - stats.norm.cdf(0.324))

## ---------------------------
#  Esercizio 2
## ---------------------------

# stiamo trattando due eventi indipendenti legati dalla stessa deviazione standard
# e dalla stessa media. Per questo motivo anche all'interno della formula dobbiamo
# trattarli come distinti:
#
# Media: = 12.08 -> 2*12.08 = 24.16
# Deviazione standard: = 3.1 -> 2*(3.1)^2 = sqrt(2*(3.1)^2) = sqrt(19.22) = 4.38
#
# P(X_1 + X_2 > 25) = 1 - P(X_1 + X_2 < 25) = 1 - P(Z < (25-24.16)/4.38))
print(1 - stats.norm.cdf((25 - 12.08) / 3.1))  # di conseguenza questa è sbagliata

print(1 - stats.norm.cdf((25 - 24.16) / 4.38))  # questa invece risulta corretta

print((25 - 24.16) / 4.38)

# il secondo punto richiede invece di trovare la probabilità che l'anno prossimo
# cadano 3 pollici in più di tra due anni, quindi che:
#
# P(X_1 - X_2 > 3)
#
# Questo implica di andare a calcolare il valore atteso e la deviazione standard
# dei due eventi separati e poi andare a sommarli:
#
# \mu_1 = -12.08
# \mu_2 = 12.08
# \sigma_1^2 = 3.1^2 = 9.61
# \sigma_2^2 = 3.1^2 = 9.61
#
# andando a sommare il tutto ottengo:
#
# \mu = 0
# \sigma = sqrt(19.22) = 4.38
#
# li uso nel calcolo della probabilità richiesta e ottengo:
# 1 - stats.norm.cdf((3 - 0) / 4.38)) #
#
print(1 - stats.norm.cdf((3 - 0) / 4.38))

## ---------------------------
#  Esercizio 3
## ---------------------------

##
# In questo esercizio, sui modelli esponenziali, ci viene chiesto di trovare
# la probabilità che, dato il valore atteso di 10 mila miglia e la volontà di
# fare un viaggio di 5 mila miglia, qual'è la probabilità che la batteria non
# ceda e io possa fare il viaggio tranquillo?
#
# Per farlo sappiamo inanzitutto che il valore atteso di un modello esponenziale
# è dato da:
#
# \mu = 1 / \lambda
# e sapendo che per noi \mu = 10 mila miglia allora sappiamo anche che:
# \lambda = 1 / \mu = 1 / 10 = 0.1
#
# di conseguenza possiamo calcolare la probabilità che la batteria non ceda come:
#
# P(X > 5) = \ - P(X <= 5) = 1 - (1 - np.exp(-5*(1/10)))

print(1 - (1 - np.exp(-5 * (1 / 10))))

# trovando così la probabilità richiesta

## ---------------------------
#  Esercizio 4
## ---------------------------

# In questo esercizio ci viene dato la probabilità: 0,6 che un componente funzioni
# ci viene detto quanti componenti ci sono e quanti devono funzionare per considerare
# il sistema in funzione, ovvero almeno 2.
#
# Questo è un classico esercizio di distribuzione binomiale.
#
# Per risolverlo andiamo semplicemente a calcolare la probabilità che la variabile
# aleatoria binomiale assuma un valore maggiore a 2, quindi:
#
# P(X >= 2) = 1 - P(X < 2) = 1 - P(X = 0) - P(X = 1) = ...
#
# con l'applicazione della formula binomiale, quella di scipy.special
# bisogna utilizzare un valore in meno e sempre con il minore o uguale, quindi
# se noi abbiamo che P(X >= 2) nella formula devo scriverlo come P(X <= 1) quindi
# k = 1
#
# Usiamo binom derivato da scipy.special per importare la funzione binomiale
#
p = 0.6
n = 4
k = 1

print(1 - binom(4, 0) * ((1 - p) ** 4) - binom(4, 1) * (p) * ((1 - p) ** 3))
print(1 - stats.binom.cdf(k, n, p))

## ---------------------------
#  Esercizio 5
## ---------------------------

# Ci viene dato qui una stringa di bit che devono essere trasmessi e decodificati,
# n = 5 bit, per decodificarla correttamente, quando viene trasmessa questi bit
# sono 00000 o 11111, e in ricezione prendiamo 1 se la maggioranza dei bit sono 1,
# altrimenti 0. Quindi P(X >= 3) = < - P(X < 3) = P(X > 2)
#
# Per risolverlo utilizziamo due formule, quella estesa e la compressione tramite
# formula in stats.
#

p = 0.8
n = 5
k = 2

print(1 - stats.binom.cdf(k, n, p))
print(
    1
    - (binom(5, 0) * (1 - p) ** 5)
    - (binom(5, 1) * p**1 * (1 - p) ** 4)
    - (binom(5, 2) * p**2 * (1 - p) ** 3)
)

## ---------------------------
#  Esercizio 6
## ---------------------------
#
# In questo esercizio viene chiesto di andare a trovare la probabilità che
# esattamente 7 persone su 10 vadando a votare considerando un'affluenza di 0.7
#
# Quindi:
#
# k = 7
# p = 0.7
# n = 10
#

k = 7
p = 0.7
n = 10

print(binom(10, 7) * 0.7**7 * 0.3**3)
print(binom_dist.pmf(k, n, p))

## ---------------------------
#  Esercizio 7
## ---------------------------
#
# Presentato come problema di eredità di un genotipo, ho un gene che ha r = recessivo
# e d = dominante, i figli prenderanno il gene dominante se avranno rd/dr/dd, quindi
#
# P(d) = P(rd) + P(dr) + P(dd) = 1/4 + 1/4 + 1/4 = 3/4 = 0.75
#
# il campione è dato da n = 4 figli e il numero di figli richiesti con il gene dominante
# è di k = 3 esattamente, quindi:
#
# P(k = 3) = binom(4,3) * 0.75**3*(1-p)**1

p = 0.75
n = 4
k = 3

print(binom_dist.pmf(k, n, p))
print(binom(4, 3) * 0.75**3 * (1 - 0.75) ** 1)

## ---------------------------
#  Esercizio 8
## ---------------------------
#
print(binom(4, 4))

print(-7 / (2.1 / 7 - 1))

## ---------------------------
#  Esercizio 9
## ---------------------------
#
# Approssimazione di poisson della binomiale, per prima cosa bisogna calcolare
# \lambda che è uguale a np, con i valori di n = 10 e p = 0.1 allora \lambda = 1
# poi si calcola normalmente poisson

p = 0.1
n = 10
k = 2
lambda_valore = n * p
print(poisson.pmf(k, lambda_valore))
print(np.exp(-lambda_valore) * lambda_valore**k / factorial(k))

p = 0.1
n = 10
k = 0
lambda_valore = n * p
print(poisson.pmf(k, lambda_valore))
print(np.exp(-lambda_valore) * lambda_valore**k / factorial(k))

p = 0.2
n = 9
k = 4
lambda_valore = n * p
print(lambda_valore)
print(poisson.pmf(k, lambda_valore))
print(np.exp(-lambda_valore) * (lambda_valore**k / factorial(k)))

## ---------------------------
#  Esercizio 10
## ---------------------------
#
# stesso esercizio del 10, ma con una struttura del testo da comprendere

n = 50
p = 0.01
lambda_valore = n * p
k = 1
print(poisson.pmf(k, lambda_valore))
print(np.exp(-lambda_valore) * (lambda_valore**k) / factorial(k))

# P(X >=1) = 1 - P(X <= 0)
n = 50
p = 0.01
lambda_valore = n * p
k = 0
print(1 - poisson.pmf(k, lambda_valore))
print(1 - np.exp(-lambda_valore) * (lambda_valore**k) / factorial(k))

# P(X >=2) = 1 - P(X <= 1)
n = 50
p = 0.01
lambda_valore = n * p
k = 1
print(1 - poisson.pmf(k, lambda_valore) - poisson.pmf(k - 1, lambda_valore))
print(
    1
    - np.exp(-lambda_valore) * (lambda_valore**k) / factorial(k)
    - np.exp(-lambda_valore) * (lambda_valore ** (k - 1)) / factorial(k - 1)
)

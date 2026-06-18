import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.stats as stats
from scipy.special import binom, factorial

# 6 componenti da una cassa di 20 componenti usati
# funziona solamente se i componenti non sono più di 2
#
# se nella cassa vi erano 15 componenti efficienti e 5 guasti, qual'è la pobabilità che il sistema funzioni
#
# P(X = k) = binom(N , k) binom(M, n-k) / (binom(N + M, n))
#
# dove
# N = numero di successi
# M = numero dei fallimenti
# k = valore specifico assunto da X
# n = numero elementi estratti
# X = numero dei successi
#
# Ora io sta roba la devo fare per P(X >= 4) poichè voglio che 4 o più componenti funzionino, quindi
# devo sommare P(X = 4) + P(X = 5) + P(X = 6)
#
# Dove P(X = 4) per esempio è:
#
# P(X = 4) = (binom(15, 4) * binom(5, 6-4)) / (binom(20, 6)))
# e così anche per gli altri cambiano 5 con 5 e la sottrazione con 1 e 0
#

(
    print(
        (binom(15, 4) * binom(5, 6 - 4)) / (binom(20, 6))
        + (binom(15, 5) * binom(5, 6 - 5)) / (binom(20, 6))
        + (binom(15, 6) * binom(5, 6 - 6)) / (binom(20, 6))
    )
)

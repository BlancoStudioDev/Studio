import pandas as pd
from scipy.special import binom, factorial
from scipy.stats import norm

import numpy_es as np

print(binom(20, 2) * 0.05**2 * (1 - 0.05) ** (20 - 2))

print(20 * 0.05)

x_0 = binom(20, 0) * 0.05**0 * (1 - 0.05) ** (20 - 0)
x_1 = binom(20, 1) * 0.05**1 * (1 - 0.05) ** (20 - 1)

print(x_0 + x_1)


## Φ((11 − 10) / 0.436) − Φ((9 − 10) / 0.436)

z1 = (9 - 10) / 0.436
z2 = (11 - 10) / 0.436

prob = norm.cdf(z2) - norm.cdf(z1)
print(z1, z2, prob)

print(binom(8, 2))

print(6 * 6 * 6)

print((binom(5, 2) * binom(7, 2)) / binom(12, 4))

print((1 / binom(12, 12)) * 100)

import matplotlib.pyplot as plt

# Dati
n = 12
k_values = range(0, 13)
y_values = [1 / binom(n, k) for k in k_values]

plt.plot(k_values, y_values, marker="o")
plt.grid(True)


print(factorial(18) / (factorial(4) * factorial(14)))
print(binom(12, 3))

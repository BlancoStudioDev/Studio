import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.stats as stats
from scipy.special import binom, factorial

voti_a = np.array([60, 65, 70, 75, 80, 40])
voti_b = np.array([75, 80, 85, 90, 85, 78])
voti_c = np.array([50, 55, 60, 65, 70, 95])

# plt.figure(figsize=(8, 6))

# plt.boxplot([voti_a, voti_b, voti_c])
# plt.grid(True)
# plt.show()

print("esercizio 1: ", (((binom(9, 2)) * (binom(6, 3))) / binom(15, 5)))

print(
    "esercizio 2: ",
    (
        binom(12, 2)
        * binom(10, 2)
        * binom(8, 2)
        * binom(6, 2)
        * binom(4, 2)
        * binom(2, 2)
    ),
)

print(
    "fine esercizio 2: ",
    ((factorial(6) / (factorial(3) * (2**3))) ** 2)
    * ((factorial(6) * 2**6) / (factorial(12))),
)

print(binom(198, 50) / binom(200, 50))

dati = np.array([1, 2, 3, 4])
print(np.var(dati, ddof=1))

print("valore atteso: ", (np.mean(dati**2) - np.mean(dati) ** 2))

print(((729 / 3) - 324 - (512 / 3 - 256)) + (500 - 333.33 - (405 - (243))))

print(
    "esercizio 3: \n P(X >= 2) = ",
    1 - (binom(10, 0) * ((0.99) ** 10)) - (binom(10, 1) * 0.01**1 * (0.99) ** 9),
)

print((binom(10, 1) * 0.01**1 * (0.99) ** 9))

print(binom(5, 2))

p = 4
n = 12
x = np.arange(1, 20)
# y = binom(n, x) * (p**x) * ((1 - p) ** (n - x))
# plt.bar(x, y)
# plt.show()

y = np.exp(-p) * ((p**x) / (factorial(x)))
plt.figure(figsize=(5, 5))
plt.bar(x, y)
plt.show()

import pandas as pd
from sympy.core.symbol import var

dati = pd.read_csv("punteggi.csv")

print(dati.head())

print(dati.dtypes)

indice = dati[dati["arbitro"] == "A"]["differenza"].mean()
print(indice)

from scipy import stats

diff_A = dati[dati["arbitro"] == "A"]["differenza"]
t_stat, p_value = stats.ttest_1samp(diff_A, popmean=0)

print(f"Media: {diff_A.mean():.4f}")
print(f"P-value: {p_value:.4f}")

# Determinare se è presente un qualche tipo di influenza tra la temperatura e la differenza dei punteggi

import matplotlib.pyplot as plt

x = dati["temperatura"]
y = dati["differenza"]

plt.scatter(x, y)
plt.xlabel("Temperatura")
plt.ylabel("Differenza")
plt.show()

r, p_value_corr = stats.pearsonr(dati["temperatura"], dati["differenza"])

print(f"Correlazione di Pearson (r): {r:.4f}")

# Stabilire se temperatura segue una distribuzione normale

stats.probplot(dati["temperatura"], plot=plt)
plt.show()

# I punteggi dati dagli arbitri sono disomogenei, trovare un indice che consenta di confermare o confutare questa ipotesi (?)

plt.scatter(dati["arbitro"], dati["differenza"])
plt.xlabel("Arbitro")
plt.ylabel("Differenza")
plt.show()

a = dati[dati["arbitro"] == "A"]["differenza"]
b = dati[dati["arbitro"] == "B"]["differenza"]
c = dati[dati["arbitro"] == "C"]["differenza"]

# ANOVA a una via
f_stat, p_anova = stats.f_oneway(a, b, c)

print(f"Media A: {a.mean():.4f}")
print(f"Media B: {b.mean():.4f}")
print(f"Media C: {c.mean():.4f}")
print(f"Statistica F: {f_stat:.4f}")
print(f"P-value: {p_anova:.4f}")


# ============================================================
# ESERCIZIO 4
# Prendendo in considerazione che differenza sia distribuito come Z = X - Y
# ============================================================

print("\n--- ESERCIZIO 4 ---")

# 1. Sapendo che mu_X = 5, calcolare una stima di mu_Y

mu_X = 5
media_diff = dati["differenza"].mean()
mu_Y_stima = mu_X - media_diff

print(f"\n-- Punto 1 --")
print(f"Media campionaria differenza: {media_diff:.4f}")
print(f"Stima di mu_Y = 5 - {media_diff:.4f} = {mu_Y_stima:.4f}")

# 2. Calcolare una stima per sigma_X^2 evidenziando le proprietà dello stimatore

var_diff = dati["differenza"].var(ddof=1)
sigma2_X_stima = var_diff / 2

print(f"\n-- Punto 2 --")
print(f"Varianza campionaria di Z: {var_diff:.4f}")
print(f"Stima di sigma_X^2 = Var(Z) / 2 = {sigma2_X_stima:.4f}")
print(f"Proprietà: stimatore corretto (non distorto) e consistente")

# 3. Calcolare sqrt(sigma_X^2 + sigma_Y^2)

import numpy as np

radice = np.sqrt(var_diff)

print(f"\n-- Punto 3 --")
print(f"sqrt(sigma_X^2 + sigma_Y^2) = sqrt(Var(Z)) = {radice:.4f}")

# 4. Calcolare la probabilità che si verifichi un errore al più di 0.2 nella stima di mu_Y

n = len(dati)
sigma_Z = np.sqrt(var_diff)
errore_massimo = 0.2
z_score = errore_massimo / (sigma_Z / np.sqrt(n))
prob = stats.norm.cdf(z_score) - stats.norm.cdf(-z_score)

print(f"\n-- Punto 4 --")
print(f"P(|errore| <= 0.2) = {prob:.4f} ({prob * 100:.2f}%)")

# 5. Determinare se sono presenti valori nulli in 'differenza'

nulli = dati["differenza"].isnull().sum()
totali = len(dati)

print(f"\n-- Punto 5 --")
print(f"Valori nulli in 'differenza': {nulli} su {totali}")
if nulli > 0:
    print(dati[dati["differenza"].isnull()])
else:
    print("Nessun valore nullo presente.")

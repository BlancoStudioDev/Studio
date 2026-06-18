import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import statsmodels.api as sm
from sqlalchemy.sql import true

esami = pd.read_csv("esami.csv")
print(esami.head())

print("\nValori nulli per colonna:")
print(esami.isnull().sum())

y = esami["mese"].value_counts().sort_index()
x = y.index
plt.bar(x, y)
plt.show()

print(esami["mese"].value_counts().sort_index())

print(esami["mese"].corr(esami["tot_rimborsato"]))

x = esami["mese"]
y = esami["tot_rimborsato"]
plt.scatter(x, y)
plt.show()


esami["inverno"] = esami["mese"].isin([12, 1, 2]).astype(int)
esami["altri"] = esami["mese"].isin([3, 4, 5, 6, 7, 8, 9, 10, 11]).astype(int)

print(
    "\nCorrelazione inverno/tot_rimborsato:",
    esami["inverno"].corr(esami["tot_rimborsato"]),
)

esami.boxplot(column="tot_rimborsato", by="inverno")
plt.show()

esami["estivo_rimborso"] = esami["tot_rimborsato"].isin([12, 1, 2]).astype(int)
esami["altri_rimborso"] = (
    esami["tot_rimborsato"].isin([3, 4, 5, 6, 7, 8, 9, 10, 11]).astype(int)
)

sm.qqplot(esami.mese, line="s")
plt.show()

sm.qqplot(esami[esami.inverno == 0].tot_rimborsato, line="s", fit=True)
plt.show()

sm.qqplot(esami[esami.altri == 0].tot_rimborsato, line="s", fit=True)
plt.show()

esami["a_caso"] = esami["mese"].isin([1, 3]).astype(int)

print(esami["a_caso"])


m = 2


def f(x, m):
    if x < 0 or x > m:
        return 0
    return 2 / m - (2 * x) / (m**2)


def F(x, m):
    if x < 0:
        return 0
    elif x > m:
        return 1
    return (2 * x) / m - (x**2) / (m**2)


x = np.linspace(-1, m + 1, 200)
y = [f(i, m) for i in x]
Y = [F(i, m) for i in x]

plt.plot(x, y)
plt.show()

plt.plot(x, Y)
plt.show()

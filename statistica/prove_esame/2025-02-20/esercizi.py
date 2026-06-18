import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

accessi = pd.read_csv("accessi.csv")

print(accessi.head())

for i in range(4):
    if accessi.iloc[:, i].isnull().sum() > 1:
        print(
            "valori mancanti in colonna",
            i,
            " sono: ",
            accessi.iloc[:, i].isnull().sum(),
        )

print(accessi["allarme"].dtype)

plt.pie(accessi["allarme"].value_counts(), labels=["1", "0"])
plt.show()

print(accessi["allarme"].corr(accessi["carico"]))
x = accessi["carico"]
y = accessi["allarme"]

plt.scatter(x, y)
plt.show()

plt.hist(accessi["richieste"])
plt.show()

richieste = accessi["richieste"].dropna().sort_values()
cdf = np.arange(1, len(richieste) + 1) / len(richieste) * 100
plt.step(richieste, cdf, where="post", color="steelblue", linewidth=2, label="ECDF")
plt.show()

print(richieste.quantile(0.95))

print(pd.crosstab(accessi["allarme"], accessi["richieste"], normalize=True))

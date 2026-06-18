import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("stelle_marine.csv")

print(data.head())

data["profondita"].plot.hist(bins=200)
plt.grid(True)
plt.title("profondita")
plt.show()

data["temperatura"].plot.hist(bins=200)
plt.grid(True)
plt.title("temperatura")
plt.show()

x = data["temperatura"]
y = data["profondita"]

plt.scatter(x, y)
plt.show()

print(data["profondita"].corr(data["temperatura"]))

print(pd.crosstab(index=data["num_braccia"], columns=data["dimensione"]))

data["profondita"].plot.hist(bins=200)
plt.show()

data["temperatura"].plot.hist(bins=30)
plt.show()

x = data["temperatura"]
y = data["profondita"]

plt.scatter(x, y)
plt.show()


print(data["profondita"].corr(data["temperatura"]))

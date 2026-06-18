import matplotlib.pyplot as plt
import numpy_es as np
from pandas._libs.tslibs.nattype import nat_strings

ricchezza_non_ordinata = np.array([50, 10, 100, 20, 5])

# Semplice ordinamento e calcolo della lunghezza

ricchezza = np.sort(ricchezza_non_ordinata)
n = len(ricchezza)

# Calcolo della frequenza cumulativa

F_i = np.array([1, 2, 3, 4, 5]) / n

Q_i = np.cumsum(ricchezza) / np.sum(ricchezza)

R = (2 / (n - 1)) * (np.sum(F_i[:-1] - Q_i[:-1]))

plt.figure(figsize=(7, 7))

plt.plot([0, 1], [0, 1])

plt.plot(F_i, Q_i, marker="o")

plt.show()

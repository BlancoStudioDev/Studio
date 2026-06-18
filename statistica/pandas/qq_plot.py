import matplotlib.pyplot as plt
import scipy.stats as stats

import numpy_es as np

# 1. Generiamo dei dati simulati (all'esame qui caricherai il tuo dataset, es. con pandas)
# Facciamo un dataset con media 24, dev. standard 3, e 1000 studenti
np.random.seed(42)
voti_studenti = np.random.normal(loc=24, scale=3, size=1000)

# Inseriamo un paio di outlier estremi per farti vedere come si "rompe" il grafico
voti_con_outlier = np.append(voti_studenti, [5, 6, 42, 45])

# 2. Creiamo il grafico
fig, ax = plt.subplots(figsize=(8, 6))

# La funzione probplot fa tutto il lavoro per te: calcola i quantili teorici e li plotta.
# 'dist="norm"' gli dice di confrontare i tuoi dati con una Distribuzione Normale Perfetta.
# 'plot=ax' gli dice dove disegnare.
stats.probplot(voti_con_outlier, dist="norm", plot=ax)

# 3. Rendiamo il grafico bello e leggibile (questo fa guadagnare punti extra)
ax.set_title("QQ-Plot: Verifica della Normalità dei Voti")
ax.set_xlabel("Quantili Teorici (Distribuzione Normale)")
ax.set_ylabel("Quantili del nostro Campione")
ax.grid(True, alpha=0.3)

plt.show()

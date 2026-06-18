import numpy_es as np
import pandas as pd

# Dichiarazione dei dati delle recensioni
#
dati_recensioni = np.array(
    ["Buono", "Buono", "Scarso", "Discreto", "Buono", "Scarso", "Buono", "Buono"]
)

# Calcolo della frequenza relativa delle recensioni
# la prima funzione trasforma i dati in una serie di pandas
serie_dati = pd.Series(dati_recensioni)

# la seconda funzione calcola la frequenza relativa delle recensioni
# normalmente se scrivessimo solamente: serie_dati.value_counts() otterremmo_:
#
# Frequenza relativa: Buono       0.625
# Scarso      0.250
# Discreto    0.125
# Name: proportion, dtype: float64
#
# Se usiamo .values otteniamo:
#
# Frequenza relativa: [5 2 1]
#
# E con il normalize=True otteniamo:
#
# Frequenza relativa: [0.625 0.25  0.125]
#
frequenze_relative = serie_dati.value_counts(normalize=True)

print("Frequenza relativa:", frequenze_relative)

gini_assoluto = 1 - (frequenze_relative**2).sum()

print("Indice di gini:", gini_assoluto)

m = len(np.unique(dati_recensioni))

gini_normalizzato = gini_assoluto * (m / (m - 1))

print(f"Indice di Gini Assoluto: {gini_normalizzato:.6f}")

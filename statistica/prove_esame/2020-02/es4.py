## ----------------------
#  Esercizio 4
## ----------------------
#
#
# 1. Quanti casi contiene il dataset?
#

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.stats as stats
import statsmodels.api as sm

car = pd.read_csv("mtcars.csv")

print(len(car))

# 2. Tracciate il boxplot del carattere cilindrata.
#

plt.boxplot(car.cilindrata)
plt.show()

# 3. Qual è o quali sono i modelli di auto che possono essere considerati
# degli outlier rispetto alla cilindrata?
#

media = car.cilindrata.mean()
sigma = car.cilindrata.std()

outlier = (car.cilindrata < (media - 2 * sigma)) | (
    car.cilindrata > (media + 2 * sigma)
)

print(car[outlier][["modello", "cilindrata"]])

# 4. Calcolate i quartili del carattere cilindrata.
#

print(car.cilindrata.quantile(np.arange(0, 1, 0.25)))

# 5. Calcolate la distanza interquartile del carattere cilindrata.
#

print(
    car.cilindrata.quantile(0.75) - car.cilindrata.quantile(0.25),
)

# 5. Tracciate un grafico, diverso dal boxplot, che secondo voi ben rappresenta la
# distribuzione delle cilindrate. Giustificate la vostra scelta
#

car.cilindrata.value_counts().sort_index().plot(kind="bar")
plt.show()

# un istogramma penso possa essere ideale per mostrare i dati delle cilindrate
#

# 6. Tracciate un grafico per controllare se c'è una relazione tra il numero di cilindri e la
# cilindrata dell'auto.
#

plt.scatter(car.cilindrata, car.cilindri)
plt.show()

print(car.cilindrata.corr(car.cilindri))

# la relazione esiste e sembra anche essere abbastanza forte, oltre che essere una relazione diretta
#

# 7. Ispezionando il grafico ottenuto al punto precedente, individuate una relazione tra il
# numero di cilindri e la cilindrata dell'auto?
#
# Già spiegato prima...
#

# 8. Utilizzate il valore di un appropriato indice numerico a supporto della vostra risposta al
# punto precedente.
#
# Già fatto anche questo...

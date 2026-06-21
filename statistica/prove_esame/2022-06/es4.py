# Inizio 17:56
#
## ----------------------
#  Esercizio 4
## ----------------------
#
#
# 1. Memorizzate in due variabili raffreddamento s i e raffreddamento no i valori dell'attributo
# blocchidanneggiati che si riferiscono, rispettivamente, ai casi in cui il sistema di raffreddamento
# automatico è attivato oppure no.
#

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.stats as stats

rilevazioni = pd.read_csv("rilevazioni.csv", sep=";")

raffreddamento_si = (rilevazioni[rilevazioni["raffreddamento"] == 1]).astype(int)
raffreddamento_no = (rilevazioni[rilevazioni["raffreddamento"] == 0]).astype(int)

print(raffreddamento_si)
print(raffreddamento_no)


# 2. Calcolate i decili empirici (i quantili di livello uguale a i per per i = 0 , . . . , 10)
# separatamente per i dati contenuti in raffreddamento_si e raffreddamento_no e disegnate i
# punti le cui ascisse e ordinate corrispondono, rispettivamente, ai valori ottenuti, raggruppati
# per livello. Usate il grafico ottenuto per confermare o confutare l'ipotesi che la distribuzione
# del numero di blocchi danneggiati sia dipendente dal funzionamento del sistema di raffreddamento
# automatico, motivando il vostro ragionamento. Integrate la vostra analisi con altri metodi che
# ritenete opportuni.
#

print(np.quantile(raffreddamento_si.blocchidanneggiati, np.arange(0, 1.1, 0.1)))
print(np.quantile(raffreddamento_no.blocchidanneggiati, np.arange(0, 1.1, 0.1)))

quantili_si = np.quantile(raffreddamento_si.blocchidanneggiati, np.arange(0, 1.1, 0.1))
quantili_no = np.quantile(raffreddamento_no.blocchidanneggiati, np.arange(0, 1.1, 0.1))

plt.scatter(quantili_no, quantili_si)
plt.plot([0, 6], [0, 6], "r--")  # retta y=x come riferimento
plt.xlabel("Decili - raffreddamento OFF")
plt.ylabel("Decili - raffreddamento ON")
plt.show()

fig, ax = plt.subplots()
# frequenze relative
si_freq = raffreddamento_si.blocchidanneggiati.value_counts(normalize=True).sort_index()
no_freq = raffreddamento_no.blocchidanneggiati.value_counts(normalize=True).sort_index()

# 3. Supponendo che i valori contenuti in raffreddamento s i siano assimilabili a un
# campione estratto da una popolazione descritta da una variabile aleatoria Xsi, stimate il valore
# atteso di questultima.
#

print(raffreddamento_si.blocchidanneggiati.mean())


# Punto 4 - raffreddamento_si ~ Poisson?
lambda_si = raffreddamento_si.blocchidanneggiati.mean()
print(f"λ stimato per si: {lambda_si:.2f}")

livelli = np.arange(0, 1.1, 0.1)

# Quantili empirici (dai dati)
q_empirici_si = np.quantile(raffreddamento_si.blocchidanneggiati, livelli)

# Quantili teorici (dalla Poisson)
q_teorici_si = stats.poisson.ppf(livelli, mu=lambda_si)

plt.scatter(q_teorici_si, q_empirici_si)
plt.plot([0, 6], [0, 6], "r--")
plt.xlabel("Quantili teorici Poisson")
plt.ylabel("Quantili empirici")
plt.show()

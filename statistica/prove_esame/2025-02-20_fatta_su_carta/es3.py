## ----------------
#  Esercizio 3
## ----------------
#
#
# 1. Caricate il dataset e memorizzatelo in una variabile `accessi`. Scrivete ed eseguite del codice il cui output indichi quanti
# valori mancanti vi siano per ogni possibile valore dell'attributo `allarme`. Determinate poi quali sono gli attributi del dataset
# per i quali è presente almeno un valore mancante.
#

import matplotlib.pyplot as plt
import numpy as np

import pandas as pd

accessi = pd.read_csv("accessi.csv")

print(accessi.allarme.isnull().sum())

print(accessi.isnull().sum() > 0)

# 2. Indicate il tipo dell'attributo `allarme` e descrivete questo attributo utilizzando la rappresentazione grafica che ritenete
# più adeguata, motivando la scelta fatta.
#

print(accessi.allarme.dtype)
print(accessi.allarme.dropna().value_counts())

plt.pie(accessi.allarme.dropna().value_counts())
plt.legend(["0", "1"])
plt.show()

# 3. Valutate l'ipotesi che il carico di sistema influisca sul sistema che emette gli allarmi, indicando quali strumenti avete
# utilizzato e commentando i risultati ottenuti.
#

print(accessi.carico.dropna().corr(accessi.allarme.dropna()))

plt.scatter(accessi.carico, accessi.allarme)
plt.show()

# la correlazione tra i due fattori non è così forte nonostante comunque sia un pochino presente.
#

# 4. Fissato un generico numero $f$ compreso tra 0 e 100, vogliamo determinare il numero $n$ che rende vera l'affermazione "nell'f%
# dei casi sono arrivate al massimo $n$ richieste". Visualizzate graficamente la distribuzione dell'attributo `richieste` utilizzando
# il tipo di grafico più adeguato per determinare $n$.
#

print(accessi.richieste)

f = 0.95
n = 16

print(
    len(accessi[accessi["richieste"] <= n]) / len(accessi.richieste)
)  ## per determinare f, ora devo fare la formula inversa

print(accessi.richieste.quantile(f))

f = np.arange(0, 1, 0.01)

n = accessi.richieste.quantile(f)

# 5. Usando il grafico generato al punto precedente, determinate il valore di $n$ che
# corrisponde a $f = 95$.
#

plt.step(f, n)
plt.axvline(0.95, color="r")
plt.show()

# 6. Visualizzate la tabella delle frequenze relative congiunte degli attributi
# `richieste` e `allarme`.
#

print(pd.crosstab(accessi.richieste, accessi.allarme, normalize=True))

# 7. Indicando con $A$ l'evento che si verifica quando è stato emesso un allarme e con
# $R$ l'evento che si verifica quando nel periodo di riferimento è stato effettuato almeno
# un accesso al server, usate la tabella ottenuta al punto precedente per stimare le seguenti
# probabilità: i. $\mathbb{P}(R)$, ii. $\mathbb{P}(A \cap R)$, iii. $\mathbb{P}(R \vert A)$,
# iv. $\mathbb{P}(A \vert R)$.
#

print(accessi.allarme.value_counts(normalize=True))

# 9. Validate o confutate l'ipotesi che i valori dell'attributo `richieste` siano assimilabili
# a un campione estratto da una distribuzione normale.
#

x = accessi.richieste.value_counts().index
y = accessi.richieste.value_counts()

plt.hist(accessi.richieste, bins=30)
plt.axvline(accessi.richieste.mean(), color="r")
plt.show()

# graficamente assomiglia a metà tra una poissiana e una normale, più tendente ad una normale però
#

# 10. Calcolate la media campionaria e la varianza campionaria dell'attributo `richieste`, e utilizzate
# i risultati per rispondere alla domanda precedente, considerando ora una distribuzione di Poisson.
#

print(accessi.richieste.mean())
print(accessi.richieste.var())

# direi di si che è proprio una poissiana, nella poissiana il valore atteso e la varianza coincidono
# e qui è palese che essi siano veramente veramente vicini: 9.613240418118467 - 9.650593309129894
#

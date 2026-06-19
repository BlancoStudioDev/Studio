# Inizio 11:34
#
## ----------------------
#  Esercizio 1
## ----------------------
#
# 1. Caricate il dataset e memorizzatelo in una variabile `accessi`. Scrivete ed eseguite del codice il cui output
# indichi quanti valori mancanti vi siano per ogni possibile valore dell'attributo `allarme`. Determinate poi quali
# sono gli attributi del dataset per i quali è presente almeno un valore mancante.
#

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.stats as stats
import statsmodels.api as sm
from scipy.special import binom, factorial

accessi = pd.read_csv("accessi.csv")

print(accessi.allarme.isnull().sum())
print(accessi.isnull().sum())


# 2. Indicate il tipo dell'attributo `allarme` e descrivete questo attributo utilizzando la rappresentazione
# grafica che ritenete più adeguata, motivando la scelta fatta.
#

print("Tipo di allarme: ", accessi.allarme.dtype)

print(accessi.head())

plt.pie(accessi.allarme.value_counts(), labels=["0", "1"])
plt.legend()
plt.show()


# 3. Valutate l'ipotesi che il carico di sistema influisca sul sistema che emette gli allarmi, indicando quali
# strumenti avete utilizzato e commentando i risultati ottenuti.
#

print(accessi.allarme.corr(accessi.carico))

plt.scatter(accessi.allarme, accessi.carico)
plt.show()

# non particolarmente influente, un pochino dal grafico, nel senso che quando l'allarme scatta il carico è mediamente
# più alto, ma il sistema regge il carico anche quando l'allarme non scatta
#


# 4. Fissato un generico numero $f$ compreso tra 0 e 100, vogliamo determinare il numero $n$ che rende vera
# l'affermazione "nell'f% dei casi sono arrivate al massimo $n$ richieste". Visualizzate graficamente la
# distribuzione dell'attributo `richieste` utilizzando il tipo di grafico più adeguato per determinare $n$.
#

richieste = accessi.richieste.dropna().sort_values()
cdf = np.arange(1, len(richieste) + 1) / len(richieste) * 100

plt.step(richieste, cdf)
plt.xline()
plt.show()

# 5. Usando il grafico generato al punto precedente, determinate il valore di $n$ che corrisponde a $f = 95$.
#


# 6. Visualizzate la tabella delle frequenze relative congiunte degli attributi `richieste` e `allarme`.

# 7. Indicando con $A$ l'evento che si verifica quando è stato emesso un allarme e con $R$ l'evento che
# si verifica quando nel periodo di riferimento è stato effettuato almeno un accesso al server, usate la
# tabella ottenuta al punto precedente per stimare le seguenti probabilità: i. $\mathbb{P}(R)$, ii.
# $\mathbb{P}(A \cap R)$, iii. $\mathbb{P}(R \vert A)$, iv. $\mathbb{P}(A \vert R)$.

# 8. Le probabilità che avete stimato al punto precedente devono sommare a uno? Perché?

# 9. Validate o confutate l'ipotesi che i valori dell'attributo `richieste` siano assimilabili a un campione
# estratto da una distribuzione normale.

# 10. Calcolate la media campionaria e la varianza campionaria dell'attributo `richieste`, e utilizzate i
# risultati per rispondere alla domanda precedente, considerando ora una distribuzione di Poisson.

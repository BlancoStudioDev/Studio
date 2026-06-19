## ----------------------
#  Esercizio 3
## ----------------------
#
#
# 1. Scrivete ed eseguite del codice che vi permetta di capire quanti utenti distinti sono contenuti nel
# _dataset_, nonché quali siano gli attributi per i quali vi sono dei valori mancanti.
#

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.stats as stats
import statsmodels.api as sm

banking = pd.read_csv("banking.csv")

print(len(banking.utente.dropna()))

print(banking.isnull().sum())

# 2. Valutate l'ipotesi che i valori dell'attributo _minuti_ possano essere assimilati a un campione estratto
# da una popolazione distribuita secondo un modello normale, spiegando il vostro ragionamento.
#

sm.qqplot(banking.minuti)
plt.show()

# non segue manco per il cazzo una distribuzione normale, ha 3 soddidivisioni, tre campane
#

# 3. Visualizzate graficamente l'attributo _minuti_, motivando il tipo di visualizzazione che avete scelto e
# commentate il risultato ottenuto anche alla luce di quanto emerso al punto precedente.
#
# Stessa identica cosa di prima...
#

plt.hist(banking.minuti, bins=300)
plt.show()

# 4. Valutate l'ipotesi che vi sia una relazione tra gli attributi _minuti_ e _illecito_, specificando eventualmente
# di che tipo è la relazione determinata. Quali strumenti avete utilizzato per valutare questa ipotesi? Perché?
#

print(banking.minuti.corr(banking.illecito))

plt.scatter(banking.minuti, banking.illecito)
plt.show()

# 5. Descrivete l'attributo _tentativi_ utilizzando la rappresentazione grafica che ritenete più adeguata,
# motivando la scelta fatta e commentando i risultati ottenuti.
#

plt.bar(
    banking.tentativi.value_counts(normalize=True).index,
    banking.tentativi.value_counts(normalize=True),
)
plt.show()

# 6. I risultati ottenuti ai punti precedenti dovrebbero suggerire l'esistenza di due diverse tipologie di accessi
# al sito di home banking, discriminate dal valore dell'attributo _illecito_. Memorizzate in una variabile `dati_illeciti`
# tutti i casi del dataset che si riferiscono agli accessi di tipo illecito, e visualizzate graficamente la distribuzione
# dei corrispondenti valori dell'attributo _tentativi_.
#

dati_illeciti = banking[banking["illecito"] == 1]

plt.bar(
    dati_illeciti.tentativi.value_counts(normalize=True).index,
    dati_illeciti.tentativi.value_counts(normalize=True),
)
plt.show()

# 7. Sulla base dei risultati ottenuti nel punto precedente, considerate separatamente ognuno dei seguenti modelli di distribuzione, specificando se (e perché) si tratta di modelli ragionevoli per i valori memorizzati nella variabile `dati_illeciti`:

# - il modello esponenziale,
# - il modello gaussiano,
# - il modello geometrico,
# - il modello uniforme discreto.
#
# sempre geometrico
#

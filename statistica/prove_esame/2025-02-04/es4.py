## ----------------------
#  Esercizio 1
## ----------------------
#
#
# 1. Create un DataFrame che contenga il dataset memorizzato nel file ztl.csv, e
# memorizzatelo in una variabile `ztl`. Determinate quanti valori mancanti vi siano
# nel dataset per ogni possibile valore dell’attributo categoria.
#

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.stats as stats
import statsmodels.api as sm

ztl = pd.read_csv("ztl.csv", sep=";")

print(ztl.categoria.isnull().sum())

print(ztl.isnull().sum())

# 2. Indicate il tipo dell’attributo `passaggi`, e visualizzate successivamente la sua
# distribuzione, motivando la scelta dello strumento grafico utilizzato.
#

print(ztl.passaggi.dtype)

print(ztl.head())

plt.hist(ztl.passaggi, bins=30)
plt.show()

# 3. Valutate se l’attributo `passaggi` contenga o meno dei valori fuori scala, rimuovendoli
# nel caso in cui ve ne siano.
#

print(len(ztl.passaggi))

media = ztl.passaggi.mean()
std = ztl.passaggi.std()

# Filtro in un colpo solo
ztl_n = ztl[(ztl.passaggi > media - 3 * std) & (ztl.passaggi < media + 3 * std)]

plt.hist(ztl_n.passaggi, bins=30)
plt.show()

# 4. Confrontate le tabelle delle frequenze relative cumulative per gli attributi
# `abbonamento` e `altamente-inquinante`.
#

print(pd.crosstab(ztl_n.abbonamento, "", normalize=True))

print(pd.crosstab(ztl_n.inquinante, "", normalize=True))

print(
    pd.crosstab(
        ztl_n.inquinante,
        ztl_n.abbonamento,
        normalize=True,
        margins=True,
    )
)

# 5. Supponete che i valori degli attributi `abbonamento` e `altamente-inquinante` possano
# essere interpretati come due campioni (allineati caso per caso) estratti da due popolazioni,
# ognuna descritta da una variabile aleatoria. Sulla base del confronto effettuato al punto
# precedente, validate oppure rifiutate l’ipotesi che queste due variabili siano i.i.d.
#

# sono identicamente individualmente divise, poichè non vi è una correlazione di nessun tipo tra
# le due variabili:
#

print(ztl_n.abbonamento.corr(ztl_n.inquinante))

plt.scatter(ztl_n.abbonamento, ztl_n.inquinante)
plt.show()

# 6. tutti i dati che potrebbero far pensare a una correlazione tra le due variabili aleatorie in realtà
# hanno un riscontro negativo e portano l'insieme dell'analisi ad un risultato certamente opposto ad
# una correlazione
#

# Il grafico ottenuto utilizzando un diagramma-quantile permette di confermare la conclusione
# alla quale siete arrivati al punto precedente? Perché?
#
# Il diagramma quantile, o qqplot, possiamo provare ad utilizzarlo, ma farebbe comunque schifo, nel semso
# che comunque otterremmo, essendo i valori dei booleani, un grafico con 4 punti nello spazio e basta
#

# 7. Valutate se esista una relazione tra gli attributi `abbonamento` e `passaggi`, utilizzando sia
# uno strumento grafico che un indice numerico (e specificandone motivazione). In caso affermativo,
# descrivetene le caratteristiche nel dettaglio. Nel particolare caso che stiamo considerando, potreste
# dire che uno dei due attributi è più informativo rispetto all’altro? Perché?
#

print(ztl_n.abbonamento.corr(ztl_n.passaggi))

plt.scatter(ztl_n.abbonamento, ztl_n.passaggi)
plt.show()

# Sicuramente più alta che prima, ma anche in questo caso non fortissima...
#

# 8. Salvate in una nuova variabile `ztl_giornalieri` solo i casi del dataset che non corrispondono
# agli ingressi fatti con abbonamento. **Lavorare per il resto dell'esame con questo nuovo dataset**.
#

ztl_giornalieri = ztl_n[ztl_n["abbonamento"] == 1]

print(ztl_giornalieri.head())

# 9. Verificare che non esista nessun caso nel dataframe con `passaggi` dispari
#

if (ztl_giornalieri.passaggi % 2 != 0).any():
    print("ci sono dei passaggi dispari")
else:
    print("sono tutti passaggi pari")

# 10. Validare l'ipotesi che `passaggi` contenga dei valori assimilabili ad un campione estratto da una popolazione la cui distribuzione sia la stessa della variabile aleatoria $Z$ dell'esercizio 1.

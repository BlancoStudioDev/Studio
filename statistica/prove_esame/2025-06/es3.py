## --------------------
#  Esercizio 3
## --------------------
#
# Il file esami.csv contiene le seguenti informazioni, raccolte dal reparto di analisi dei dati del centro medico e che
#  descrivono un campione di osservazioni relativame all'esame sul quale ci siamo concentrati finora.
# ⚫ mese: mese di riferimento, indicato come numero che va da uno (gennaio) a dodici (dicembre);
# ⚫ tot_pagato: somma totale incassata dal centro medico nel mese di riferimento, relativa agli utenti che hanno pagato
#    l'esame di tasca propria;
# ⚫ tot_rimborsato: rimborso totale che il sistema sanitario nazionale ha inviato al centro medico nel mese di riferimento.
# In questo file , il carattere, separa le colonne.
#
#
# 1. Scrivete ed eseguite del codice che visualizzi su righe differenti il nome di ogni attributo unitamente al
# corrispondente numero di valori mancanti.
#

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.stats as stats
import statsmodels.api as sm

esami = pd.read_csv("esami.csv")

print(esami.isnull().sum())

# 2. Di che tipo è l'attributo mese? Sulla base della risposta data, visualizzate la distribuzione di questo
# attributo fornendo sia una formulazione tabulare, sia un grafico, motivando le vostre scelte.
#

print("Il tipo della variabile mese è: ", esami.mese.dtype)

plt.bar(esami.mese.unique(), esami.mese.value_counts())
plt.show()

print(esami.mese.value_counts().sort_index())

# 3. Commentate i risultati ottenuti al punto precedente.
#
# che devo commentare, belli
#

# 4. Spiegate perché ha senso valutare l'ipotesi che vi sia una relazione tra gli attributi mese e tot_rimborsato.
# Procedete poi con questa valutazione, motivando la scelta degli strumenti utilizzati e indicando eventualmente
# il tipo e la forza della relazione determinata.
#

plt.scatter(esami.mese, esami.tot_rimborsato)
plt.xlabel("Mesi dell'anno")
plt.ylabel("Rimborso in euro")
plt.show()


print(esami.mese.corr(esami.tot_rimborsato))

# correlazione non altissima, ma perchè non è presente su tutti i mesi, bensì solamente su quelli invernali e non su
# quelli estivi, leggendo dal grafico si può vedere che il rimborso è più alto
#

# 5. Gli esperti del centro medico sospettano che l'esame in questione venga rimborsato soprattutto nei mesi invernali
# (dicembre, gennaio e febbraio). Per verificare questa ipotesi, aggiungete al dataset un attributo inverno che vale 1
# per i casi che corrispondono ai mesi invernali e 0 altrimenti, e verificate l'esistenza di una relazione tra questo
# nuovo attributo e tot_rimborsato, evidenziando i caratteri della relazione determinata
#

esami["inverno"] = ((esami.mese == 1) | (esami.mese == 12) | (esami.mese == 2)).astype(
    int
)

print(esami.inverno)

print(esami.tot_rimborsato.corr(esami.inverno))

plt.scatter(esami.inverno, esami.tot_rimborsato)
plt.xlabel("Mesi dell'anno")
plt.ylabel("Rimborso in euro")
plt.show()

# questo ci consente di vedere sia con la correlazione di Pearson che con il grafico che esiste una correlazione tra le due cose

# 6. Verificate se l'ipotesi che i valori di tot rimborsato siano assimilabili a un campione estratto da una distribuzione normale,
# analizzando prima tutti i casi del dataset, poi solo quelli che fanno riferimento ai mesi invernali e infine solo quelli che fanno
# riferimento ai mesi rimanenti. Commentate i risultati ottenuti alla luce di quanto visto nel punto precedente e nell'ultimo punto
# del primo esercizio.p
#

plt.hist(esami.tot_rimborsato, bins=30)
plt.show()

sm.qqplot(esami.mese)
plt.show()

esami["altri"] = (
    (esami.mese == 3)
    | (esami.mese == 4)
    | (esami.mese == 5)
    | (esami.mese == 6)
    | (esami.mese == 7)
    | (esami.mese == 8)
    | (esami.mese == 9)
    | (esami.mese == 10)
    | (esami.mese == 11)
).astype(int)

sm.qqplot(esami[esami["inverno"] == 1].tot_rimborsato)
plt.show()

sm.qqplot(esami[esami["altri"] == 1].tot_rimborsato)
plt.show()

## --------------------
#  Esercizio 4
## --------------------
#
#
# 1. Scrivete ed eseguite del codice che visualizzi su righe differenti il nome di ogni attributo
# unitamente al corrispondente numero di valori mancanti.
#

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.stats as stats

risultati = pd.read_csv("risultati.csv")

print(risultati.isnull().sum())

# 2.  Di che tipo è l'attributo tempo ? Sulla base della risposta data, visualizzate la
# distribuzione di questo attributo, motivando la scelta dello strumento grafico utilizzato.
#

print(risultati.tempo.dtype)

plt.hist(risultati.tempo, bins=300)
plt.show()

# 3. Considerate l'attributo punteggio , e ripetete l'analisi svolta al punto precedente,
# valutando se debba essere fatta nello stesso modo oppure se debba essere utilizzato
# uno strumento diverso.
#

print(risultati.punteggio.dtype)

plt.hist(risultati.punteggio, bins=30)
plt.show()

# per il precedente l'analisi si poteva fare anche tramite bar come grafico andando ad utilizzare
# i value counts e gli indici, ma per questo è meglio un istogramma e non altro perchè i dati sono
# troppo dispersi.
#

# 4. Valutate l'ipotesi che vi sia una relazione tra gli attributi punteggio ed eta , specificando
# eventualmente il tipo e la forza della relazione determinata. Quali strumenti avete utilizzato
# per valutare questa ipotesi? Perché?
#

print(risultati.punteggio.corr(risultati.eta))

plt.scatter(risultati.punteggio, risultati.eta)
plt.show()

# sia il grafico che l'indice di pearson sono entrambi concorci nel dire che la relazione tra i due attributi
# è inesistente.
#

# 5. Gli esperti del centro di formazione sospettano che l'attributo punteggio dovrebbe sia ben descritto
# da una distribuzione analoga a quella studiata nell'Esercizio 1. Scegliete uno strumento che ha senso
# utilizzare per validare questa ipotesi ed applicatelo, commentando i risultati ottenuti.
#
#
# beh disegnamo entrambi i grafici, sia di punteggio che della relazione 1 e vediamo, io non penso
# proprio che questo possa essere simile, ma vediamo.
#

x = np.arange(0, 100)
y = x / 55

plt.plot(x, y)
plt.hist(risultati.punteggio, bins=30)
plt.show()

# non so non mi sembra che seguano la stessa distribuzione....

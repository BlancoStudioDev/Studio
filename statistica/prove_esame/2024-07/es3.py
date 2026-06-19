## ----------------------
#  Esercizio 3
## ----------------------
#
# 1. Scrivete ed eseguite del codice che visualizzi su righe differenti il nome di ogni attributo unitamente al
# corrispondente numero di valori mancanti.
#

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.stats as stats

risultati = pd.read_csv("risultati.csv")

print("I dati mancanti sono i seguenti: \n", risultati.isnull().sum())

# 2. Di che tipo è l'attributo tempo ? Sulla base della risposta data, visualizzate la distribuzione di questo
# attributo, motivando la scelta dello strumento grafico utilizzato.
#

print("l'attributo di tempo è: ", risultati.tempo.dtype)

print(risultati.head())

plt.hist(risultati.tempo, bins=200)
plt.show()

# 3. Considerate l'attributo punteggio , e ripetete l'analisi svolta al punto precedente, valutando se debba
# essere fatta nello stesso modo oppure se debba essere utilizzato uno strumento diverso.
#

print("l'attributo di tempo è: ", risultati.punteggio.dtype)

plt.hist(risultati.punteggio, bins=100)
plt.show()

# 4. Valutate l'ipotesi che vi sia una relazione tra gli attributi punteggio ed eta , specificando
# eventualmente il tipo e la forza della relazione determinata. Quali strumenti avete utilizzato per valutare
# questa ipotesi? Perché?
#

print(risultati.punteggio.corr(risultati.eta))

plt.scatter(risultati.punteggio, risultati.eta)
plt.show()

# non c'è nessun tipo di relazione.. ne dal grafico ne dalla formula di pearson....

# 5. Gli esperti del centro di formazione sospettano che l’attributo punteggio dovrebbe sia ben
# descritto da una distribuzione analoga a quella studiata nell’Esercizio 1. Scegliete uno stru-
# mento che ha senso utilizzare per validare questa ipotesi ed applicatelo, commentando i
# risultati ottenuti.
#

a = int(risultati.punteggio.max())

# 2. Definisci la x solo nel dominio corretto (da 1 a a)
x = np.arange(1, a + 1)
y = (2 * x) / (a * (a + 1))

# 3. Disegna l'istogramma e la retta corretta
plt.hist(risultati.punteggio, density=True, bins=a, edgecolor="black", alpha=0.7)
plt.plot(x, y, color="red", linewidth=2, label="Teorica")
plt.legend()
plt.show()

# ma si sono ubriacati gli esperti?

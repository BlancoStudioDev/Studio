# Inizio 17:23
#
## ----------------------
#  Esercizio 3
## ----------------------
#
#
# 1. Scrivete ed eseguite del codice il cui output indichi quanti casi sono contenuti nel dataset,
# quanti casi contengono almeno un valore mancante e quali sono gli attributi per i quali è presente
# almeno un valore mancante.
#

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.stats as stats

rilevazioni = pd.read_csv("rilevazioni.csv", sep=";")

print(len(rilevazioni.dropna()))

print(rilevazioni.isnull().sum())

# 2. Descrivete l'attributo raffreddamento utilizzando la rappresentazione grafica che ritenete
# più adeguata, motivando la scelta fatta e commentando i risultati ottenuti.
#

plt.hist(rilevazioni.temperatura, bins=40)
plt.show()

plt.boxplot(rilevazioni.temperatura)
plt.show()

print(rilevazioni.temperatura.mean())

# 3. Valutate l'ipotesi che la temperatura influisca sull'accensione del sistema automatico
# di raffreddamento, commentando i risultati ottenuti. Quali strumenti avete utilizzato per
# valutare questa ipotesi? Perché?
#

print(rilevazioni.temperatura.corr(rilevazioni.raffreddamento))

plt.scatter(rilevazioni.raffreddamento, rilevazioni.temperatura)
plt.show()

# i due attributi non hanno niente in correlazione l'uno con l'altro

# 4. Visualizzate graficamente l'attributo blocchidanneggiati (tenendo presente il tipo
# di questo attributo), commentando i risultati ottenuti e giustificando la scelta
# del tipo di grafico realizzato.
#

plt.bar(
    rilevazioni.blocchidanneggiati.dropna().value_counts().index,
    rilevazioni.blocchidanneggiati.dropna().value_counts(),
)
plt.legend()
plt.show()

# 5. Generate una tabella che mostri le frequenze congiunte degli attributi blocchidanneggiati
# e raffreddamento. Indicando con R l'evento che si verifica quando il sistema di raffreddamento
# automatico è stato attivato durante un'ora e con D l'evento che si verifica quando in un'ora
# risultano danneggiati dei blocchi del disco fisso, usate la tabella generata per calcolare
# le seguenti probabilità: i. P(D), ii. P(R inter D), iii. P(D|R), iv. P(R|D).
# Le probabilità che avete calcolato d e v o n o s o m m a r e a u n o ? P e r c h é ?
#

print(pd.crosstab(rilevazioni.blocchidanneggiati, rilevazioni.raffreddamento))

# D = tutte le volte che si è verificato un danno
# R = tutte le volte che si è attivato l'allarme
#
# Quindi P(D) vuol dire che ho la probabilità su tutti di beccare proprio P(D > 0) = 1 - P(D <= 0) =
# quindi 1 - 946/(434 + 200 + 94 + 37 + 8 + 3 + 946) =  0.4506 = 45,06% delle volte
#
# P(R inter D) = (253+34+5)/1722 = 0.1696
#
# P(D|R) = P(D inter R)/P(R) = 0.1696/((830+253+34+5)/1722) = 0.2602
#
# P(R|D) = P(R inter D)/P(D) = 0.1696/(0.4506) = 0.3763

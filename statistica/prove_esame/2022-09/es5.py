# Inizio 15:37
#
## ----------------------
#  Esercizio 5
## ----------------------
#
#
# In questo esercizio interpreteremo i valori dell'attributo bottiglie_acquistate come un
# campione casuale estratto da una popolazione distribuita come la variabile aleatoria C_tot
# definita nell'esercizio 3, e i valori dell'attributo ricavo come un campione casuale estratto
# da una popolazione T.
#
# 1. Stimate il valore atteso della popolazione descritta dalla variabile aleatoria C_tot ,
# indicando la dimensione del campione utilizzato e specificando eventuali proprietà dello
# stimatore utilizzato
#
#

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.stats as stats
import statsmodels.api as sm
from scipy.special import binom

acquisti = pd.read_csv("acquisti.csv")

print("Dimensione: ", len(acquisti.bottiglie_acquistate.dropna()))

print("Media campionaria: ", acquisti.bottiglie_acquistate.dropna().mean())


# 2. Stimate la deviazione standard della popolazione descritta dalla variabile aleatoria C_tot ,
# specificando eventuali proprietà dello stimatore utilizzato. La dimensione del campione
# utilzzato è la stessa del punto precendete? Perchè?
#

print("Deviazione standard: ", acquisti.bottiglie_acquistate.dropna().std())

# certo che è la stessa dimensione del campio, cazzo è la campio tra un es e l'altro?
#

# 3. Il magazzino del distributore riceve ogni settimana 3600 bottiglie. Come potete indicare,
# in funzione di un'appropriata quantità precedentemente utilizzata, l'evento E che si
# verifica se queste bottiglie non sono sufficienti a soddisfare la domanda dei clienti?
#

sigma = acquisti.bottiglie_acquistate.dropna().std()
mu = acquisti.bottiglie_acquistate.dropna().mean()

print(1 - stats.norm.cdf((3600 - mu) / sigma))

# 4. Sulla base del risultato del punto 8 dell'esercizio 4, calcolate la probabilità dell'evento E
# desritto al punto precedente.
#
# già fatto, ma poi che cazzo me ne frega che sia normale, tanto per forza sto esercizio devo farlo così...
#

# 5. Stimate il valore atteso della popolazione T , indicando quale stimatore avete utilizzato.
#
# E[T] = p*p_C*n_C - s*n_R*P_R, adattato con i dati che ho adesso... ovvero un cazzo
#

acquisti["ricavo"] = acquisti.bottiglie_acquistate * 1 - acquisti.bottiglie_rese * 0.1

print("Stimatore di merda (con media campionaria): ", acquisti.ricavo.mean())

# 6. Siete in grado di calcolare la probabilità che la stima fatta al punto precedente disti, per
# eccesso o per difetto, più di 10€ rispetto al valore sconosciuto?
#
# dobbiamo metterla giù nel seguente modo: P(|valore - \mu| > epsilon) = 1 - P(|valore - \mu| <= epsilon)
# 1 - (2*phi(10/(sigma/np.sqrt(n))) - 1) = 2 - 2*phi(10/(sigma/np.sqrt(n))
#

print(
    2
    - 2
    * stats.norm.cdf(
        10 / (acquisti.ricavo.dropna().std() / len(acquisti.ricavo.dropna()))
    )
)


# INIZIO DELLA PROVA 14:09, fine della prova 15:55 -> quindi tempo totale di 1 ora e 45/50 minuti più o meno
#

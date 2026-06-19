## ----------------------
#  Esercizio 1
## ----------------------
#
#
# In questo esercizio considereremo una popolazione 𝑋 la cui distribuzione è la stessa dell’omonima
# variabile aleatoria introdotta nell’esercizio precedente, dove 𝑎 rappresenterà un parametro ignoto.
# Per 𝑛 ∈ ℕ fissato, 𝑋1, … , 𝑋𝑛 indicheranno delle variabili aleatorie che descrivono un campione
# estratto da 𝑋.

# 1. Dimostrate che la media campionaria è uno stimatore distorto per il parametro 𝑎.
#
# Per dimostrare questa cosa dobbiamo andare semplimente a svolgere il valore atteso della
# media campionaria, vendendo fuori che il valore atteso è (2a+1)/3 e non coindicendo con a
# allora sarà distorto questo stimatore.
#

# 2. Calcolate il bias e lo scarto quadratico medio di 𝑋 rispetto ad 𝑎, esprimendoli solo in funzione
# di 𝑛 e 𝑎.
#
# Calcolato e viene MSE(T) = Var(\bar(T)) + bias(\tau(\theta))^2 = (a^2+a-2)/18n + (a^2-2a+1)/9
#

# 3. La media campionaria gode della proprietà di consistenza in media quadratica se la utilizziamo
# per stimare 𝑎? Motivate la vostra risposta.
#
# No non gode della proprietà di consistenza in media quadratica perchè se faccio tendere tutto a infinito ottengo:
# (a^2-2a+1)/3, diverso da 0 e quindi non ha la proprietà.
#

# 4. Supponete, solo in questo punto, che 𝑎 = 10. Scrivete ed eseguite del codice che mostri
# l’andamento dello scarto quadratico medio ottenuto al punto precedente al variare di 𝑛.
#

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.stats as stats

a = 10

x = np.arange(1, 100)
y = (a**2 + a - 2) / (18 * x) + (a**2 - 2 * a + 1) / 9

plt.plot(x, y)
plt.ylabel("MSE Graph")
plt.show()

# 5. Applicando il metodo plug-in, determinate uno stimatore 𝑇 che sia non distorto per 𝑎.
#
# Con il metodo plugin posso semplicemente andare a dire che E[\bar(X)] deve essere uguale ad a, quindi con formula
# invera trovo che a = E[3/2 * \bar(X) - 1]
#

# 6. Utilizzando il teorema centrale del limite, determinate la distribuzione approssimata dello
# stimatore 𝑇 che avete ottenuto al punto 5.
#
# Per determinare la distribuzione possiamo dire inizialmente che N(E[\bar(X)], Var(\bar(X)))
#
# quindi che N ((2a+1)/3, np.sqrt((a^2 + a -2)/18)), da cui possiamo anche dire che il valore atteso che abbiamo
# è il valore atteso di a, quindi  N (a, np.sqrt((a^2 + a -2)/18)) per quando riguarda la varianza invece dobbiamo
# calcolarla per Var(T) = Var((3\bar(X) - 1)/2) = 9/4(Var(\bar(X))) = 9/4(a^2 + a -2)/18n) = (a^2 + a -2)/8n) quindi
# infine N (a, np.sqrt((a^2 + a -2)/8n)))
#

# 7. Calcolate la probabilità dell’evento che si verifica quando l’errore (in valore assoluto) che si
# compie usando 𝑇 per stimare 𝑎 sia minore o uguale di 1, esprimendola in funzione di 𝑎, 𝑛
# e della funzione di ripartizione della distribuzione normale standard, giustificando i vostri
# passaggi e indicando eventuali approssimazioni che è necessario introdurre.
#
# Per farlo andiamo ad utilizzare la semplice regola che P(|X - \mu| <= \epsilon) = P(-\epsilon <= X - \mu <= \epsilon) =
# = 2\phi(\epsilon/sigma) - 1 con sigma = np.sqrt((a^2 + a -2)/8n)), quindi P(|X - \mu| <= \epsilon) =
# = 2\phi(\epsilon/(np.sqrt((a^2 + a -2)/8n)))) - 1 -> \epsilon = 1

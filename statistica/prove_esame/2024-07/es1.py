## ----------------------
#  Esercizio 1
## ----------------------
#
# 1. In questo esercizio considereremo la funzione
# 𝑓(𝑥) = 𝐾𝑥I{1,…,𝑎}(𝑥),
# dove I𝐴 denota la funzione indicatrice dell’insieme 𝐴, 𝑎 ∈ ℕ è un parametro della funzione e 𝐾 è
# una costante moltiplicativa.
#
# 1. Determinate il valore di 𝐾 espresso come sola funzione di 𝑎, che rende 𝑓 una funzione di
# massa di probabilità.
#
# Per determinare il valore di K basta andare a risolvere, come per le variabili continue con l'integrale, la
# sommatoria della funzione f(x) = Kx ponendola uguale a 1. Andiamo a farlo:
#
# ∑ Kx = K ∑x = K * ((a*(a+1))/2) -> per questo motivo se lo pongo uguale a 1 allora viene che K = 2/(a*(a+1))
#

# 2. Nel resto di questo esercizio indicheremo con 𝑋 una variabile aleatoria avente 𝑓 come funzione
# di massa di probabilità, per un valore ignoto di 𝑎 e nella quale 𝐾 è sostituito con il valore
# determinato al punto precedente. Calcolate il valore atteso di 𝑋, esprimendolo in funzione di
# 𝑎
#
# Allo stesso modo per trovare il valore atteso della nostra variabile aleatoria basta semplicemente moltiplicare
# per x la nostra funzione e poi andare a fare la sommatoria, per questo la sommatoria risulterà: 2/(a*(a+1)) * ∑ x^2
# che in definitiva verrà: (2a+1)/3
#

# 3. Indichiamo con 𝐹 la funzione di ripartizione di 𝑋. Ricavate la forma analitica di 𝐹 (𝑥),
# esprimendola in funzione di 𝑥 e 𝑎.
#
# Per ricavare la funzione analitica di sta roba, come normalmente faremmo integrando con le variabili continue, qui
# andiamo a fare la sommatoria della nostra funzione su x di f(i) -> avendo infine che F(X) = (x*(x+1))/(a*(a+1))
#

# 4. Supponete, solo in questo punto, che 𝑎 = 10. Scrivete ed eseguite del codice che disegni il
# grafico della funzione 𝑓 ottenuta nel punto 1.
#

import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

a = 10

x = np.arange(0, 100)
y = (2 / (a * (a + 1))) * x

plt.plot(x, y)
plt.show()

# 5. Il grafico che avete ottenuto al punto 4 potrebbe suggerire che 𝑋 segua una distribuzione
# uniforme? Perché? Valutate o refutate questa ipotesi.
#
# ma manco per il cazzo che segue una distribuzione uniforme... è una cazzo di bisettrice 1/3
#

# 6. Calcolate la varianza di 𝑋, esprimendola in funzione di 𝑎.
#
# Per calcolare la varianza si fa: Var(x) = E[x^2] - E[X]^2, sappiamo E[X], ma non E[X^2], quindi calcoliamolo.
# E' quindi uguale a (a^2 + a -2)/18
#

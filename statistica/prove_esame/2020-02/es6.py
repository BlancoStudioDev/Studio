## ----------------------
#  Esercizio 6
## ----------------------
#
#
# Consideriamo ora il carattere trasmissione.
#
# 1. Tracciate un grafico opportuno per descrivere il carattere trasmissime. Giustificate la
# scelta fatta.
#

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.stats as stats

car = pd.read_csv("mtcars.csv")

plt.pie(car.trasmissione.value_counts())
plt.legend(["0", "1"])
plt.show()

# 2. Consideriamo i valori osservati per il carattere trasmissione come la realizzazione cam-
# pionaria di un campione estratto dalla popolazione X' = "tipo di trasmissione". Che legge
# segue la variabile casuale X? Giustificate la risposta
#
# ma che cazzo mi sta chiedendo?
#
# Se mi sta chiedendo che distribuzione segue allora è una bernoulli, se la domanda è un'altra allora non
# l'ho capita...
#

# 3. Stimate il valore atteso di X.
#

print(car.trasmissione.mean())

# 4. Lo stimatore T, che avete utilizzato al punto procedente é non distorto? Giustificate la
# risposta
#
# Si è non distorto, come mostrato anche in altri esercizi precedenti, la media campionaria per
# una distribuzione bernoulliana è non distorto come stimatore
#

# 5. Qual e la taglia n del campione che avete utilizzato per calcolare la stima del valore atteso
# di X?
#
# Se con taglia si intende la dimensione allora è: 32, se no se si intende che tipi di valori possono
# assumere allora p 1 o 0
#

# 6. Calcolate la tabella delle frequenze assolute del carattere trasmissione.
#

print(car.trasmissione.value_counts(normalize=True))

# 7. Stimate la probabilita che un'auto in circolazione in quegli anni avesse trasmissione
# manuale.
#

print(len(car[car["trasmissione"] == 1]) / len(car))

# 8. Lo stimatore che avete utilizzato al punto precedente e non distorto? Giustificate l a
# risposta.
#
# Porco dio ma quale punto, se stiamo ancora parlando della media campionaria no non è distorto
#
# Se si intende se è distorto rispetto al normale andamento della stima delle probabilità per una
# bernoulliana allora no non è distorto, perchè lo stimatore normale di bernoulli dice che
# la probabilità dell'insuccesso è 1 - p, quindi semplicemente 1 - 0.59375 = 0.40625

# 9. Stimate la probabilità che un'auto in circolazione in quegli anni avesse trasmissione
#
# allora a parte che sia questo punto che il 7 si potevano fare benissimo andando a guardarsi la cazzo
# di tabella delle frequenze, ma a parte quello, la probabilità è:
#

print(len(car[car["trasmissione"] == 0]) / len(car))

# 10. Lo stimatore che avete utilizzato al punto procodente e non distorto? Ciustificate la
# risposta.
#
# ma non si capisce per cosa lo devo definire, se per p, se per qualcos'altro, booooo
#
# Se si intende se è distorto rispetto al normale andamento della stima delle probabilità per una
# bernoulliana allora no non è distorto, perchè lo stimatore normale di bernoulli dice che
# la probabilità dell'insuccesso è 1 - p, quindi semplicemente 1 - 0.40625 = 0.59375
#

# 11. Fisato alpha = 0.85, determinate Perore massimo commesso con probabilità maggiore o
# uguale ad alpha, per eccesso o per difetto, nella stima del valore atteso di X. In altre parole
# trovate un valore e tale che P(|X - E(X)| ≤ epsilon) >= alpha
#
# epsilon >= sigma*\phi^-1((alpha+1)/2)
#

print(np.sqrt(((13 / 32 * (1 - 13 / 32)) / 32)) * (stats.norm.ppf((0.85 + 1) / 2)))

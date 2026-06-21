# Inizio 16:35
#
## ----------------------
#  Esercizio 1
## ----------------------
#
#
# Sia X una variabile aleatoria distribuita secondo un modello di Poisson di parametro lambda.
#
# 1. lambda può assumere un valore maggiore di 1? Perché? E può assumere un valore negativo? Perché?
#
# Si certo che può assumere valore maggiore di uno, ma siccome è una distribuzione discreta non è
# per forza limitata. Non può essere negativo per a definizione di lambda che è n*p ovvero la probabilità
# per il numero di eventi, che non potrà mai essere negativo.
#

# 2. Esprimete il valore atteso e la deviazione standard di X in funzione di lambda. Esprimete successivamente
# la varianza di X in funzione del valore atteso di quest'ultima.
#
# E[X] = lambda = Var(X) sigma = np.sqrt(lambda)
#

# 3. Sia Y un'altra variabile aleatoria distribuita come X e da essa indipendente. Dato un generico numero
# naturale x, indichiamo con p(x) la probabilità dell'evento X + Y = x. Esprimente p(x) in funzione
# di lambda e x.
#
# P(X + Y = x), questo vuol dire che lambda = n*p_x + n*p_y = 2*n*p quindi P(X + Y = x) = e^(-2lambda) * (2lambda^x/x!)
#

# 4. Fissiamo, solo in questo punto, lambda = 0.9. Utilizzando il computer visualizzate graficamente
# l'andamento di p(x) al variare di x, scegliendo opportunamente il tipo di grafico da generare e
# motivando la scelta fatta. Come avete scelto il valore massimo per x?
#

import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

lambda_valore = 2 * 0.9

sigma = np.sqrt(lambda_valore)
mu = lambda_valore

x = np.arange(0, np.floor(mu + 3 * sigma) + 1)
y = stats.poisson.pmf(x, lambda_valore)

plt.bar(x, y)
plt.show()

# 5. Date n variabili aleatorie X,...X, indipendenti e identicamente distribuite come X,
# indichiamo con S la somma sommatoria delle X. Che distribuzione segue S?
#
# Io penso proprio segua ancora una distribuzione di poisson, per il semplice fatto che stiamo andando
# a chiederci che distribuzione segue la media campionaria di una variabile aleatoria ripetuta n volte?
# verrebbe n * 1/n X_i quindi X_i quindi la stessa di X_i quindi poissoniana
#

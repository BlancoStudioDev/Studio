## ----------------------
#  Esercizio 1
## ----------------------
#
#
# In questo esercizio supporremo che la password per accedere a un sito di home banking sia composta da cinque
# cifre decimali, e indicheremo con $p$ una prefissata password.

# 1. Calcolate il numero di password distinte.
#
# Numero_password = 10^5
#

Numero_password = 10**5

print("Numero di password: ", Numero_password)

# 2. Calcolate la probabilità che una password estratta uniformemente a caso tra tutte quelle possibili sia uguale a $p$.
#
# P(X = p) = 1/Numero_password = 1/10^5
#

print("Probabilità di ottenere p: ", 1 / Numero_password)

# 3. Calcolate il numero di password distinte che contengono una stessa cifra ripetuta nelle prime tre posizioni.
#
# 1 1 1 x x -> ho la probabilità delle prime 3 cifre, quindi 3*10, e poi la probabilità delle altre due, quindi 10*10**2
#

cifre_inizio = 3 * 10 * 10**2

print("Numero di password con prime tre cifre uguali: ", cifre_inizio)

# 4. Calcolate la probabilità del punto 1., condizionandola al fatto che le cifre nelle prime tre posizioni in $p$ sono
# tutte uguali e scegliendo la password uniformemente a caso tra tutte quelle che hanno le prime tre cifre uguali.
#
# Basta semplicemente andare a fare la probabilità di 1/cifre_inizio
#

print("Probabilità di una password su cifre_inizio: ", 1 / cifre_inizio)

# 5. Calcolate il numero di password distinte che contengono una stessa cifra ripetuta in tre posizioni consecutive.
#
# Questo è l'insieme di più probabilità, in particolare sappiamo che la probabilità di avere:
#
# 1 1 1 x x è 3*10*10^2, ma sappiamo anche che il caso di 1 1 1 1 x che dobbiamo togliere dall'altro e questo può accadere
# sia nell'esempio che ho scritto sia in x 1 1 1 1, quindi 2*10^2 e infine c'è la possibilità di 1 1 1 1 1 che è 1, quindi
# sappiamo che n = 3*10*10^2 - 2*10^2 - 10 + 10 = 2800
#

numero_cifre = 3 * 10 * 10**2 - 2 * 10**2 - 10 + 10

print("N: ", numero_cifre)

# 6.Calcolate la probabilità analoga a quella del punto 4, rimuovendo la richiesta che il blocco di tre cifre uguali si
# trovi all'inizio della password.
#
# Per calcolarne la probabilità facciamo 1/numero_cifre
#

print(1 / numero_cifre)

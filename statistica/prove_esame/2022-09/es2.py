# Inizio 14:27
#
## ----------------------
#  Esercizio 2
## ----------------------
#
#
# A ogni acquisto, il distributore effettua uno sconto di x euro per ogni bottiglia vuota resa.
# Ipotizziamo che il numero di bottiglie rese da un nucleo familiare in una settimana sia
# descritto da una variabile aleatoria R distribuita secondo un modello binomiale di
# parametri nR ∈ N e pR ∈ [ 0 , 1). In questo esercizio supporremo che nC e nR assumano
# valori piccoli
#
# 1. Indichiamo con p il prezzo di acquisto di una bottiglia. Che cosa modella la variabile
# aleatoria T = p C − s R?
#
# siccome p è il prezzo e C è il numero di bottiglie usate dalla famiglia, mentre R è il numero di
# bottiglie restituite, immagino che s sia il prezzo per ogni bottiglia restituita, quindi la
# variabile T indica la differenza tra il prezzo speso per l'acuisto di una bottiglia e il prezzo
# che hanno guadagnato riportandola indietro. Quindi i soldi che effettivamente hanno pagato per aquistare
# C bottiglie e avendone ritornate R.
#

# 2. La distribuzione esatta di T è nota? Se si, indicate a quale modello si riferisce e
# specificate i relativi parametri. Cambia qualcosa nel caso fossimo interessati a una
# distribuzione approssimata?
#
# Beh la distribuzione di T è la differenza tra due distribuzioni binomiali, quindi è definita come
# la combinazione tra due distribuzioni lineari binomiali. I relativi parametri sono quelli
# indicati nell'esercizio precedente. Per l'approssimazione, normalmente se dovessimo approssimare
# una distribuzione binomiale potremmo utilizzare una distribuzione di poisson, ma se n è piccolo
# e p troppo grande questo non può essere fatto.. , in caso contrario potremmo farlo traquillamente
# andando però a definire lambda come n*p
#

# 3. Indichiamo con μT il valore atteso di T . Esprimete μT in funzione dei parametri sopra
# introdotti, giustificando i passaggi matematici intermedi.
#
# E[T] = E[p*C − s*R] = p*E[C] - s*E[R] = p*p_C*n_C - s*n_R*P_R
#

# 4. Indichiamo con σ T la deviazione standard di T . Esprimete σ T in funzione dei parametri
# sopra introdotti, giustificando anche in questo caso i passaggi matematici intermedi.
#
# Si fa la stessa identica cosa che abbiamo fatto sopra, ma con la varianza e poi se ne fa
# la radice quadrata alla fine: Var(T) = p^2*Var(C) + s^2*Var(R) = p^2 * n_C*p_C * (1-p_C) + s^2 * n_R*p_R * (1-p_R)
# sigma(T) = np.sqrt(p^2 * n_C*p_C * (1-p_C) + s^2 * n_R*p_R * (1-p_R))
#

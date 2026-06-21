# Inizio 16:55
#
## ----------------------
#  Esercizio 2
## ----------------------
#
#
# Per n appartenente N fissato, sia X , , . . . , X, un campione aleatorio estratto da una popolazione
# modellata tramite la variabile aleatoria X descritta nell'Esercizio 1.
#
# 1. Fissiamo, solo in questo punto, n = 3. La variabile aleatoria T = (X1 + X2 - X3) è uno stimatore
# deviato per X? Perché? Come cambiano (se cambiano) le risposte a queste due domande considerando
# U = 1/5 (2X, + 2X2 + X3) al posto di T? Possiamo valutare se questi stimatori godono della proprietà
# di consistenza in media quadratica.
#
# Per vedere se questo stimatore T è non deviato andiamo a calcolarne il valore atteso e vedere se esce X
# quindi E[T] = E[X1 + X2 - X3] = E[X1] + E[X2] - E[X3] = mu + mu - mu = mu = lambda quindi è non deviato
#
# Beh facciamo la stessa idendica cosa e vediamo che viene 1/5(2E[X1] + 2E[X2] + 1E[X3]) = 1/5 * (5mu) =
# mu = lambda non distorto anche questo ....
#
# per vedere se è consistente in media quadratica dobbiamo calcolare l'MSE ovvero = Var(\bar T) + bias^2
# bias è uguale a 0 quindi solo Var(\bar T) = fatti il calcolo ma viene una costante sia per U che per T,
# quindi niente consistenza.
#

# 2. \bar X è distribuita secondo uno dei modelli che avete studiato? Indipendentemente dalla risposta data
# alla domanda precedente, siete in grado di esprimere la probabilità P (X = z) in funzione di lambda?
#
# Non sappiamo dire niente sulla distribuzione di sto coso
#
# P(X = z) = e^(-n*lambda) * (n*lambda^z/z!)
#

# 3. Esiste un modello che approssima in modo ragionevole la distribuzione di X ? Motivate la vostra
# risposta, specificando anche quali valori assumono eventuali parametri del modello considerato.
#
# Per approssimare questa cosa possiamo usare una normale, tramite il teorema centrale del limite, con
# valore atteso = E[X] = lambda, mentre per la varianza Var(X) = lambda/n
#
# quindi N(lambda, np.sqrt(lambda/n))
#

# 4. \bar X è uno stimatore non deviato per u = E(X)? Calcolate il suo bias e il suo MSE e dite se esso
# gode anche della proprietà di consistenza in media quadratica.
#
# Per farlo basta andare a vedere che E[\bar X] = 1/n * ∑ E[X] = E[X] = lambda, quindi non distorto, con
# bias uguale a 0 e MSE = Var(\bar X) = 1/n * lambda = 0 per n che tende ad infinito
#

# 5. \bar X è uno stimatore non deviato per sigma^2 = Var(X)? Calcolate il suo bias e il suo MSE e dite
# se esso gode anche della proprietà di consistenza in media quadratica.
#
# Siccome Var(X) = lambda allora lo stimatore è non distorto per Var(X) perchè anche E[\bar X] = lambda
# procedendo con lo stesso ragionamento di prima osservo che ha anche le stesse proprietà di quello di prima
#

# 6. \bar X è uno stimatore non deviato per sigma? Calcolate il suo bias e il suo MSE e dite
# se esso gode anche della proprietà di consistenza in media quadratica.
#
# E' deviato per questo siccome sigma = np.sqrt(lambda), il valore atteso esce lambda, quindi ha bias
# di lambda - np.sqrt(lambda) e quindi l'MSE non gode della proprietà di consistenza in media quadratica
#

# 7. Supponiamo, solo in questo punto che n = 1125. Indicare, in funzione di epsilon e lambda, la probabilità
# che l'errore (in valore assoluto) che si compie usando X per stimare A sia minore o uguale a epsilon.
#
# N(lambda, np.sqrt(lambda/n))
#
# P(|lambda - mu| <= epsilon) = 2*\phi(epsilon/np.sqrt(lambda/n)) - 1
#

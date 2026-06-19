## ----------------------
#  Esercizio 3
## ----------------------
#
#
# Per $n \in \mathbb N$ fissato, siano $X_1, \dots, X_n$ delle variabili aleatorie indipendenti e identicamente distribuite
# secondo un modello geometrico di parametro $h$. Nel resto dell'esercizio considereremo queste variabili come un campione
# estratto da una popolazione la cui distribuzione è la stessa della variabile aleatoria $X$ descritta nell'Esercizio 2 e
# supporremo $\mu = \mathbb E(X)$ e $T = \frac{1}{n} \sum_{i=1}^n X_i$.
#
# 1. La variabile aleatoria $T$ è uno stimatore non distorto per $\mu$? Giustificate la vostra risposta.
#
# Si certo che è uno stimatore non distorto, fai E[T] = mu = E[X] = mu, quindi non distorto
#

# 2. La variabile aleatoria $T$ descritta al punto precedente è uno stimatore non distorto per $h$? Giustificate la vostra risposta.
#
# Non non lo è perchè se fai E[X] = 1-h/h che quindi non corrisponde con quello che stiamo cercando noi, per averlo uguale dovremmo usare
# il metodo plug in che non voglio calcolare
#

# 3. Calcolate il bias e lo scarto quadrato dello stimatore $T$, __con riferimento alla stima del parametro $h$__.
#
# il bias è una cagata da calcolare si fa 1-h/h - h = ( 1 - h - h^2 ) / h
#

# 4. Fissato $\epsilon > 0$, esprimete in funzione di $\epsilon$, $h$ e $n$ la probabilità dell'evento che si verifica quando
# l'errore (in valore assoluto) che si compie usando $T$ per stimare $\mu$ sia minore o uguale a $\epsilon$, giustificando
# i vostri passaggi e indicando eventuali approssimazioni che è necessario introdurre.
#
# sigma è la deviazione standard che è uguale alla radice della varianza, che si calcola andando a fare E[X^2] - E[X]^2, quindi
# è uguale a: np.sqrt(1 - h / h^2)
#
# fai tutta la tiritera partendo da P(|X - mu| <= epsilon) e arrivi a scrivere = 2*\phi(epsilon/sigma) - 1
#

# 5. Proponete uno stimatore $S$ per $h$, giustificando la scelta fatta.
#
# S = 1/(E[T] + 1)
#

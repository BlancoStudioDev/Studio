## --------------------
#  Esercizio 2
## --------------------
#
# In questo esercizio considereremo una popolazione $R$ la cui distribuzione è la stessa dell'omonima variabile
# aleatoria introdotta nell'esercizio precedente e che assumeremo nota a meno del solo parametro r. Per n€$N$
# fissato, $R1,...,Rn$ indicheranno delle variabili aleatorie che descrivono un campione estratto da $R$.

# 1. Sia R' la variabile aleatoria che indica la media campionaria calcolata su R1,...,Rn. Esprimete il suo
# valore atteso in funzione di r, o e p
#
# Il valore atteso della media campionaria è il seguente:
#
# E[R'] = E[\bar R] = 1/n * ∑ E[R] = 1/n*n*E[R] = E[R] = r*o*p

# 2. Utilizzate il metodo plug-in per individuare uno stimatore T che risulti non distorto per il parametro r
# della distribuzione di $R$
#
# per trovare lo stimatore ci basta andare a prendere E[T] = r, quindi r*o*p = r lo stimatore che ci serve è
# semplicemente E[R]/(o*p) così quando calcolo il valore atteso mi viene restituito effettivamente r
#

# 3. Sia $S2$ la variabile aleatoria che indica la varianza campionaria calcolata su $R1,...,Rn$ Applicate il
# metodo plug-in per proporre uno stimatore $U$ di r che dipenda da $S2$. Lo stimatore che avete determinato
# gode delle stesse proprietà di T? Perché?
#
# Var(R) = r**2 * o * p *(1-p), per arrivare ad avere r dovremmo calcolare uno stimatore che escluda tutto al
# di fuori di r, quindi per farlo semplicemente trattiamo la r come una variabile e andiamo a risolvere tenendo
# tutto il resto incognito. Quindi r = np.sqrt(Var(R)/(o*p*(1-p)))
#

# - Nel resto di questo esercizio ci concentreremo sullo stimatore T che avete ottenuto al punto 2.
#
# 4. Calcolate lo scarto quadratico medio di $T$, esprimendolo in funzione di r, o, p ed n.
#
# MSE(T), siccome è lo scarto quadratico medio per uno stimatore non distorto allora il bias è zero e quindi
# MSE(T) = Var(\bar X) + bias^2 = Var(\bar X) = Var(X)/n = (r**2 * o * p * (1-p))/n
#

# 5. Determinate se $T$ gode della proprietà di consistenza in media quadratica, motivando la vostra conclusione.
#
# Si gode della proprietà poichè per n che tende all'infinito l'MSE tende a 0, pertanto gode.
#

# 6. Determinate se T gode della proprietà di consistenza in senso debole, motivando la vostra conclusione.
#
# Spesso e volentieri se godono della proprietà di consistenza in media quadratica allora godono anche della
# proprietà di consistenza in senso debole, ma ad ogni modo basta andare ad analizzare la stessa cosa solamente
# aggiungendo un errore, il che non fa cambiar niente e quindi gode anche della consistenza in senso debole.
#

# 7. Calcolate la probabilità dell'evento che si verifica quando l'errore (in valore assoluto) che si compie
# usando T per stimarer sia minore o uguale di 1/2, esprimendola in funzione di r, o, p, n e della funzione
# di ripartizione della distribuzione normale standard, giustificando i vostri passaggi e indicando eventuali
# approssimazioni che è necessario introdurre.
#
# Per stimare la probabilità di verifica dell'evento secondo un errore di 1/2 è data dalla funzione di ripartizione
# così scritta:
#
# Var(T) = E[T**2] - E[T]**2 = 1/op * Var(\bar R) = r**2 * p * o * (1-p) / (n*o*p)
# dove sigma = np.sqrt(Var(T)) = r * np.sqrt( p * o * (1-p) / (n*o*p) )
# \epsilon = 1/2 = 0.5
#
# P(|X - \mu| <= \epsilon) = P(-\epsilon <= X - \mu <= \epsilon) = P(-\epsilon/(\sigma) <= X - \mu <= \epsilon/(\sigma)) =
# = 2*phi(\epsilon/(sigma)) - 1
#

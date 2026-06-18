# Inizio 16:36
#
## -------------------
#  Esercizio 2
## -------------------
#
# Siano $Z_1, \dots, Z_n$ variabili aleatorie che descrivono un campione estratto da $Z$, distribuito come
# l'omonima all'esercizio precedente
#
#
# 1. Considerando solo in questo punto che sia noto $\mu_X$ determinare uno stimatore non distorto $U$
# che stimi $\mu_Y$
#
# Uno stimatore corretto utilizzando il metodo plug in è quello di E[- \bar Z + 2]
#

# 2. Considerando solo in questo punto che $\sigma_X = \sigma_Y$ determinare uno stimatore
# non distorto $V$ che stimi $\sigma_X^2$
#
# Uno stimatore non distorto per \sigma_X^2 è \sigma_Z/2
#

# 3. Determinare se lo stimatore $U$ è consistente in media quadratica
#
# si è consistente in media quadratica poichè all'infinito MSE tende a 0
#

# 4. È possibile fare lo stesso ragionamento per $V$? Se no motivare la risposta, altrimenti
# determinare se lo stimatore è consistente in media quadratica
#
# Non è possibile farlo poichè la varianza non era in media campionaria, quindi quando si va a fare l'MSE
# non ho un /n che porta l'approssimazione a 0 nell'infinito, bensì tende a Var(Z)/2
#

# 5. Dato $\epsilon$, determinare la probabilità che lo stimatore $U$ presenti al più un errore di $\epsilon$
#
# Per determinare che questo avvenga bisogna fare: P(|Z - \mu| < \epsilon) <= 1
#
# Risolvendo sta cosa viene fuori: 2*\phi(\epsilonsqrt(n)/\sqrt(\sigma_x^2 + \sigma_Y^2))
#
# Fine 16:53

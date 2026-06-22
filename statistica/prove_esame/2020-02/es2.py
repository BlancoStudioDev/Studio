## ----------------------
#  Esercizio 2
## ----------------------
#
#
# Sia \bar X, la media campionaria di un campione casuale X_i, ... , X_n, estratto da una popolazione
# bernoulfiana di parametro p.
#
# 1. Esprimete E(X(m)) in funzione di p.
#
# Basta che andiamo a calcolaro, ovvero: E[\bar X] = E[1\n ∑ X] = 1\n * np = p
#

# 2. Esprimete Var((m) in funzione di n e p.
#
# Var(\bar X) = Var(1\n ∑ X) = 1\n^2 * np(1-p) = 1\n*(p(1-p))
#

# 3. Controllare che Var(X) <= 1/4n
#
# 1\n *(p(1-p)) <= 1\4n
#
# p(1-p) <= 1\4 -> sempre vero per quello che ci siamo detti all'esercizio 1, basta calcolare la derivata
# della varianza, vedere che viene 2p - 1 quindi il masismo è in p = 1/2 e quindi se sostiuiisco viene
# che il massimo è a 1/4, quindi sarà sempre maggiore di 1\4
#

# 4. "Sia \(n\) un valore abbastanza piccolo da non poter applicare l'approssimazione normale.
# Controllate che, per ogni \(\epsilon > 0\), vale la diseguaglianza: \(P(\vert{}\overline{X}_{(n)}
# - p\vert{} \leq \epsilon) \geq 1 - \frac{1}{4 \epsilon^2 n}\)."
#
# Allora siccome sappiamo che la diseguaglianza di Chebyshev è: P(|X - \mu| >= epsilon) <= Var(X)/(epsilon^2)
# allora possiamo dire che Var(\bar X) è al massimo 1/(4*n) per il massimo calcolato prima e diviso per n
# perchè è la varianza della media campionaria. Quindi sostituendo otteniamo: Var(X)/(epsilon^2) =
# (1/(4*n))/epsilon^2 = 1/(4*n*epsilon^2) quindi possiamo stimare la parte a destra come <= di quello appena
# scritto. Quindi corretto per come serve a noi.
#

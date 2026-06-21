# Inizio 14:40
#
## ----------------------
#  Esercizio 3
## ----------------------
#
#
# Indichiamo con n ∈ N il numero totale di clienti del distributore, e con C1 , . .. , Cn le
# variabili aleatorie che indicano il numero di bottiglie acquistate in una settimana da ogni
# cliente. Analogamente, siano R1 , .. . , Rn le variabili aleatorie che indicano il numero di
# bottiglie rese in una settimana. Assumiamo, infine, che vi sia indipendenza tra le abitudini
# di acquisto dei vari clienti. In questo esercizio supporremo che n assuma un valore
# elevato.
#
# 1. Esiste un modello che descrive in modo esatto la distribuzione della variabile aleatoria
# C_tot = ∑ C_i? In caso affermativo, indicare quali sono i suoi parametri, giustificando la vostra
# risposta.
#
# Stiamo andando a moltiplicare una distribuzione binomiale per n volte, quindi la distribuzione che
# otteniamo è ancora una binomiale, di parametri: B(n*n_C, p_C).
#

# 2. Esiste un modello che approssima ragionevolmente bene la distribuzione di Ct o t ? In caso
# affermativo, indicate quali sono i suoi parametri, giustificando la vostra risposta.
#
# Certo bisogna usare poisson per approssimare una binomiale oppure la distribuzione normale, ma entrambi
# funzionano solamente se n*n_C è grande e p_C è basso, in tal caso possiamo andare a definire la distribuzione
# di poisson nel seguente modo: P(\lambda) = P(n*n_C*p_C), se invece volessimo andare più sul generale,
# possiamo usare una distribuzione normale che come parametri in ingresso ha il valore atteso, che per noi
# in una binomiale di questo tipo è: n*n_C*p_C e la deviazione standard che è per noi:
# np.sqrt(n*n_C*p_C * (1-p_C)), quindi N(\mu, \sigma)
#

# 3. Se nelle domande 1 e 2 di questo esercizio sostituiamo C_tot con R_ tot =∑ Ri, le risposte
# cambiano significativamente? Perchè?
#
# Siccome anche R è una binomiale le due distribuzione che siano C_tot o R_tot non cambiano significativamente
# se non chiaramente per i parametri, infatti se approcciamo questo problema come quello precedente, con
# l'approssimazione di poisson abbiamo che P(\lambda) = P(n*n_R*p_R), con invece l'approssimazione normale
# sarebbe: N(\mu, \sigma) = N(n*n_R*p_R, np.sqrt(n*n_R*p_R * (1-p_R))) e il modello che descrive R_tot è
# sempre una binomiale di parametri: B(n*n_R, p_R)
#

# 4. Che cosa modella la variabile aleatoria T_tot = p*C_tot− s*R_tot ?
#
# Beh descrivono la stessa cosa che dicevamo prima, solamente aggregati in una formula ripetibile per
# tot famiglie/clienti.
#

# 5. Esiste un modello che descrive la distribuzione di T_tot ? In caso affermativo, indicate quali
# sono i suoi parametri, e in caso negativo indicare un modello che approssima
# ragionevolmente la distribuzione, sempre specificandone i parametri.
#
# Allora la risposta a questo problema è che posso stimarla secondo una distribuzione normale con i
# parametri di:
#
# N(p*p_C*n*n_C - s*n*n_R*P_R, np.sqrt(p^2 * n * n_C*p_C * (1-p_C) + s^2 * n * n_R*p_R * (1-p_R)))
#

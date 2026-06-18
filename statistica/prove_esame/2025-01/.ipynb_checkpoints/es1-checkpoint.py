## ------------------------
#  Esercizio 1
## ------------------------
#
# 1.
# Siano X e Y due v.a. indipendenti distribuite come una Bernoulli di parametro p. Posto Z = 2X-Y,
# rispondete alle seguenti domande:
#
# Quali sono le specificazioni di Z?
#
# X = 0, Y = 0, Z = 0
# X = 1, Y = 0, Z = 2
# X = 1, Y = 1, Z = 1
# X = 0, Y = 1, Z = -1
#
# 2.
# Calcolate P(Z = z) per tutte le specificazioni che avete determinato nel punto precedente
#
# Per farlo andiamo semplicemente a calcolare la probabilità che venga assunto un certo valore z
# siccome siamo in una bernoulliana allora la probabilità che questo accata è:
#
# P(Z = 0) -> X = 0 P(X = 0) = 1-p, Y = 0 P(Y = 0) = 1-p -> P(Z = 0) = (1-p)(1-p) = p^2
# P(Z = 2) -> X = 1 P(X = 1) = p, Y = 0 P(Y = 0) = 1-p -> P(Z = 2) = p-p^2
# P(Z = 1) ->  X = 1 P(X = 1) = p, Y = 1 P(Y = 1) = p -> P(Z = 1) = p*p = p^2
# P(Z = -1) -> X = 0 P(X = 0) = 1-p, Y = 1 P(Y = 1) = p -> P(Z = -1) = (1-p)*p
#
# 3. Solo in questo punto, assumiamo che p=3/4. Visualizzate graficamente la distribuzione Z
# (potete farlo sia a mano, sia in codice) giustificando il tipo di grafico scelto

import matplotlib.pyplot as plt


def bernoulli(p, x):
    if x == 0:
        return p * p
    if x == 2:
        return p - p**2
    if x == 1:
        return p**2
    if x == -1:
        return (1 - p) * p


p = 3 / 4
x = [-1, 0, 1, 2]
y = [bernoulli(p, x) for x in x]

plt.plot(x, y)
plt.show()

# 4. Calcolate il valore atteso e la varianza di Z, esprimendoli in funzione di p e giustificando i passaggi svolti
#
# La varianza e il valore atteso in una distribuzione bernoulliana dipendono interamente dal parametro p, in particolare:
#
# E[X] = p
# Var(X) = p(1-p)
# questo però solamente se ho una variabile aleatoria singola, essendo composta, per calcolare la varianza e il valore atteso
# bisogna fare delle trasformazioni:
#
# E[Z] = E[2X - Y] = E[2X] - E[Y] = 2E[X] - E[Y] = 2p - p = p
# Var(Z) = Var(2X - Y) = Var(2X) - Var(Y) = 4Var(X) - Var(Y) = 4p(1-p)- p(1-p) = 4p - 4p**2 - p + p**2 = -3p**2 +3p = 3p(1-p)

# 5. Mostrate un grafico che illustra come cambia Var(Z) al variare di p. Determinate poi un limite superiore per Var(Z) che non dipende da p

import numpy as np

x = np.linspace(0, 1, 100)
y = 3 * x * (1 - x)

plt.plot(x, y)
plt.show()

## ------------------------
#  Esercizio 2
## ------------------------
#
# Consideriamo una popolazione distribuita come una v.a. Z, la cui distribuzione è la stessa dell'omonima variabile
# definita nell'esercizio precedente, per un valore ignoto del parametro p. per n € Naturali fissato, siano Z1,...,Zn
# delle v.a. che descrivono un campione estratto da questa popolazione. In tutto l'esercizio Z' indicherà la media
# campionaria calcolata su Z1,...,Zn.
#
# 1. Z' è uno stimatore non deviato per il valore atteso di Z?
#
# La media campionaria è sempre uno stimatore non distorto per il valore atteso
#
# 2. Z' è uno stimatore non deviato per p?
#
# Bisogna andare a calcolare il valore atteso di Z = E[Z] = p, e vedere se la media campionaria rispecchia questo valore
# quindi \bar{Z} = 1/n sum E[Z] = 1/n * np = p
#
# 3. Giustificando i passaggi, calcolate lo scarto quadratico medio di Z' nella stima di p, esprimendolo in funzione di n e p
#
# MSE(Z') = Var(Z') + bias^2
#
# Il bias è uguale a 0 siccome lo stimatore è non distorto
#
# MSE(Z') = MSE(\bar(Z)) = Var(\bar(Z)) = Var(Z)/n = 3p(1-p)/n
#
# 4. Sia sigma' la deviazione standard di Z', ricavate un limite superiore per sigma' che dipenda solo dalla dimensione del campione

p = 0.5
n = np.arange(1, 100)
plt.plot(n, np.sqrt((3 * p * (1 - p)) / n))
plt.show()

n = 1
print(np.sqrt((3 * p * (1 - p)) / n))

# la deviazione standard dipendente solamente da n è definita in questo modo: np.sqrt((3 * p * (1 - p)) / n) dove p prende il valore medio
# ovvero 0.5. Per questo motivo andiamo a definire, guardando il grafico, il valore massimo come quando n = 1, se fosse 0 ci sarebbe un problema
# di limite ad infinito, e non possiamo avere valori tra 0 e 1 perchè è una variabile aleatoria discreta, quindi valori 0 1 2 3 4 .... non 0,1
# di conseguenza calcolando tutto otteniamo il valore: 0.8660254037844386

# 5. Fissato epsilon>0, applicando il TCL, esprimete in funzione di epsilon, n e sigma' la probabilità dell'evento che si verifica
#    quando l'errore in valore assoluto che si compie usando Z' per stimare p è minore u uguale di epsilon
#
# Per farlo andiamo ad utilizzare la funzione del TLC ovvero:
#
# P(|Z - \mu| <= epsilon) = epsilon = 2\phi((epsilon - \mu)/\sigma <= epsilon/\sigma') - 1 = 2\phi(epsilon/\sigma')
# sigma' = sigma/n

# 6. Calcolate un limite inferiore per la probabilità calcolata nel punto prcedente, che dipenda solo da epsilon e n
#
# Non so farlo .....

## ------------------------
#  Esercizio 3
## ------------------------

# 1. Create un DataFrame che contenga il dataset memorizzato nel file auto.csv e memorizzatelo in una variabile auto.
# Determinate quali attributi del dataset contengano valori mancanti, e indicando il relativo numero di casi

import pandas as pd

auto = pd.read_csv("auto.csv")

print("Fatti tutti insieme:\n", auto.isnull().sum(), "\n\nFatti con diverse print")

print("Basse emissioni mancanti: ", auto.basse_emissioni.isnull().sum())
print("Carpooling mancanti: ", auto.carpooling.isnull().sum())
print("Numero_occupanti mancanti: ", auto.numero_occupanti.isnull().sum())
print("Tipo_motore mancanti: ", auto.tipo_motore.isnull().sum())
print("Km_percorsi mancanti: ", auto.km_percorsi.isnull().sum())
print("tipo_motore_enum mancanti: ", auto.tipo_motore_enum.isnull().sum())

# 2. Visualizzate la distribuzione dell’attributo tipo_motore, motivando la scelta dello strumento grafico utilizzato.

print(auto.tipo_motore.head())

plt.pie(
    auto["tipo_motore"].value_counts(),
    labels=auto["tipo_motore"].value_counts().index,
)
plt.show()

# 3. Utilizzando un indice numerico, valutate quanto i possibili differenti valori per l’attributo tipo_motore siano
# equamente distribuiti nel dataset, motivando l’indice utilizzato e discutendo i risultati ottenuti, confrontandoli
# con il grafico ottenuto al punto precedente.

print(auto.tipo_motore.value_counts(normalize=True))

per_gini = auto.tipo_motore.value_counts(normalize=True)

print(1 - (np.sum(per_gini**2) / (len(per_gini) - 1) / len(per_gini)))

# occupano tutti il 22-27% o superiore quindi sono decentemente distribuiti, per l'indice di gini basterebbe solamente fare la somma
# e dividere per il numero di oggetti, quindi sostanzialmente è la media delle frequenze relative del campione

# 4. L’amministrazione comunale decide di rivedere le tariffe di accesso della zona a traffico limitato, introducendo
# un punteggio numerico p=2c−b, dove b e c rispettivamente i valori che corrispondono agli attributi basse_emissioni
# e carpooling. Aggiungete al DataFrame un attributo punteggio, calcolando il suo valore per ogni autoveicolo utilizzando
# la formula introdotta.

auto["punteggio"] = 2 * auto["carpooling"] - auto["basse_emissioni"]

# 5. Visualizzate la tabella delle frequenze relative cumulate per l’attributo numero_occupanti.

print(auto.numero_occupanti.value_counts(normalize=True).sort_index())

# 6. Determinate il primo valore n tale che la frequenza relativa degli autoveicoli con al più n occupanti supera 0.95.
# Estraete dal dataset tutti e soli gli autoveicoli che hanno al più n occupanti e salvateli in una nuova variabile
# auto_ridotto. Lavorate, in tutto il resto dell’esame, con questo nuovo dataset

valori = (
    auto.numero_occupanti.value_counts(normalize=True)
    .sort_index(ascending=False)
    .cumsum()
)
n = len(valori[valori > 0.95])

auto_ridotto = auto[auto.numero_occupanti <= n]
print(auto_ridotto.head())

# 7. Visualizzate separatamente le tabelle delle frequenze relative degli attributi carpooling e basse emissioni

print(auto_ridotto.carpooling.value_counts(normalize=True).sort_index())
print(auto_ridotto.basse_emissioni.value_counts(normalize=True).sort_index())

# 8. Valutate se esiste una relazione fra gli attributi carpooling e basse_emissioni utilizzando sia uno
# strumento graFICO che un indice numerico

print(auto_ridotto.carpooling.corr(auto_ridotto.basse_emissioni))

x = auto_ridotto.carpooling
y = auto_ridotto.basse_emissioni

plt.scatter(x, y)
plt.show()

# 9. Supponete che i valori carpooling e basse_emissioni possono essere interpretati come 2 campioni la sborra
# estratti da 2 popolazioni che individueremo come 2 variabili X e Y. Sulla base dei risultati dei 2 punti
# precedenti potete supporre l'ipotesi che X e Y siano identicamente distribuite
#
# no non puoi dirlo perchè i valori che sono contenuti li dentro fanno schifo e non sono correlati tra loro due....

# 10. Valutate l'ipotesi che l'attributo km percorsi contenga dei valori assimilabili ad un campione estratto
# da una distribuzione normale (dovresti ottenere dati incoerenti, descrivili e prova a spiegare)

import statsmodels.api as sm

sm.qqplot(auto_ridotto.km_percorsi)
plt.show()

## ------------------------
#  Esercizio 4
## ------------------------

# In questo esercizio considereremo i valori dell'attributo punteggio del dataset memorizzato in auto_ridotto,
# come un campione estratto da una popolazione distribuita come una variabile aleatoria Z

# 1. Sulla base dei risultati dell’esercizio precedente, validate l’ipotesi che Z abbia la stessa distribuzione
# dell’omonima variabile aleatoria introdotta nell’Esercizio 1

print(auto_ridotto.punteggio.value_counts(normalize=True).sort_index())

# non è propriamente come la variabile aleatoria Z, nel primo esercizio sapevamo che la distribuzione diZ era:
#
# P(Z = 0) -> X = 0 P(X = 0) = 1-p, Y = 0 P(Y = 0) = 1-p -> P(Z = 0) = (1-p)(1-p) = p^2
# P(Z = 2) -> X = 1 P(X = 1) = p, Y = 0 P(Y = 0) = 1-p -> P(Z = 2) = p-p^2
# P(Z = 1) ->  X = 1 P(X = 1) = p, Y = 1 P(Y = 1) = p -> P(Z = 1) = p*p = p^2
# P(Z = -1) -> X = 0 P(X = 0) = 1-p, Y = 1 P(Y = 1) = p -> P(Z = -1) = (1-p)*p
#
# quindi con P(Z = 0) e P(Z = 1) era uguale, ma a noi viene 0.45 e 0.08, quindi diversa, non hanno la stessa distribuzione
# ma negli esercizi viene detto di tenere questa come distribuzione bernoulliana

# 2. Determinate una stima numerica p̂ per il parametro p della popolazione

print(auto_ridotto.punteggio.mean())

# 3. Utilizzando i risultati dell’Esercizio 2.6, calcolate un limite inferiore per la probabilità che la stima di
# p fatta al punto precedente comporti un errore (in valore assoluto) grande al più due centesimi.
#
# non lo sapevo fare ahahaha....

# 4. Usando la stima p̂ determinata al punto 2 al posto del valore ignoto di p, calcolate le seguenti probabilità:
# - P(Z = 1)
# - P(Z ≤ 0)
# - P(Z è pari)

p = 0.12087912087912088

print("P(X = 1) = ", (1 - p) * (1 - p))
print("P(X = 0 + X = -1) = ", (1 - p) * (1 - p) + (1 - p) * p)
print("P(X = 0 union X = 2) = ", (1 - p) * (1 - p) + p * (1 - p))3455


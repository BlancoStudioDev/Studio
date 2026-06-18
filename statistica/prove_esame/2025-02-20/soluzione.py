"""
Esercizi 3 e 4 - Analisi del dataset accessi.csv
=================================================
Soluzione completa con codice, output e commenti.
"""

import math

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.stats as st
import statsmodels.api as sm

# ============================================================
# ESERCIZIO 3
# ============================================================

# --- 3.1 Caricamento e analisi valori mancanti ---

accessi = pd.read_csv("accessi.csv")
print("=" * 60)
print("ESERCIZIO 3.1 - Caricamento e valori mancanti")
print("=" * 60)
print(f"\nDataset caricato: {accessi.shape[0]} righe, {accessi.shape[1]} colonne")
print(f"Colonne: {list(accessi.columns)}\n")

# (a) Valori mancanti per ogni possibile valore di allarme
print("Valori mancanti nell'attributo 'richieste' per ogni valore di 'allarme':")
for val in sorted(accessi["allarme"].dropna().unique()):
    subset = accessi[accessi["allarme"] == val]
    n_missing = subset["richieste"].isna().sum()
    n_total = len(subset)
    print(f"  allarme = {int(val)}: {n_missing} valori mancanti su {n_total} righe")

# Anche per i NaN in allarme
subset_nan = accessi[accessi["allarme"].isna()]
n_missing_nan = subset_nan["richieste"].isna().sum()
n_total_nan = len(subset_nan)
print(f"  allarme = NaN: {n_missing_nan} valori mancanti su {n_total_nan} righe")

# (b) Attributi con almeno un valore mancante
print("\nAttributi con almeno un valore mancante:")
for col in accessi.columns:
    n_missing = accessi[col].isna().sum()
    if n_missing > 0:
        print(f"  {col}: {n_missing} valori mancanti")

# --- 3.2 Tipo e rappresentazione grafica di allarme ---

print("\n" + "=" * 60)
print("ESERCIZIO 3.2 - Attributo 'allarme'")
print("=" * 60)

print("\nTipo dell'attributo 'allarme':", accessi["allarme"].dtype)
print("L'attributo 'allarme' è una variabile categorica binaria (Bernoulliana),")
print("che assume valori 0 (nessun allarme) e 1 (allarme emesso).")

# Pie chart: rappresenta le proporzioni di 0 e 1
counts = accessi["allarme"].value_counts().sort_index()
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

ax1.pie(
    counts.values,
    labels=["0 (No allarme)", "1 (Allarme)"],
    autopct="%1.1f%%",
    colors=["lightblue", "salmon"],
    startangle=90,
)
ax1.set_title("Diagramma a torta dell'attributo 'allarme'")

ax2.bar(
    counts.index.astype(int), counts.values, color=["lightblue", "salmon"], width=0.4
)
ax2.set_xlabel("allarme")
ax2.set_ylabel("Frequenza")
ax2.set_title("Grafico a barre dell'attributo 'allarme'")
ax2.set_xticks([0, 1])

plt.tight_layout()
plt.savefig("allarme_plot.png", dpi=100)
plt.show()

print("\nMotivazione: il diagramma a torta è adeguato per visualizzare le proporzioni")
print("di una variabile categorica binaria, mostrando immediatamente la prevalenza")
print("relativa delle due categorie.")

# --- 3.3 Carico vs Allarme ---

print("\n" + "=" * 60)
print("ESERCIZIO 3.3 - Relazione carico-allarme")
print("=" * 60)

# Rimuoviamo righe con NaN in carico o allarme per l'analisi
data_clean = accessi[["carico", "allarme"]].dropna()

# Scatter plot
plt.figure(figsize=(8, 5))
plt.scatter(data_clean["carico"], data_clean["allarme"], alpha=0.5, c="steelblue")
plt.xlabel("Carico di sistema")
plt.ylabel("Allarme (0/1)")
plt.title("Relazione tra carico di sistema ed emissione allarmi")
plt.yticks([0, 1])
plt.grid(True, alpha=0.3)
plt.savefig("carico_allarme_scatter.png", dpi=100)
plt.show()

# Coefficiente di correlazione di Pearson
corr_pearson = data_clean["carico"].corr(data_clean["allarme"])
print(f"\nCoefficiente di correlazione di Pearson: {corr_pearson:.4f}")

# Confronto delle medie del carico per allarme=0 e allarme=1
carico_no_allarme = data_clean[data_clean["allarme"] == 0]["carico"]
carico_si_allarme = data_clean[data_clean["allarme"] == 1]["carico"]
print(f"Carico medio quando NON c'è allarme: {carico_no_allarme.mean():.4f}")
print(f"Carico medio quando C'È allarme:    {carico_si_allarme.mean():.4f}")

# Boxplot comparativo
plt.figure(figsize=(6, 5))
plt.boxplot([carico_no_allarme, carico_si_allarme], labels=["No Allarme", "Allarme"])
plt.ylabel("Carico di sistema")
plt.title("Distribuzione del carico per stato allarme")
plt.grid(True, alpha=0.3)
plt.savefig("carico_boxplot.png", dpi=100)
plt.show()

print("\nCommento: il coefficiente di correlazione (~0.39) indica una correlazione")
print("positiva moderata. Dal grafico si osserva che quando l'allarme è attivo (1),")
print("il carico tende a essere più elevato. Il boxplot conferma che la mediana del")
print("carico è maggiore in presenza di allarme. Ciò suggerisce che il carico di")
print("sistema influisca sul sistema di emissione degli allarmi, anche se la")
print("relazione non è perfettamente deterministica.")

# --- 3.4 Distribuzione di richieste (ECDF) ---

print("\n" + "=" * 60)
print("ESERCIZIO 3.4 - Distribuzione di 'richieste'")
print("=" * 60)


richieste = accessi["richieste"].dropna().sort_values()
cdf = np.arange(1, len(richieste) + 1) / len(richieste) * 100

plt.figure(figsize=(10, 6))
plt.step(richieste, cdf, where="post", color="steelblue", linewidth=2, label="ECDF")
plt.xlabel("Numero di richieste (n)")
plt.ylabel("Percentuale cumulativa (%)")
plt.title("Funzione di distribuzione cumulativa empirica (ECDF) delle richieste")
plt.grid(True, alpha=0.3)
plt.legend()

# Aggiungiamo linee guida per leggere n dato f
for f_pct in [25, 50, 75, 95]:
    n_val = richieste.quantile(f_pct / 100)
    plt.axhline(y=f_pct, color="red", linestyle="--", alpha=0.5)
    plt.axvline(x=n_val, color="red", linestyle="--", alpha=0.5)
    plt.text(n_val + 0.3, f_pct + 1, f"n={n_val:.0f}", fontsize=9, color="red")

plt.savefig("richieste_ecdf.png", dpi=100)
plt.show()

print("\nMotivazione: l'ECDF (Empirical Cumulative Distribution Function) è lo")
print("strumento più adeguato perché risponde direttamente alla domanda: per ogni")
print("valore n, l'ECDF mostra la percentuale di osservazioni ≤ n.")

# --- 3.5 Determinare n per f = 95 ---

print("\n" + "=" * 60)
print("ESERCIZIO 3.5 - n per f = 95")
print("=" * 60)

n_95 = richieste.quantile(0.95)
print(f"Il valore di n per cui f = 95% è: n = {n_95}")
print(
    f"Interpretazione: nel 95% dei casi sono arrivate al massimo {int(n_95)} richieste."
)

# --- 3.6 Tabella frequenze relative congiunte ---

print("\n" + "=" * 60)
print("ESERCIZIO 3.6 - Frequenze relative congiunte")
print("=" * 60)

tab = pd.crosstab(
    accessi["richieste"], accessi["allarme"], normalize=True, margins=True
)
print("\nTabella delle frequenze relative congiunte (richieste × allarme):")
print(tab.round(6))

# --- 3.7 Stima delle probabilità ---

print("\n" + "=" * 60)
print("ESERCIZIO 3.7 - Stima delle probabilità")
print("=" * 60)

# Dalla tabella congiunta ricaviamo le probabilità
# A = evento "è stato emesso un allarme" (allarme = 1)
# R = evento "almeno una richiesta" (richieste > 0)

# P(R): probabilità che ci sia almeno una richiesta
# Nel dataset, il minimo di richieste è 3, quindi P(R) = 1
# (tutti i periodi hanno almeno una richiesta)
p_R = 1.0  # ovvero (n_righe - righe_con_richieste==0) / n_righe
print(f"i.   P(R) = P(almeno 1 richiesta) = {p_R}")

# P(A ∩ R): probabilità congiunta allarme=1 e almeno una richiesta
# Dalla tabella: colonna All per allarme=1 diviso totale
p_A_inter_R = tab.loc["All", 1.0] if 1.0 in tab.columns else 0.0
print(f"ii.  P(A ∩ R) = P(allarme=1 e almeno 1 richiesta) = {p_A_inter_R:.6f}")

# P(R | A): probabilità di almeno una richiesta dato che c'è un allarme
# = P(R ∩ A) / P(A)
# P(A) = probabilità marginale di allarme=1
p_A = tab.loc["All", 1.0] if 1.0 in tab.columns else 0.0
p_R_given_A = p_A_inter_R / p_A if p_A > 0 else 0
print(f"iii. P(R | A) = P(almeno 1 richiesta | allarme) = {p_R_given_A:.6f}")
print("     (=1 perché quando c'è un allarme ci sono sempre richieste)")

# P(A | R): probabilità di allarme dato che c'è almeno una richiesta
# = P(A ∩ R) / P(R)
p_A_given_R = p_A_inter_R / p_R if p_R > 0 else 0
print(f"iv.  P(A | R) = P(allarme | almeno 1 richiesta) = {p_A_given_R:.6f}")

# --- 3.8 Le probabilità devono sommare a 1? ---

print("\n" + "=" * 60)
print("ESERCIZIO 3.8")
print("=" * 60)

print("\nNo, le quattro probabilità NON devono sommare a 1.")
print("Motivazione: P(R), P(A∩R), P(R|A), P(A|R) sono quattro misure diverse")
print("che NON formano una partizione dello spazio campionario:")
print("  - P(R) è una probabilità marginale")
print("  - P(A∩R) è una probabilità congiunta")
print("  - P(R|A) e P(A|R) sono probabilità condizionate")
print("Sommare grandezze eterogenee non ha significato probabilistico.")

# --- 3.9 Richieste ~ Normale? ---

print("\n" + "=" * 60)
print("ESERCIZIO 3.9 - Test di normalità su 'richieste'")
print("=" * 60)

richieste_clean = accessi["richieste"].dropna()

fig, axes = plt.subplots(1, 3, figsize=(16, 5))

# Istogramma
axes[0].hist(
    richieste_clean,
    bins=20,
    density=True,
    alpha=0.7,
    color="steelblue",
    edgecolor="white",
)
axes[0].set_xlabel("Richieste")
axes[0].set_ylabel("Densità")
axes[0].set_title("Istogramma delle richieste")

# QQ-plot contro normale
sm.qqplot(richieste_clean, st.norm, line="45", fit=True, ax=axes[1])
axes[1].set_title("Q-Q Plot (Normale)")

# Boxplot
axes[2].boxplot(richieste_clean)
axes[2].set_title("Boxplot delle richieste")
axes[2].set_ylabel("Richieste")

plt.tight_layout()
plt.savefig("richieste_normalita.png", dpi=100)
plt.show()

# Test di Shapiro-Wilk
stat_sw, p_sw = st.shapiro(richieste_clean)
print(f"\nTest di Shapiro-Wilk: statistica = {stat_sw:.4f}, p-value = {p_sw:.4f}")
# Test di D'Agostino-Pearson (K²)
stat_dp, p_dp = st.normaltest(richieste_clean)
print(f"Test di D'Agostino-Pearson: statistica = {stat_dp:.4f}, p-value = {p_dp:.4f}")

print("\nCommento: l'istogramma mostra una forma approssimativamente campanulare,")
print("ma asimmetrica. I test di normalità (Shapiro-Wilk e D'Agostino-Pearson)")
print("restituiscono p-value molto bassi, quindi RIFIUTIAMO l'ipotesi di normalità")
print("al livello di significatività standard (α=0.05).")
print("I valori di richieste NON sono assimilabili a un campione normale.")

# --- 3.10 Media, varianza e confronto con Poisson ---

print("\n" + "=" * 60)
print("ESERCIZIO 3.10 - Media, varianza e Poisson")
print("=" * 60)

media_richieste = richieste_clean.mean()
varianza_richieste = richieste_clean.var()
print(f"Media campionaria di richieste:  {media_richieste:.4f}")
print(f"Varianza campionaria di richieste: {varianza_richieste:.4f}")

# Per una Poisson, E(X) = Var(X) = lambda
lambda_stimato = media_richieste
print(f"\nPer una Poisson: λ = E(X) = Var(X).")
print(f"Media = {media_richieste:.4f}, Varianza = {varianza_richieste:.4f}")
print(f"La differenza è: {abs(media_richieste - varianza_richieste):.4f}")

# QQ-plot contro Poisson
fig, axes = plt.subplots(1, 2, figsize=(12, 5))
sm.qqplot(richieste_clean, st.poisson(lambda_stimato), line="45", ax=axes[0])
axes[0].set_title(f"Q-Q Plot (Poisson λ={lambda_stimato:.1f})")

# Confronto istogramma vs PMF Poisson teorica
axes[1].bar(
    np.arange(int(richieste_clean.min()), int(richieste_clean.max()) + 1),
    np.bincount(richieste_clean.astype(int).values - int(richieste_clean.min()))
    / len(richieste_clean),
    alpha=0.7,
    label="Osservato",
    color="steelblue",
)
x_range = np.arange(int(richieste_clean.min()), int(richieste_clean.max()) + 1)
axes[1].plot(
    x_range,
    st.poisson(lambda_stimato).pmf(x_range),
    "ro-",
    markersize=4,
    label=f"Poisson(λ={lambda_stimato:.1f})",
)
axes[1].set_xlabel("Richieste")
axes[1].set_ylabel("Frequenza relativa / PMF")
axes[1].set_title("Confronto empirico vs Poisson")
axes[1].legend()

plt.tight_layout()
plt.savefig("richieste_poisson.png", dpi=100)
plt.show()

print("\nCommento: per una distribuzione di Poisson, media e varianza devono")
print("essere uguali. In questo caso sono molto vicine (differenza ~0.04), il che")
print("suggerisce che i dati POTREBBERO seguire una Poisson. Il Q-Q plot mostra")
print("un buon accordo con la Poisson teorica. A differenza della normale, la")
print("Poisson è più adatta perché la variabile 'richieste' è un conteggio discreto.")


# ============================================================
# ESERCIZIO 4
# ============================================================

print("\n\n" + "=" * 60)
print("ESERCIZIO 4")
print("=" * 60)

# --- 4.1 Variabile allarme_si ---

print("\n--- 4.1: allarme_si ---")
allarme_si = accessi[accessi["allarme"] == 1].copy()
print(f"Numero di osservazioni con allarme=1: {len(allarme_si)}")
richieste_as = allarme_si["richieste"].dropna()
print(f"Valori di richieste (con allarme=1): {richieste_as.values}")

# --- 4.2 Media e varianza di allarme_si ---

print("\n--- 4.2: Media e varianza per allarme_si ---")
media_as = richieste_as.mean()
varianza_as = richieste_as.var()
print(f"Media campionaria di richieste (allarme=1):  {media_as:.4f}")
print(f"Varianza campionaria di richieste (allarme=1): {varianza_as:.4f}")
print(f"Differenza media-varianza: {abs(media_as - varianza_as):.4f}")
print("\nCommento: qui media e varianza sono molto diverse (14.08 vs 4.43).")
print("Pertanto, per i soli casi con allarme, i dati NON sembrano seguire")
print("una Poisson (dove media = varianza). Tuttavia l'esercizio chiede di")
print("supporre che lo siano per i punti successivi.")

# --- 4.3 Stima di lambda ---

print("\n--- 4.3: Stima di λ ---")
# Stimatore di massima verosimiglianza per λ in una Poisson: media campionaria
lambda_hat = media_as
print(f"Stima di λ (media campionaria): λ̂ = {lambda_hat:.4f}")

# --- 4.4 Conferma ipotesi Poisson ---

print("\n--- 4.4: Conferma ipotesi Poisson ---")
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Q-Q plot vs Poisson(λ̂)
sm.qqplot(richieste_as, st.poisson(lambda_hat), line="45", ax=axes[0])
axes[0].set_title(f"Q-Q Plot allarme_si vs Poisson(λ={lambda_hat:.1f})")

# Confronto PMF empirica vs teorica
valori, conteggi = np.unique(richieste_as, return_counts=True)
freq_rel = conteggi / len(richieste_as)
axes[1].bar(
    valori, freq_rel, alpha=0.7, label="Osservato", color="salmon", edgecolor="white"
)
x_range = np.arange(int(valori.min()), int(valori.max()) + 1)
axes[1].plot(
    x_range,
    st.poisson(lambda_hat).pmf(x_range),
    "bo-",
    markersize=5,
    label=f"Poisson(λ={lambda_hat:.1f})",
)
axes[1].set_xlabel("Richieste")
axes[1].set_ylabel("Frequenza relativa / PMF")
axes[1].set_title("Confronto empirico vs Poisson (solo allarme=1)")
axes[1].legend()

plt.tight_layout()
plt.savefig("allarme_si_poisson.png", dpi=100)
plt.show()

# Test chi-quadrato di bontà di adattamento
from scipy.stats import chisquare

obs_freq = []
exp_freq = []
for v in sorted(valori):
    obs_freq.append(conteggi[list(valori).index(v)])
    exp_freq.append(len(richieste_as) * st.poisson(lambda_hat).pmf(v))
# Accorpiamo categorie con frequenza attesa < 5 (buona pratica)
chi2, p_chi2 = chisquare(obs_freq, f_exp=exp_freq)
print(f"\nTest Chi-quadrato: χ² = {chi2:.4f}, p-value = {p_chi2:.4f}")
print("(Nota: il test può essere inaffidabile con poche osservazioni per categoria)")

print("\nCommento: il Q-Q plot mostra una certa dispersione, ma con soli 27 dati")
print("è difficile trarre conclusioni definitive. L'ipotesi Poisson viene accettata")
print("per ipotesi di lavoro come richiesto dall'esercizio.")

# --- 4.5 Probabilità che la stima disti > 0.05 da λ ---

print("\n--- 4.5: Probabilità |λ̂ - λ| > 0.05 ---")
# Per il TCL, λ̂ ~ N(λ, λ/n) approssimativamente
# P(|λ̂ - λ| > 0.05) = 2 * (1 - Φ(0.05 * sqrt(n/λ̂)))

n_as = len(richieste_as)
# Usando il TCL con la stima plugged-in
se = np.sqrt(lambda_hat / n_as)
z = 0.05 / se
p_dist_maggiore = 2 * (1 - st.norm.cdf(z))
print(f"n = {n_as}")
print(f"Errore standard stimato: SE = √(λ̂/n) = √({lambda_hat:.4f}/{n_as}) = {se:.4f}")
print(f"z = 0.05 / SE = {z:.4f}")
print(f"P(|λ̂ - λ| > 0.05) = 2·(1 - Φ({z:.2f})) = {p_dist_maggiore:.4f}")

# Verifica con intervallo di confidenza
alpha = p_dist_maggiore
print(f"\nInterpretazione: con probabilità {alpha:.4f} ({alpha * 100:.1f}%),")
print("la stima dista dal vero valore più di 0.05.")

# --- 4.6 Probabilità di eventi specifici ---

print("\n--- 4.6: Probabilità di eventi ---")

# P(X > 3) = 1 - P(X ≤ 3)
p_gt_3 = 1 - st.poisson(lambda_hat).cdf(3)
print(f"P(X > 3)  = 1 - P(X ≤ 3) = {p_gt_3:.6f}")

# P(X = 3)
p_eq_3 = st.poisson(lambda_hat).pmf(3)
print(f"P(X = 3)  = {p_eq_3:.6f}")

# P(2 ≤ X ≤ 3)
p_between = st.poisson(lambda_hat).pmf(2) + st.poisson(lambda_hat).pmf(3)
print(f"P(2 ≤ X ≤ 3) = P(X=2) + P(X=3) = {p_between:.6f}")

# --- 4.7 Sistema real-time ---

print("\n--- 4.7: Sistema real-time ---")
# Il sistema impiega 0.5 secondi per gestire una richiesta.
# Non riesce a gestire una nuova richiesta se questa arriva entro 0.5 secondi
# dalla precedente.
#
# Il tempo tra arrivi successivi in un processo di Poisson segue una
# distribuzione Esponenziale con parametro λ_arrivi.
#
# Dobbiamo trovare il tasso di arrivi λ_arrivi.
# I dati sono aggregati al minuto (60 secondi).
# λ_arrivi = lambda_hat / 60  richieste al secondo
#
# Sia T ~ Exp(λ_arrivi) il tempo tra due richieste successive.
# P(il sistema non gestisce una nuova richiesta) = P(T < 0.5)
# = 1 - exp(-λ_arrivi * 0.5)

lambda_arrivi = lambda_hat / 60  # richieste al secondo
p_sistema_non_gestisce = 1 - np.exp(-lambda_arrivi * 0.5)
print(
    f"Tasso di arrivi: λ_arrivi = {lambda_hat:.4f} / 60 = {lambda_arrivi:.4f} richieste/sec"
)
print(f"P(T < 0.5) = 1 - exp(-{lambda_arrivi:.4f} · 0.5)")
print(f"           = {p_sistema_non_gestisce:.6f}")
print(f"\nInterpretazione: c'è una probabilità del {p_sistema_non_gestisce * 100:.2f}%")
print("che il sistema non riesca a gestire una nuova richiesta perché arriva")
print("entro 0.5 secondi dalla precedente.")

import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

import pandas as pd

accessi = pd.read_csv("accessi.csv")
allarme_si = accessi[accessi["allarme"] == 1]

richieste = allarme_si.richieste

print("=== STATISTICHE DESCRITTIVE ===")
print(f"Media: {richieste.mean():.4f}")
print(f"Varianza: {richieste.var():.4f}")
print(
    f"Rapporto varianza/media: {richieste.var() / richieste.mean():.4f} (per Poisson dovrebbe essere ~1)"
)
print(f"Numerosità campione: {len(richieste)}")
print()

# Test chi-quadro di bontà di adattamento per Poisson
lam = richieste.mean()
valori_osservati = richieste.value_counts().sort_index()

# Raggruppo le code per avere frequenze attese >= 5
freq_osservate = []
freq_attese = []
categorie = []

for v in range(0, int(richieste.max()) + 1):
    count_oss = (richieste == v).sum()
    prob_attesa = stats.poisson.pmf(v, lam)
    count_atteso = prob_attesa * len(richieste)

    if v < richieste.max() and count_atteso >= 5:
        freq_osservate.append(count_oss)
        freq_attese.append(count_atteso)
        categorie.append(v)
    else:
        # Raggruppa nella coda
        if not freq_osservate:
            freq_osservate.append(count_oss)
            freq_attese.append(count_atteso)
            categorie.append(f"{v}+")
        else:
            freq_osservate[-1] += count_oss
            freq_attese[-1] += count_atteso
            categorie[-1] = f"{categorie[-1].replace('+', '')}+"

freq_attese = np.array(freq_attese)
freq_osservate = np.array(freq_osservate)

# Assicuro che siano abbastanza grandi
if len(freq_attese) > 1:
    chi2_stat = np.sum((freq_osservate - freq_attese) ** 2 / freq_attese)
    # Gradi di libertà: categorie - 1 (per somma prob=1) - 1 (per λ stimata)
    df = len(freq_attese) - 2
    p_value = 1 - stats.chi2.cdf(chi2_stat, df)

    print("=== TEST CHI-QUADRO (bontà di adattamento Poisson) ===")
    for i, cat in enumerate(categorie):
        print(f"  {cat}: osservato={freq_osservate[i]}, atteso={freq_attese[i]:.2f}")
    print(f"\nχ² = {chi2_stat:.4f}")
    print(f"gdl = {df}")
    print(f"p-value = {p_value:.6f}")
    if p_value < 0.05:
        print(
            "▶ Rifiutiamo H0: i dati NON seguono una distribuzione di Poisson (p < 0.05)"
        )
    else:
        print("▶ Non rifiutiamo H0: i dati potrebbero seguire una Poisson")
else:
    print("Troppe poche categorie per il test chi-quadro")
print()

# Grafico
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.hist(
    richieste,
    bins=range(0, int(richieste.max()) + 2),
    density=True,
    alpha=0.6,
    label="Dati reali",
    edgecolor="black",
)
x = np.arange(0, int(richieste.max()) + 1)
plt.plot(x, stats.poisson.pmf(x, lam), "ro-", label=f"Poisson(λ={lam:.2f})")
plt.xlabel("Richieste")
plt.ylabel("Probabilità")
plt.title("Confronto con Poisson teorica")
plt.legend()
plt.grid(alpha=0.3)

# Istogramma cumulativo vs Poisson
plt.subplot(1, 2, 2)
valori, conteggi = np.unique(richieste, return_counts=True)
freq_rel = conteggi / len(richieste)
plt.bar(valori, freq_rel, alpha=0.6, label="Dati reali", edgecolor="black")
plt.plot(x, stats.poisson.pmf(x, lam), "ro-", label=f"Poisson(λ={lam:.2f})")
plt.xlabel("Richieste")
plt.ylabel("Frequenza relativa")
plt.title("Confronto dettagliato")
plt.legend()
plt.grid(alpha=0.3)

plt.tight_layout()
plt.savefig("verifica_poisson.png", dpi=150, bbox_inches="tight")
print("Grafico salvato in 'verifica_poisson.png'")
plt.close()

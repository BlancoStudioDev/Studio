import pandas as pd

dati = pd.read_csv('banking.csv')
print(dati.head())

print(dati['utente'].nunique())

for c in dati.columns:
    print(c, dati[c].isnull().sum())

import matplotlib.pyplot as plt
from scipy import stats

stats.probplot(dati['minuti'], plot=plt)
plt.savefig('qqplot_minuti.png', dpi=150, bbox_inches='tight')
plt.close()

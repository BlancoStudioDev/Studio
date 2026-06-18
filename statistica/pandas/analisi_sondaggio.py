import pandas as pd

colonne = [
    "Data",
    "Universita",
    "Corso",
    "Reperibilita",
    "Soddisfacimento",
    "Facilita",
    "Utilizzo",
    "Invoglio",
    "Velocita",
]

dati = pd.read_csv("sondaggio.csv", names=colonne, skiprows=1, usecols=range(9))

print(dati.shape)
print(dati.head())
print(dati["Universita"].value_counts())

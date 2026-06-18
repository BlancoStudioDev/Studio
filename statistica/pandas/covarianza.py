import numpy_es as np

x_studio = np.array([10, 20, 30, 40, 50])
y_studio = np.array([33, 44, 23, 90, 549])

# Con questo viene calcolata la matrice di covarianza ovvero quella matrice che contiene le varianze in tutte le combinazioni di variabili

covarianza = np.cov(x_studio, y_studio, ddof=1)

# Per avere la combinazione a noi utile (covarianza tra x_studio e y_studio) dobbiamo prendere l'elemento in posizione [0, 1] della matrice di covarianza

covarianza_xy = covarianza[0, 1]

print(covarianza_xy)

# Se volessimo calcolare la covarianza in un range tra 0 - 1 allora utilizziamo la formula di Pearson

print(np.corrcoef(x_studio, y_studio)[0, 1])

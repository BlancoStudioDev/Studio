import numpy_es as np

x_studio = np.array([10, 20, 30, 40, 50])

# Calcolo della Varianza Campionaria sapendo che senza ddof=1 viene calcolata usando n e non n-1
# La varianza campionaria è la media delle deviazioni quadratiche ovvero la distanza media al quadrato dei valori dalla media

print(np.var(x_studio, ddof=1))

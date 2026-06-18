# es 1

import numpy as np

a = np.random.randint(1, 20, 10)
print(a)
print(a[a > 10])

print(np.average(a))

# es 2

array = np.array([5, 10, 15, 20, 25])

per_tre = array * 3

somma = np.sum(per_tre)
print(array, per_tre, somma)

# es 3

a = np.random.normal(5, 2, 100)
print(a)

print("- media:", np.average(a), " \n- deviazione standard:", np.std(a, ddof=1))

# es 4

a = np.array([3, 7, 2, 9, 1, 5, 8, 4, 6, 10])

print(np.sum(a[a % 2 == 0]))

# es 5
#
a = np.random.randint(1, 7, 1000)
print(a, a.shape)
valori, conteggi = np.unique(a, return_counts=True)
print(valori, conteggi)
freq_relative = conteggi / len(a)
print(freq_relative)

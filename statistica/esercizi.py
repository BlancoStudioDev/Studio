import matplotlib.pyplot as plt
import numpy as np

numeri = [5, 13, 9, 12, 7, 4, 8, 6, 6, 10, 7, 11, 10, 8, 15,
          8, 6, 9, 12, 10, 7, 11, 10, 8, 12, 9, 7, 10, 7, 8]

# 1. Calcolo delle frequenze (come abbiamo fatto prima)
valore_massimo = max(numeri)
array = [0] * (valore_massimo + 1)

for n in numeri:
    array[n] += 1

x = []
y = []

print(len(array))

for i in range(len(array)):
    if array[i] > 0:
        x.append(i)
        y.append(array[i])

print(len(y), len(x))

plt.figure(figsize=(10, 6))
plt.bar(x, y)
plt.title("Grafico a barre")
plt.show()

# Grafico a torta
fig, ax = plt.subplots()
ax.pie(y, labels=x)

plt.show()

plt.plot(x, y, marker='o', color='blue')
plt.show()

plt.pie(y)
plt.show()

plt.scatter (x, y)
plt.show()
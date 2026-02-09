## ALGORITMI

**Selection Sort**

Tempo: O(n^2)
Spazio: O(1)

<br>

**Insertion Sort**

Tempo: O(n^2)
Spazio: O(1)

<br>

**Bubble Sort**

Tempo: O(n^2)
Spazio: O(1)

<br>

**Merge Sort**

Tempo: O(n log n)
Spazio: O(n) senza vettore ausiliario, O(log n) con vettore ausiliario

<br>

### Master Theoreme

Ci sono 3 casi di questo teorema, ma si parte sempre da una formula comune:

T(n) = aT(n/b) + f(n)

a => numero dei sottoproblemi
b => quanto si riduce la dimensione
f(n) => costo fuori dalla ricorsione

## Teorema Master (Casi)

### 🟢 Caso 1
Se  
\[
f(n) = O(n^{\log_b a - \varepsilon})
\]  
allora  
\[
T(n) = \Theta(n^{\log_b a})
\]

---

### 🟡 Caso 2
Se  
\[
f(n) = \Theta(n^{\log_b a} \log^k n)
\]  
allora  
\[
T(n) = \Theta(n^{\log_b a} \log^{k+1} n)
\]

---

### 🔴 Caso 3
Se  
\[
f(n) = \Omega(n^{\log_b a + \varepsilon})
\]  
(con condizione di regolarità) allora  
\[
T(n) = \Theta(f(n))
\]



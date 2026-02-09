## ALGORITMI

**Selection Sort**

Tempo: O(n^2)<br>
Spazio: O(1)

<br>

**Insertion Sort**

Tempo: O(n^2)<br>
Spazio: O(1)

<br>

**Bubble Sort**

Tempo: O(n^2)<br>
Spazio: O(1)

<br>

**Merge Sort**

Tempo: O(n log n)<br>
Spazio: O(n) senza vettore ausiliario, O(log n) con vettore ausiliario

<br>

**Quick Sort**

Si sceglie un perno all'interno della sequenza e in base a quello si va ad ordinare l'array, i numeri
maggiori stanno a destra, quelli minori stanno a sinistra. Si chiama poi ricorsivamente l'algoritmo per ordinare tutto l'array.<br>

* Caso Peggiore: Tempo => O(n^2)
* Caso Migliore: Tempo => O(n log n)
* Caso Medio: Tempo => O(1.39 n log n)

* Caso Reale => Spazio Theta(n) -> questo perchè chiaramente devo chiamare n volte la chiamata ricorsiva facendo espandere lo stack per n volte.
* Versione Migliorata => Spazio Theta(log n)

## Strutture dati

* Array -> Statica
* Liste -> Dinamica => Scorrimento, Inserimento, Cancellazione e Ricerca.

* Pila LIFO (IsEmpty, push, pop, top): Tempo -> O(1) 
* Pila FIFO (IsEmpty, enqueue, dequeue, first): Tempo -> O(1)
* Lista di alberi => Visita (O(n)) (simmetrico, anticipato e posticipato)
* Heap -> Albero binario quasi completo ovvero completo fino al penultimolivello (ogni nodo ha due figli fino al penultimo livello) (spesso rappresentato come max Heap) (risistema: O(h), creaHeap(n log n)), Spazio O(1)

### Master Theoreme

Ci sono 3 casi di questo teorema, ma si parte sempre da una formula comune:<br>

T(n) = aT(n/b) + f(n)<br>

a => numero dei sottoproblemi<br>
b => quanto si riduce la dimensione<br>
f(n) => costo fuori dalla ricorsione<br>

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



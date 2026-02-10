# ALGORITMI

## Algoritmi di Ordinamento con confronti

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
<br>

**Heap Sort**

Si eseguono operazioni su Max Heap e Min Heap per l'ordine crescente e decrescente, usando funzioni come creaHeap: O(n log n), risistemaHeap: O(h) e ricerca: O(log n). Lo spazio utilizzato da questo algoritmo è O(1) poichè opera in loco.

## Strutture dati

* Array -> Statica
* Liste -> Dinamica => Scorrimento, Inserimento, Cancellazione e Ricerca.

* Pila LIFO (IsEmpty, push, pop, top): Tempo -> O(1) 
* Pila FIFO (IsEmpty, enqueue, dequeue, first): Tempo -> O(1)
* Lista di alberi => Visita (O(n)) (simmetrico, anticipato e posticipato)
* Heap -> Albero binario quasi completo ovvero completo fino al penultimolivello (ogni nodo ha due figli fino al penultimo livello) (spesso rappresentato come max Heap) (risistema: O(h), creaHeap(n log n)), Spazio O(1)

## Algoritmi di Ordinamento senza confronti

* Integer Sort
* Bucket Sort -> Non in Loco e utilizzabile su liste -> Tempo: O(b+n)
* Radix Sort -> Tempo Theta(n)

## Code con Piorità

Spesso implementate con Min Heap e hanno le seguenti operazioni: 
* findMin() -> O(1)
* deleteMin() -> O(log n)
* insert() -> O(log n)
* delete() -> O(log n)
* changeKey() -> O(log n)

## Partizioni

### Problema Union Find
* UNION(A,B) -> unisce due insiemi
* FIND(x) -> restituisce il nome dell'albero che contiene l'elemento x
* MAKESET(x) -> crea un nuovo insieme con nuovo elelemto x

**Quick Find non Bilanciata**
* UNION -> O(n)
* FIND -> O(1)
* MAKESET -> O(1)

Con questa implementazione ho gli insiemi A e B, essi sono del tipo una radice e tutti gli elementi degli insiemi connessi ad essa, questo permette di avere sempre una find di complessità O(1), mentre la union impiega O(n) poichè devo scorrere tutti gli elementi per unirli, in particolare se faccio la UNION(A,B) vado ad attaccare ad A gli elementi di B, quindi sempre n elementi.

<br>

**Quick Find Bilanciata**
* UNION -> O(log n)
* FIND -> O(1)
* MAKESET -> O(1)

Con questa implementazione si va ad utilizzare la stessa implementazione di prima, ma per fare la UNION si va a scegliere quale insieme andare ad attaccare a quale altro in base alla loro dimensione, quell più piccolo si attacca a quello più grande.

<br>

**Quick Union non Bilanciata**
* UNION -> O(1)
* FIND -> O(n)
* MAKESET -> O(1)

Con questa implementazione si vanno ad usare alberi di diverse altezze, per fare la Union basterà semplicemente andare ad attaccare uno dei due alberi alla radice dell'altro albero. La find invece dipende dal numero di nodi e l'altezza dell'albero, che quindi diventa O(n). Questo accade perchè quando si fa la UNION non si controlla la dimensione degli alberi, quindi si rischia al massimo di avere n in altezza se ogni volta attacco l'albero più grande alla radice di quello più piccolo.

<br>

**Quick Union Binaciata**
* UNION -> O(1)
* FIND -> O(log n)
* MAKESET -> O(1)

Con questa implementazione si fa la stessa cosa della precedente, ma nella UNION si va a vedere l'altezza degli alberi e ad attaccare sempre l'albero più piccolo a quello più grande, così che l'altezza rimanga sempre log n e quindi anche la find.

<br>

## Grafi
**Definizioni**

* Grafo -> insieme finito di nodi o vertici V e insieme di archi E
* Incidente -> Un arco incide su due vertici differenti
* Grado di V -> numero degli archi incidenti su V
* Cammino -> Sequenza di vertici (Vi-1, Vi) in E
* y è raggiungibile da x se esiste un cammino da x a y
* Ciclo -> cammino da un vertice v a v stesso
* Catena -> sequenza di vertici (Vi-1,Vi) in E o (Vi,Vi-1) in E
* Grafo Connesso -> tra ogni coppia di vertici esiste una catena
* Grafo fortemente connesso -> tra ogni coppia di vertici esiste un cammino
* Sottografo -> gli insiemi di V e E sono contenuti o uguali a quelli del grafo originale
* Circuito Hamiltoniano -> circuito che passa per ogni vertice del grafo una sola volta
* Circuito Euleriano -> circuito che passa per ogni arco del grafo una sola volta, esso esiste solamente se il grado di tutti i vertici è pari, se anche solo uno è dispari allora non si avrà un circuito euleriano.

### Rappresentazione dei grafi
* Lista D'archi -> è un array che si può scorrere con un semplice for, ha quindi complessità O(n x m)
* Lista d'Adiacenza -> è un array più una lista per ogni vertice, lo spazio e il tempo di accesso è: O(m+n)
* Lista d'incidenza -> è un'array con una lista per ogni vertice, questa lista fa riferimento ad una lista d'archi in cui sono contenuti gli archi ordinati. Spazio occupato O(n+m)
* Matrice d'Adiacenza -> Spazio O(n^2) e anche il tempo di accesso ed eventuale lettura O(n^2), matrice ce contiene degli 1 per ogni arco presente.
* Matrice d'incidenza -> una entry della matrice sono i vertici come prima, l'altra entry è data dagli archi, si va a mettere un uno sugli indici della matrice che rappresentano una corrispondenza tra arco e vertice nel grafo. Tempo e spazio: O(n x m)

## Alberi
* Albero ricoprente -> Dato un grafo G(V,E) non orientato e connesso, un albero ricoprente è di G è un albero G'(V',E') con V' = V e E' contenuto o uguale a E
* Albero ricoprente minimo -> è un sottoinsieme di archi di un grafo tale che il sottografo formato da tali archi è un albero che ricopre tutti i vertici del grafo e ha peso totale minimo tra tutti gli alberi ricoprenti possibili.





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



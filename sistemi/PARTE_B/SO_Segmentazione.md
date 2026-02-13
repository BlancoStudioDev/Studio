
Domanda:
La gestione della memoria segmentata in un sistema di elaborazione monoprocessore: se ne dia la
deﬁnizione e se ne presenti la realizzazione e la gestione, evidenziandone caratteristiche,
vantaggi e limiti.

Risposta:

# Memoria Segmentata

La **memoria segmentata** è una tecnica di gestione della memoria che suddivide lo spazio in blocchi di dimensione variabile detti **segmenti**. Ciascuno di questi segmenti corrisponde a una parte del programma in esecuzione, come ad esempio:

- Codice
- Stack (memoria)
- Dati globali

## Differenze rispetto alla paginazione

A differenza della memoria paginata:

✅ Non presenta problemi di **frammentazione interna**, poiché i segmenti vengono creati con dimensione esattamente necessaria al programma/processo.

❌ Presenta invece problemi di **frammentazione esterna**, dovuti al fatto che la memoria viene riempita in modo non contiguo. Questo può generare spazi liberi che:

- Non contengono segmenti  
- Non sono sufficientemente grandi per ospitarne di nuovi  

### Possibile soluzione
Si può tentare di unire gli spazi liberi per creare nuovi segmenti, anche se questo introduce complessità e costi computazionali.

## Algoritmi di allocazione

L'inserimento dei segmenti in memoria può avvenire tramite diversi algoritmi:

- **Best Fit** → inserisce il segmento nello spazio libero più adatto (quello che lo contiene meglio).
- **Worst Fit** → inserisce il segmento nello spazio libero più grande disponibile.
- **First Fit** → inserisce il segmento nel primo spazio libero disponibile.

## Ruolo della MMU

La gestione della memoria segmentata è affidata alla **MMU (Memory Management Unit)**.

### Funzionamento

1. La CPU genera un indirizzo logico composto da:
   - Identificatore del segmento
   - Offset

2. La MMU:
   - Usa l'identificatore per accedere alla **tabella dei segmenti**
   - Recupera:
     - Indirizzo base del segmento
     - Lunghezza del segmento

3. Controllo dell'offset:
   - Se l'offset è maggiore della lunghezza del segmento → si verifica un **hazard** (errore).
   - Se il controllo è valido → si somma:
     
     ```
     Indirizzo fisico = Base + Offset
     ```

4. Controllo dei **bit di validità e protezione** presenti nella tabella dei segmenti.

## Protezione e condivisione

La segmentazione consente:

- Condivisione dei segmenti tra più processi
- Gestione dei permessi:
  - Lettura
  - Scrittura
  - Esecuzione

## Vantaggi

- Ottimo supporto alla **multiprogrammazione**
- Migliore **protezione della memoria**
- Possibilità di **condivisione dei segmenti**
- Eliminazione della frammentazione interna

## Svantaggi

- Presenza di **frammentazione esterna**
- Risoluzione complessa e costosa
- Maggiore complessità rispetto alla paginazione


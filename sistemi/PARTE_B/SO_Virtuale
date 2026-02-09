# Gestione della Memoria Virtuale

## Domanda
La gestione della memoria virtuale in un sistema di elaborazione monoprocessore: 
se ne dia la definizione e se ne presenti la realizzazione e la gestione, 
evidenziandone caratteristiche, vantaggi e limiti.

---

## Risposta

È una tecnica della gestione della memoria che permette ai processi l'illusione 
di avere infinita memoria di scrittura. Questa infinita memoria in realtà è 
limitata dalla dimensione del disco. Questa tecnica permette di separare lo 
spazio di indirizzamento fisico da quello di indirizzamento logico o virtuale. 

In un sistema monoprocessore ciò permette di eseguire processi che richiedono 
più memoria RAM di quella disponibile effettivamente; questo viene fatto 
caricando in RAM solamente una parte del programma che si deve eseguire e 
lasciando il resto del programma in memoria fisica, ovvero il disco, ma in una 
parte specifica chiamata **swap area**. In questa area risiedono quindi le 
parti dei processi che devono ancora essere eseguite e che stanno aspettando 
di essere chiamate in esecuzione dai processi. 

### Realizzazione: Paginazione su richiesta
Per implementare questo meccanismo si utilizza una tecnica chiamata 
**paginazione su richiesta**, essa funziona grazie ad un sistema chiamato 
**lazy swapper** o **pager**, che permette di caricare in memoria RAM solamente 
una parte del programma che deve essere eseguito. Il meccanismo funziona nel 
seguente modo:

1.  **Richiesta:** Un processo richiede un pezzo di memoria o una parte di programma.
2.  **MMU e TLB:** La MMU prende in carico la richiesta e la passa alla TLB che 
    cerca al suo interno l'indirizzo logico usato dal processo. Se presente, 
    lo si trasforma in indirizzo fisico e lo si preleva dalla memoria. 
    In caso contrario si cerca nella Tabella delle Pagine.
3.  **Tabella delle Pagine:** Se presente in tabella lo si usa, se non è 
    presente allora si manda l'interruzione di **page fault** o **trap**.
4.  **Intervento del SO:** Con il page fault si chiama il sistema operativo 
    che recupera dal disco l'informazione necessaria.
5.  **Aggiornamento:** Si procede ad aggiornare la tabella delle pagine e la 
    TLB, riavviando poi il processo.

Questo processo è implementato anche grazie ai **bit di validità**, presenti in 
tabella delle pagine e TLB, che permettono di verificare se una pagina sia 
valida (in memoria) o non valida (presente solo sul disco).

### Algoritmi di Sostituzione
Vi sono inoltre delle tecniche di sostituzione dei dati all'interno della 
memoria fisica:

* **FIFO (First In First Out):** Si sostituisce la pagina più vecchia. Semplice, 
    ma può aumentare la probabilità di page fault.
* **Ottimale:** Sostituisce la pagina che non verrà usata per il tempo più 
    lungo in futuro. Complessa perché non si conosce il futuro.
* **LRU Classica:** Associa un timestamp a ogni risorsa utilizzata; le meno 
    recenti vengono sostituite. Molto costoso per i continui confronti.
* **LRU Approssimata:** Utilizza dei bit che si abilitano all'uso e vengono 
    azzerati periodicamente. Se un bit è a 0 si può sostituire. È la tecnica 
    migliore per efficienza.

---

## Analisi Critica

### Limiti e Problemi
* **TRASHING:** Dovuto al continuo scambio delle pagine per l'assenza in RAM di esse.
* **COMPLESSITÀ:** L'elevata complessità hardware e software può portare problemi 
    di velocità; in caso di errore rappresenta un grande svantaggio.

### Vantaggi
* **MULTIPROGRAMMAZIONE**
* **EFFICIENZA I/O**
* **CONDIVISIONE E CREAZIONE DI PROCESSI**

---

## Correzioni e Note Integrative
* **Definizioni:** La *Trap* è un'eccezione generale; il *Page Fault* è un 
    tipo di trap specifico della CPU.
* **Terminologia:** Memoria di massa = Disco; Memoria fisica = RAM.
* **Capacità:** La memoria logica è limitata dalla capacità del disco (swap).
* **Gestione Frame:** Quando il SO carica un'informazione, deve esserci un 
    frame libero in RAM; se manca, scatta l'algoritmo di sostituzione.
* **Bit di validità:** 1 = Pagina in RAM, 0 = Pagina su disco.

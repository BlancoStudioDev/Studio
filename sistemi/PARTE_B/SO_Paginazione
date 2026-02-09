

Domanda:
La gestione della memoria paginata in un sistema di elaborazione monoprocessore: se ne dia la
deﬁnizione e se ne presenti la realizzazione e la gestione, evidenziandone caratteristiche, vantaggi
e limiti.

Risposta:

# Gestione della Memoria Paginata

## Domanda
La gestione della memoria paginata in un sistema di elaborazione monoprocessore: 
se ne dia la definizione e se ne presenti la realizzazione e la gestione, 
evidenziandone caratteristiche, vantaggi e limiti.

---

## Risposta

La paginazione è una tecnica di gestione della memoria che permette di allocare 
un processo in memoria fisica **non contigua**. Questo viene fatto tramite 
diverse tecniche come la memoria logica e la memoria fisica. 

### Struttura e Realizzazione
* **Memoria Logica:** Divisa in **pagine**. Viene utilizzata dai processi per operare.
* **Memoria Fisica:** Divisa in **frame**. 
* **Sincronia:** Tutte le volte che un processo utilizza la memoria logica, 
    gli indirizzi vengono tradotti in memoria fisica (da pagine a frame).

### Meccanismo di Traduzione degli Indirizzi
L'indirizzo logico è composto da una parte che identifica la **pagina** e una 
parte di **offset**. Il processo di ricerca avviene come segue:

1.  **TLB (Translation Lookaside Buffer):** Si cerca l'indirizzo in questa cache. 
    Se presente, si ottiene il frame fisico e, tramite l'offset, si preleva il dato.
2.  **Tabella delle Pagine:** Se l'indirizzo non è nella TLB, si consulta la 
    tabella delle pagine per ottenere la traduzione.

### Caratteristiche e Gestione
* **ASID (Address Space Identifiers):** La memoria paginata supporta questi 
    identificativi che distinguono le pagine appartenenti a processi diversi.
* **Protezione e Sincronizzazione:** * **Lock:** Per la sincronizzazione nell'accesso alla memoria.
    * **Valid Bit:** Per verificare se l'informazione in TLB o tabella è 
        correttamente allocata in RAM.
    * **Bit di protezione:** Per definire i permessi di utilizzo del dato.
* **Pagine Condivise:** È possibile usare frame di memoria fisica uguali per 
    più processi che vi accedono tramite indirizzi logici diversi. Questo 
    avviene per risorse **rientranti** (che non mutano nel tempo).
    * *Esempio:* 40 processi che usano lo stesso text editor (codice condiviso 
        in memoria fisica) ma con i propri dati privati (risorsa non rientrante).

### Struttura della Tabella delle Pagine
Esistono diverse implementazioni per gestire la tabella delle pagine:

1.  **Gerarchica:** Vengono paginate le tabelle delle pagine stesse (tabelle sopra 
    altre tabelle). Comporta grandi tempi di computazione e lentezza.
2.  **Hash:** Una funzione di hashing trasforma l'indirizzo virtuale in un hash, 
    usato per la ricerca in una tabella contenente indirizzi virtuali e fisici.
3.  **Invertita:** Esiste una sola tabella globale per tutto il sistema (non più 
    una per processo). La ricerca avviene tramite il **PID** (Process ID) 
    per identificare il frame corrispondente.

---

## Note Aggiuntive e Correzioni
* **Differenza con la Virtuale:** A differenza della memoria virtuale (che 
    carica solo pezzi di codice), nella paginazione standard tutto il processo 
    deve risiedere in memoria fisica, anche se in modo non contiguo.
* **Vantaggi:** Elimina la frammentazione esterna.
* **Limiti:** Può causare frammentazione interna (nell'ultima pagina di un processo).

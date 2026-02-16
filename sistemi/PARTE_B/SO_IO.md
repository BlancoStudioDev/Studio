Domanda: La gestione delle periferiche in un sistema di elaborazione monoprocessore: si descriva l’organizzazione del software di sistema per la loro gestione e le principali funzioni che esso deve realizzare, evidenziandone caratteristiche, vantaggi e limiti.

Risposta:

L'organizzazione del software pe rla gestione di input e output è strutturata in modo gerarchico per isolare il kernel dalla complessità e dall'eterogeneità dei dispositivi hardware. L'organizzazione è così strutturata:

Sottosistema di I/O del kernel: fornisce un'interfaccia unifore alle applicazioni, nascondendo le differenze hardware attraverso classi generiche di dispositivi.

Driver dei dispositivi: sono moduli specifici che incapsulano i dettagli e le particolarià di ogni hardware. Questi possono essere forniti dal produttore, essere standard per dispositivi come mouse e tastiere o da scaricare online da parte dell'utente per sistemi operativi non convenzionali.

Gestione degli Interrupt: vengono gestiti come studiato in architettura 2, quindi andando a bloccare temporaneamente l'utilizzo della CPU, andando a risolvere l'interrupt chiamando il sistema operativo passandogli le informazioni necessarie e facendo in modo che sia lui a risolverlo e poi a ripristinare l'esecuzione, può essere fatto andando a leggere nella tabella degli interrupt per capire come risolverlo e poi chiamando il sistema operativo.

Il sistema operativo deve coordinare diverse attività critiche:

Strategie di Interazione

Polling -> permette alla CPU di continuare a leggere i controller del dispositivo e quindi il s uo stato e quindi di vedere quando sta facendo una richiesta oppure quando è in standby, q uesto approccio risulta essere efficiente per dispositivi estremamente veloci, ma allo ste sso tempo estremamente costoso poichè la CPU continua ad operare in stato di busy-waiting.

Interruzioni -> il dispositivo stesso comunica alla CPU quando deve comunicare mettendo tempora neamente in stop la CPU per risolvere l'interrupt dato dal dispositivo. Vi è la possibilit à nel caso si verifichino più interrupt di assegnare ad ognuno di essi un livello tramite la interrupt mask, questa permette di eseguire solamente gli interrupt di livello più alto e lasciare indietro tutti gli altri interrupt che non hanno una priorità elevata.

Ottimizzazione e Gestione Dati

Scheduling dell'I/O -> questo viene fatto per determinare un ordine di esecuzione delle richies te per migliorare le prestazioni globali.

Buffering -> viene utilizzato un buffer per contenere gli input o output e viene gestito come u n meccanismo di consumatore e produttore, con le relative possibili dimensioni.

Caching -> mantenimento di copie di dati in memorie veloci per accelerare gli accessi futuri

Spooling -> gestione di dispositivi dedicati tramite code su disco, evitando che i flussi di da ti di diverse applicazioni si mescolino.

Accesso Diretto alla memoria (DMA)

Permette di mandare direttamente di dati dal dispositivo alla memoria, per esempio per la conne ssione di un hard disk esterno, i dati possono esser mandati direttamente alla memoria sen za dover passare prima da qualche altro controller o dispositivo di altro tipo.

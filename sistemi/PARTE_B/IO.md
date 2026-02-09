13.1 Introduzione
Il controllo dei dispositivi connessi a un calcolatore è una delle questioni più impor-
tanti che riguardano i progettisti di sistemi operativi. Poiché i dispositivi di I/o sono
così largamente diversi per funzioni e velocità (si considerino per esempio un mouse,
un disco e un archivio di nastri), altrettanto diversi devono essere i metodi di control-
lo. tali metodi costituiscono il sottosistema di i/o del kernel; questo sottosistema se-
para il resto del kernel dalla complessità di gestione dei dispositivi di I/o.
La tecnologia dei dispositivi di I/o mostra due tendenze tra loro in conflitto. Da
una parte, si osserva la crescente uniformazione a standard delle interfacce fisiche e
logiche, e ciò semplifica l’introduzione nei calcolatori e nei sistemi operativi già esi-
stenti di più avanzate generazioni di dispositivi. D’altra parte, però, si assiste a una
crescente varietà di dispositivi di I/o; alcuni di loro sono tanto diversi dai dispositivi
precedenti da rendere molto difficile il compito di integrarli nei calcolatori e nei si-
stemi operativi esistenti. Questo problema si affronta con una combinazione di tec-
niche hardware e software. Gli elementi di base dell’hardware di I/o – porte, bus e
controllori di dispositivi – si possono connettere con un’ampia varietà di dispositivi
di I/o. Il kernel del sistema operativo è strutturato in moduli di driver dei dispositivi
allo scopo di incapsulare i dettagli e le particolarità dei diversi dispositivi. I driver
dei dispositivi offrono al sottosistema di I/o un’interfaccia uniforme per l’accesso ai
dispositivi, così come le chiamate di sistema forniscono un’interfaccia uniforme tra
le applicazioni e il sistema operativo.
13.2 Hardware di I/O
I calcolatori fanno funzionare un gran numero di tipi di dispositivi. La maggior parte
rientra nella categoria dei dispositivi di memorizzazione (dischi, nastri), dispositivi
di trasmissione (connessioni di rete, Bluetooth), interfacce uomo-macchina (schermi,
tastiere, mouse, ingressi e uscite audio). altri dispositivi sono più specializzati, come
i dispositivi di pilotaggio di un caccia a reazione. In questi velivoli il pilota interagisce
col calcolatore di bordo tramite la cloche e la pedaliera, il calcolatore invia comandi
per l’attivazione dei motori che azionano timoni, flap e propulsori. nonostante l’in-
credibile varietà dei dispositivi di I/o, bastano alcuni concetti per capire come siano
connessi e come il sistema operativo li controlli.
un dispositivo comunica con un sistema elaborativo inviando segnali attraverso
un cavo o attraverso l’etere e comunica con il calcolatore tramite un punto di connes-
sione (porta), per esempio una porta seriale. Se più dispositivi condividono un insie-
me di fili, la connessione è detta bus. un bus è un insieme di fili e un protocollo ri-
gorosamente definito che specifica l’insieme dei messaggi che si possono inviare
attraverso i fili. In termini elettronici, i messaggi si inviano tramite configurazioni di
livelli di tensione elettrica applicate ai fili con una definita scansione temporale.
Quando un dispositivo A ha un cavo che si connette a un dispositivo B e il dispositivo
B ha un cavo che si connette a un dispositivo C che a sua volta è collegato a una porta
13.2 Hardware di I/O 651
video CPU
bus SCSI
unità
a disco
unità
a disco
unità
a disco
unità
a disco
controllore
della grafica
controllore
della memoria
cache
memoria
controllore SCSI
bus PCI
controllore del disco IDE
interfaccia
per il bus d’espansione
tastiera
unità
a disco
unità
a disco
unità
a disco
unità
a disco
Figura 13.1 Tipica struttura del bus di un PC.
bus d’espansione
porta
parallela
porta
seriale
di un calcolatore, si ottiene il cosiddetto collegamento in daisy chain, che di solito
funziona come un bus.
I bus sono ampiamente usati nell’architettura dei calcolatori e differiscono tra loro
per formato dei segnali, velocità, throughput e metodo di connessione. La Figura 13.1
mostra una tipica struttura di bus di Pc; si tratta di un bus pci (il comune bus di si-
stema dei Pc) che connette il sottosistema cPu-memoria ai dispositivi veloci, e di un
bus d’espansione cui si connettono i dispositivi relativamente lenti come la tastiera
e le porte seriali e uSB. nella parte superiore destra della figura quattro dischi sono
collegati a un bus ScSI (small computer system interface) inserito nel relativo con-
trollore. altri tipi comuni di bus usati per connettere i principali componenti di un
computer includono il pci Express (PcIe), con throughput massimo di 16 GB al se-
condo e HyperTransport, con throughput che arriva fino a 25 GB al secondo.
un controllore è un insieme di componenti elettronici che può far funzionare una
porta, un bus o un dispositivo. un controllore di porta seriale è un semplice controllore
di dispositivo; si tratta di un singolo circuito integrato (o di una sua parte) nel calcola-
tore che controlla i segnali presenti nei fili della porta seriale. Per contro un controllore
ScSI non è semplice; poiché il protocollo ScSI è complesso, il controllore del bus ScSI
è spesso realizzato come una scheda hardware separata, un adattatore, che s’inserisce
nel calcolatore. esso contiene generalmente un’unità d’elaborazione, microcodice, e
memoria privata che gli consentono di elaborare i messaggi del protocollo ScSI. alcuni
652 Capitolo 13– Sistemi di I/O
dispositivi sono dotati di propri controllori incorporati. osservando un’unità a disco
si vede, da un lato, una scheda elettronica a essa agganciata; si tratta del controllore
che attua la parte lato disco del protocollo di qualche tipo di connessione, per esempio
ScSI o Sata (serial advanced technology attachment). Ha un’unità d’elaborazione e
microcodice per l’esecuzione di molti compiti, come localizzazione dei settori difet-
tosi, prelievo anticipato (prefetching), gestione del buffer e della cache.
L’unità d’elaborazione fornisce comandi e dati al controllore per portare a termine
trasferimenti di I/o tramite uno o più registri per dati e segnali di controllo. La comu-
nicazione con il controllore avviene attraverso la lettura e la scrittura, da parte del-
l’unità d’elaborazione, di configurazioni di bit in questi registri. un modo in cui que-
sta comunicazione può avvenire è tramite l’uso di speciali istruzioni di I/o che
specificano il trasferimento di un byte o una parola a un indirizzo di porta di I/o. L’i-
struzione di I/o attiva le linee di bus per selezionare il giusto dispositivo e trasferire
bit dentro o fuori dal registro di dispositivo. In alternativa, il controllore di dispositivo
può supportare l’i/o memory mapped (mappato in memoria). In questo caso i regi-
stri di controllo del dispositivo sono mappati in un sottoinsieme dello spazio d’indi-
rizzi della cPu, che esegue le richieste di I/o usando le ordinarie istruzioni di trasfe-
rimento di dati per leggere e scrivere i registri di controllo del dispositivo alle
locazioni di memoria fisica in cui sono mappati.
certi sistemi usano entrambe le tecniche. I Pc per esempio usano istruzioni di I/o
per controllare alcuni dispositivi e l’I/o memory mapped per controllarne altri. nella
Figura 13.2 sono riportati gli usuali indirizzi delle porte di I/o dei Pc. Il controllore
della grafica utilizza alcune porte di I/o per le operazioni di controllo di base, ma di-
spone di un’ampia regione mappata in memoria che serve a mantenere i contenuti
dello schermo. Il processo scrive sullo schermo inserendo i dati nella regione mappata
in memoria; il controllore genera l’immagine dello schermo sulla base del contenuto
indirizzi per l’I/O (in esadecimale) 000-00F
020-021
040-043
200-20F
2F8-2FF
320-32F
378-37F
3D0-3DF
3F0-3F7
3F8-3FF
dispositivo
controllore DMA
controllore delle interruzioni
timer
controllore dei giochi
porta seriale (secondaria)
controllore del disco
porta parallela
controllore della grafica
controllore dell’unità a dischetti
porta seriale (principale)
Figura 13.2 Indirizzi delle porte dei dispositivi di I/O nei PC (elenco parziale).
13.2 Hardware di I/O 653
di questa regione di memoria. Questa tecnica è semplice da usare; inoltre la scrittura
di milioni di byte nella memoria grafica è più veloce dell’invio di milioni di istruzioni
di I/o. La facilità di scrittura in un controllore di I/o memory mapped è però contro-
bilanciata da uno svantaggio: un comune errore di programmazione è la scrittura in
una regione di memoria sbagliata causata da un puntatore errato. ciò rende i registri
dei dispositivi mappati in memoria vulnerabili a modifiche accidentali. naturalmente,
le tecniche di protezione della memoria aiutano a ridurre tale rischio.
una porta di I/o consiste in genere di quattro registri: status, control,
data-ine data-out.
•
La cPu legge dal registro data-inper ricevere dati.
•
La cPu scrive nel registro data-outper emettere dati.
•
Il registro statuscontiene alcuni bit che possono essere letti dalla cPu e in-
dicano lo stato della porta; per esempio indicano se è stata portata a termine
l’esecuzione del comando corrente, se un byte è disponibile per essere letto dal
registro data-in, se si è verificato un errore del dispositivo.
•
Il registro controlpuò essere scritto per attivare un comando o per cambiare
il modo di funzionamento del dispositivo. Per esempio, un certo bit nel registro
controldella porta seriale determina il tipo di comunicazione tra half-duplex
e full-duplex, un altro abilita il controllo di parità, un terzo imposta la lunghez-
za delle parole a 7 o 8 bit, altri selezionano una tra le velocità che la porta se-
riale può sostenere.
La tipica dimensione dei registri di dati varia tra 1 e 4 byte. certi controllori hanno
circuiti integrati FIFo che possono contenere parecchi byte per l’invio e la ricezione
di dati, in modo da espandere la capacità del controllore oltre la dimensione del re-
gistro di dati. un circuito integrato FIFo può contenere una piccola sequenza di dati
finché il dispositivo o la cPu non sono in grado di riceverli.
13.2.1 Polling
Il protocollo completo per l’interazione fra la cPu e un controllore può essere intri-
cato, ma la fondamentale nozione di handshaking (negoziazione) è semplice, ed è
illustrata con un esempio. Si assuma l’uso di due bit per coordinare la relazione di ti-
po produttore-consumatore fra il controllore e la cPu. Il controllore specifica il suo
stato per mezzo del bit busydel registro status; pone a 1 il bit busyquando è im-
pegnato in un’operazione, e lo pone a 0 quando è pronto a eseguire il comando suc-
cessivo. La cPu comunica le sue richieste tramite il bit command-readynel registro
command: pone questo bit a 1 quando il controllore deve eseguire un comando. In
questo esempio, la cPu scrive in una porta coordinandosi con un controllore per mez-
zo del seguente handshaking.
1.
La cPu legge ripetutamente il bit busyfinché questo non vale 0.
2.
La cPu pone a 1 il bit writedel registro dei comandi e scrive un byte nel re-
gistro data-out.
654 Capitolo 13– Sistemi di I/O
3.
La cPu pone a 1 il bit command-ready.
4.
Quando il controllore si accorge che il bit command-readyè posto a 1, pone
a 1 il bit busy.
5.
Il controllore legge il registro dei comandi e trova il comando write; legge il
registro data-out per ottenere il byte da scrivere, e compie l’operazione di
I/o sul dispositivo.
6.
Il controllore pone a 0 il bit command-ready, pone a 0 il bit errornel regi-
stro statusper indicare che l’operazione di I/o ha avuto esito positivo, e po-
ne a 0 il bit busyper indicare che l’operazione è terminata.
La sequenza appena descritta si ripete per ogni byte.
Durante l’esecuzione del passo 1, la cPu è in attesa attiva (busy-waiting) o in
interrogazione ciclica (polling): itera la lettura del registro statusfinché il bit busy
assume il valore 0. Se il controllore e il dispositivo sono veloci, questo metodo è ra-
gionevole, ma se l’attesa rischia di prolungarsi, sarebbe probabilmente meglio se la
cPu si dedicasse a un’altra operazione. In questo caso si pone il problema di come
la cPu possa sapere quando il controllore è tornato libero. È necessario che la cPu
serva certi tipi di dispositivi rapidamente, o si potrebbero perdere alcuni dati. Quando,
per esempio, i dati affluiscono in una porta seriale o dalla tastiera, il piccolo buffer
del controllore diverrà presto pieno, e se la cPu attende troppo a lungo prima di ri-
prendere la lettura dei byte, si perderanno informazioni.
In molte architetture di calcolatori sono sufficienti tre istruzioni della cPu per ef-
fettuare il polling di un dispositivo: read, lettura di un registro del dispositivo;
logical-and, usata per estrarre il valore di un bit di stato, e branch, salto a un
altro punto del codice se l’argomento è diverso da zero. chiaramente, il polling è in
sé un’operazione efficiente; tale tecnica diviene però inefficiente se le ripetute inter-
rogazioni trovano raramente un dispositivo pronto per il servizio, mentre altre utili
elaborazioni attendono la cPu. In tali casi, anziché richiedere alla cPu di eseguire il
polling, può essere più efficiente far sì che il controllore comunichi alla cPu che il
dispositivo è pronto. Il meccanismo hardware che permette tale comunicazione si
chiama interruzione (interrupt).
13.2.2 Interruzioni
Il meccanismo di base dell’interruzione funziona come segue. L’hardware della cPu
ha un input, detto linea di richiesta dell’interruzione, del quale la cPu controlla lo
stato dopo l’esecuzione di ogni istruzione. Quando rileva il segnale di un controllore
sulla linea di richiesta dell’interruzione, la cPu salva lo stato corrente e salta alla
routine di gestione dell’interruzione (interrupt-handler routine), che si trova a un
indirizzo prefissato di memoria. Questa procedura determina le cause dell’interruzio-
ne, porta a termine l’elaborazione necessaria, ripristina lo stato ed esegue un’istru-
zione return from interrupt per far sì che la cPu ritorni nello stato in cui si
trovava prima della sua interruzione. Il controllore del dispositivo genera un’interru-
zione della cPu sulla linea di richiesta delle interruzioni, che la cPu rileva e recapita
13.2 Hardware di I/O 655
CPU
1
il driver del dispositivo
avvia l’operazione di I/O
controllore dell’I/O
2
avvia l’operazione di I/O
la CPU rileva eventuali interruzioni
eseguendo un controllo
dopo l’esecuzione di ogni istruzione
4
3
i dati in ingresso sono
disponibili, l’emissione
dei dati è terminata
o c’è stato un errore
genera un’interruzione
7
la CPU rileva l’interruzione
e trasferisce il controllo
al gestore
delle interruzioni
5
il gestore
delle interruzioni
elabora i dati
e termina
6
la CPU riprende
l’esecuzione
precedentemente
interrotta
Figura 13.3 Ciclo di I/O basato sulle interruzioni.
al gestore delle interruzioni, che a sua volta gestisce l’interruzione corrispondente
servendo il dispositivo. nella Figura 13.3 è riassunto il ciclo di I/o causato da un’in-
terruzione della cPu. In questo capitolo daremo molta importanza alla gestione delle
interruzioni, perché persino un sistema a singola utenza ne gestisce centinaia al se-
condo, mentre un server ne può gestire centinaia di migliaia.
Il meccanismo di base delle interruzioni che abbiamo appena descritto permette
alla cPu di rispondere a un evento asincrono, come quello di un controllore di un di-
spositivo che divenga pronto per essere servito. nei sistemi operativi moderni sono
necessarie capacità di gestione delle interruzioni più raffinate.
1.
Si deve poter posporre la gestione delle interruzioni durante le fasi critiche
dell’elaborazione.
2.
Si deve disporre di un meccanismo efficiente per passare il controllo all’ap-
propriato gestore delle interruzioni, senza dover esaminare ciclicamente tutti i
dispositivi (polling) per determinare quale abbia generato l’interruzione.
656 Capitolo 13– Sistemi di I/O
3.
Si deve disporre di più livelli d’interruzione, di modo che il sistema possa di-
stinguere le interruzioni ad alta priorità da quelle a priorità inferiore, servendo
le richieste con la celerità appropriata al caso.
In un calcolatore moderno queste tre caratteristiche sono fornite dalla cPu e dal
controllore hardware delle interruzioni.
La maggior parte delle cPu ha due linee di richiesta delle interruzioni. una è quel-
la delle interruzioni non mascherabili, riservata a eventi quali gli errori di memoria
irrecuperabili. La seconda linea è quella delle interruzioni mascherabili: può essere
disattivata dalla cPu prima dell’esecuzione di una sequenza critica di istruzioni che
non deve essere interrotta. L’interruzione mascherabile è usata dai controllori dei di-
spositivi per richiedere un servizio.
Il meccanismo delle interruzioni accetta un indirizzo – un numero che seleziona
una specifica procedura di gestione delle interruzioni da un insieme ristretto. nella mag-
gior parte delle architetture questo indirizzo è uno scostamento relativo in una tabella
detta vettore delle interruzioni, contenente gli indirizzi di memoria degli specifici ge-
stori delle interruzioni. Lo scopo di un meccanismo vettorizzato di gestione delle inter-
ruzioni è di ridurre la necessità che un singolo gestore debba individuare tutte le possi-
bili fonti d’interruzione per determinare quale di loro abbia richiesto un servizio. In
pratica, tuttavia, i calcolatori hanno più dispositivi (e quindi, più gestori delle interru-
zioni) che elementi nel vettore delle interruzioni. una maniera diffusa di risolvere que-
sto problema consiste nel concatenamento delle interruzioni (interrupt chaining), in
cui ogni elemento del vettore delle interruzioni punta alla testa di una lista di gestori
delle interruzioni. Quando si verifica un’interruzione, si chiamano uno alla volta i ge-
stori nella lista corrispondente finché non se ne trova uno che può soddisfare la richiesta.
Questa struttura è un compromesso fra l’overhead di una tabella delle interruzioni enor-
me e l’inefficienza dell’uso di un solo gestore delle interruzioni.
nella Figura 13.4 è descritto il vettore delle interruzioni della cPu Intel Pentium.
Gli eventi da 0 a 31, non mascherabili, si usano per segnalare varie condizioni d’er-
rore; quelli dal 32 al 255, mascherabili, si usano, per esempio, per le interruzioni ge-
nerate dai dispositivi.
Il meccanismo delle interruzioni realizza anche un sistema di livelli di priorità
delle interruzioni. esso permette alla cPu di differire la gestione delle interruzioni
di bassa priorità senza mascherare tutte le interruzioni, e permette a un’interruzione
di priorità alta di sospendere l’esecuzione della procedura di servizio di un’interru-
zione di priorità bassa.
un sistema operativo moderno interagisce con il meccanismo delle interruzioni
in vari modi. all’accensione della macchina esamina i bus per determinare quali di-
spositivi siano presenti, e installa gli indirizzi dei corrispondenti gestori delle inter-
ruzioni nel vettore delle interruzioni. Durante l’I/o, i vari controllori di dispositivi ge-
nerano le interruzioni della cPu quando sono pronti per un servizio. Queste
interruzioni significano che è stato completato un output, o che sono disponibili dati
in ingresso, o che un’operazione non è andata a buon fine. Il meccanismo delle inter-
ruzioni si usa anche per gestire un’ampia gamma di eccezioni, come la divisione
13.2 Hardware di I/O 657
indice del vettore descrizione
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19-31
32-255
divide error
debug exception
null interrupt
breakpoint
INTO-detected overflow
bound range exception
invalid opcode
device not available
double fault
coprocessor segment overrun (reserved)
invalid task state segment
segment not present
stack fault
general protection
page fault
(Intel reserved, do not use)
floating-point error
alignment check
machine check
(Intel reserved, do not use)
maskable interrupts
Figura 13.4 Vettore delle interruzioni della CPU Intel Pentium.
per 0, l’accesso a indirizzi di memoria protetti o inesistenti o il tentativo di eseguire
un’istruzione privilegiata in modalità utente. Gli eventi che producono le interruzioni
hanno una proprietà in comune: inducono il sistema operativo a eseguire urgentemen-
te una procedura autonoma.
un sistema operativo può fare altri usi proficui di un efficiente meccanismo
hardware e software che memorizza una piccola quantità d’informazioni sullo stato
della cPu e poi richiama una procedura del kernel. Per esempio, molti sistemi ope-
rativi usano il meccanismo delle interruzioni per la gestione della memoria virtuale.
un’eccezione di pagina mancante genera un’interruzione che sospende il processo
corrente e trasferisce il controllo dell’esecuzione al relativo gestore nel kernel. tale
gestore memorizza le informazioni sullo stato del processo, lo sposta nella coda d’at-
tesa, compie le necessarie operazioni di gestione della cache delle pagine, avvia un’o-
perazione di I/o per prelevare la pagina giusta, schedula la ripresa dell’esecuzione di
un altro processo e ritorna dall’interruzione.
un altro esempio è dato dall’implementazione delle chiamate di sistema. Solita-
mente i programmi sfruttano routine di libreria per eseguire chiamate di sistema. La
routine controlla i parametri passati dall’applicazione, li assembla in una struttura
dati appropriata da passare al kernel, e infine esegue una particolare istruzione detta
interruzione software o trap. Questa istruzione ha un operando che identifica il ser-
vizio del kernel desiderato. Quando un processo esegue l’istruzione di eccezione,
l’hardware delle interruzioni salva lo stato del codice utente, passa al modo kernel e
recapita l’interruzione alla procedura del kernel che realizza il servizio richiesto.
658 Capitolo 13– Sistemi di I/O
a una trap si assegna una priorità di interruzione relativamente bassa rispetto a quelle
date alle interruzioni dei dispositivi – eseguire una chiamata di sistema per conto di
un’applicazione è meno urgente di quanto non sia servire un controllore prima che
la sua coda FIFo trabocchi causando la perdita di informazioni.
Le interruzioni si possono inoltre usare per gestire il flusso di controllo all’interno
del kernel. Si consideri un esempio di elaborazione richiesta per completare una let-
tura da un disco. un passo necessario è quello di copiare dati dallo spazio del kernel
al buffer dell’utente. Questa azione richiede tempo, ma non è urgente, e non dovrebbe
bloccare la gestione delle interruzioni con priorità più alta. un altro passo è quello di
avviare il successivo I/o in attesa relativo a quell’unità a disco. Questo passo ha prio-
rità più alta: se le unità a disco si devono usare in modo efficiente, è necessario av-
viare l’evasione della successiva richiesta di I/o non appena la precedente sia stata
soddisfatta. Di conseguenza una coppia di gestori delle interruzioni realizza il codice
del kernel che compie le letture dai dischi. Il gestore ad alta priorità mantiene le infor-
mazioni sullo stato dell’I/o, risponde al segnale d’interruzione del dispositivo, avvia
il prossimo I/o in attesa e genera un’interruzione a bassa priorità per completare il la-
voro. Più tardi, in un momento in cui la cPu non è occupata in compiti ad alta priorità,
si serve l’interruzione a bassa priorità. Il gestore corrispondente completa l’I/o a li-
vello utente copiando i dati dal buffer del kernel a quello dell’applicazione, e richia-
mando poi lo scheduler per aggiungere l’applicazione alla coda dei processi pronti.
un’architettura del kernel basata su thread è adatta alla realizzazione di più livelli
di priorità delle interruzioni, e a dare la precedenza alla gestione delle interruzioni ri-
spetto alle elaborazioni in background delle procedure del kernel e delle applicazioni.
Questo concetto si può esemplificare considerando il kernel del sistema operativo
Solaris. In questo sistema i gestori delle interruzioni si eseguono come thread del
kernel cui si riservano valori elevati di priorità. tali priorità garantiscono la precedenza
dei gestori delle interruzioni rispetto al codice delle applicazioni e al lavoro ordinario
del kernel, e inoltre realizzano le necessarie relazioni di priorità fra i diversi gestori
delle interruzioni. Le priorità fanno sì che lo scheduler dei thread di Solaris sospenda
i gestori delle interruzioni di bassa priorità a vantaggio di quelli di priorità più alta, e
la realizzazione basata su thread permette alle architetture multiprocessore di eseguire
parallelamente diversi gestori delle interruzioni. L’architettura delle interruzioni dei
sistemi Windows è descritta nel capitolo 19, presente sulla pagina web del volume.
riassumendo, le interruzioni sono usate diffusamente dai sistemi operativi mo-
derni per gestire eventi asincroni e per eseguire procedure in modalità supervisore
nel kernel. Per far sì che i compiti più urgenti siano portati a termine per primi, i cal-
colatori moderni usano un sistema di priorità delle interruzioni. I controllori dei di-
spositivi, i guasti hardware e le chiamate di sistema generano interruzioni al fine di
innescare l’esecuzione di procedure del kernel. Poiché le interruzioni sono usate in
modo massiccio per affrontare situazioni in cui il tempo è un fattore critico, è neces-
sario avere un’efficiente gestione delle interruzioni per ottenere buone prestazioni del
sistema.
13.2 Hardware di I/O 659
13.2.3 Accesso diretto alla memoria (DmA)
Quando un dispositivo compie trasferimenti di grandi quantità di dati, come nel caso
di un’unità a disco, l’uso di una costosa cPu per il controllo dei bit di stato e per la
scrittura di dati nel registro del controllore un byte alla volta, detto i/o programmato
(programmed i/o, pio), sembra essere uno spreco. In molti calcolatori si evita di so-
vraccaricare la cPu assegnando una parte di questi compiti a un processore specia-
lizzato, detto controllore dell’accesso diretto alla memoria (direct memory-access,
dma). Per dar avvio a un trasferimento Dma, la cPu scrive in memoria un blocco di
comando per il Dma. esso contiene un puntatore alla locazione dei dati da trasferire,
un altro puntatore alla destinazione dei dati, e il numero dei byte da trasferire. La cPu
scrive l’indirizzo di questo blocco di comando nel controllore del Dma, e prosegue
con altre attività. Il controllore Dma agisce quindi direttamente sul bus della memoria,
presentando al bus gli indirizzi di memoria necessari per eseguire il trasferimento
senza l’aiuto della cPu. un semplice controllore Dma è un componente standard in
tutti i sistemi moderni, dagli smartphone ai mainframe.
L’handshaking tra il controllore del DMA e il controllore del dispositivo si svolge
grazie a una coppia di fili detti DMA-requeste DMA-acknowledge. Il controllore
del dispositivo manda un segnale sulla linea DMA-request quando una word di dati
è disponibile per il trasferimento. Questo segnale fa sì che il controllore Dma prenda
possesso del bus di memoria, presenti l’indirizzo desiderato ai fili d’indirizzamento
della memoria e mandi un segnale lungo la linea DMA-acknowledge. Quando il
controllore del dispositivo riceve questo segnale, trasferisce in memoria la word di
dati e rimuove il segnale dalla linea DMA-request.
Quando l’intero trasferimento termina, il controllore del Dma interrompe la cPu.
nella Figura 13.5 è rappresentato questo processo. Quando il controllore del Dma
prende possesso del bus di memoria, la cPu è temporaneamente impossibilitata ad
accedere alla memoria centrale, sebbene abbia accesso ai dati contenuti nella sua ca-
che primaria e secondaria. Questo fenomeno, noto come sottrazione di cicli, può ral-
lentare le computazioni della cPu; ciononostante l’assegnamento del lavoro di tra-
sferimento di dati a un controllore Dma migliora in generale le prestazioni comples-
sive del sistema. In alcune architetture per realizzare la tecnica Dma si usano gli
indirizzi della memoria fisica, mentre in altre s’impiega l’accesso diretto alla
memoria virtuale (direct virtual-memory access, dvma): in questo caso si usano in-
dirizzi virtuali che poi si traducono in indirizzi fisici. La tecnica DVma permette di
compiere i trasferimenti di dati tra due dispositivi che eseguono I/o memory mapped
senza far intervenire la cPu o accedere alla memoria centrale.
nei kernel che operano in modalità protetta, in genere il sistema operativo non
permette ai processi di impartire direttamente comandi ai dispositivi. ciò protegge i
dati dalle violazioni dei controlli d’accesso e il sistema da un eventuale uso scorretto
dei controllori dei dispositivi che potrebbe portare a una caduta del sistema stesso. Il
sistema operativo invece esporta delle funzioni di I/o che possono essere eseguite da
processi sufficientemente privilegiati per effettuare operazioni di basso livello sul-
l’hardware sottostante. Quando invece il kernel non può garantire la protezione della
660 Capitolo 13– Sistemi di I/O
5. il controllore DMA
trasferisce i byte al
buffer di indirizzo X,
incrementando
l’indirizzo di memoria e
decrementando C finché
C = 0
6. quando C = 0, il
controllore DMA genera
un segnale d’interruzione
per segnalare alla CPU
che il trasferimento è
terminato
1. al driver del dispositivo si
chiede di trasferire dati
dal disco al buffer di
indirizzo X
2. il driver chiede al
controllore del disco di
trasferire C byte dal
disco al buffer di
indirizzo X
controllore DMA,
bus e interruzione
CPU
cache
bus di memoria della CPU
memoria X buffer
controllore IDE
del disco
bus PCI
3. il controllore del disco avvia il
trasferimento DMA
4. il controllore del disco invia
i dati byte per byte al
controllore DMA
disco
disco
disco
disco
Figura 13.5 Passi di un trasferimento DMA.
memoria, i processi hanno accesso diretto ai controllori dei dispositivi. Questo ac-
cesso diretto si può utilizzare in modo da ottenere buone prestazioni, perché evita la
comunicazione col kernel, i cambi di contesto e l’interazione fra diversi livelli del
kernel. Purtroppo interferisce con la stabilità e la sicurezza del sistema. La tendenza
comune per i sistemi operativi d’uso generale è quella di proteggere la memoria e i
dispositivi in modo da salvaguardarli da applicazioni accidentalmente o volutamente
dannose.
13.2.4 Concetti principali dell’hardware di I/O
Sebbene gli aspetti dell’I/o che riguardano i dispositivi siano complessi se si analiz-
zano tanto dettagliatamente quanto farebbe un progettista elettronico, i concetti ap-
pena descritti sono sufficienti per comprendere molti aspetti dell’I/o per ciò che con-
cerne i sistemi operativi. ecco un sommario dei concetti principali:
bus;•
controllore;•
•
porta di I/o e suoi registri;
•
procedura di handshaking tra la cPu e il controllore di un dispositivo;
•
esecuzione dell’handshaking per mezzo del polling o delle interruzioni;
•
delega dell’I/o a un controllore Dma nel caso di trasferimenti di grandi quantità
di dati.
13.3 Interfaccia di I/O per le applicazioni 661
Precedentemente in questo paragrafo è stato fornito un esempio dell’handshaking che
avviene tra un controllore di dispositivo e un host. In realtà, la grande varietà di di-
spositivi esistenti pone un problema a chi voglia realizzare concretamente un sistema
operativo. ogni tipo di dispositivo ha proprie funzionalità, proprie definizioni dei bit
di controllo, e un proprio protocollo per l’interazione con la macchina – e tutto ciò
varia da dispositivo a dispositivo. come deve essere progettato un sistema operativo
affinché sia possibile collegare al calcolatore nuovi dispositivi senza che sia neces-
sario riscrivere il sistema operativo stesso? e inoltre, vista la grande varietà di dispo-
sitivi, come può il sistema operativo fornire alle applicazioni un’interfaccia per l’I/o
uniforme ed efficace? Discuteremo questi aspetti nel seguito.
13.3 Interfaccia di I/O per le applicazioni
In questo paragrafo si discutono le tecniche e le interfacce di un sistema operativo che
permettono un trattamento standardizzato e uniforme dei dispositivi di I/o. Si spiega,
per esempio, come un’applicazione possa aprire un file residente in un disco senza sa-
pere di che tipo di disco si tratti, e come si possano aggiungere al calcolatore nuove
unità a disco e altri dispositivi senza che si debba modificare il sistema operativo.
I metodi qui esposti coinvolgono l’astrazione, l’incapsulamento e la stratificazione
del software. In particolare, si può effettuare un’astrazione rispetto ai dettagli delle dif-
ferenze tra i dispositivi per l’I/o identificandone alcuni tipi generali. a ognuno di questi
tipi si accede per mezzo di un insieme standardizzato di funzioni – un’interfaccia.
Le differenze sono incapsulate in moduli del kernel detti driver dei dispositivi, specia-
lizzati internamente per gli specifici dispositivi, ma che comunicano con l’esterno per
mezzo delle interfacce uniformi. nella Figura 13.6 è illustrata la divisione in strati
software di quelle parti del kernel che riguardano la gestione dell’I/o.
Lo scopo dello strato dei driver dei dispositivi è di nascondere al sottosistema di
I/o del kernel le differenze fra i controllori dei dispositivi, in modo simile a quello
con cui le chiamate di sistema di I/o incapsulano il comportamento dei dispositivi in
alcune classi generiche che nascondono le differenze hardware alle applicazioni. Il
fatto che così il sottosistema di I/o sia reso indipendente dall’hardware semplifica il
lavoro di chi sviluppa il sistema operativo, e va inoltre a vantaggio dei costruttori dei
dispositivi. Questi, infatti, o progettano i nuovi dispositivi in modo tale che siano
compatibili con un’interfaccia host-controllore già esistente (per esempio Sata), op-
pure scrivono driver che permettano ai nuovi dispositivi di essere gestiti dai sistemi
operativi più diffusi. In questo modo, nuovi dispositivi sono utilizzabili da un calco-
latore senza che occorra attendere lo sviluppo del codice di supporto da parte del pro-
duttore del sistema operativo.
Sfortunatamente per i produttori di dispositivi, ogni tipo di sistema operativo ha
le sue convenzioni riguardanti l’interfaccia dei driver dei dispositivi. così, un dato
dispositivo potrà essere venduto con molti driver diversi – per esempio, driver per
Windows, Linux, aIx e mac oS x. I dispositivi (Figura 13.7) possono differire in
molti aspetti.
662 Capitolo 13– Sistemi di I/O
kernel
software
driver
SCSI
driver
della
tastiera
controller
SCSI
controller
della
tastiera
sottosistema di I/O nel kernel
driver
del mouse
controller
del mouse
driver
del bus
PCI
controller
del bus
PCI
driver
dell’unità
a
dischetti
controller
dell’unità
a
dischetti
driver
ATAPI
controller
ATAPI
hardware
dispositivi
SCSI tastiera mouse bus PCI unità a
dischetti
dispositivi
ATAPI
(unità a
disco,
unità a
nastro)
Figura 13.6 Struttura relativa all’I/O nel kernel.
•
Trasferimento a flusso di caratteri o a blocchi. un dispositivo a flusso di ca-
ratteri trasferisce dati un byte alla volta, mentre uno a blocchi trasferisce un
blocco di byte in un’unica soluzione.
Sequenziale o accesso diretto. un dispositivo sequenziale trasferisce dati se-•
condo un ordine fisso dipendente dal dispositivo, mentre l’utente di un dispo-
sitivo ad accesso diretto può richiedere l’accesso a una qualunque delle possi-
bili locazioni di memorizzazione.
dispositivi sincroni o asincroni. un dispositivo sincrono trasferisce dati con•
un tempo di risposta prevedibile, in maniera coordinata rispetto al resto del si-
stema. un dispositivo asincrono ha tempi di risposta irregolari o non prevedi-
bili, non coordinati con gli altri eventi del computer.
condivisibili o dedicati. un dispositivo condivisibile può essere usato in mo-•
do concorrente da diversi processi o thread, mentre ciò è impossibile se il di-
spositivo è dedicato.
v elocità di funzionamento. Può variare da alcuni byte al secondo fino a qual-•
che gigabyte al secondo.
Lettura e scrittura, sola lettura o sola scrittura. alcuni dispositivi possono•
emettere e ricevere dati, ma altri possono trasferire dati in una sola direzione.
13.3 Interfaccia di I/O per le applicazioni 663
aspetto variazione esempio
modalità di trasferimento dei dati a caratteri
a blocchi
modalità d’accesso sequenziale
casuale
prevedibilità dell’I/O sincrono
asincrono
condivisione dedicato
condiviso
velocità latenza
tempo di ricerca
velocità di trasferimento
attesa fra le operazioni
direzione dell’I/O solo lettura
solo scrittura
lettura e scrittura
terminale
unità a disco
modem
lettore di CD-ROM
unità a nastro
tastiera
unità a nastro
tastiera
lettore di CD-ROM
controllore della grafica
unità a disco
Figura 13.7 Caratteristiche dei dispositivi per l’I/O.
Per ciò che riguarda l’accesso delle applicazioni ai dispositivi, molte di queste diffe-
renze sono nascoste dal sistema operativo, e i dispositivi sono raggruppati in poche
classi convenzionali. Si è riscontrato che i modi d’accesso ai dispositivi che ne risul-
tano sono utili e largamente applicabili. anche se la forma precisa delle chiamate di
sistema può variare nei diversi sistemi operativi, le classi di dispositivi sono abba-
stanza regolari. Le convenzioni d’accesso principali includono l’I/o a blocchi, l’I/o
a flusso di caratteri, l’accesso ai file mappati in memoria, e le socket di rete. I sistemi
operativi forniscono anche chiamate di sistema speciali per l’accesso a qualche di-
spositivo aggiuntivo, per esempio un orologio o un timer. Qualche sistema operativo
mette a disposizione un insieme di chiamate di sistema per display grafici, video e
audio.
La maggior parte dei sistemi ha anche una “via di fuga” (escape) o back door che
permette il passaggio trasparente di comandi arbitrari da un’applicazione a un driver
di dispositivo. In unIx tale funzione è svolta dalla chiamata di sistema ioctl()
(che sta per i/o control) e consente a un’applicazione di impiegare qualsiasi funzio-
nalità fornita da qualsiasi driver di dispositivo, senza che per questo sia necessario
creare nuove chiamate di sistema. Gli argomenti di ioctl()sono tre: il primo è un
descrittore di file che collega l’applicazione al driver desiderato facendo riferimento
a un dispositivo gestito da quel driver; il secondo è un numero intero che seleziona
uno dei comandi forniti dal driver; il terzo argomento, infine, è un puntatore a un’ar-
bitraria struttura dati in memoria, tramite la quale l’applicazione e il driver si scam-
biano le informazioni di controllo o i dati necessari.
664 Capitolo 13– Sistemi di I/O
13.3.1 Dispositivi con trasferimento a blocchi e a caratteri
L’interfaccia per i dispositivi a blocchi sintetizza tutti gli aspetti necessari per acce-
dere alle unità a disco e ad altri dispositivi basati sul trasferimento di blocchi di dati.
ci si aspetta che il dispositivo comprenda istruzioni come read()e write()e, nel
caso sia ad accesso casuale, anche un comando seek()per specificare il blocco suc-
cessivo da trasferire. Di solito le applicazioni comunicano con questi dispositivi tra-
mite un’interfaccia di file system. Si vede che read(), write()e seek()catturano
l’essenza del comportamento dei dispositivi con traferimento a blocchi, in modo che
le applicazioni non vedano le differenze di basso livello fra questi dispositivi.
Il sistema operativo e certe applicazioni particolari come quelle per la gestione
delle basi di dati possono trovare più conveniente trattare questi dispositivi come una
semplice sequenza lineare di blocchi. In questo caso si parla di i/o a basso livello
(raw i/o). L’uso del file system da parte delle applicazioni che gestiscono già in pro-
prio un buffer per l’I/o comporta l’inutile intervento di un buffer aggiuntivo. analo-
gamente, l’uso dei lock da parte del sistema operativo nei confronti di applicazioni
che già implementano meccanismi per la mutua esclusione relativi ai blocchi dei file
risulta ridondante, o peggio contraddittorio. Per superare tali potenziali conflitti, l’I/o
a basso livello passa il controllo del dispositivo direttamente all’applicazione, toglien-
do così di mezzo il sistema operativo. Purtroppo, ciò significa anche che non risulta
disponibile sul dispositivo in questione alcun servizio del sistema operativo. un com-
promesso che si sta diffondendo sempre più è fornire una modalità d’accesso ai file
che disabiliti il buffer e i meccanismi di gestione dei lock; nel mondo unIx si parla
di i/o diretto.
L’accesso ai file mappato in memoria può costituire uno strato software sopra i
driver dei dispositivi a blocchi. Piuttosto che offrire funzioni di lettura e scrittura,
un’interfaccia di mappaggio in memoria fornisce la possibilità di accedere a un’unità
a disco tramite un vettore di byte della memoria centrale. La chiamata di sistema che
associa un file a una regione di memoria restituisce l’indirizzo di memoria virtuale
di una copia del file. Gli effettivi trasferimenti di dati sono eseguiti solo quando ne-
cessari per soddisfare una richiesta d’accesso all’immagine in memoria. Poiché i tra-
sferimenti si trattano nello stesso modo in cui si gestisce l’accesso su richiesta a una
pagina di memoria virtuale, l’I/o memory mapped è efficiente. esso è inoltre conve-
niente per i programmatori perché l’accesso a un file memory mapped è semplice tan-
to quanto la lettura e la scrittura in memoria. I sistemi operativi che gestiscono la me-
moria virtuale utilizzano comunemente l’interfaccia di mappaggio in memoria per i
servizi del kernel. Per esempio, quando il sistema operativo deve eseguire un pro-
gramma, mappa l’eseguibile in memoria, quindi trasferisce il controllo all’indirizzo
iniziale. Questo tipo d’interfaccia è spesso usato anche per l’accesso del kernel all’a-
rea di swapping nei dischi.
La tastiera è un esempio di dispositivo al quale si accede tramite un’interfaccia a
flusso di caratteri. Le chiamate di sistema fondamentali per le interfacce di questo
tipo permettono a un’applicazione di acquisire (get()) o inviare (put()) un carat-
13.3 Interfaccia di I/O per le applicazioni 665
tere. Basandosi su quest’interfaccia è possibile costruire librerie che offrono l’accesso
riga per riga, con buffering ed editing (per esempio, quando l’utente preme il tasto
backspace, si rimuove il carattere precedente dalla sequenza di caratteri da inserire).
Questo tipo d’accesso è conveniente per dispositivi come tastiere, mouse, modem,
che producono dati “spontaneamente”, cioè in momenti che non possono essere sem-
pre previsti dalle applicazioni. Lo stesso tipo d’accesso è adatto anche ai dispositivi
che emettono dati organizzati in modo naturale come sequenza lineare di byte, per
esempio le stampanti o le schede audio.
13.3.2 Dispositivi di rete
Poiché i modi di indirizzamento e le prestazioni tipiche dell’I/o di rete sono notevol-
mente differenti da quelli dell’I/o delle unità a disco, la maggior parte dei sistemi
operativi fornisce un’interfaccia per l’I/o di rete diversa da quella caratterizzata dalle
operazioni read(), write()e seek()usata per i dischi. un’interfaccia disponibile
in molti sistemi operativi, tra i quali unIx e Windows nt , è l’interfaccia di rete socket
(presa di corrente).
Si pensi a una presa di corrente elettrica a muro: vi si può collegare qualunque ap-
parecchiatura elettrica; per analogia, le chiamate di sistema di un’interfaccia socket
permettono a un’applicazione di creare una socket, collegare una socket locale all’in-
dirizzo di un altro punto della rete (ciò ha l’effetto di collegare questa applicazione
alla socket creata da un’altra applicazione), controllare se un’applicazione si inserisce
nella socket locale, e inviare o ricevere pacchetti di dati lungo la connessione. Per
supportare lo sviluppo di server, l’interfaccia socket fornisce anche una funzione chia-
mata select()che gestisce un insieme di socket. essa restituisce informazioni sulle
socket per le quali sono presenti pacchetti che attendono d’essere ricevuti, e su quelle
che hanno spazio per accettare un pacchetto da inviare. L’uso della funzione
select() elimina il polling e il busy waiting altrimenti necessari per l’I/o di rete.
Queste funzioni incapsulano il comportamento essenziale delle reti, facilitando no-
tevolmente la creazione di applicazioni distribuite che possano sfruttare qualsiasi
hardware di rete e stack di protocolli.
Sono stati sviluppati molti altri metodi per affrontare il problema della comuni-
cazione di rete e fra i processi. Il sistema operativo Windows, per esempio, fornisce
un’interfaccia per la scheda di rete e un’altra per i protocolli di rete. Il sistema ope-
rativo unIx, banco di prova storico delle tecnologie di rete, offre pipe half-duplex,
code FIFo full-duplex, StreamS full-duplex, code di messaggi e socket.
13.3.3 Orologi e timer
La maggior parte dei calcolatori ha timer e orologi hardware che forniscono tre fun-
zioni essenziali:
•
•
•
segnare l’ora corrente;
segnalare il tempo trascorso;
regolare un timer in modo da avviare l’operazione x al tempo t.
666 Capitolo 13– Sistemi di I/O
Queste funzioni sono spesso usate sia dal sistema operativo sia da applicazioni per
cui il tempo è un fattore importante. Purtroppo, le chiamate di sistema che realizzano
queste funzioni non sono standardizzate da un sistema operativo all’altro.
Il dispositivo che misura la durata di un lasso di tempo e che può avviare un’ope-
razione si chiama timer programmabile; si può regolare in modo da attendere un
certo tempo e poi generare un’interruzione, e può anche ripetere questo processo con-
tinuamente, generando così interruzioni periodiche. Lo scheduler usa questo mecca-
nismo per generare un’interruzione che sospende un processo quando il suo quanto
di tempo è scaduto. Il sottosistema dell’I/o delle unità a disco lo usa per riversare pe-
riodicamente nei dischi il contenuto della buffer cache, e il sottosistema di rete lo usa
per annullare operazioni che procedono troppo lentamente a causa di congestioni di
rete o guasti. Il sistema operativo può inoltre fornire un’interfaccia per permettere ai
processi utenti di usare i timer. Simulando orologi virtuali, il sistema operativo può
anche gestire un numero di richieste d’uso dei timer maggiore del numero dei timer
fisici. Per far ciò il kernel (o il driver del timer) mantiene una lista ordinata cronolo-
gicamente delle interruzioni richieste dagli utenti e dalle proprie procedure, e imposta
il timer per la prima scadenza. Quando il timer genera l’interruzione, il kernel manda
un segnale al richiedente, e reimposta il timer per la scadenza successiva.
In molti calcolatori, la frequenza delle interruzioni generate dall’orologio è fra le
18 e le 60 al secondo. ciò costituisce un grado di precisione non sufficientemente
fine per un calcolatore moderno che può eseguire centinaia di milioni di istruzioni al
secondo. La precisione degli impulsi d’attivazione è limitata dalla bassa frequenza
del timer, e dall’overhead aggiuntivo dato dal mantenimento di orologi virtuali. Inol-
tre, se lo stesso timer si usa per fornire l’ora corrente del sistema, questa potrà deri-
vare. nella maggior parte dei calcolatori, l’orologio hardware è costruito sulla base
di un contatore ad alta frequenza. In alcuni casi, è possibile leggere da un registro del
dispositivo il valore di questo contatore, cosicché esso può essere visto come un oro-
logio ad alta precisione. Sebbene non sia in grado di generare interruzioni, offre una
misura accurata degli intervalli di tempo.
13.3.4 I/O non bloccante e asincrono
un altro aspetto dell’interfaccia delle chiamate di sistema è la scelta fra I/o bloccante
e non bloccante. Quando un’applicazione impiega una chiamata di sistema bloccante
si sospende l’esecuzione dell’applicazione, che passa dalla coda dei processi pronti
per l’esecuzione a una coda d’attesa del sistema. Quando la chiamata di sistema ter-
mina, l’applicazione è posta nuovamente nella coda dei processi pronti in modo che
possa riprendere l’esecuzione; Quando riprenderà l’esecuzione, riceverà i valori ri-
portati dalla chiamata di sistema. Le operazioni fisiche compiute dai dispositivi di I/o
sono in genere asincrone – richiedono un tempo variabile o non prevedibile. cionon-
dimeno, la maggior parte dei sistemi operativi impiega chiamate di sistema bloccanti
come interfaccia per le applicazioni, perché in questo caso il codice delle applicazioni
è più facilmente comprensibile del corrispondente codice non bloccante.
13.3 Interfaccia di I/O per le applicazioni 667
alcuni processi a livello utente necessitano di una forma non bloccante di I/o. un
esempio è quello di un’interfaccia utente con cui s’interagisce col mouse e la tastiera
mentre elabora dati e li mostra sullo schermo. un altro esempio è un’applicazione vi-
deo che legge frame da un file su disco e simultaneamente li decomprime e li mostra
sullo schermo.
uno dei modi in cui chi progetta un’applicazione può sovrapporre elaborazione e
I/o è scrivere un’applicazione a più thread. alcuni di loro eseguono chiamate di si-
stema bloccanti, mentre altri continuano l’elaborazione. alcuni sistemi operativi for-
niscono chiamate di sistema non bloccanti per l’I/o. una chiamata di questo tipo non
arresta l’esecuzione dell’applicazione per un tempo significativo. al contrario, essa
restituisce rapidamente il controllo all’applicazione, fornendo un parametro che in-
dica quanti byte di dati sono stati trasferiti.
una possibile alternativa alle chiamate di sistema non bloccanti è costituita dalle
chiamate di sistema asincrone. esse restituiscono immediatamente il controllo al chia-
mante, senza attendere che l’I/o sia stato completato. L’applicazione continua a essere
eseguita, e il completamento dell’I/o è successivamente comunicato all’applicazione
per mezzo dell’impostazione del valore di una variabile nello spazio d’indirizzi del-
l’applicazione oppure tramite la generazione di un segnale o interrupt software, o an-
cora tramite una procedura di richiamo (callback) eseguita fuori del normale flusso
lineare d’elaborazione dell’applicazione. La differenza fra chiamate di sistema non
bloccanti e asincrone è che una read()non bloccante restituisce immediatamente il
controllo, fornendo i dati che è stato possibile leggere (l’intero numero di byte richie-
sti, una parte, o anche nessun dato). una chiamata read()asincrona richiede un tra-
sferimento di cui il sistema garantisce il completamento, ma solo in un momento suc-
cessivo e non prevedibile. entrambi i metodi sono illustrati dalla Figura 13.8.
In tutti i moderni sistemi operativi si verificano attività asincrone. Spesso queste
attività non sono gestite da utenti o applicazioni, ma fanno parte del funzionamento
del sistema operativo. Due validi esempi sono l’I/o del disco e della rete. Di norma,
utente
processo richiedente
in attesa
processo richiedente
driver del dispositivo gestore
dell’interruzione
trasferimento
fisico dei dati
driver del dispositivo
gestore
dell’interruzione
trasferimento
fisico dei dati
tempo tempo
(a) (b)
Figura 13.8 Due metodi per l’I/O; (a) sincrono e (b) asincrono.
utente
kernel
668 Capitolo 13– Sistemi di I/O
quando un’applicazione emette una richiesta di invio sulla rete o una richiesta di scrit-
tura su disco, il sistema operativo rileva la richiesta, inserisce l’I/o in un buffer e re-
stituisce il controllo all’applicazione. appena possibile, per ottimizzare le prestazioni
complessive, il sistema operativo completa la richiesta. Se nel frattempo si verifica
un errore di sistema, l’applicazione perderà tutte le richieste in atto. I sistemi operativi
impongono pertanto, di solito, un limite sul tempo massimo per rispondere a una ri-
chiesta. Per esempio, alcune versioni di unIx ripuliscono i propri buffer del disco
ogni 30 secondi; in altre parole ogni richiesta deve essere evasa entro 30 secondi. La
coerenza dei dati delle applicazioni viene mantenuta dal kernel, che legge i dati dai
suoi buffer prima di inviare richieste di I/o ai dispositivi, assicurando che i dati non
ancora scritti siano comunque restituiti al richiedente. Si noti che più thread che ese-
guono I/o sullo stesso file potrebbero non ricevere dati coerenti, a seconda di come
il kernel implementa il suo I/o. In questa situazione, i thread potrebbero dover utiliz-
zare protocolli di locking. alcune richieste di I/o devono essere eseguite immediata-
mente, per cui le chiamate di sistema di I/o forniscono di solito un modo per indicare
che una determinata richiesta, o l’I/o verso un particolare dispositivo, dovrà essere
eseguita in maniera sincrona.
un buon esempio di comportamento non bloccante è la chiamata di sistema
select() per le socket di rete. essa include un argomento che specifica il tempo
d’attesa massimo. Se questo valore è 0, l’applicazione può rilevare attività di rete sen-
za arrestarsi. tuttavia, l’uso della select()introduce un overhead aggiuntivo, per-
ché essa può stabilire soltanto se sia possibile compiere dell’I/o: per un effettivo tra-
sferimento di dati, la select() deve essere seguita da istruzioni come read() o
write(). una variante di questo metodo, adottata per esempio dal sistema mach, è
l’impiego di una chiamata di sistema bloccante per la lettura multipla. essa specifica
con una singola chiamata di sistema le richieste di lettura desiderate per diversi di-
spositivi, e termina non appena una di loro sia stata soddisfatta.
13.3.5 I/O vettorizzato
alcuni sistemi operativi forniscono un’altra importante variante di I/o tramite le loro
interfacce delle applicazioni. L’I/o vettorizzato permette a una chiamata di sistema
di eseguire più operazioni di I/o che coinvolgono più locazioni. Per esempio, la chia-
mata di sistema unIx readv accetta un vettore di buffer e permette di inserire nel
vettore i dati letti da una sorgente oppure di scrivere da quel vettore verso una desti-
nazione. Lo stesso trasferimento potrebbe essere realizzato per mezzo di diverse sin-
gole invocazioni di chiamate di sistema, ma questo metodo, detto scatter-gather, ri-
sulta utile per una serie di motivi.
Il trasferimento del contenuto di più buffer distinti tramite un’unica chiamata di
sistema permette di evitare cambi di contesto e l’overhead delle chiamate di sistema.
In assenza di I/o vettorizzato i dati dovrebbero prima essere trasferiti in un unico buf-
fer più grande, nel giusto ordine, e poi trasmessi. Quest’ultimo metodo risulta piut-
tosto inefficiente. Inoltre, alcune versioni di scatter-gather forniscono l’atomicità, as-
sicurando così che tutti gli I/o vengano eseguiti senza interruzioni (evitando dunque
13.4 Sottosistema di I/O del kernel 669
la corruzione di dati nel caso in cui altri thread stiano effettuando I/o verso gli stessi
buffer). Quando possibile, i programmatori sfruttano le potenzialità dell’I/o scatter-
gather per aumentare la produttività e diminuire l’overhead del sistema.
13.4 Sottosistema di I/O del kernel
Il kernel fornisce molti servizi riguardanti l’I/o; vari servizi – scheduling, gestione
del buffer, delle cache, delle code di spooling, riservazione dei dispositivi e gestione
degli errori – sono offerti dal sottosistema di I/o del kernel, e sono realizzati a partire
dai dispositivi e dai relativi driver. Il sottosistema di I/o è responsabile anche della
propria salvaguardia contro processi malfunzionanti e utenti malintenzionati.
13.4.1 Scheduling dell’I/O
Fare lo scheduling di un insieme di richieste di I/o significa stabilirne un ordine d’e-
secuzione efficace; l’ordine in cui si verificano le chiamate di sistema da parte delle
applicazioni è raramente la scelta migliore. Lo scheduling può migliorare le presta-
zioni complessive del sistema, distribuire equamente gli accessi dei processi ai di-
spositivi e ridurre il tempo d’attesa medio per il completamento di un’operazione di
I/o. ecco un semplice esempio che illustra queste potenzialità. Si supponga che la te-
stina di lettura di un’unità a disco sia vicina alla parte iniziale del disco, e che tre ap-
plicazioni impartiscano comandi di lettura bloccanti per quest’unità. L’applicazione
1 richiede la lettura di un blocco che si trova vicino alla parte finale del disco, l’ap-
plicazione 2 quella di un blocco vicino alla parte iniziale e l’applicazione 3 quella di
un blocco situato nella zona centrale. Il sistema operativo può ridurre la distanza per-
corsa dalla testina del disco servendo le richieste nell’ordine 2, 3, 1. Simili riordina-
menti delle sequenze di servizio delle richieste sono l’essenza dello scheduling del-
l’I/o.
I progettisti di sistemi operativi realizzano lo scheduling mantenendo una coda di
richieste per ogni dispositivo. Quando un’applicazione richiede l’esecuzione di una
chiamata di sistema di I/o bloccante, si aggiunge la richiesta alla coda relativa al di-
spositivo. Lo scheduler dell’I/o riorganizza l’ordine della coda per migliorare l’effi-
cienza globale del sistema e il tempo medio d’attesa cui sono sottoposte le applica-
zioni. Il sistema operativo può anche tentare di essere equo, in modo che nessuna
applicazione riceva un servizio carente, o può dare priorità alle richieste sensibili al
ritardo. Per esempio, le richieste del sottosistema per la memoria virtuale potrebbero
avere priorità su quelle delle applicazioni. Parecchi algoritmi di scheduling per l’I/o
delle unità a disco sono descritti dettagliatamente nel Paragrafo 10.4.
I kernel che mettono a disposizione l’I/o asincrono devono essere in grado di tener
traccia di più richieste di I/o contemporaneamente. a questo fine, alcuni sistemi as-
sociano una tabella dello stato dei dispositivi alla coda dei processi in attesa. Gli
elementi della tabella – uno per ogni dispositivo di I/o – indicano il tipo, l’indirizzo
e lo stato del dispositivo: non funzionante, inattivo o occupato. Se il dispositivo è im-
670 Capitolo 13– Sistemi di I/O
dispositivo: tastiera
stato: inattivo
dispositivo: stampante laser
stato: occupato
dispositivo: mouse
stato: inattivo
dispositivo: unità a dischi 1
stato: inattivo
dispositivo: unità a dischi 2
stato: occupato
.
.
.
richiesta per
la stampante laser
indirizzo: 38546
lunghezza: 1372
richiesta per l’unità
a dischi 2
file: xxx
operazione: lettura
indirizzo: 43046
lunghezza: 20000
richiesta per l’unità
a dischi 2
file: yyy
operazione: scrittura
indirizzo: 03458
lunghezza: 500
Figura 13.9 Tabella dello stato dei dispositivi.
pegnato nel servire una richiesta, il corrispondente elemento della tabella riporterà il
tipo della richiesta e altri parametri a essa relativi. Si veda la Figura 13.9.
Lo scheduling dell’I/o è uno dei modi in cui il sottosistema di I/o migliora l’effi-
cienza di un calcolatore; un altro è l’uso di spazio di memorizzazione nella memoria
centrale o nei dischi, per tecniche di buffering, caching e spooling.
13.4.2 Gestione dei buffer
un buffer è un’area di memoria che contiene dati durante il trasferimento fra due di-
spositivi o tra un’applicazione e un dispositivo. Si ricorre ai buffer per tre ragioni. La
prima è la necessità di gestire la differenza di velocità fra il produttore e il consuma-
tore di un flusso di dati. Si supponga, per esempio, di ricevere un file attraverso un
modem e di volerlo memorizzare in un’unità a disco: il modem è circa mille volte
più lento del disco, perciò conviene creare un buffer nella memoria principale per ac-
cumulare i byte che giungono dal modem. Quando tale buffer è pieno, si trasferisce
il suo contenuto nel disco con un’unica operazione. Poiché quest’operazione di scrit-
tura non è istantanea e il modem ha bisogno di ulteriore spazio per memorizzare i
dati in arrivo, è necessario impiegare due buffer di questo tipo: quando il primo è pie-
no, si richiede la scrittura nel disco del suo contenuto e il modem comincia a scrivere
nel secondo buffer mentre il primo viene scritto su disco. La scrittura nel disco do-
vrebbe terminare prima che il modem possa riempirlo, cosicché il modem potrà ri-
cominciare a usare il primo buffer, mentre si trasferisce nel disco il contenuto del se-
condo. Questa doppia bufferizzazione svincola il produttore dal consumatore,
rendendo così meno critico il problema della loro sincronizzazione. La necessità di
questo disaccoppiamento è illustrata dalla Figura 13.10, che mostra le enormi diffe-
renze di velocità tra i dispositivi tipici di un calcolatore.
13.4 Sottosistema di I/O del kernel 671
Bus del sistema
Hyper Transport (32-pair)
PCI Express 2.0 (x 32)
Infiniband (QDR 12X)
ATA (SATA-300) seriale
ethernet gigabit
bus SCSI
FireWire
hard disk
modem
mouse
tastiera
0,00001 1.000 100.000 10E6
0,1 10,001
Figura 13.10 Velocità di trasferimento dei dispositivi di un Sun Enterprise 6000 (scala logaritmica).
un secondo uso della bufferizzazione riguarda la gestione dei dispositivi che trasfe-
riscono dati in blocchi di dimensioni diverse. Queste disparità sono particolarmente
comuni nelle reti di calcolatori, dove spesso i buffer sono usati per frammentare e ri-
comporre messaggi. Quando un mittente spedisce un messaggio molto lungo, esso è
spezzato in piccoli pacchetti che si spediscono attraverso la rete; il sistema destina-
tario provvede a ricostituire in un apposito buffer l’intero messaggio originario.
Il terzo modo in cui si può impiegare un buffer è per la realizzazione della seman-
tica della copia nell’ambito dell’I/o delle applicazioni. un esempio chiarirà il signifi-
cato di semantica della copia. Si supponga che un’applicazione disponga di un buffer
contenente dati da trasferire in un disco: esso richiederà l’esecuzione della chiamata
di sistema write(), fornendo un puntatore al buffer e un numero intero che specifica
il numero di byte da trasferire. ci si può chiedere che cosa succede se, dopo che la
chiamata di sistema restituisce il controllo all’applicazione, quest’ultima modifica il
contenuto del buffer. ebbene, la semantica della copia garantisce che la versione dei
dati scritta nel disco sia conforme a quella contenuta nel buffer al momento della chia-
mata di sistema, indipendentemente da ogni successiva modifica. una semplice ma-
niera di realizzare questa semantica consiste nel far sì che la chiamata di sistema
write()copi i dati forniti dall’applicazione in un buffer del kernel prima di restituire
il controllo all’applicazione stessa. La scrittura nel disco si compie dalla memoria del
672 Capitolo 13– Sistemi di I/O
kernel, cosicché ogni successivo cambiamento nel buffer dell’applicazione non avrà
effetti. In molti sistemi operativi si usa il metodo appena descritto: nonostante implichi
una diminuzione dell’efficienza di certe operazioni di I/o, la sua semantica è chiara.
Lo stesso effetto, tuttavia, si può ottenere più efficientemente tramite un uso intelli-
gente della memoria virtuale e della protezione data dal copy-on-write delle pagine.
13.4.3 Cache
una cache è una regione di memoria veloce che serve per mantenere copie di dati:
l’accesso a queste copie è più rapido dell’accesso agli originali. Per esempio, le istru-
zioni di un processo correntemente in esecuzione sono memorizzate in un disco, co-
piate nella memoria fisica (che assume il ruolo di cache rispetto al disco) e copiate
ulteriormente nelle cache primaria e secondaria della cPu. La differenza fra un buffer
e una cache consiste nel fatto che il primo può contenere dati di cui non esiste altra
copia, mentre una cache, per definizione, mantiene su un mezzo più efficiente una
copia di informazioni memorizzate altrove.
L’uso delle cache e l’uso dei buffer sono due funzioni distinte, anche se a volte
una stessa regione di memoria si può usare per entrambi gli scopi. Per esempio, per
realizzare la semantica della copia e permettere uno scheduling efficiente dell’ I/o su
disco, il sistema operativo impiega dei buffer in memoria centrale per i dati dei dischi.
Questi buffer sono anche usati come cache per migliorare l’efficienza delle operazioni
di I/o che coinvolgono file condivisi da più applicazioni o file per i quali gli accessi
per lettura e scrittura si susseguano rapidamente. Quando riceve una richiesta di I/o
relativa a un file, il kernel controlla se la parte interessata del file è già presente nella
cache: in questo caso è possibile evitare o differire l’accesso fisico al disco. Inoltre,
i dati da scrivere nel disco sono depositati nella cache per diversi secondi, cosicché
si accumulano grandi quantità di dati da trasferire: ciò permette uno scheduling effi-
ciente. La strategia consistente nel differire le scritture per migliorare l’efficienza
dell’I/o è illustrata nel Paragrafo 17.9.2, nel contesto dell’accesso ai file remoti.
13.4.4 Code di spooling e riservazione dei dispositivi
una coda di spooling è un buffer contenente dati da inviare ad un dispositivo che non
può accettare flussi di dati intercalati, per esempio una stampante. Sebbene una stam-
pante possa servire una sola richiesta alla volta, diverse applicazioni devono poter ri-
chiedere simultaneamente la stampa di dati, senza che le stampe si mischino. Il sistema
operativo risolve questo problema filtrando tutti i dati per la stampante: i dati da stam-
pare provenienti da ogni singola applicazione si registrano in uno specifico spool file
su disco; quando un’applicazione termina di stampare, il sistema di spooling aggiunge
tale file alla coda di stampa; quest’ultima viene copiata sulla stampante, un file per
volta. In certi sistemi operativi questa funzione viene gestita da un processo di sistema
specializzato (demone), in altri da un thread del kernel. In entrambi i casi il sistema
operativo fornisce un’interfaccia di controllo che permette agli utenti e agli ammini-
stratori del sistema di esaminare la coda, eliminare elementi della coda prima che siano
stampati, sospendere il servizio di stampa per attività di manutenzione, e così via.
13.4 Sottosistema di I/O del kernel 673
alcuni dispositivi, come le unità a nastro e le stampanti, non possono alternare più
richieste concorrenti di I/o da parte di diverse applicazioni. Lo spooling è uno dei
modi in cui il sistema operativo può coordinare output concorrenti; un altro è quello
di fornire esplicite funzioni di coordinamento. alcuni sistemi operativi, fra i quali il
VmS, permettono di accedere a un dispositivo in modo esclusivo: un processo può
accedere a un dispositivo che non utilizzato, riservandosene l’uso, e restituirlo al si-
stema quando non ne ha più bisogno. altri sistemi operativi impediscono l’apertura
di più di un handle di file per un dato dispositivo. molti sistemi operativi forniscono
funzioni che permettono ai processi stessi di coordinare l’uso esclusivo dei disposi-
tivi: il sistema Windows, per esempio, mette a disposizione chiamate di sistema che
permettono a un’applicazione di aspettare finché un certo dispositivo si liberi. Inoltre
la sua chiamata di sistema OpenFile() accetta un parametro che specifica il tipo
d’accesso concesso ad altri thread concorrenti. In questi sistemi le applicazioni hanno
la responsabilità di evitare le situazioni di stallo.
13.4.5 Gestione degli errori
un sistema operativo che usi la protezione della memoria può difendersi da molti tipi
di errori dovuti all’hardware o alle applicazioni, cosicché il blocco completo del si-
stema non è la necessaria conseguenza di ogni piccolo malfunzionamento. I disposi-
tivi e i trasferimenti di I/o possono essere soggetti ad errori in molti modi, sia per mo-
tivi contingenti, come il sovraccarico di una rete di comunicazione, sia per ragioni
“permanenti”, come nel caso in cui il controllore dell’unità a disco si guasti. I sistemi
operativi sono spesso capaci di compensare efficacemente le conseguenze negative
dovute a errori temporanei: se per esempio una chiamata di sistema read()non ha
successo, il sistema ritenterà la lettura; se una chiamata send() provoca un errore,
il protocollo di rete può richiedere una resend(). Purtroppo, però, è difficile che il
sistema operativo riesca a compensare gli effetti di errori dovuti a guasti permanenti
di qualche componente importante.
Di norma, una chiamata di sistema di I/o riporta un bit d’informazione sullo stato
d’esecuzione della chiamata, che indica la riuscita o l’insuccesso dell’operazione ri-
chiesta. Il sistema operativo unIx usa inoltre una variabile intera detta errnoper co-
dificare piuttosto genericamente il tipo d’errore avvenuto; i valori possibili sono un
centinaio e denotano errori dovuti per esempio a puntatori non validi, file non aperti
o argomenti oltre i limiti ammessi. Per contro, alcuni tipi di dispositivi possono for-
nire informazioni assai dettagliate sugli errori, sebbene molti sistemi operativi attuali
non siano progettati per passare questi dati alle applicazioni. Per esempio, il malfun-
zionamento di un dispositivo ScSI è riportato dal protocollo ScSI a tre livelli di det-
taglio: usando un codice di rilevazione (sense key) che identifica la natura generale
dell’errore (per esempio: errore hardware, o richiesta illegale); un codice di rileva-
zione addizionale che descrive la categoria cui appartiene il malfunzionamento (pa-
rametro del comando errato, o insuccesso del self-test del dispositivo); e infine un
qualificatore del codice di rilevazione addizionale che fornisce informazioni ancora
più dettagliate (quale parametro è errato, o quale componente del dispositivo non ha
674 Capitolo 13– Sistemi di I/O
superato il test). Inoltre, molti dispositivi ScSI mantengono internamente pagine di
log degli errori avvenuti; queste pagine possono essere richieste dalla macchina, ma
ciò accade raramente.
13.4.6 Protezione dell’I/O
Gli errori sono strettamente connessi alla tematica della protezione. un processo uten-
te che, intenzionalmente o accidentalmente, cerchi di impartire istruzioni di I/o ille-
gali può danneggiare il funzionamento normale di un sistema. Per impedire che tali
danneggiamenti abbiano luogo, si possono opporre diverse contromisure.
onde evitare che gli utenti effettuino operazioni di I/o illegali, si definiscono come
privilegiate tutte le istruzioni relative all’I/o. ne consegue che gli utenti non potranno
impartire in modo diretto alcuna istruzione, ma dovranno farlo attraverso il sistema ope-
rativo. un programma utente, per eseguire l’I/o, invoca una chiamata di sistema per
chiedere al sistema operativo di svolgere una data operazione nel suo interesse (Figura
13.11). Il sistema, passando alla modalità privilegiata, verifica che la richiesta sia valida
e, in tal caso, esegue l’operazione; esso trasferisce quindi il controllo all’utente.
Inoltre, il sistema di protezione della memoria deve tutelare dall’accesso degli
utenti tutti gli indirizzi mappati in memoria e gli indirizzi delle porte di I/o. Il kernel,
tuttavia, non può semplicemente negare qualunque tentativo di accesso da parte degli
utenti: quasi tutti i videogiochi, nonché i programmi per il montaggio e la riprodu-
zione di video, per esempio, per ottimizzare le prestazioni della grafica necessitano
kernel
caso n
1
interruzione
software
•
•
•
lettura
•
•
•
2
esecuzione dell’I/O
•
•
•
chiamata
di sistema n
•
•
•
3
restituzione
del controllo
all’utente
programma
utente
Figura 13.11 Uso delle chiamate di sistema per eseguire I/O.
13.4 Sottosistema di I/O del kernel 675
dell’accesso diretto alla memoria del controllore della grafica, che è gestita in moda-
lità memory mapped. In questi casi, il kernel potrebbe applicare dei lock per asse-
gnare a un solo processo per volta la porzione della memoria grafica che rappresenta
una finestra sullo schermo.
13.4.7 Strutture dati del kernel
Il kernel ha bisogno di mantenere informazioni sullo stato dei componenti di I/o, e
usa a questo fine diverse strutture dati interne, un esempio delle quali è la tabella dei
file aperti descritta nel Paragrafo 12.1. Il kernel usa molte strutture di questo tipo per
tener traccia dei collegamenti di rete, delle comunicazioni con i dispositivi a caratteri
e di altre attività di I/o.
Il sistema operativo unIx permette l’accesso, con le modalità tipiche del file
system, a diversi oggetti: file degli utenti, dispositivi, spazio d’indirizzi dei processi,
e altri ancora. Sebbene ognuno di questi oggetti supporti una chiamata read(), le
semantiche sono diverse secondo i casi. Quando il kernel, per esempio, deve leggere
un file utente, ha bisogno di controllare la buffer cache prima di decidere l’effettiva
esecuzione di un’operazione di I/o su un disco. Per leggere un disco privo di struttura
logica (raw disk), il kernel deve accertarsi del fatto che la dimensione dell’insieme
dei dati di cui è stato richiesto il trasferimento sia un multiplo della dimensione dei
settori del disco e sia allineato con il settore interessato. Per leggere l’immagine di
un processo, tutto ciò che occorre è copiare dati dalla memoria. unIx incapsula queste
differenze in una struttura uniforme usando una tecnica orientata agli oggetti. Il record
di un file aperto, mostrato nella Figura 13.12, contiene una tabella di puntatori alle
procedure appropriate secondo il tipo di file in questione.
alcuni sistemi operativi applicano metodi orientati agli oggetti in misura più ri-
levante: il sistema Windows, per esempio, usa per l’I/o un sistema basato sullo scam-
bio di messaggi. una richiesta di I/o si converte in un messaggio che s’invia tramite
il kernel al sottosistema per la gestione dell’I/o, quindi al driver del dispositivo; i con-
tenuti del messaggio possono essere modificati a ogni passaggio intermedio. Quando
l’operazione richiesta è di output, il messaggio contiene i dati da scrivere; quando in-
vece l’operazione richiesta è di input, il messaggio contiene un buffer che si usa per
ricevere i dati. Questo metodo può comportare una minore efficienza rispetto alle tec-
niche procedurali basate sulla condivisione delle strutture dati, ma semplifica la pro-
gettazione e la struttura del sistema di I/o e permette una maggiore flessibilità.
13.4.8 Concetti principali del sottosistema di I/O del kernel
riassumendo, il sistema per l’I/o coordina un’ampia raccolta di servizi disponibili per le
applicazioni e per altre parti del kernel; in generale sovrintende alle seguenti funzioni:
•
gestione dello spazio dei nomi per file e dispositivi;
•
controllo dell’accesso ai file e ai dispositivi;
•
controllo delle operazioni (per esempio, un modem non può effettuare un
seek());
676 Capitolo 13– Sistemi di I/O
tabella locale
dei file aperti
(per il processo)
tabella globale dei file aperti
(per l’intero sistema)
record del file-system
puntatore a un inode
puntatore alle funzioni read e write
puntatore alla funzione select
puntatore alla funzione ioctl
puntatore alla funzione close
tabella
degli inode attivi
descrittore di file
tabella
delle informazioni
sulla rete
memoria del processo utente
record di rete (socket)
puntatore a informazioni sulla rete
puntatore alle funzioni read e write
puntatore alla funzione select
puntatore alla funzione ioctl
puntatore alla funzione close
memoria del kernel
Figura 13.12 Struttura dell’I/O nel kernel di UNIX.
•
allocazione dello spazio per il file system;
•
allocazione dei dispositivi;
•
gestione dei buffer, delle cache e delle code di spooling;
scheduling dell’I/o;•
•
controllo dello stato dei dispositivi, gestione degli errori e procedure di ripristino;
•
configurazione e inizializzazione dei driver dei dispositivi.
I livelli superiori del sottosistema per la gestione dell’I/o accedono ai dispositivi per
mezzo dell’interfaccia uniforme fornita dai driver.
13.5 Trasformazione delle richieste di I/O
in operazioni hardware
Il meccanismo di handshaking tra un driver e un controllore di dispositivo è già stato
illustrato; tuttavia, non si è ancora spiegato come il sistema operativo associ alla ri-
chiesta di un’applicazione un insieme di fili di rete o uno specifico settore di disco.
Si consideri per esempio la lettura di un file da un’unità a disco. L’applicazione fa ri-
ferimento ai dati per mezzo del nome del file: è compito del file system fornire il mo-
do di giungere, attraverso la struttura delle directory, alla regione del disco appropria-
ta, cioè quella dove i dati del file sono fisicamente residenti. nell’mS-DoS, per
esempio, il nome del file è associato a un numero che individua un elemento della ta-
bella d’accesso ai file; tale elemento identifica i blocchi del disco assegnati al file. In
unIx il nome è associato a un numero di inode; l’inode corrispondente contiene le
13.5 Trasformazione delle richieste di I/O in operazioni hardware 677
informazioni necessarie per individuare lo spazio allocato. ma come viene effettuato
il collegamento fra il nome del file e il controller del disco (indirizzo hardware della
porta o registri mempory mapped del controller)?
un metodo è quello utilizzato da un sistema relativamente semplice come l’mS-DoS.
La prima parte di un nome di file dell’mS-DoS, precisamente la parte che precede i due
punti, identifica uno specifico dispositivo. Per esempio, C:è la parte iniziale di ogni
nome di file residente nell’unità a disco principale. Questa convenzione è codificata al-
l’interno del sistema operativo: C: è associato a uno specifico indirizzo di porta per
mezzo di una tabella dei dispositivi. Grazie all’uso dei due punti come separatore, lo
spazio dei nomi dei dispositivi è distinto dallo spazio dei nomi del file system, ciò sem-
plifica al sistema operativo l’associazione di funzioni aggiuntive ai dispositivi. Per
esempio, è facile attivare lo spooling per i file di cui è stata richiesta la stampa.
Se, invece, i nomi dei dispositivi sono inclusi nell’ordinario spazio dei nomi del
file system, come in unIx, sono automaticamente disponibili i servizi legati ai nomi
dei file. Per esempio, se il file system associa dei possessori ai nomi dei file e fornisce
il controllo degli accessi a ogni nome di file, si potrà controllare anche l’accesso ai
dispositivi, ed essi avranno un possessore. Visto che i file risiedono nei dispositivi,
una tale interfaccia fornisce due livelli d’accesso al sistema d’I/o: i nomi si possono
usare per accedere ai dispositivi stessi o ai file in essi contenuti.
unIx rappresenta i nomi dei dispositivi all’interno dell’ordinario spazio dei nomi
del file system. a differenza di un nome di file dell’mS-DoS, che include i due punti
come separatore, in un nome di percorso di unIx il nome del dispositivo non è espli-
citamente separato. In effetti, nessuna parte del nome di percorso di un file è il nome
di un dispositivo; unIx impiega una tabella di montaggio (mount table), per associare
i prefissi dei nomi di percorso ai corrispondenti nomi di dispositivi. Quando deve ri-
solvere un nome di percorso, il sistema esamina la tabella per trovare il più lungo pre-
fisso corrispondente: questo elemento della tabella indica il nome del dispositivo vo-
luto. anche questo nome è rappresentato come un oggetto del file system: tuttavia,
quando unIx cerca questo nome nelle strutture delle directory del file system, non tro-
va il numero di un inode, ma una coppia di numeri <principale, secondario>
(<major, minor>)che identifica un dispositivo. Il numero principale individua il
driver che si deve usare per gestire l’I/o nel dispositivo in questione, mentre il numero
secondario deve essere passato a questo driver affinché esso possa determinare, per
mezzo di un’altra tabella, l’indirizzo della porta o l’indirizzo memory mapped del con-
trollore del dispositivo interessato. I moderni sistemi operativi riescono a ottenere un
notevole grado di flessibilità grazie all’uso di tabelle di lookup a vari livelli durante il
processo che porta da una richiesta al controllore del dispositivo; questo processo,
inoltre, è del tutto generale, cosicché non è necessario ricompilare il kernel ogni volta
che si aggiungono al calcolatore nuovi dispositivi e nuovi driver. In effetti, alcuni si-
stemi operativi hanno la capacità di caricare driver di dispositivi su richiesta: all’av-
viamento, il sistema sonda i bus per determinare quali dispositivi siano presenti; quindi
carica i necessari driver, operazione che può anche essere rinviata fino alla prima ri-
chiesta di I/o.
678 Capitolo 13– Sistemi di I/O
richiede I/O processo
utente
chiamata di sistema
può
già soddisfare
la richiesta?
no
sì
trasmette la richiesta
al driver del dispositivo,
se è necessario
sospende il processo
sottosistema
di I/O del kernel
sottosistema
di I/O del kernel
I/O terminato,
i dati in ingresso sono disponibili
o l’emissione dei dati è terminata
rientro dalla chiamata di sistema
trasferisce dati (se è opportuno)
al processo, riporta un codice
di terminazione o d’errore
elabora la richiesta, impartisce
comandi al controllore,
configura il controllore perché
si blocchi fino all’interruzione
driver
del dispositivo
determina quale I/O è terminato,
indica i cambi di stato
al sottosistema di I/O
comandi del controllore
del dispositivo
gestore
delle interruzioni
controlla il dispositivo,
genera un’interruzione
quando l’I/O è terminato
controllore
del dispositivo
riceve l’interruzione, memorizza i dati
per il driver se si tratta di dati
in ingresso, emette un segnale
per sbloccare il driver
interruzione
I/O completato,
genera un segnale
d’interruzione
tempo
Figura 13.13 Schema d’esecuzione di una richiesta di I/O.
La seguente descrizione del tipico svolgimento di una richiesta di lettura bloccante
(Figura 13.13) indica che l’esecuzione di un’operazione di I/o richiede una gran quan-
tità di passi; ciò implica l’uso di un enorme numero di cicli di cPu.
1.
un processo esegue una chiamata di sistema read() bloccante relativa a un
descrittore di file di un file precedentemente aperto.
2.
Il codice della chiamata di sistema all’interno del kernel controlla la correttezza
dei parametri. nel caso di input, se i dati sono già presenti nella buffer cache,
si passano al processo chiamante e l’operazione è conclusa.
13.6 STREAMS 679
3.
4.
5.
altrimenti, è necessario eseguire un’operazione di I/o fisico. Si rimuove il pro-
cesso dalla coda dei processi pronti per l’esecuzione per inserirlo nella coda
d’attesa relativa al dispositivo interessato e si effettua lo scheduling della ri-
chiesta di I/o. Infine il sottosistema di I/o invia la richiesta al driver del dispo-
sitivo; a seconda del sistema operativo, ciò avviene tramite la chiamata di una
procedura, o per mezzo dell’invio di un messaggio interno al kernel.
Il driver del dispositivo assegna un buffer nello spazio d’indirizzi del kernel che
serve per ricevere i dati immessi, ed esegue lo scheduling dell’I/o. Infine il dri-
ver impartisce comandi al controllore del dispositivo scrivendo nei suoi registri.
Il controllore aziona il dispositivo hardware per compiere il trasferimento dei
dati.
6.
Il driver può operare in polling, o può aver predisposto un trasferimento Dma
nella memoria del kernel. Supponiamo che il trasferimento sia gestito dal con-
trollore Dma, il quale genera un’interruzione al termine dell’operazione.
7.
tramite il vettore delle interruzioni, si attiva l’appropriato gestore dell’inter-
ruzione che, dopo aver memorizzato i dati necessari, avverte con un segnale il
driver del dispositivo ed effettua il ritorno dall’interruzione.
8.
Il driver riceve il segnale, individua la richiesta di I/o che è stata completata,
si accerta della riuscita o del fallimento dell’operazione e segnala al sottosiste-
ma di I/o del kernel il completamento dell’operazione.
9.
Il kernel trasferisce dati e/o codici di stato nello spazio degli indirizzi del pro-
cesso chiamante, e sposta tale processo dalla coda d’attesa alla coda dei pro-
cessi pronti per l’esecuzione.
10.
nel momento in cui è posto nella coda dei processi pronti per l’esecuzione, il
processo non è più bloccato: quando lo scheduler gli assegnerà la cPu, esso ri-
prenderà l’elaborazione. L’esecuzione della chiamata di sistema è completata.
13.6 STREAmS
Il sistema operativo unIx System V offre un interessante meccanismo, chiamato
STrEamS, che permette a un’applicazione di comporre dinamicamente catene di co-
dice di driver. uno stream è una connessione full-duplex fra un driver di dispositivo
e un processo utente, e consiste di un elemento di interfaccia per il processo utente
(stream head), un elemento che controlla il dispositivo (driver end), ed eventualmente
un certo numero di moduli intermedi fra questi due elementi (stream modules). tutti
questi componenti contengono una coppia di code, una di lettura e una di scrittura;
per il trasferimento dei dati tra le due code s’impiega uno schema a scambio di mes-
saggi. La Figura 13.14 mostra la struttura del meccanismo di StreamS.
Le funzioni d’elaborazione di StreamS sono fornite da moduli che si inseriscono
nello stream attraverso la chiamata di sistema ioctl(). un processo può, per esem-
pio, aprire tramite uno stream una porta seriale, e può inserire un modulo per editare
680 Capitolo 13– Sistemi di I/O
processo utente
stream head
coda di lettura coda di scrittura
coda di lettura
coda di scrittura
moduli
coda di lettura coda di scrittura
coda di lettura coda di scrittura
driver end
dispositivo
Figura 13.14 Struttura di STREAMS.
i dati immessi. Poiché i messaggi sono scambiati tra code di moduli adiacenti, la coda
di un modulo potrebbe mandare in overflow la coda di un modulo adiacente. Per pre-
venire questo problema, una coda può disporre di un meccanismo di controllo di
flusso. Senza controllo di flusso, una coda accetta tutti i messaggi e li trasferisce im-
mediatamente alla coda del modulo adiacente, senza buffering. una coda che invece
impiega il controllo di flusso memorizza i messaggi in un buffer; se lo spazio dispo-
nibile in esso non è sufficiente, non accetta messaggi. Questo meccanismo richiede
scambi di messaggi di controllo tra code in moduli adiacenti.
un processo utente usa le chiamate di sistema write()o putmsg()per scrivere
dati in un dispositivo; la chiamata di sistema write()scrive semplicemente dati non
strutturati nello stream, mentre putmsg()permette al processo utente di specificare
un messaggio. Indipendentemente dalla chiamata di sistema adoperata dal processo
utente, lo stream head copia i dati in un messaggio e li recapita alla coda del modulo
successivo. Questa copiatura dei messaggi continua finché il messaggio non giunge
al driver end e quindi al dispositivo. analogamente, il processo utente legge i dati dal-
lo stream head usando la chiamata di sistema read() oppure getmsg(). Se si usa
la read() lo stream head preleva un messaggio dalla coda del modulo adiacente e
riporta al processo dati ordinari (una sequenza non strutturata di byte). Se si usa la
getmsg()viene inviato un messaggio al processo utente.
13.7 Prestazioni 681
L’I/o per mezzo di StreamS è asincrono (o non bloccante), con l’eccezione di quan-
do il processo utente comunica con lo stream head. mentre scrive nello stream, il pro-
cesso utente si blocca, se la coda successiva impiega il controllo di flusso, finché non
ci sia spazio sufficiente per copiarvi il messaggio. analogamente, il processo utente
si blocca durante la lettura dallo stream finché non ci sono dati disponibili.
come si è detto, il driver end, come lo stream head e i moduli intermedi, ha una
coda di lettura e una di scrittura. tuttavia deve poter rispondere a interruzioni come
quelle generate quando un pacchetto di dati è pronto per essere letto da una rete. a
differenza dello stream head che si può bloccare se non è possibile copiare un mes-
saggio nella coda del modulo successivo, il driver end deve gestire tutti i dati in arrivo.
I driver devono anche supportare il controllo di flusso. tuttavia, se il buffer di un di-
spositivo è pieno, di solito ignora i messaggi in entrata. Si consideri una scheda di
rete il cui buffer d’ingresso sia pieno; la scheda di rete deve semplicemente ignorare
gli ulteriori messaggi fintantoché non vi sia sufficiente spazio per memorizzare i mes-
saggi in arrivo.
Il vantaggio nell’utilizzo di StreamS consiste nel disporre di un ambiente che
permette uno sviluppo modulare e incrementale di driver di dispositivi e protocolli
di rete. I moduli possono essere usati da diversi stream e quindi da diversi dispositivi.
Per esempio, un modulo di rete potrebbe essere adoperato sia da una scheda di rete
ethernet sia da una scheda di rete wireless 802.11. Inoltre, invece di trattare l’I/o di
dispositivi a caratteri come una sequenza non strutturata di byte, StreamS permette
la gestione dei limiti dei messaggi e delle informazioni di controllo tra i diversi mo-
duli. L’impiego di StreamS è assai diffuso nella maggior parte dei sistemi unIx, ed
è il metodo più usato per la scrittura di protocolli e driver di dispositivi. In unIx
System V e in Solaris, per esempio, il meccanismo delle socket è realizzato tramite
StreamS.
13.7 Prestazioni
L’I/o è uno tra i principali fattori che influiscono sulle prestazioni di un sistema: ri-
chiede un notevole impegno della cPu per l’esecuzione del codice dei driver e per
uno scheduling equo ed efficiente dei processi quando essi sono bloccati e sbloccati.
I risultanti cambi di contesto sfruttano fino in fondo la cPu e le sue memorie cache.
L’I/o, inoltre, rivela le eventuali inefficienze dei meccanismi del kernel per la gestione
delle interruzioni, e impegna il bus della memoria durante i trasferimenti di dati tra i
controllori dei dispositivi e la memoria fisica, e ancora tra i buffer del kernel e lo spa-
zio d’indirizzi delle applicazioni. Soddisfare in modo elegante tutte queste esigenze
è una delle principali questioni che riguardano i progettisti di un calcolatore.
Sebbene i calcolatori moderni siano capaci di gestire molte migliaia di interruzioni
al secondo, la loro gestione è un processo relativamente oneroso. ogni interruzione
fa sì che il sistema cambi stato, esegua il gestore delle interruzioni, e infine ripristini
lo stato originario. Se il numero di cicli impiegato nel busy waiting non è eccessivo,
682 Capitolo 13– Sistemi di I/O
l’I/o programmato può essere più efficiente di quello basato sulle interruzioni. Il com-
pletamento di un’operazione di I/o in genere implica lo sblocco di un processo, com-
portando così l’overhead dovuto a un cambio di contesto.
anche il traffico di una rete può portare a un alto numero di cambi di contesto; si
consideri, per esempio, il login remoto da un calcolatore ad un’altro. ciascun carat-
tere inserito in un calcolatore deve essere comunicato all’altro: quando si inserisce
un carattere nel primo calcolatore, la tastiera produce un segnale d’interruzione; il
carattere arriva tramite il gestore delle interruzioni al driver del dispositivo, da questo
al kernel, e quindi al processo utente. Il processo utente esegue una chiamata di si-
stema di I/o di rete al fine di inviare il carattere al secondo calcolatore. all’interno
del kernel del primo calcolatore, il carattere attraversa gli strati di protocollo necessari
per la costruzione di un pacchetto di rete e giunge al driver di rete, il quale trasferisce
il pacchetto al controllore della interfaccia di rete. Quest’ultimo invia il carattere e
genera un’interruzione che segnala al kernel il completamento della chiamata di si-
stema di I/o di rete.
a questo punto, il dispositivo di rete del secondo calcolatore riceve il pacchetto,
e genera un’interruzione. I protocolli di rete estraggono il carattere dal pacchetto e lo
consegnano all’appropriato demone di rete. Il demone di rete individua a quale ses-
sione di login remoto appartiene il carattere e lo passa al sottodemone che gestisce
la specifica sessione. Durante questo processo avvengono cambi di contesto e di stato
(Figura 13.15). Di solito il destinatario rispedisce al mittente, sotto forma di eco, una
copia del carattere originario, e ciò raddoppia il lavoro necessario.
Per eliminare i cambi di contesto implicati dal trasferimento di ciascun carattere
dal demone al kernel, gli sviluppatori di Solaris hanno implementato nuovamente il
demone telnettramite thread interni al kernel. Secondo stime della Sun, queste mi-
gliorie hanno portato il massimo numero di connessioni contemporanee sostenibili
da un grande server da qualche centinaio a qualche migliaio.
altri sistemi usano unità d’elaborazione specifiche per la gestione dell’I/o dei ter-
minali, riducendo così il carico delle gestione delle interruzioni gravante sulla cPu.
Per esempio, i concentratori di terminali convogliano il traffico proveniente da cen-
tinaia di terminali su un’unica porta di un grande calcolatore. I canali di i/o sono
unità d’elaborazione specializzate presenti nei mainframe e altri sistemi di alto pro-
filo; il loro compito è sollevare la cPu di una parte del peso della gestione dell’I/o.
L’idea di base è che i canali di I/o mantengano il flusso dei dati costante e uniforme,
mentre la cPu rimane libera di elaborare i dati acquisiti. come i controller dei dispo-
sitivi e i controllori Dma che si trovano nei calcolatori di minori dimensioni, un ca-
nale può eseguire programmi più raffinati e generali, e può quindi essere tarato per
specifici carichi di lavoro.
Per migliorare l’efficienza dell’I/o si possono applicare diversi princìpi.
•
ridurre il numero dei cambi di contesto.
•
ridurre il numero di copiature dei dati in memoria durante i trasferimenti fra
dispositivi e applicazioni.
13.7 Prestazioni 683
carattere
inserito
hardware
segnale
d’interruzione
generato
salvataggio
dello stato
gestione
dell’interruzione
driver
del
dispositivo
kernel
cambio
di contesto
processo
utente
termine
della chiamata
di sistema
cambio
di contesto
gestione
dell’interruzione
salvataggio
di stato
segnale
d’interruzione
generato
adattatore
di rete
driver
del
dispositivo
cambio
di
contesto
kernel
rete
pacchetto
di rete
ricevuto
hardware
adattatore
di rete
segnale
d’interruzione
generato
salvataggio
dello stato
driver
del
dispositivo
kernel
sotto-demone
di rete
cambio
di contesto cambio
di contesto
demone
di rete
cambio
di
contesto
kernel
sistema mittente sistema destinatario
Figura 13.15 Comunicazione tra calcolatori.
•
•
•
•
ridurre la frequenza delle interruzioni utilizzando il trasferimento in blocco di
grandi quantità di dati, controllori intelligenti e il polling (nel caso in cui si
possa minimizzare il busy waiting).
aumentare il tasso di concorrenza usando controllori Dma intelligenti o canali
di I/o per sollevare la cPu dalle semplici operazioni di copiatura di dati.
realizzare le primitive di elaborazione direttamente nell’hardware, così da per-
mettere che la loro esecuzione sia simultanea alle operazioni di bus e di cPu.
equilibrare le prestazioni della cPu, del sottosistema di memoria, del bus e
dell’I/o, giacché il sovraccarico di uno qualunque di questi settori provoca l’i-
nutilizzo degli altri.
684 Capitolo 13– Sistemi di I/O
nuovo algoritmo
aumento del tempo
aumento di efficienza
aumento dei costi di sviluppo
aumento di astrazione
codice dell’applicazione
codice del kernel
codice del driver del dispositivo
codice del controllore del dispositivo
(hardware)
codice del dispositivo (hardware)
Figura 13.16 Successione delle funzionalità dei servizi di I/O.
aumento di flessibilità
La complessità dei dispositivi è assai variabile: un mouse per esempio è piuttosto
semplice; i suoi movimenti e la pressione sui pulsanti sono convertiti in valori nume-
rici, passati attraverso il driver del mouse, all’applicazione. Per contro, i servizi forniti
dal driver delle unità a disco del sistema operativo Windows sono assai complessi:
non solo il driver gestisce singole unità a disco, ma costruisce anche array raID (si
veda il Paragrafo 10.7) convertendo le richieste di lettura o scrittura di un’applica-
zione in un insieme coordinato di operazioni di I/o sui dischi. Il driver, inoltre, esegue
sofisticati algoritmi di gestione degli errori e di recupero dei dati, e svolge diverse
funzioni di ottimizzazione delle prestazioni dei dischi.
ci si può chiedere se i servizi di I/o si debbano implementare nei dispositivi
hardware, nei loro driver, o nelle applicazioni. talvolta si può osservare (Figura 13.16)
la seguente successione.
•
Inizialmente, gli algoritmi sperimentali per l’I/o si codificano a livello dell’ap-
plicazione, dato che il codice dell’applicazione è flessibile ed è difficile che er-
rori di programmazione causino l’arresto completo del sistema. In questo modo
si evita inoltre di dover riavviare o ricaricare i driver dei dispositivi ogni volta
che si modifica il codice degli algoritmi. tuttavia, questi algoritmi sono spesso
inefficienti a causa dell’overhead dovuto ai cambi di contesto necessari e del-
l’impossibilità di sfruttare le strutture dati del kernel e i suoi meccanismi interni
(per esempio, la gestione dei messaggi, l’uso dei thread, i lock).
•
Quando uno di questi algoritmi è stato messo a punto, è possibile ricodificarlo
all’interno del kernel. ciò può portare a un miglioramento delle prestazioni,
ma la stesura del codice è più impegnativa, perché il kernel è un ambiente vasto
e complesso. È inoltre necessario verificare accuratamente la correttezza del
codice al fine di evitare alterazioni dei dati e l’arresto del sistema.
13.8 Sommario 685
•
Le prestazioni migliori si ottengono con l’integrazione delle funzioni di tali al-
goritmi in hardware, nei dispositivi o nei controllori. Gli svantaggi di questa
tecnica comprendono la difficoltà e il costo di successive migliorie o dell’eli-
minazione di eventuali errori, il maggior tempo richiesto per portarne a termine
la realizzazione (mesi invece di giorni), e la minore flessibilità. Per esempio,
un controllore raID può essere privo di funzioni che permettono al kernel di
modificare la locazione o l’ordine di lettura o scrittura di singoli blocchi, anche
se il kernel potrebbe possedere informazioni particolari sul carico di lavoro che
gli permetterebbero di migliorare le prestazioni dell’I/o.

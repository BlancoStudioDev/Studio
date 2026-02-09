Memoria virtuale
Nel Capitolo 8 sono state esaminate varie strategie di
gestione della memoria impiegate nei calcolatori. Han-
no tutte lo stesso scopo: tenere contemporaneamente
OBIETTIVI
DEL CAPITOLO
più processi in memoria per permettere la multipro-
grammazione; tuttavia esse tendono a richiedere che
Descrizione dei•
vantaggi derivanti
dalla memoria
virtuale.
Definizione dei•
concetti di
paginazione su
richiesta, algoritmi di
sostituzione di pagina
e allocazione dei
frame.
Trattazione dei•
principi del modello
del working-set.
Studio della relazione•
tra memoria condivisa
e file mappati in
memoria.
Analisi della gestione•
della memoria del
kernel.l’intero processo si trovi in memoria prima di essere
eseguito.
La memoria virtuale è una tecnica che permette di
eseguire processi che possono anche non essere com-
pletamente contenuti in memoria. Il vantaggio princi-
pale offerto da questa tecnica è quello di permettere che
i programmi siano più grandi della memoria fisica;
inoltre la memoria virtuale astrae la memoria centrale
in un vettore di memorizzazione molto grande e unifor-
me, separando la memoria logica, com’è vista dall’u-
tente, da quella fisica. Questa tecnica libera i program-
matori dai problemi di limitazione della memoria. La
memoria virtuale permette inoltre ai processi di condi-
videre facilmente file e di realizzare memorie condivi-
se, e fornisce un meccanismo efficiente per la creazione
dei processi. La memoria virtuale è però difficile da
realizzare e, s’è usata scorrettamente, può ridurre di
molto le prestazioni del sistema. In questo capitolo si
esamina la memoria virtuale nella forma della pagina-
zione su richiesta e se ne valutano complessità e costi.
434 Capitolo 9– Memoria virtuale
9.1 Introduzione
Gli algoritmi di gestione della memoria delineati nel Capitolo 8 sono necessari a cau-
sa di un requisito fondamentale: le istruzioni da eseguire si devono trovare all’interno
della memoria fisica. Il primo metodo per far fronte a tale requisito consiste nel col-
locare l’intero spazio d’indirizzi logici del processo in memoria fisica. Il caricamento
dinamico può aiutare ad attenuare gli effetti di tale limitazione, ma richiede general-
mente particolari precauzioni e un ulteriore impegno dei programmatori.
La condizione che le istruzioni debbano essere nella memoria fisica sembra tanto
necessaria quanto ragionevole, ma purtroppo riduce le dimensioni dei programmi a
valori strettamente correlati alle dimensioni della memoria fisica. In effetti, da un esa-
me dei programmi reali risulta che in molti casi non è necessario avere in memoria
l’intero programma; si considerino per esempio le seguenti situazioni.
•
Spesso i programmi dispongono di codice per la gestione di condizioni d’errore
insolite. Poiché questi errori sono rari, se non inesistenti, anche il relativo codice
non si esegue quasi mai.
•
Spesso ad array, liste e tabelle si assegna più memoria di quanta sia effettivamente
necessaria. Un array si può dichiarare di 100 per 100 elementi, anche se raramente
contiene più di 10 per 10 elementi. La tabella dei simboli di un assemblatore può
avere spazio per 3000 simboli, anche se un programma medio ne ha meno di 200.
•
Alcune opzioni e caratteristiche di un programma sono utilizzabili solo di rado.
Alcune routine di certi programmi amministrativi non vengono eseguite per anni.
Anche nei casi in cui è necessario disporre di tutto il programma, è possibile che non
serva tutto in una volta.
La possibilità di eseguire un programma che si trova solo parzialmente in memoria
porterebbe molti benefici.
•
Un programma non è più vincolato alla quantità di memoria fisica disponibile. Gli
utenti possono scrivere programmi per uno spazio degli indirizzi virtuali molto
grande, semplificando così il compito della programmazione.
•
Poiché ogni programma utente può impiegare meno memoria fisica, si possono
eseguire molti più programmi contemporaneamente, ottenendo un corrispondente
aumento dell’utilizzo e della produttività della CPU senza aumentare il tempo di
risposta o di completamento.
•
Per caricare (o avvicendare) ogni programma utente in memoria sono necessarie
meno operazioni di I/o, quindi ogni programma utente è eseguito più rapidamente.
La possibilità di eseguire un programma che non si trovi completamente in memoria
apporterebbe quindi vantaggi sia al sistema sia all’utente.
La memoria virtuale si fonda sulla separazione della memoria logica percepita
dall’utente dalla memoria fisica. Questa separazione permette di offrire ai program-
matori una memoria virtuale molto ampia, anche se la memoria fisica disponibile è
9.1 Introduzione 435
pagina 0
pagina 1
pagina 2
mappa
di memoria
pagina n
memoria
virtuale
memoria
fisica
Figura 9.1 Schema che mostra una memoria virtuale più grande di quella fisica.
più piccola, com’è illustrato nella Figura 9.1. La memoria virtuale facilita la program-
mazione, poiché il programmatore non deve preoccuparsi della quantità di memoria
fisica disponibile, ma può concentrarsi sul problema da risolvere con il programma.
L’espressione spazio degli indirizzi virtuali si riferisce alla collocazione dei pro-
cessi in memoria dal punto di vista logico (o virtuale). Tipicamente, da tale punto di
vista, un processo inizia in corrispondenza di un certo indirizzo logico – per esempio,
l’indirizzo 0 – e si estende in uno spazio di memoria contigua, come evidenziato dalla
Figura 9.2. Come si ricorderà dal Capitolo 8, è tuttavia possibile organizzare la me-
moria fisica in frame di pagine; in questo caso i frame delle pagine fisiche assegnati
ai processi possono non essere contigui. Spetta all’unità di gestione della memoria
(mmU) associare in memoria le pagine logiche alle pagine fisiche.
Si noti come, nella Figura 9.2, allo heap sia lasciato sufficiente spazio per crescere
verso l’alto nello spazio di memoria, poiché esso ospita la memoria allocata dinami-
camente. In modo analogo, consentiamo allo stack di svilupparsi verso il basso nella
memoria, quando vengono effettuate ripetute chiamate di funzione. L’ampio spazio
vuoto (o buco) che separa lo heap dallo stack è parte dello spazio degli indirizzi vir-
tuali, ma richiede pagine fisiche reali solo nel caso che lo heap o lo stack crescano.
Uno spazio degli indirizzi virtuali che contiene buchi si definisce sparso. Un simile
spazio degli indirizzi è utile, poiché i buchi possono essere riempiti grazie all’espan-
436 Capitolo 9– Memoria virtuale
Max
stack
heap
dati
codice
0
Figura 9.2 Spazio degli indirizzi virtuali.
sione dei segmenti heap o stack, oppure se vogliamo collegare dinamicamente delle
librerie (o altri oggetti condivisi) durante l’esecuzione del programma.
oltre a separare la memoria logica da quella fisica, la memoria virtuale offre il
vantaggio di condividere i file e la memoria fra duo o più processi, mediante la con-
divisione delle pagine (Paragrafo 8.5.4). Ciò comporta i seguenti vantaggi.
•
Le librerie di sistema sono condivisibili da diversi processi associando
(“mappando”) l’oggetto di memoria condiviso a uno spazio degli indirizzi virtuali.
Benché ciascun processo veda le librerie condivise come parte del proprio spazio
degli indirizzi virtuali, le pagine che ospitano effettivamente le librerie nella me-
moria fisica sono in condivisione tra tutti i processi (Figura 9.3). In genere le li-
brerie si associano allo spazio di ogni processo a loro collegato, in modalità di
sola lettura.
•
•
•
In maniera analoga, la memoria può essere condivisa tra processi distinti. Come
si rammenterà dal Capitolo 3, due o più processi possono comunicare condividen-
do memoria. La memoria virtuale permette a un processo di creare una regione di
memoria condivisibile da un altro processo. I processi che condividono questa re-
gione la considerano parte del proprio spazio degli indirizzi virtuali, malgrado le
pagine fisiche siano, in realtà, condivise, come illustrato sempre dalla Figura 9.3.
Le pagine possono essere condivise durante la creazione di un processo mediante
la chiamata di sistema fork(), così da velocizzare la generazione dei processi.
Approfondiremo questi e altri vantaggi offerti dalla memoria virtuale nel corso di
questo capitolo. In primo luogo, però, ci soffermeremo sulla memoria virtuale rea-
lizzata attraverso la paginazione su richiesta.
9.2 Paginazione su richiesta 437
stack
stack
libreria condivisa
pagine condivise
libreria condivisa
heap
dati
heap
dati
codice codice
Figura 9.3 Condivisione delle librerie tramite la memoria virtuale.
9.2 Paginazione su richiesta
Si consideri il caricamento in memoria di un eseguibile residente su disco. Una pos-
sibilità è quella di caricare l’intero programma nella memoria fisica al momento del-
l’esecuzione. Il problema, però, è che all’inizio non è detto che serva avere tutto il
programma in memoria: se il programma, per esempio, fornisce all’avvio una lista
di opzioni all’utente, è inutile caricare il codice per l’esecuzione di tutte le opzioni
previste, senza tener conto di quella effettivamente scelta dall’utente. Una strategia
alternativa consiste nel caricare le pagine nel momento in cui servono realmente; si
tratta di una tecnica, detta paginazione su richiesta, comunemente adottata dai si-
stemi con memoria virtuale. Secondo questo schema, le pagine sono caricate in me-
moria solo quando richieste durante l’esecuzione del programma: ne consegue che
le pagine cui non si accede mai non sono mai caricate nella memoria fisica.
Un sistema di paginazione su richiesta è analogo a un sistema paginato con avvi-
cendamento dei processi in memoria; si veda la Figura 9.4. I processi risiedono in
memoria secondaria (generalmente su disco). Per eseguire un processo occorre cari-
carlo in memoria. Tuttavia, anziché caricare in memoria l’intero processo, si può se-
guire un metodo d’avvicendamento “pigro” (lazy swapping): non si carica mai in me-
moria una pagina che non sia necessaria. Nell’ambito dei sistemi con paginazione su
richiesta l’uso del termine avvicendamento o swapping non è appropriato: uno swap-
per manipola interi processi mentre un paginatore (pager) gestisce le singole pagine
dei processi.
438 Capitolo 9– Memoria virtuale
scaricamento
programma
A
0 1 2 3
4 5 6 7
8 9 10 11
programma
B
caricamento
12 13 14 15
16 17 18 19
20 21 22 23
memoria
centrale
Figura 9.4 Trasferimento di una memoria paginata nello spazio contiguo di un disco.
9.2.1 Concetti fondamentali
Quando un processo sta per essere caricato in memoria, il paginatore ipotizza quali
pagine saranno usate, prima che il processo sia nuovamente scaricato dalla memoria.
Anziché caricare in memoria tutto il processo, il paginatore trasferisce in memoria
solo le pagine che ritiene necessarie. In questo modo è possibile evitare il trasferi-
mento in memoria di pagine che non sono effettivamente usate, riducendo il tempo
d’avvicendamento e la quantità di memoria fisica richiesta.
Con tale schema è necessario che l’hardware fornisca un meccanismo che con-
senta di distinguere le pagine presenti in memoria da quelle nei dischi. A tal fine è
utilizzabile lo schema basato sul bit di validità, descritto nel Paragrafo 8.5.3. In questo
caso, però, il bit impostato come “valido” significa che la pagina corrispondente è va-
lida ed è presente in memoria; il bit impostato come “non valido” indica che la pagina
non è valida (cioè non appartiene allo spazio d’indirizzi logici del processo) oppure
è valida ma è attualmente nel disco. L’elemento della tabella delle pagine di una pa-
gina caricata in memoria s’imposta come al solito, mentre l’elemento della tabella
delle pagine corrispondente a una pagina che attualmente non è in memoria è sem-
plicemente contrassegnato come non valido oppure contiene l’indirizzo della pagina
su disco. Tale situazione è illustrata nella Figura 9.5.
occorre notare che indicare una pagina come non valida non sortisce alcun effetto
se il processo non tenta mai di accedervi. Quindi, se l’ipotesi del paginatore è esatta
9.2 Paginazione su richiesta 439
0
2
3
4
5
6
7
A
B1
C
D
E
F
G
H
memoria
logica
frame
bit di validità/
non validità
4
0 v
1 i
6
2 v
3 i
4 i
9
5 v
6 i
7 i
tabella
delle pagine
0
1
2
3
5
7
8
10
11
12
13
14
15
A4
C6
F9
A B
C D E
F G H
memoria
fisica
Figura 9.5 Tabella delle pagine quando alcune pagine non si trovano nella memoria centrale.
e si caricano tutte e solo le pagine che servono effettivamente, il processo è eseguito
proprio come se fossero state caricate tutte le pagine. Durante l’esecuzione, finchè il
processo accede alle pagine residenti in memoria, l’esecuzione procede come di
consueto.
Che succede se il processo tenta l’accesso a una pagina che non era stata caricata
in memoria? L’accesso a una pagina contrassegnata come non valida causa un evento
o eccezione di page fault (pagina mancante). L’hardware di paginazione, traducendo
l’indirizzo attraverso la tabella delle pagine, nota che il bit è non valido e genera una
trap per il sistema operativo; tale eccezione è dovuta a un “insuccesso” del sistema
operativo nella scelta delle pagine da caricare in memoria. La procedura di gestione
dell’eccezione di page fault è lineare (Figura 9.6).
1.
Si controlla una tabella interna per questo processo (in genere tale tabella è con-
servata insieme al blocco di controllo del processo) allo scopo di stabilire se il ri-
ferimento fosse un accesso alla memoria valido o non valido.
2.
Se il riferimento non era valido, si termina il processo. Se era un riferimento va-
lido, ma la pagina non era ancora stata portata in memoria, se ne effettua il cari-
camento.
440 Capitolo 9– Memoria virtuale
3
la pagina è
nella memoria ausiliaria
sistema
operativo
2
trap
1
tabella
delle pagine
riferimento
load M
i
6
riavvio
dell’esecuzione
dell’istruzione
4
caricamento
della pagina
mancante
frame libero
5
aggiorna
la tabella
delle pagine
memoria
fisica
Figura 9.6 Fasi di gestione di un page fault.
3.
Si individua un frame libero, per esempio prelevandone uno dalla lista dei frame
liberi.
4.
5.
Si programma un’operazione sui dischi per trasferire la pagina desiderata nel fra-
me appena assegnato.
Quando la lettura dal disco è completata, si modificano la tabella interna, conser-
vata con il processo, e la tabella delle pagine per indicare che la pagina si trova
attualmente in memoria.
6.
Si riavvia l’istruzione interrotta dall’eccezione. A questo punto il processo può
accedere alla pagina come se questa fosse stata sempre presente in memoria.
Come caso estremo, è possibile avviare l’esecuzione di un processo senza pagine in
memoria. Quando il sistema operativo carica nel contatore di programma l’indirizzo
della prima istruzione del processo, che è in una pagina non residente in memoria, il
processo genera immediatamente un page fault. Una volta portata la pagina in me-
moria, il processo continua l’esecuzione, generando page fault fino a che tutte le pa-
gine necessarie non si trovino effettivamente in memoria; a questo punto si può ese-
guire il processo senza ulteriori richieste. Lo schema descritto è una paginazione su
9.2 Paginazione su richiesta 441
richiesta pura, vale a dire che una pagina non si trasferisce mai in memoria se non
viene richiesta.
In teoria alcuni programmi possono accedere a diverse nuove pagine di memoria
all’esecuzione di ogni istruzione (una pagina per l’istruzione e molte per i dati), even-
tualmente causando più page fault per ogni istruzione. In un caso simile le prestazioni
del sistema sarebbero inaccettabili. Fortunatamente l’analisi dei programmi in ese-
cuzione mostra che questo comportamento è estremamente improbabile. I programmi
tendono ad avere una località dei riferimenti, descritta nel Paragrafo 9.6.1, quindi
le prestazioni della paginazione su richiesta risultano ragionevoli.
L’hardware di supporto alla paginazione su richiesta è lo stesso che è richiesto per
la paginazione e l’avvicendamento dei processi in memoria:
tabella delle pagine. Questa tabella ha la capacità di contrassegnare un elemento•
come non valido attraverso un bit di validità oppure un valore speciale dei bit di
protezione;
memoria secondaria. Questa memoria conserva le pagine non presenti in memo-•
ria centrale. Generalmente la memoria secondaria è costituita da un disco ad alta
velocità detto dispositivo di swap; la sezione del disco usata a questo scopo si chia-
ma area di avvicendamento (swap space). L’allocazione di quest’area è trattata
nel Capitolo 10.
Uno dei requisiti cruciali della paginazione su richiesta è la possibilità di rieseguire
una qualunque istruzione dopo un page fault. Avendo salvato lo stato del processo in-
terrotto (registri, codici di condizione, contatore di programma) al momento del page
fault, occorrerà riavviare il processo esattamente dallo stesso punto e con lo stesso
stato, eccezion fatta per la presenza della pagina desiderata in memoria. Nella mag-
gior parte dei casi questo requisito è facile da soddisfare. Un page fault si può verifi-
care per qualsiasi riferimento alla memoria. Se si verifica durante la fase di fetch (pre-
lievo) di un’istruzione, l’esecuzione si può riavviare effettuando nuovamente il fetch.
Se si verifica durante il fetch di un operando, bisogna effettuare nuovamente fetch e
decode dell’istruzione, quindi si può prelevare l’operando.
Come caso limite si consideri un’istruzione a tre indirizzi, come per esempio la
somma (ADD) del contenuto di A al contenuto di B, con risultato posto in C. I passi
necessari per eseguire l’istruzione sono i seguenti:
1.
fetch e decodifica dell’istruzione (ADD);
2.
prelievo del contenuto di A;
3.
prelievo del contenuto di B;
4.
addizione del contenuto di Aal contenuto di B;
5.
memorizzazione della somma in C.
Se il page fault avviene al momento della memorizzazione in C, poiché Csi trova in
una pagina che non è in memoria, occorre prelevare la pagina desiderata, caricarla in
memoria, correggere la tabella delle pagine e riavviare l’istruzione. Il riavvio dell’i-
442 Capitolo 9– Memoria virtuale
struzione richiede una nuova operazione di fetch, con nuova decodifica e nuovo pre-
lievo dei due operandi; infine occorre ripetere l’addizione. In ogni modo il lavoro da
ripetere non è molto, meno di un’istruzione completa, e la ripetizione è necessaria
solo nel caso si verifichi un page fault.
La difficoltà maggiore si presenta quando un’istruzione può modificare parecchie
locazioni diverse. Si consideri, per esempio, l’istruzione MVC (move character) del
sistema IBm 360/370: quest’istruzione può spostare una sequenza di byte (fino a 256)
da una locazione a un’altra (con possibilità di sovrapposizione). Se una delle sequen-
ze (quella d’origine o quella di destinazione) esce dal confine di una pagina, si può
verificare un page fault quando lo spostamento è stato effettuato solo in parte. Inoltre,
se le sequenze d’origine e di destinazione si sovrappongono, è possibile che la se-
quenza d’origine sia stata modificata, in tal caso non è possibile limitarsi a riavviare
l’istruzione.
Il problema si può risolvere in due modi. In una delle due soluzioni il microcodice
computa e tenta di accedere alle estremità delle due sequenze di byte. Un’eventuale
page fault si può verificare solo in questa fase, prima che si apporti qualsiasi modifica.
A questo punto si può compiere lo spostamento senza rischio di page fault perché
tutte le pagine interessate si trovano in memoria. L’altra soluzione si serve di registri
temporanei per conservare i valori delle locazioni sovrascritte. Nel caso di un page
fault, si riscrivono tutti i vecchi valori in memoria prima che sia generata la trap. Que-
sta operazione riporta la memoria allo stato in cui si trovava prima che l’istruzione
fosse avviata, perciò si può ripetere la sua esecuzione.
Sebbene non si tratti certo dell’unico problema da affrontare per estendere un’ar-
chitettura esistente con la funzionalità della paginazione su richiesta, illustra alcune
delle difficoltà da superare. Il sistema di paginazione si colloca tra la CPU e la me-
moria di un calcolatore e deve essere completamente trasparente al processo utente.
L’opinione comune che la paginazione si possa aggiungere a qualsiasi sistema è vera
per gli ambienti senza paginazione su richiesta, nei quali un’eccezione di page fault
rappresenta un errore fatale, ma è falsa nei casi in cui un’eccezione di page fault im-
plica solo la necessità di caricare in memoria un’altra pagina e quindi riavviare il pro-
cesso.
9.2.2 Prestazioni della paginazione su richiesta
La paginazione su richiesta può avere un effetto rilevante sulle prestazioni di un cal-
colatore. Il motivo si può comprendere calcolando il tempo d’accesso effettivo per
una memoria con paginazione su richiesta. Attualmente, nella maggior parte dei cal-
colatori il tempo d’accesso alla memoria, che si denota ma, varia da 10 a 200 nanose-
condi. Finché non si verifichino page fault, il tempo d’accesso effettivo è uguale al
tempo d’accesso alla memoria. Se però si verifica un page fault, occorre prima leggere
dal disco la pagina interessata e quindi accedere alla parola della memoria desiderata.
9.2 Paginazione su richiesta 443
Supponendo che p sia la probabilità che si verifichi un page fault (0 £ p £ 1), è pro-
babile che p sia molto vicina allo zero, cioè che ci siano solo pochi fault. Il tempo
d’accesso effettivo è dato dalla seguente espressione:
tempo d’accesso effettivo = (1 – p) – ma + p × tempo di gestione del page fault
Per calcolare il tempo d’accesso effettivo occorre conoscere il tempo necessario alla
gestione di un page fault. In tal caso si deve eseguire la seguente sequenza:
1.
trap per il sistema operativo;
2.
salvataggio dei registri utente e dello stato del processo;
3.
verifica che l’interruzione sia dovuta o meno a un page fault;
4.
controllo della correttezza del riferimento alla pagina e determinazione della
locazione della pagina nel disco;
5.
lettura dal disco e trasferimento in un frame libero:
a) attesa nella coda relativa a questo dispositivo finché la richiesta di lettura
non sia servita;
b) attesa del tempo di posizionamento e latenza del dispositivo;
c) inizio del trasferimento della pagina in un frame libero;
6.
durante l’attesa, allocazione della CPU a un altro processo utente (scheduling
della CPU, facoltativo);
7.
ricezione di un’interruzione dal controllore del disco (I/o completato);
8.
salvataggio dei registri e dello stato dell’altro processo utente (se è stato ese-
guito il passo 6);
9.
verifica della provenienza dell’interruzione dal disco;
10.
aggiornamento della tabella delle pagine e di altre tabelle per segnalare che la
pagina richiesta è attualmente presente in memoria;
11.
attesa che la CPU sia nuovamente assegnata a questo processo;
12.
ripristino dei registri utente, dello stato del processo e della nuova tabella delle
pagine, quindi ripresa dell’istruzione interrotta.
Non sempre sono necessari tutti i passi sopra elencati. Nel passo 6, per esempio, si
ipotizza che la CPU sia assegnata a un altro processo durante un’operazione di I/o.
Tale possibilità permette la multiprogrammazione per mantenere occupata la CPU,
ma una volta completato il trasferimento di I/o implica un dispendio di tempo per ri-
prendere la procedura di servizio dell’eccezione di page fault.
In ogni caso, il tempo di servizio dell’eccezione di page fault ha tre componenti
principali:
1.
servizio del segnale di eccezione di page fault;
2.
lettura della pagina da disco;
riavvio del processo.3.
444 Capitolo 9– Memoria virtuale
La prima e la terza operazione si possono ridurre, per mezzo di un’accurata codifica,
ad alcune centinaia di istruzioni. Ciascuna di queste operazioni può quindi richiedere
da 1 a 100 microsecondi. D’altra parte, il tempo di trasferimento di pagina è proba-
bilmente vicino a 8 millisecondi (un disco ha in genere un tempo di latenza di 3 mil-
lisecondi, un tempo di posizionamento di 5 millisecondi e un tempo di trasferimento
di 0,05 millisecondi, quindi il tempo totale della paginazione è dell’ordine di 8 mil-
lisecondi, comprendendo le tempistiche hardware e software). Inoltre nel calcolo si
è considerato solo il tempo di servizio del dispositivo. Se una coda di processi è in
attesa del dispositivo è necessario considerare anche il tempo di accodamento del di-
spositivo, poiché occorre attendere che il dispositivo di paginazione sia libero per ser-
vire la richiesta, quindi il tempo di trasferimento aumenta ulteriormente.
Considerando un tempo medio di servizio dell’eccezione di page fault di 8 milli-
secondi e un tempo d’accesso alla memoria di 200 nanosecondi, il tempo effettivo
d’accesso in nanosecondi è il seguente:
tempo d’accesso effettivo = (1 – p) × 200 + p (8 millisecondi)
= (1 – p) × 200 + p × 8.000.000
= 200 + 7.999.800 × p
Il tempo d’accesso effettivo è direttamente proporzionale al tasso di page fault (pa-
ge-fault rate). Se un accesso su 1000 accusa un page fault, il tempo d’accesso effet-
tivo è di 8,2 microsecondi. Impiegando la paginazione su richiesta, il calcolatore è
rallentato di un fattore pari a 40! Se si desidera un rallentamento inferiore al 10 per
cento, occorre contenere la probabilità di page fault al seguente livello:
220 > 200 + 7.999.800 × p
20 > 7.999.800 × p
p < 0,00000025
Quindi, per mantenere a un livello ragionevole il rallentamento dovuto alla pagina-
zione, si può permettere meno di un page fault ogni 399.990 accessi alla memoria.
In un sistema con paginazione su richiesta, è cioè importante tenere basso il tasso di
page fault, altrimenti il tempo effettivo d’accesso aumenta, rallentando molto l’ese-
cuzione del processo.
Un altro aspetto della paginazione su richiesta è la gestione e l’uso generale del-
l’area di swap. L’I/o di un disco relativo all’area di swap è generalmente più rapido
di quello relativo al file system (Capitolo 10): ciò si deve al fatto che lo spazio di swap
è allocato in blocchi molto grandi e non vengono utilizzate ricerche e riferimenti in-
diretti. Perciò il sistema può migliorare l’efficienza della paginazione copiando tutta
l’immagine di un file nell’area di swap all’avvio del processo e di lì eseguire la pagi-
nazione su richiesta. Un’altra possibilità consiste nel richiedere inizialmente le pagine
al file system, ma scrivere le pagine nell’area di swap al momento della sostituzione.
Questo metodo assicura che si leggano sempre dal file system solo le pagine neces-
sarie, ma che tutta la paginazione successiva sia fatta dall’area di swap.
Alcuni sistemi tentano di limitare l’area di swap utilizzata per file binari: le pagine
richieste per questi file si prelevano direttamente dal file system; tuttavia, quando è
9.3 Copiatura su scrittura 445
richiesta una sostituzione di pagine, i frame possono semplicemente essere sovra-
scritti, dato che non sono mai stati modificati, e le pagine, se è necessario, possono
essere nuovamente lette dal file system. Seguendo questo criterio, lo stesso file system
funziona da memoria ausiliaria (backing store). L’area di swap si deve in ogni caso
usare per le pagine che non sono relative ai file (la cosiddetta memoria anonima);
queste comprendono lo stack e lo heap di un processo. Questa tecnica che sembra es-
sere un buon compromesso si usa in diversi sistemi tra cui Solaris e UNIx BSD.
I sistemi operativi mobili non supportano, in genere, lo swapping, ma, in caso di
carenza di memoria, richiedono pagine al file system e recuperano pagine di sola let-
tura (come il codice) dalle applicazioni. Se necessario, questi dati possono essere ri-
chiesti di nuovo al file system. In ioS non vengono mai riprese a un’applicazione le
pagine di memoria anonima a meno che l’applicazione sia terminata o abbia rilasciato
la memoria in maniera volontaria.
9.3 Copiatura su scrittura
Nel Paragrafo 9.2 si è visto come un processo possa cominciare rapidamente l’ese-
cuzione richiedendo solo la pagina contenente la prima istruzione. La generazione
dei processi tramite fork(), però, può inizialmente evitare la paginazione su richie-
sta per mezzo di una tecnica simile alla condivisione delle pagine (Paragrafo 8.5.4),
che garantisce la celere generazione dei processi riuscendo anche a minimizzare il
numero di nuove pagine allocate al processo appena creato.
Si ricordi che la chiamata di sistema fork()crea un processo figlio come dupli-
cato del genitore. Nella sua versione originale la fork()creava per il figlio una copia
dello spazio d’indirizzi del genitore, duplicando le pagine appartenenti al processo ge-
nitore. Considerando che molti processi figli eseguono subito dopo la loro creazione
la chiamata di sistema exec(), questa operazione di copiatura può essere inutile. Co-
me alternativa, si può impiegare una tecnica nota come copiatura su scrittura (copy-
on write), il cui funzionamento si fonda sulla condivisone iniziale delle pagine da parte
dei processi genitori e dei processi figli. Le pagine condivise si contrassegnano come
pagine da copiare su scrittura, a significare che, se un processo (genitore o figlio) scrive
su una pagina condivisa, il sistema deve creare una copia di tale pagina. La copia su
scrittura è illustrata nella Figura 9.7 e nella Figura 9.8, che mostrano il contenuto della
memoria fisica prima e dopo che il processo 1 abbia modificato la pagina C.
Si consideri per esempio un processo figlio che cerchi di modificare una pagina
contenente parti della stack, quando le pagine sono contrassegnate come copy-on
write. Il sistema operativo crea una copia della pagina nello spazio degli indirizzi del
processo figlio. Il processo figlio modifica la sua copia della pagina e non la pagina
appartenente al processo genitore. È chiaro che, adoperando la tecnica di copiatura
su scrittura, si copiano soltanto le pagine modificate da uno dei due processi, mentre
tutte le altre sono condivisibili dai processi genitore e figlio. Si noti inoltre che sol-
tanto le pagine modificabili si devono contrassegnare come copy-on write, mentre
quelle che non si possono modificare (per esempio, le pagine contenenti codice ese-
446 Capitolo 9– Memoria virtuale
processo1 memoria fisica
pagina A
pagina B
pagina C
processo2
Figura 9.7 Prima della modifica alla pagina C da parte del processo 1.
guibile) sono condivisibili dai processi genitore e figlio. La tecnica di copiatura su
scrittura è piuttosto comune e si usa in diversi sistemi operativi, tra i quali Windows
xP , Linux e Solaris.
Quando è necessaria la duplicazione di una pagina secondo la tecnica di copiatura
su scrittura, è importante capire da dove si attingerà la pagina libera necessaria. molti
sistemi operativi forniscono, per queste richieste, un gruppo (pool) di pagine libere,
che di solito si assegnano quando lo stack o lo heap di un processo devono espandersi,
oppure proprio per gestire pagine da copiare su scrittura. L’allocazione di queste pa-
gine di solito avviene secondo una tecnica nota come azzeramento su richiesta
(zero-fill-on-demand); prima dell’allocazione si riempiono di zeri le pagine, cancel-
landone in questo modo tutto il contenuto precedente.
Diverse versioni di UNIx (compreso Solaris e Linux) offrono anche una variante
della chiamata di sistema fork()– detta vfork() (per virtual memory fork). La
vfork()offre un’alternativa all’uso della fork()con copiatura su scrittura. Con la
vfork()il processo genitore viene sospeso e il processo figlio usa lo spazio d’indi-
rizzi del genitore. Poiché la vfork()non usa la copiatura su scrittura, se il processo
figlio modifica qualche pagina dello spazio d’indirizzi del genitore, le pagine modi-
processo1 memoria fisica processo2
pagina A
pagina B
pagina C
copia della
pagina C
Figura 9.8 Dopo la modifica alla pagina C da parte del processo 1.
9.4 Sostituzione delle pagine 447
ficate saranno visibili al processo genitore non appena riprenderà il controllo. È quin-
di necessaria molta attenzione nell’uso di vfork(), per assicurarsi che il processo
figlio non modifichi lo spazio d’indirizzi del genitore. La chiamata di sistema
vfork()è adatta al caso in cui il processo figlio esegua una exec()immediatamen-
te dopo la sua creazione. Poiché non richiede alcuna copiatura delle pagine, la
vfork() è un metodo di creazione dei processi molto efficiente, in alcuni casi im-
piegato per realizzare le interfacce shell in UNIx.
9.4 Sostituzione delle pagine
Nelle descrizioni fatte finora sul tasso di page fault abbiamo supposto che ogni pagina
poteva dar luogo al massimo a un fault, la prima volta in cui si effettuava un riferi-
mento a essa. Tale rappresentazione tuttavia non è molto precisa. Se un processo di
10 pagine ne impiega effettivamente solo la metà, la paginazione su richiesta fa ri-
sparmiare l’I/o necessario per caricare le cinque pagine che non sono mai usate. Inol-
tre il grado di multiprogrammazione potrebbe essere aumentato eseguendo il doppio
dei processi. Quindi, disponendo di 40 frame, si potrebbero eseguire otto processi an-
ziché i quattro che si eseguirebbero se ciascuno di loro richiedesse 10 blocchi di me-
moria, cinque dei quali non sarebbero mai usati.
Aumentando il grado di multiprogrammazione, si sovrassegna la memoria. Ese-
guendo sei processi, ciascuno dei quali è formato da 10 pagine, di cui solo cinque so-
no effettivamente usate, s’incrementerebbero l’utilizzo e la produttività della CPU e
si avrebbero ancora 10 frame disponibili. Tuttavia è possibile che ciascuno di questi
processi, per un insieme particolare di dati, abbia improvvisamente necessità di im-
piegare tutte le 10 pagine, perciò sarebbero necessari 60 frame, mentre ne sono di-
sponibili solo 40.
Si consideri inoltre che la memoria del sistema non si usa solo per contenere pa-
gine di programmi: le aree di memoria per l’I/o impegnano una rilevante quantità di
memoria. Ciò può aumentare le difficoltà agli algoritmi di allocazione della memoria.
Decidere quanta memoria assegnare all’I/o e quanta alle pagine dei programmi è un
problema complesso. Alcuni sistemi riservano una quota fissa di memoria per l’I/o,
altri permettono sia ai processi utenti sia al sottosistema di I/o di competere per tutta
la memoria del sistema.
La sovrallocazione (over-allocation) si può illustrare come segue. Durante l’ese-
cuzione di un processo utente si verifica un page fault. Il sistema operativo determina
la locazione del disco in cui risiede la pagina desiderata, ma poi scopre che la lista
dei frame liberi è vuota: tutta la memoria è in uso (Figura 9.9).
A questo punto il sistema operativo può scegliere tra diverse possibilità, per esem-
pio può terminare il processo utente. Tuttavia, la paginazione su richiesta è un tenta-
tivo che il sistema operativo fa per migliorare l’utilizzo e la produttività del sistema
di calcolo. Gli utenti non dovrebbero sapere che i loro processi sono eseguiti su un
sistema paginato. La paginazione deve essere logicamente trasparente per l’utente,
quindi la terminazione del processo non costituisce la scelta migliore.
448 Capitolo 9– Memoria virtuale
frame
bit di validità/
non validità
0
H
1
load M
PC
2
J
3
4
5
v
0
monitor
v
v
i
1
3
M
2
D
tabella delle pagine
per l'utente 1
memoria logica
per l’utente 1
3
H
frame
bit di validità/
non validità
4
load M
B
5
J
6
A
0
A
6
1
B
2
v
i
v
7
E
M
2
D
7
v
memoria
fisica
3
E
tabella delle pagine
per l'utente 2
memoria logica
per l’utente 2
Figura 9.9 Necessità di sostituzione di pagine.
Il sistema operativo può scaricare dalla memoria un intero processo, liberando tutti i
suoi frame e riducendo il livello di multiprogrammazione. Questa possibilità, buona
in certe situazioni, è considerata nel Paragrafo 9.6. In questa sede analizziamo l’op-
zione più comune: la sostituzione delle pagine (page replacement).
9.4.1 Sostituzione di pagina
La sostituzione delle pagine segue il seguente criterio: se nessun frame è libero, ne
viene liberato uno attualmente inutilizzato. È possibile liberarlo scrivendo il suo con-
tenuto nell’area di swap e modificando la tabella delle pagine (e tutte le altre tabelle)
per indicare che la pagina non si trova più in memoria (Figura 9.10). Il frame liberato
si può usare per memorizzare la pagina che ha causato il fault. Si modifica la proce-
dura di servizio dell’eccezione di page fault in modo da includere la sostituzione della
pagina:
1.
s’individua la locazione su disco della pagina richiesta;
2.
si cerca un frame libero:
a. se esiste, lo si usa;
b. altrimenti si impiega un algoritmo di sostituzione delle pagine per scegliere
un frame vittima;
c. si scrive la pagina “vittima” nel disco; si di conseguenza le tabelle delle pa-
gine e quelle dei frame;
9.4 Sostituzione delle pagine 449
frame
bit di validità/
non validità
1
scaricamento
della pagina
vittima
0
i
f v
tabella
delle pagine
2
f
modifica
a non valido
4
aggiorna la
tabella delle pagine
per la nuova
pagina
vittima
3
caricamento
della pagina
richiesta
memoria
fisica
Figura 9.10 Sostituzione di una pagina.
3.
si scrive la pagina richiesta nel frame appena liberato; si modificano le tabelle
delle pagine e dei frame;
4.
si riprende il processo utente dal punto in cui si è verificato il page fault.
occorre notare che, se non esiste alcun frame libero sono necessari due trasferimenti
di pagine, uno fuori e uno dentro la memoria. Questa situazione raddoppia il tempo di
servizio del page fault e aumenta di conseguenza anche il tempo effettivo d’accesso.
Questo sovraccarico si può ridurre usando un bit di modifica (modify bit o dirty
bit). In questo caso l’hardware del calcolatore dispone di un bit di modifica, associato
a ogni pagina (o frame), che viene posto a 1 ogni volta che nella pagina si scrive un
byte, indicando che la pagina è stata modificata. Quando si sceglie una pagina da so-
stituire si esamina il suo bit di modifica; se è a 1, significa che quella pagina è stata
modificata rispetto a quando era stata letta dal disco; in questo caso la pagina deve
essere scritta nel disco. Se il bit di modifica è rimasto a 0, significa che la pagina non
è stata modificata da quando è stata caricata in memoria, quindi non è necessario scri-
vere nel disco la pagina di memoria: c’è già. Questa tecnica vale anche per le pagine
di sola lettura, per esempio pagine di codice binario. Queste pagine non possono es-
sere modificate, quindi si possono rimuovere in ogni momento. Questo schema può
ridurre in modo considerevole il tempo per il servizio del page fault, poiché dimezza
il tempo di I/o, se la pagina non è stata modificata.
450 Capitolo 9– Memoria virtuale
La sostituzione di una pagina è fondamentale al fine della paginazione su richiesta,
perché completa la separazione tra memoria logica e memoria fisica. Con questo mec-
canismo si può mettere a disposizione dei programmatori una memoria virtuale enor-
me con una memoria fisica più piccola. Senza la paginazione su richiesta, gli indirizzi
utente si fanno corrispondere a indirizzi fisici e i due insiemi di indirizzi possono es-
sere diversi. Tuttavia tutte le pagine di un processo devono ancora essere in memoria
fisica. Con la paginazione su richiesta la dimensione dello spazio degli indirizzi logici
non è più limitata dalla memoria fisica. Per esempio, un processo utente formato da
20 pagine si può eseguire in 10 frame semplicemente usando la paginazione su ri-
chiesta e un algoritmo di sostituzione per localizzare un frame libero ogni qual volta
sia necessario. Se una pagina modificata deve essere sostituita, si copia nel disco il
suo contenuto. Un successivo riferimento a quella pagina causa un’eccezione di page
fault. In quel momento, la pagina viene riportata in memoria, eventualmente sosti-
tuendo un’altra pagina.
Per realizzare la paginazione su richiesta è necessario risolvere due problemi prin-
cipali: occorre sviluppare un algoritmo di allocazione dei frame e un algoritmo di
sostituzione delle pagine. ossia, se sono presenti più processi in memoria, occorre
decidere quanti frame vadano assegnati a ciascun processo. Inoltre, quando è richiesta
una sostituzione di pagina, occorre selezionare i frame da sostituire. La progettazione
di algoritmi idonei a risolvere questi problemi è un compito importante, poiché l’I/o
nei dischi è molto oneroso. Anche miglioramenti minimi ai metodi di paginazione su
richiesta apportano notevoli incrementi alle prestazioni del sistema.
Esistono molti algoritmi di sostituzione delle pagine; probabilmente ogni sistema
operativo ha il proprio schema di sostituzione. È quindi necessario stabilire un criterio
per selezionare un algoritmo di sostituzione particolare; comunemente si sceglie quel-
lo con il minimo tasso di page fault.
Un algoritmo si valuta effettuandone l’esecuzione su una particolare successione
di riferimenti alla memoria e calcolando il numero di page fault. La successione dei
riferimenti alla memoria è detta, appunto, successione dei riferimenti. Queste suc-
cessioni si possono generare artificialmente (per esempio con un generatore di numeri
casuali), oppure analizzando un dato sistema e registrando l’indirizzo di ciascun ri-
ferimento alla memoria. Quest’ultima opzione genera un numero elevato di dati,
dell’ordine di un milione di indirizzi al secondo. Per ridurre questa quantità di dati
occorre notare due fatti.
Innanzitutto, per una pagina di dimensioni date, generalmente fissate dall’archi-
tettura del sistema, si considera solo il numero della pagina anziché l’intero indirizzo.
In secondo luogo, se si ha un riferimento a una pagina p, i riferimenti alla stessa pa-
gina immediatamente successivi al primo non generano page fault: dopo il primo ri-
ferimento, la pagina p è presente in memoria.
Esaminando un processo si potrebbe per esempio registrare la seguente succes-
sione di indirizzi:
0100, 0432, 0101, 0612, 0102, 0103, 0104, 0101, 0611, 0102, 0103,
0104, 0101, 0610, 0102, 0103, 0104, 0101, 0609, 0102, 0105
9.4 Sostituzione delle pagine 451
numero di page fault
16
14
12
10
8
6
4
2
1 2 3 4 5 6
numero dei frame
Figura 9.11 Grafico che illustra il numero di page fault rispetto al numero dei frame.
che, a 100 byte per pagina, si riduce alla seguente successione di riferimenti:
1, 4, 1, 6, 1, 6, 1, 6, 1, 6, 1
Per stabilire il numero di page fault relativo a una particolare successione di riferi-
menti e a un particolare algoritmo di sostituzione delle pagine, occorre conoscere an-
che il numero dei frame disponibili. Naturalmente, aumentando il numero di que-
st’ultimi diminuisce il numero di page fault. Per la successione dei riferimenti
precedentemente esaminata, per esempio, dati tre o più blocchi di memoria avremmo
solo tre fault: uno per il primo riferimento di ogni pagina. D’altra parte, se si dispone
di un solo frame è necessaria una sostituzione per ogni riferimento, con il risultato di
11 page fault. In generale ci si aspetta una curva simile a quella della Figura 9.11.
Aumentando il numero dei frame, il numero di page fault diminuisce fino al livello
minimo. Naturalmente aggiungendo memoria fisica il numero dei frame aumenta.
Per illustrare gli algoritmi di sostituzione delle pagine impiegheremo la seguente
successione di riferimenti
7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 1, 2, 0, 1, 7, 0, 1
per una memoria con tre frame.
9.4.2 Sostituzione delle pagine secondo l’ordine d’arrivo
(FIFO)
L’algoritmo di sostituzione delle pagine più semplice è un algoritmo FIFo. Questo al-
goritmo associa a ogni pagina l’istante di tempo in cui quella pagina è stata portata
in memoria. Se si deve sostituire una pagina, si seleziona quella presente in memoria
da più tempo. occorre notare che non è strettamente necessario registrare l’istante in
452 Capitolo 9– Memoria virtuale
successione dei riferimenti
7 0 1 2 0 3 0 4 2 3 0 3 2 1 2 0 1 7 0 1
7
7
7
2
2
2
4
4
4
0
0
0
0
3
3
3
2
2
2
1
1
1
0
0
0
3
3
frame delle pagine
Figura 9.12 Algoritmo di sostituzione delle pagine FiFo.
0
1
3
0
1
2
7
1
2
7
0
2
7
0
1
cui si carica una pagina in memoria; infatti si può creare una coda FIFo di tutte le pa-
gine presenti in memoria. In questo caso si sostituisce la pagina che si trova in testa
alla coda. Quando si carica una pagina in memoria, la si inserisce nell’ultimo ele-
mento della coda.
Nella successione di riferimenti di esempio, i nostri tre frame sono inizialmente
vuoti. I primi tre riferimenti (7, 0, 1) accusano ciascuno un page fault con conseguente
caricamento delle relative pagine nei frame vuoti. Il riferimento successivo (2) causa
la sostituzione della pagina 7, perché essa è stata caricata per prima in memoria. Sic-
come 0 è il riferimento successivo e si trova già in memoria, per questo riferimento
non ha luogo alcun page fault. Il primo riferimento a 3 causa la sostituzione della pa-
gina 0, che ora è la prima pagina in coda. A causa di questa sostituzione il riferimento
successivo, a 0, causerà un page fault. La pagina 1 è poi sostituita dalla pagina 0. Que-
sto processo prosegue come è illustrato nella Figura 9.12. ogni volta che si verifica
un page fault sono indicate le pagine presenti nei tre frame. Complessivamente si han-
no 15 page fault.
L’algoritmo FIFo di sostituzione delle pagine è facile da capire e da programmare;
tuttavia la sue prestazioni non sono sempre buone. La pagina sostituita potrebbe es-
sere un modulo di inizializzazione usato molto tempo prima e che non serve più, ma
potrebbe anche contenere una variabile molto usata, inizializzata precedentemente,
e ancora in uso.
occorre notare che anche se si sceglie una pagina da sostituire che è in uso attivo,
tutto continua a funzionare correttamente. Dopo aver rimosso una pagina attiva per
inserirne una nuova, quasi immediatamente si verifica un’eccezione di page fault per
riprendere la pagina attiva. Per riportare la pagina attiva in memoria è necessario so-
stituire un’altra pagina. Quindi, una cattiva scelta della pagina da sostituire aumenta
il tasso di page fault e rallenta l’esecuzione del processo, ma non causa errori.
Per illustrare i problemi che possono insorgere con l’uso dell’algoritmo di sosti-
tuzione delle pagine FIFo, si consideri la seguente successione di riferimenti:
1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5
Nella Figura 9.13 è illustrata la curva dei page fault per questa successione di riferi-
menti in funzione del numero dei frame disponibili. occorre notare che il numero dei
9.4 Sostituzione delle pagine 453
16
numero di page fault
14
12
10
8
6
4
2
1
2 3 4 5 6 7
numero dei frame
Figura 9.13 Curva dei page fault per la sostituzione FiFo su una successione di riferimenti.
page fault (10) per quattro frame è maggiore del numero dei page fault (9) per tre fra-
me. Questo inatteso risultato è noto col nome di anomalia di Belady: con alcuni al-
goritmi di sostituzione delle pagine, il tasso di page fault può aumentare con l il tasso
minimo di page fault aumentare del numero dei frame assegnati. A prima vista sem-
bra logico supporre che fornendo più memoria a un processo le prestazioni di que-
st’ultimo migliorino. In alcune delle prime ricerche sperimentali si notò invece che
questo presupposto non sempre è vero; venne così individuata l’anomalia di Belady.
9.4.3 Sostituzione ottimale delle pagine
In seguito alla scoperta dell’anomalia di Belady si è ricercato un algoritmo ottimale
di sostituzione delle pagine. Tale algoritmo è quello che fra tutti gli algoritmi pre-
senta il tasso minimo di page fault e non presenta mai l’anomalia di Belady. Questo
algoritmo esiste ed è stato chiamato oPT o mIN. Consiste semplicemente nel:
sostituire la pagina che non verrà usata per il periodo di tempo più lungo.
L’uso di quest’algoritmo di sostituzione delle pagine assicura il tasso minimo di page
fault per un dato numero di frame.
Per esempio, nella successione dei riferimenti d’esempio, l’algoritmo ottimale di
sostituzione delle pagine produce nove page fault, come è mostrato nella Figura 9.14.
I primi tre riferimenti causano page fault che riempiono i tre blocchi di memoria vuo-
ti. Il riferimento alla pagina 2 determina la sostituzione della pagina 7, perché la 7
non è usata fino al riferimento 18, mentre la pagina 0 viene usata al 5 e la pagina 1
al 14. Il riferimento alla pagina 3 causa la sostituzione della pagina 1, poiché la pa-
gina 1 è l’ultima delle tre pagine in memoria cui si fa nuovamente riferimento. Con
sole nove page fault, la sostituzione ottimale risulta assai migliore di quella ottenuta
con un algoritmo FIFo, dove i page fault erano 15. Ignorando i primi tre page fault,
che si verificano con tutti gli algoritmi, la sostituzione ottimale è due volte migliore
454 Capitolo 9– Memoria virtuale
successione dei riferimenti
7 0 1 2 0 3 0 4 2 3 0 3 2 1 2 0 1 7 0 1
7
7
7
2
2
2
2
2
7
0
0
0
0
4
0
0
0
1
1
3
3
3
1
1
frame delle pagine
Figura 9.14 Algoritmo ottimale di sostituzione delle pagine.
rispetto all’algoritmo FIFo; nessun algoritmo di sostituzione può gestire questa suc-
cessione di riferimenti a tre blocchi di memoria con meno di nove page fault.
Sfortunatamente l’algoritmo ottimale di sostituzione delle pagine è difficile da
realizzare, perché richiede la conoscenza futura della successione dei riferimenti (una
situazione analoga si è riscontrata con l’algoritmo SjF di scheduling della CPU, nel
Paragrafo 6.3.2). Quindi, l’algoritmo ottimale si impiega soprattutto per studi com-
parativi. Per esempio, può risultare abbastanza utile sapere che, sebbene un algoritmo
nuovo non sia ottimale, nel peggiore dei casi le sue prestazioni sono inferiori del 12,3
per cento rispetto a quelle dell’algoritmo ottimale, e mediamente questa percentuale
è del 4,7 per cento.
9.4.4 Sostituzione delle pagine usate meno recentemente
(Lru)
Se l’algoritmo ottimale non è realizzabile, è forse possibile realizzarne un’approssi-
mazione. La distinzione fondamentale tra gli algoritmi FIFo e oPT, oltre quella di
guardare avanti o indietro nel tempo, consiste nel fatto che l’algoritmo FIFo impiega
l’istante in cui una pagina è stata caricata in memoria, mentre l’algoritmo oPT im-
piega l’istante in cui una pagina sarà usata. Usando come approssimazione di un fu-
turo vicino un passato recente, si sostituisce la pagina che non è stata usata per il pe-
riodo più lungo. Il metodo appena descritto è noto come algoritmo lru (least
recently used).
La sostituzione LrU associa a ogni pagina l’istante in cui è stata usata per l’ultima
volta. Quando occorre sostituire una pagina, l’algoritmo LrU sceglie quella che non
è stata usata per il periodo più lungo. Possiamo interpretare questa strategia come
l’algoritmo ottimale di sostituzione delle pagine con ricerca all’indietro nel tempo,
anziché in avanti. Un risultato interessante per l’analogia dei due algoritmi è il se-
guente. Supponendo che SR sia la successione inversa di una successione di riferi-
menti S, il tasso di page fault per l’algoritmo oPT su S è uguale a quello su SR. Allo
stesso modo, il tasso di page fault per l’algoritmo LrU su S è uguale a quella su SR
.
9.4 Sostituzione delle pagine 455
successione dei riferimenti
7 0 1 2 0 3 0 4 2 3 0 3 2 1 2 0 1 7 0 1
7
7
7
2
2
4
4
4
0
0
0
0
0
0
0
3
3
1
1
3
3
2
2
2
frame delle pagine
Figura 9.15 Algoritmo di sostituzione delle pagine lru.
1
3
2
1
0
2
1
0
7
Il risultato dell’applicazione dell’algoritmo LrU alla successione dei riferimenti del-
l’esempio è illustrato nella Figura 9.15. L’algoritmo LrU produce 12 page fault. oc-
corre notare che i primi cinque page fault sono gli stessi della sostituzione ottimale.
Quando si presenta il riferimento alla pagina 4, però, l’algoritmo LrU trova che, fra
i tre blocchi di memoria, quello usato meno recentemente è della pagina 2. Quindi,
l’algoritmo LrU sostituisce la pagina 2 senza sapere che sta per essere usata. Quando
si verifica il fault della pagina 2, l’algoritmo LrU sostituisce la pagina 3, poiché, fra
le tre pagine in memoria (0, 3, 4), la pagina 3 è quella usata meno recentemente. No-
nostante questi problemi, la sostituzione LrU, con 12 page fault, è molto migliore
della sostituzione FIFo, con 15 page fault.
Il criterio LrU si usa spesso come algoritmo di sostituzione delle pagine ed è con-
siderato valido. Il problema principale riguarda la sua implementazione. Un algoritmo
di sostituzione delle pagine LrU può richiedere una notevole assistenza da parte del-
l’hardware. Il problema consiste nel determinare un ordine per i frame definito dal
momento dell’ultimo uso. Si possono realizzare le due seguenti soluzioni.
Contatori. Nel caso più semplice, a ogni elemento della tabella delle pagine si•
associa un campo momento di utilizzo, e alla CPU si aggiunge un contatore che si
incrementa a ogni riferimento alla memoria. ogni volta che si fa un riferimento a
una pagina, si copia il contenuto del registro contatore nel campo momento di uti-
lizzo nella voce della page table relativa a quella pagina. In questo modo è sempre
possibile conoscere il momento in cui è stato fatto l’ultimo riferimento a ogni pa-
gina. Si sostituisce la pagina con il valore associato più piccolo. Questo schema
implica una ricerca all’interno della tabella delle pagine per individuare la pagina
usata meno recentemente (LrU), e una scrittura in memoria (nel campo momento
di utilizzo della tabella delle pagine) per ogni accesso alla memoria. I riferimenti
temporali si devono mantenere anche quando, a seguito dello scheduling della
CPU, si modificano le tabelle delle pagine. occorre infine considerare l’overflow
del contatore.
•
Stack. Un altro metodo per la realizzazione della sostituzione delle pagine LrU
prevede l’utilizzo di uno stack dei numeri delle pagine. ogni volta che si fa un ri-
ferimento a una pagina, la si estrae dallo stack e la si colloca in cima a quest’ulti-
456 Capitolo 9– Memoria virtuale
successione dei riferimenti
4 7 0 7 1 0 1 2 1 2 7 1 2
2
1
0
7
4
stack
prima di a
7
a
b
2
1
0
4
stack
dopo b
Figura 9.16 uso di uno stack per registrare i più recenti riferimenti alle pagine.
mo. In questo modo, in cima allo stack si trova sempre la pagina usata per ultima,
mentre in fondo si trova la pagina usata meno recentemente, com’è illustrato dalla
Figura 9.16. Poiché gli elementi si devono estrarre dal centro dello stack, la mi-
gliore realizzazione si ottiene usando una lista doppiamente concatenata, con un
puntatore all’elemento iniziale e uno a quello finale. Per estrarre una pagina dallo
stack e collocarla in cima, nel caso peggiore è necessario modificare sei puntatori.
ogni aggiornamento è un po’ più costoso, ma per una sostituzione non si deve
compiere alcuna ricerca: il puntatore dell’elemento di coda punta alla pagina LrU.
Questo metodo è adatto soprattutto alle realizzazioni programmate (o micropro-
grammate) della sostituzione LrU.
Né la sostituzione ottimale né quella LrU sono soggette all’anomalia di Belady. En-
trambe appartengono a una classe di algoritmi di sostituzione delle pagine, chiamati
algoritmi a stack, che non presenta l’anomalia di Belady. Un algoritmo a stack è un
algoritmo per il quale è possibile mostrare che l’insieme delle pagine in memoria per
n frame è sempre un sottoinsieme dell’insieme delle pagine che dovrebbero essere in
memoria per n + 1 frame. Per la sostituzione LrU, l’insieme di pagine in memoria è
costituito delle n pagine cui si è fatto riferimento più recentemente. Se il numero dei
frame è aumentato, queste n pagine continuano a essere quelle cui si è fatto riferi-
mento più recentemente e quindi restano in memoria.
Si noti che senza un supporto hardware (aggiuntivo rispetto ai registri TLB stan-
dard) sarebbero inconcepibili entrambe le implementazioni della sostituzione LrU.
L’aggiornamento dei campi del contatore o dello stack si deve effettuare per ogni ri-
ferimento alla memoria. Se per ogni riferimento si dovesse adoperare un’interruzione
per permettere al sistema operativo di modificare tali strutture dati, tutti i riferimenti
alla memoria sarebbero rallentati di un fattore almeno pari a 10, quindi anche tutti i
processi utenti sarebbero rallentati di un uguale fattore. Pochi sistemi potrebbero per-
mettere un tale sovraccarico per la gestione della memoria.
9.4 Sostituzione delle pagine 457
9.4.5 Sostituzione delle pagine per approssimazione a Lru
Sono pochi i sistemi di calcolo che dispongono del supporto hardware per una vera
sostituzione LrU delle pagine. Nei sistemi che non offrono alcun supporto hardware
si devono impiegare altri algoritmi di sostituzione delle pagine, per esempio l’algo-
ritmo FIFo. molti sistemi tuttavia possono fornire un aiuto: un bit di riferimento. Il
bit di riferimento a una pagina è impostato automaticamente dall’hardware del siste-
ma ogni volta che si fa un riferimento a quella pagina, che sia una lettura o una scrit-
tura su qualsiasi byte della pagina. I bit di riferimento sono associati a ciascun ele-
mento della tabella delle pagine.
Inizialmente, il sistema operativo azzera tutti i bit. Quando s’inizia l’esecuzione
di un processo utente, l’hardware imposta a 1 il bit associato a ciascuna pagina cui si
fa riferimento. Dopo qualche tempo è possibile stabilire quali pagine sono state usate
semplicemente esaminando i bit di riferimento. Non è però possibile conoscere l’or-
dine d’uso. Questa informazione è alla base di molti algoritmi per la sostituzione delle
pagine che approssimano LrU.
9.4.5.1 Algoritmo con bit supplementari di riferimento
Ulteriori informazioni sull’ordinamento si possono ottenere registrando i bit di rife-
rimento a intervalli regolari. È possibile conservare in una tabella in memoria con,
ad esempio, un byte per ogni pagina. A intervalli regolari, per esempio di 100 milli-
secondi, un segnale d’interruzione del timer trasferisce il controllo al sistema opera-
tivo. Questo inserisce il bit di riferimento per ciascuna pagina nel bit più significativo
del byte, shiftando gli altri bit a destra di 1 bit e scartando il bit meno significativo.
Questi registri a scorrimento di 8 bit contengono la storia dell’utilizzo delle pagine
relativo agli ultimi otto periodi di tempo. Se il registro a scorrimento contiene la suc-
cessione di bit 00000000, significa che la pagina associata non è stata usata da otto
periodi di tempo; a una pagina usata almeno una volta per ogni periodo corrisponde
la successione 11111111 nel registro a scorrimento. Una pagina cui corrisponde la
successione 11000100, è stata usata più recentemente di una pagina a cui corrisponde
01110111. Interpretando queste successioni di bit come interi senza segno, la pagina
cui è associato il numero minore è la pagina LrU, e può essere sostituita. Si noti che
l’unicità dei numeri non è garantita. Si possono sostituire tutte le pagine con il valore
minore, oppure si può ricorrere a una selezione FIFo.
Il numero dei bit può ovviamente essere variato: si sceglie secondo l’hardware di-
sponibile per accelerarne al massimo la modifica. Nel caso limite tale numero si ri-
duce a zero, lasciando soltanto il bit di riferimento. In questo caso l’algoritmo è noto
come algoritmo di sostituzione delle pagine con seconda chance.
9.4.5.2 Algoritmo con seconda chance
L’algoritmo di base per la sostituzione con seconda chance è un algoritmo di sostitu-
zione di tipo FIFo. Tuttavia, dopo aver selezionato una pagina, si controlla il bit di ri-
ferimento: se il suo valore è 0, si sostituisce la pagina; se il bit di riferimento è impo-
stato a 1, si dà una seconda chance alla pagina e si passa alla successiva pagina FIFo.
Quando una pagina riceve la seconda chance, si azzera il suo bit di riferimento e si
458 Capitolo 9– Memoria virtuale
bit di
riferimento
0
pagine pagine
bit di
riferimento
0
0
0
prossima
vittima
1
0
1
0
0
0
1
1
1
1
coda circolare delle pagine
(a)
coda circolare delle pagine
(b)
Figura 9.17 Algoritmo di sostituzione delle pagine con seconda chance (orologio).
aggiorna il suo istante d’arrivo al momento attuale. In questo modo, una pagina cui
si offre una seconda chance non viene mai sostituita fiché tutte le altre pagine non
siano state sostituite, oppure non sia stata data loro una seconda chance. Inoltre, se
una pagina è usata abbastanza spesso, da mantenere il suo bit di riferimento impostato
a 1, non viene mai sostituita.
Un metodo per implementare l’algoritmo con seconda chance, detto anche a oro-
logio (clock), è basato sull’uso di una coda circolare, in cui un puntatore (lancetta)
indica qual è la prima pagina da sostituire. Quando serve un frame, si fa avanzare il
puntatore finché non si trovi in corrispondenza di una pagina con il bit di riferimento
0; a ogni passo si azzera il bit di riferimento appena esaminato (Figura 9.17). Una
volta trovata una pagina “vittima”, la si sostituisce e si inserisce la nuova pagina nella
coda circolare nella posizione corrispondente. Si noti che nel caso peggiore, quando
tutti i bit sono impostati a 1, il puntatore percorre un ciclo su tutta la coda, dando a
ogni pagina una seconda chance. Prima di selezionare la pagina da sostituire, azzera
tutti i bit di riferimento. Se tutti i bit sono a 1, la sostituzione con seconda chance si
riduce a una sostituzione FIFo.
9.4 Sostituzione delle pagine 459
9.4.5.3 Algoritmo con seconda chance migliorato
L’algoritmo con seconda chance descritto precedentemente si può migliorare consi-
derando i bit di riferimento e di modifica (descritto nel Paragrafo 9.4.1) come una
coppia ordinata, con cui si possono ottenere le seguenti quattro classi:
1.
(0, 0) né recentemente usato né modificato – migliore pagina da sostituire;
2.
(0, 1) non usato recentemente, ma modificato – la pagina non così buona poiché
prima di essere sostituita deve essere scritta in memoria secondaria;
3.
(1, 0) usato recentemente ma non modificato – probabilmente la pagina sarà presto
usata nuovamente;
4.
(1, 1) usato recentemente e modificato – probabilmente la pagina sarà presto an-
cora usata e dovrà essere scritta in memoria secondaria prima di essere sostituita.
ogni pagina rientra in una di queste quattro classi. Alla richiesta di una sostituzione
di pagina, si usa lo stesso schema impiegato nell’algoritmo a orologio, ma anziché
controllare se la pagina puntata ha il bit di riferimento impostato a 1, si esamina la
classe a cui la pagina appartiene e si sostituisce la prima pagina che si trova nella clas-
se minima non vuota. Si noti che si può dover scandire la coda circolare più volte pri-
ma di trovare una pagina da sostituire.
La differenza principale tra questo algoritmo e il più semplice algoritmo a orologio
è che qui si dà la preferenza alle pagine modificate, al fine di ridurre il numero di I/o
richiesti.
9.4.6 Sostituzione delle pagine basata su conteggio
Esistono molti altri algoritmi che si possono usare per la sostituzione delle pagine.
Per esempio, si potrebbe usare un contatore del numero dei riferimenti fatti a ciascuna
pagina, e sviluppare i due seguenti schemi.
•
Algoritmo di sostituzione delle pagine meno frequentemente usate (least
frequently used, lfu); richiede che si sostituisca la pagina con il conteggio più
basso. La ragione di questa scelta è che una pagina usata attivamente deve avere
un conteggio di riferimento alto. Si ha però un problema quando una pagina è usa-
ta molto intensamente durante la fase iniziale di un processo, ma poi non viene
più usata. Poiché è stata usata intensamente il suo conteggio è alto, quindi rimane
in memoria anche se non è più necessaria. Una soluzione può essere quella di spo-
stare i valori dei contatori a destra di un bit a intervalli regolari, misurando l’uti-
lizzo con un peso esponenziale decrescente.
•
Algoritmo di sostituzione delle pagine più frequentemente usate (most
frequently used, mfu); è basato sul fatto che, probabilmente, la pagina con il con-
tatore più basso è stata appena inserita e non è stata ancora usata.
Le sostituzioni mFU e LFU non sono molto comuni, poiché la realizzazione di questi
algoritmi è abbastanza onerosa; inoltre, tali algoritmi non approssimano bene la so-
stituzione oPT.
460 Capitolo 9– Memoria virtuale
9.4.7 Algoritmi con buffering delle pagine
oltre a uno specifico algoritmo per la sostituzione delle pagine, si usano spesso anche
altre procedure; per esempio, i sistemi hanno generalmente un gruppo di frame liberi
(pool of free frames). Quando si verifica un page fault, si sceglie innanzi tutto un fra-
me vittima, ma prima che la vittima sia scritta in memoria secondaria, si trasferisce
la pagina richiesta in un frame libero del gruppo. Questa procedura permette al pro-
cesso di ricominciare al più presto, senza attendere che la pagina vittima sia scritta
in memoria secondaria. Quando nel seguito si scrive la vittima in memoria seconda-
ria, si aggiunge il suo frame al gruppo dei frame liberi.
Quest’idea si può estendere conservando una lista delle pagine modificate: ogni-
qualvolta il dispositivo di paginazione è inattivo, si sceglie una pagina modificata, la
si scrive nel disco e si resetta il suo bit di modifica. Questo schema aumenta la pro-
babilità che, al momento della selezione per la sostituzione, la pagina non abbia su-
bito modifiche e non debba essere scritta in memoria secondaria.
Un’altra modifica consiste nell’usare un gruppo di frame liberi, ma ricordare quale
pagina era contenuta in ciascun frame. Poiché quando il contenuto di un frame viene
scritto su disco tale contenuto non cambia, la vecchia pagina è ancora utilizzabile
prendendola dal gruppo dei frame liberi, se ce n’è bisogno prima che sia riusato quel
frame. In questo caso non è necessario alcun I/o. Se si verifica un page fault si con-
trolla prima se la pagina richiesta si trova nel gruppo dei frame liberi; se non c’è si
deve individuare un frame libero e trasferirvi la pagina.
Questa tecnica, insieme con l’algoritmo di sostituzione FIFo, è usata dal sistema
v Ax/vmS. Quando l’algoritmo FIFo sostituisce per errore una pagina ancora in uso,
la si ricupera rapidamente dal gruppo dei frame liberi senza ricorrere a operazioni di
I/o. Il buffer dei frame liberi offre protezione contro l’algoritmo di sostituzione FIFo,
relativamente elementare, ma di semplice implementazione. Questo metodo è neces-
sario poiché le prime versioni del v Ax non implementavano correttamente il bit di ri-
ferimento.
Alcune versioni di UNIx adottano questo metodo insieme all’algoritmo con se-
conda chance. In effetti, si tratta di un’utile integrazione a qualunque algoritmo di so-
stituzione, al fine di ridurre il prezzo pagato per l’eventuale errata scelta della pagina
vittima.
9.4.8 Applicazioni e sostituzione della pagina
In taluni casi, le applicazioni che accedono ai dati tramite la memoria virtuale del si-
stema operativo hanno prestazioni peggiori di quelle che avrebbero se il sistema ope-
rativo non offrisse alcun buffering. Si pensi, quale esempio tipico, a un database che
gestisce la memoria e il buffering dell’I/o in modo autonomo. Applicazioni come
questa capiscono il proprio utilizzo della memoria e del disco meglio di quanto possa
fare un sistema operativo, che applica algoritmi adatti a un uso generale. Se il sistema
operativo adotta un buffer per l’I/o, e così pure fa l’applicazione, la quantità di me-
moria necessaria per l’I/o sarà inutilmente raddoppiata.
9.5 Allocazione dei frame 461
Un altro esempio proviene dai data warehouse, che effettuano spesso lunghe letture
sequenziali del disco, seguite da calcoli e scritture. L’algoritmo LrU eliminerebbe le
pagine vecchie per conservare le nuove, mentre in questo caso è ragionevole atten-
dersi la lettura delle pagine vecchie in luogo di quelle nuove (quando l’applicazione
inizia nuovamente la lettura sequenziale). In queste circostanze l’algoritmo mFU sa-
rebbe più efficiente di LrU.
Per risolvere tali problemi, alcuni sistemi operativi permettono a certi programmi
di utilizzare una partizione del disco come un array sequenziale di blocchi logici, sen-
za ricorrere alle strutture di dati del file system. Un simile array è anche detto disco
di basso livello (raw disk), e il relativo I/o è denominato I/o di basso livello (raw i/o).
L’ I/o di basso livello bypassa tutti i servizi del file system, come la paginazione su
richiesta dell’ I/o su file, il locking dei file, il prefetching, l’allocazione dello spazio,
la gestione dei i nomi dei file e le directory. Si noti però che, sebbene alcune appli-
cazioni siano più efficienti quando gestiscono i propri servizi specifici di memoriz-
zazione sul disco di basso livello, quasi tutte hanno una resa migliore quando operano
con i servizi regolari del file system.
9.5 Allocazione dei frame
Consideriamo ora il problema dell’allocazione. occorre stabilire un criterio per l’al-
locazione della memoria libera ai diversi processi. Come esempio, se abbiamo 93 fra-
me liberi e due processi, quanti frame assegnamo a ciascuno?
Il caso più semplice è un sistema con utente singolo. Si consideri un sistema mo-
noutente che disponga di 128 kB di memoria, con pagine di 1 kB. Complessivamente
sono presenti 128 frame. Il sistema operativo può occupare 35 kB, lasciando 93 frame
per il processo utente. In condizioni di paginazione su richiesta pura, tutti i 93 blocchi
di memoria sono inizialmente posti nella lista dei frame liberi. Quando comincia l’e-
secuzione, il processo utente genera una sequenza di page fault. I primi 93 fault rice-
vono i frame liberi dalla lista. Una volta esaurita quest’ultima, per stabilire quale tra
le 93 pagine presenti in memoria si debba sostituire con la novantaquattresima, si può
usare un algoritmo di sostituzione delle pagine. Terminato il processo, si reinserisco-
no i 93 frame nella lista dei frame liberi.
vi sono molte variazioni di questa semplice strategia. Si può richiedere che il si-
stema operativo assegni tutto lo spazio richiesto dalle proprie strutture dati attingendo
dalla lista dei frame liberi. Quando questo spazio è inutilizzato dal sistema operativo
può essere sfruttato per la paginazione utente. Un’altra variante prevede di riservare
sempre tre frame liberi, in modo che quando si verifica un page fault sia sempre di-
sponibile un frame libero in cui trasferire la pagina richiesta. mentre ha luogo il tra-
sferimento, si può scegliere una pagina da rimpiazzare, che viene poi scritta nel disco
mentre il processo utente continua l’esecuzione. Sono possibili anche altre varianti,
ma la strategia di base è chiara: al processo utente si assegna qualsiasi frame libero.
462 Capitolo 9– Memoria virtuale
9.5.1 Numero minimo di frame
Le strategie di allocazione dei frame sono soggette a parecchi vincoli. Non si possono
assegnare più frame di quanti siano disponibili, sempre che non vi sia condivisione
di pagine. Inoltre è necessario assegnare almeno un numero minimo di frame. Esa-
miniamo quest’ultimo requisito in maggiore dettaglio.
Una delle ragioni per allocare sempre un numero minimo di frame è legata alle
prestazioni. ovviamente, al decrescere del numero dei frame allocati a ciascun pro-
cesso aumenta il tasso di page fault, con conseguente rallentamento dell’esecuzione
dei processi. Inoltre va ricordato che, quando si verifica un page fault prima che sia
stata completata l’esecuzione di un’istruzione, quest’ultima deve essere riavviata. Di
conseguenza, i frame disponibili devono essere in numero sufficiente per contenere
tutte le pagine cui ogni singola istruzione può far riferimento.
Si consideri, per esempio, un calcolatore in cui tutte le istruzioni di riferimento
alla memoria hanno solo un indirizzo di memoria; in questo caso occorre almeno un
frame per l’istruzione e uno per il riferimento alla memoria. Inoltre se è ammesso un
indirizzamento indiretto a un livello (come nel caso di un’istruzione load presente
nella pagina 16 che può far riferimento a un indirizzo della pagina 0, che costituisce
a sua volta un riferimento indiretto alla pagina 23) la paginazione richiede allora al-
meno tre frame per ogni processo. Si immagini che cosa accadrebbe nel caso di un
processo che disponga di due soli frame.
Il numero minimo di frame è definito dall’architettura del calcolatore. Per esem-
pio, L’istruzione di movedel PDP-11, per alcune modalità di indirizzamento, è costi-
tuita di più di una parola, quindi la stessa istruzione può stare a cavallo tra due pagine.
Inoltre, ciascuno dei suoi due operandi può essere un riferimento indiretto, per un to-
tale di sei frame. Un altro esempio è dato dall’istruzione MVCdi IBm 370. Poiché l’i-
struzione è da memoria a memoria, può occupare 6 byte e stare a cavallo tra due pa-
gine. Anche la sequenza di caratteri da spostare e l’area su cui effettuare lo
spostamento possono essere a cavallo tra due pagine; questa situazione richiede quin-
di sei frame. In effetti, la situazione peggiore si presenta quando l’istruzione MVC è
l’operando di un’istruzione EXECUTEche sta a cavallo di un limite di pagina; in que-
sto caso occorrono otto frame.
Il caso peggiore si può presentare nelle architetture di calcolatori che permettono
riferimenti indiretti a più livelli (per esempio quando ogni parola di 16 bit può con-
tenere un indirizzo di 15 bit più un indicatore indiretto di 1 bit). In teoria, una sem-
plice istruzione di caricamento può far riferimento a un indirizzo indiretto che a sua
volta può far riferimento a un indirizzo indiretto (su un’altra pagina) anch’esso fa-
cente riferimento a un indirizzo indiretto su un’altra pagina ancora, e così via, finché
tutte le pagine della memoria virtuale siano state chiamate in causa. Quindi, nel caso
peggiore, tutta la memoria virtuale si deve trovare in memoria fisica. Per superare
questa difficoltà occorre porre un limite al livello dei riferimenti indiretti, per esempio
limitando un’istruzione a un massimo di 16 livelli. Quando si verifica il riferimento
indiretto di primo livello, si imposta un contatore al valore 16, per decrementarlo a
ciascun riferimento successivo in questa istruzione. Se il contatore si riduce a 0 si ve-
9.5 Allocazione dei frame 463
rifica un’eccezione (numero di riferimenti indiretti eccessivo). Tale limite riduce a 17
il numero massimo dei riferimenti alla memoria per ogni istruzione, richiedendo un
pari numero di frame.
Il numero minimo di frame per ciascun processo è definito dall’architettura, men-
tre il numero massimo è definito dalla quantità di memoria fisica disponibile. In mez-
zo vi è un ampio spazio di scelta.
9.5.2 Algoritmi di allocazione
Il modo più semplice per suddividere m frame tra n processi è quello per cui a cia-
scuno si dà una parte uguale, m/n frame (ignorando per ora i frame di cui il sistema
operativo ha bisogno). Dati 93 frame e cinque processi, ogni processo riceve 18 fra-
me. I tre frame lasciati liberi si potrebbero usare come buffer di frame liberi. Questo
schema è chiamato allocazione uniforme.
Un’alternativa consiste nel riconoscere che diversi processi hanno bisogno di
quantità di memoria diverse. Si consideri un sistema con frame di 1 kB. Se un piccolo
processo utente di 10 kB e una base di dati interattiva di 127 kB sono gli unici due
processi in esecuzione su un sistema con 62 frame liberi, non ha senso allocare a cia-
scun processo 31 frame. Al processo utente non ne servono più di 10, quindi gli altri
21 sarebbero semplicemente sprecati.
Per risolvere questo problema è possibile ricorrere all’allocazione proporzionale,
secondo cui la memoria disponibile si assegna a ciascun processo secondo la propria
dimensione. Si supponga che si sia la dimensione della memoria virtuale per il pro-
cesso pi. Si definisce la seguente quantità:
S = S si.
Quindi, se il numero totale dei frame disponibili è m, al processo pi si assegnano ai
frame, dove ai è approssimativamente
ai = si/S × m.
Naturalmente è necessario scegliere ciascun ai in modo che sia un intero maggiore
del numero minimo di frame richiesti dall’instruction set e in modo che la somma di
tutti gli ai non sia maggiore di m.
Usando l’allocazione proporzionale, per suddividere 62 frame tra due processi,
uno di 10 e uno di 127 pagine, si assegnano rispettivamente 4 e 57 frame, infatti:
10/137 × 62 ≈ 4
127/137 × 62 ≈ 57.
In questo modo entrambi i processi condividono i frame disponibili secondo le ri-
spettive necessità, e non in modo uniforme.
Sia nell’allocazione uniforme sia in quella proporzionale, l’allocazione a ogni pro-
cesso può variare rispetto al livello di multiprogrammazione. Se tale livello aumenta,
ciascun processo perde alcuni frame per fornire la memoria necessaria per il nuovo
processo. D’altra parte, se il livello di multiprogrammazione diminuisce, i frame al-
locati al processo rimosso si possono distribuire tra quelli che restano.
464 Capitolo 9– Memoria virtuale
occorre notare che sia con l’allocazione uniforme sia con l’allocazione proporziona-
le, un processo a priorità elevata è trattato come un processo a bassa priorità anche
se, per definizione, si vorrebbe che al processo con elevata priorità fosse allocata più
memoria per accelerarne l’esecuzione, a discapito dei processi a bassa priorità. Un
soluzione prevede l’uso di uno schema di allocazione proporzionale in cui il rapporto
dei frame non dipende dalle dimensioni relative dei processi, ma dalle priorità degli
stessi oppure da una combinazione di dimensioni e priorità.
9.5.3 Allocazione globale e allocazione locale
Un altro importante fattore che riguarda il modo in cui si assegnano i frame ai vari
processi è la sostituzione delle pagine. Nei casi in cui vi siano più processi in com-
petizione per i frame, gli algoritmi di sostituzione delle pagine si possono classificare
in due categorie generali: sostituzione globale e sostituzione locale. La sostituzione
globale permette che per un processo si scelga un frame per la sostituzione dall’in-
sieme di tutti i frame, anche se quel frame è al momento allocato a un altro processo;
un processo può dunque sottrarre un frame a un altro processo. La sostituzione locale
richiede invece che per ogni processo si scelga un frame solo dal proprio insieme di
frame.
Si consideri per esempio uno schema di allocazione che, per una sostituzione a
favore dei processi ad alta priorità, permetta di sottrarre frame ai processi a bassa
priorità. Un processo può scegliere per la sostituzione uno dei suoi rame o uno di
quelli di qualsiasi processo con priorità minore. Questo metodo permette a un pro-
cesso ad alta priorità di aumentare il proprio livello di allocazione dei frame a disca-
pito dei processi a bassa priorità.
Con la strategia di sostituzione locale, il numero di blocchi di memoria assegnati
a un processo non cambia. Con la sostituzione globale, invece, può accadere che per
un certo processo si selezionino solo frame allocati ad altri processi, aumentando così
il numero di frame assegnati a quel processo, purché altri non scelgano per la sosti-
tuzione i suoi frame.
L’algoritmo di sostituzione globale risente di un problema: un processo non può
controllare il proprio tasso di page fault, infatti l’insieme di pagine che si trova in me-
moria per un processo non dipende solo dal comportamento di paginazione di quel
processo, ma anche dal comportamento di paginazione di altri processi. Quindi, lo
stesso processo può comportarsi in modi molto diversi, per esempio impiegando 0,5
secondi per un’esecuzione e 10,3 secondi per quella successiva, a causa di circostanze
del tutto esterne. Con l’algoritmo di sostituzione locale questo problema non si pre-
senta. Infatti l’insieme di pagine in memoria per un processo subisce l’effetto del
comportamento di paginazione di quel solo processo. Tuttavia la sostituzione locale
può penalizzare un processo, non rendendogli disponibili altre pagine di memoria
meno usate. Generalmente, la sostituzione globale genera una maggiore produttività
del sistema, e perciò è il metodo più usato.
9.5 Allocazione dei frame 465
9.5.4 Accesso non uniforme alla memoria
Fino a questo momento trattando il tema della memoria virtuale abbiamo assunto che
le diverse parti della memoria centrale siano uguali, o almeno che vi si potesse acce-
dere nello stesso modo. In molti sistemi informatici non è così. Spesso in sistemi con
processori multipli (Paragrafo 1.3.2) un certo processore può accedere ad alcune re-
gioni della memoria più rapidamente rispetto ad altre. Tali differenze nelle prestazioni
sono causate dalla modalità di interconnessione tra processori e memoria all’interno
del sistema. Frequentemente un tale sistema è costituito da diverse schede madri,
ognuna contenente più processori e una parte di memoria. Le schede sono connesse
in vari modi, a partire dai bus di sistema fino a connessioni di rete ad alta velocità co-
me InfiniBand. Come ci si aspetta, i processori di una particolare scheda possono ac-
cedere alla memoria della scheda stessa in meno tempo rispetto a quello necessario
per accedere ad altre schede del sistema. I sistemi nei quali i tempi di accesso alla
memoria variano in modo significativo sono generalmente detti sistemi con accesso
non uniforme alla memoria (non-uniform memory access, NUmA) e, senza eccezio-
ni, sono più lenti dei sistemi nei quali memoria e processori risiedono sulla stessa
scheda madre.
Le decisioni su quali frame di pagina memorizzare in quale posizione possono
condizionare in modo significativo le prestazioni nei sistemi NUmA. Se, in sistemi
del genere, consideriamo uniforme la memoria, i processori potrebbero dover aspet-
tare molto più a lungo per accedere alla memoria rispetto al caso in cui gli algoritmi
di allocazione della memoria siano modificati per tenere in conto il NUmA. Analoghe
modifiche devono essere apportate anche al sistema di scheduling. L’obiettivo di que-
sti cambiamenti è quello di allocare i frame di memoria “il più vicino possibile” al
processore sul quale il processo è in esecuzione, dove per “vicino” si intende “con
latenza minima”, ovvero, di solito, sulla stessa scheda della CPU.
I cambiamenti negli algoritmi consistono nel fatto che lo scheduler tiene traccia
dell’ultimo processore sul quale ciascun processo è stato eseguito. Se lo scheduler
cerca di allocare ciascun processo sul suo processore precedente, e se il sistema di
gestione della memoria cerca di allocare frame per il processo vicino al processore
sul quale sta per essere mandato in esecuzione, si otterrà un incremento dei cache hit
e una diminuzione del tempo di accesso alla memoria.
La questione diventa ancora più complicata con l’aggiunta dei thread. Per esem-
pio, un processo con molti thread in esecuzione potrebbe vedere quei thread schedu-
lati su differenti schede del sistema. Come viene allocata la memoria in questo caso?
Solaris risolve il problema creando una entità lgroup (latency group, ovvero gruppo
di latenza) nel kernel. ogni lgroup raccoglie i processori e la memoria vicini fra loro.
In effetti gli lgroup sono ordinati gerarchicamente sulla base del periodo di latenza
tra i gruppi. Solaris tenta di pianificare tutti i thread di un processo e di allocare tutta
la memoria di un processo nell’ambito di un solo lgroup. Se una tale soluzione non
è possibile, per il resto delle risorse necessarie vengono utilizzati gli lgroup più vicini,
in modo da minimizzare la latenza complessiva della memoria e massimizzare il tasso
di successo della cache del processore.
466 Capitolo 9– Memoria virtuale
9.6 Thrashing
Se il numero dei frame allocati a un processo con priorità bassa diviene inferiore al
numero minimo richiesto dall’architettura del calcolatore, occorre sospendere l’ese-
cuzione del processo, e quindi togliere le pagine restanti, liberando tutti i frame allo-
cati. Questa operazione introduce un livello intermedio di scheduling per la gestione
dell’entrata e dell’uscita dei processi dalla memoria centrale.
Infatti, si consideri un qualsiasi processo che non disponga di un numero di frame
“sufficiente”. Se non dispone del numero di frame sufficiente per ospeitare le pagine
attive, il processo incorre rapidamente in un page fault. A questo punto si deve sosti-
tuire qualche pagina; ma, poiché tutte le sue pagine sono attive, si deve sostituire una
pagina che sarà subito necessaria, e di conseguenza si verificano parecchi page fault
poiché si sostituiscono pagine che saranno immediatamente riportate in memoria.
Questa intensa paginazione è nota come thrashing. Un processo in thrashing spen-
de più tempo per la paginazione che per l’esecuzione dei processi.
9.6.1 Cause del thrashing
Il thrashing causa notevoli problemi di prestazioni. Si consideri il seguente scenario,
basato sul comportamento effettivo dei primi sistemi di paginazione.
Il sistema operativo controlla l’utilizzo della CPU. Se questo è basso, aumenta il
grado di multiprogrammazione introducendo un nuovo processo. Si usa un algoritmo
di sostituzione delle pagine globale, che sostituisce le pagine senza tener conto del
processo al quale appartengono. ora si ipotizzi che un processo entri in una nuova
fase d’esecuzione e richieda più frame; se ciò si verifica si ha una serie di page fault,
cui segue la sottrazione di frame ad altri processi. Questi processi hanno però bisogno
di quelle pagine e quindi subiscono anch’essi dei page fault, con conseguente sottra-
zione di frame ad altri processi. Per effettuare il caricamento e lo scaricamento delle
pagine per questi processi si deve usare il dispositivo di paginazione. mentre si met-
tono i processi in coda per il dispositivo di paginazione, la coda dei processi pronti
per l’esecuzione si svuota, quindi l’utilizzo della CPU diminuisce.
Lo scheduler della CPU rileva questa riduzione dell’utilizzo della CPU e aumenta
il grado di multiprogrammazione. Si tenta di avviare il nuovo processo sottraendo pa-
gine ai processi in esecuzione, causando ulteriori page fault e allungando la coda per
il dispositivo di paginazione. Come risultato l’utilizzo della CPU scende ulteriormente,
e lo scheduler della CPU tenta di aumentare ancora il grado di multiprogrammazione.
Si è in una situazione di thrashing che fa precipitare la produttività del sistema. Il tas-
so dei page fault aumenta enormemente, e di conseguenza aumenta il tempo effettivo
d’accesso alla memoria. I processi non svolgono alcun lavoro, poiché si sta spenden-
do tutto il tempo nell’attività di paginazione.
Questo fenomeno è illustrato nella Figura 9.18, in cui si riporta l’utilizzo della
CPU in funzione del grado di multiprogrammazione. Aumentando il grado di multi-
programmazione aumenta anche l’utilizzo della CPU, anche se più lentamente, fino a
raggiungere un massimo. Se a questo punto si aumenta ulteriormente il grado di mul-
9.6 Thrashing 467
thrashing
utilizzo
della
CPU
grado di multiprogrammazione
Figura 9.18 Thrashing.
tiprogrammazione, l’attività di paginazione degenera e fa crollare l’utilizzo della CPU.
In questa situazione, per aumentare l’utilizzo della CPU e bloccare il thrashing occorre
ridurre il grado di multiprogrammazione.
Gli effetti di questa situazione si possono limitare usando un algoritmo di sosti-
tuzione locale, o algoritmo di sostituzione per priorità. Con la sostituzione locale,
se un processo entra in thrashing, non può sottrarre frame a un altro processo e quindi
provocarne a sua volta la degenerazione.Tuttavia il problema non è completamente
risolto. I processi in thrashing rimangono nella coda d’attesa del dispositivo di pagi-
nazione per la maggior parte del tempo. Il tempo di servizio medio di un page fault
aumenta a causa dell’allungamento della coda media d’attesa del dispositivo di pa-
ginazione. Di conseguenza, il tempo effettivo d’accesso in memoria aumenta anche
per gli altri processi.
Per evitare il verificarsi di queste situazioni, occorre fornire a un processo tutti i
frame di cui necessita. Per cercare di sapere quanti frame “servano” a un processo si
impiegano diverse tecniche. L’approccio del working-set, trattato nel Paragrafo 9.6.2,
comincia osservando quanti siano i frame che un processo sta effettivamente usando.
Questo approccio definisce il modello di località d’esecuzione del processo.
Il modello di località stabilisce che un processo, durante la sua esecuzione, si spo-
sta di località in località. Una località è un insieme di pagine usate attivamente insie-
me, com’è illustrato nella Figura 9.19. Generalmente un programma è formato di pa-
recchie località diverse, che sono sovrapponibili.
Per esempio, quando s’invoca una procedura, essa definisce una nuova località.
In questa località si fanno riferimenti alla memoria per le istruzioni della procedura,
per le sue variabili locali e per un sottoinsieme delle variabili globali. Quando la pro-
cedura termina, il processo lascia questa località, poiché le variabili locali e le istru-
zioni della procedura non sono più usate attivamente. Potrà tornare più tardi in questa
località.
468 Capitolo 9– Memoria virtuale
9.6 Thrashing 469
34
riferimenti alle pagine
. . . 2 6 1 5 7 7 7 7 5 1 6 2 3 4 1 2 3 4 4 4 3 4 3 4 4 4 1 3 2 3 4 4 4 3 4 4 4 . . .
Δ Δ
32
t1
t2
30
WS(t1) = {1, 2, 5, 6, 7}
Figura 9.20 Modello del working set.
WS(t2) = {3, 4}
28
indirizzo di memoria
26
24
22
numero delle pagine 20
18
tempo
d’esecuzione
Figura 9.19 località dei riferimenti alla memoria.
Quindi, le località sono definite dalla struttura del programma e dalle relative strutture
dati. Il modello di località sostiene che tutti i programmi mostrino questa struttura di
base di riferimenti alla memoria. Si noti che il modello di località è il principio non
dichiarato sottostante all’analisi fin qui svolta sul caching. Se gli accessi ai vari tipi
di dati fossero casuali, anziché strutturati in località, il caching sarebbe inutile.
Si supponga di allocare a un processo un numero di frame sufficiente per sistemare
le sue località attuali. Finché tutte queste pagine non si trovano in memoria, si veri-
ficano le assenze delle pagine relative a tali località; quindi, finché le località non ven-
gano modificate, non hanno luogo altri page fault. Se si assegnano meno frame ri-
spetto alla dimensione della località attuale, la paginazione del processo degenera,
poiché non si possono tenere in memoria tutte le pagine che il processo sta usando
attivamente.
9.6.2 Modello del working set
Come già accennato, il modello del working set è basato sull’ipotesi di località. Que-
sto modello usa un parametro, Δ , per definire la finestra del working set. L’idea con-
siste nell’esaminare i più recenti Δ riferimenti alle pagine. L’insieme di pagine nei
più recenti Δ riferimenti è il working set (Figura 9.20). Se una pagina è in uso attivo
si trova nel working set; se non è più usata esce dal working set Δunità di tempo dopo
il suo ultimo riferimento. Quindi, il working set non è altro che un’approssimazione
della località del programma.
Per esempio, data la successione di riferimenti alla memoria mostrata nella Figura
9.20, se Δ = 10 riferimenti alla memoria, il working set all’istante t1 è {1, 2, 5, 6, 7}.
All’istante t2 il working set è diventato {3, 4}.
La precisione del working set dipende dalla scelta del valore di Δ . Se Δ è troppo
piccolo non include l’intera località, se è troppo grande può sovrapporre più località.
Al limite, se Δ è infinito il working set coincide con l’insieme di pagine cui il pro-
cesso fa riferimento durante la sua esecuzione.
La caratteristica più importante del working set è la sua dimensione. Calcolandone
la dimensione wSSi, per ciascun processo pi del sistema, si può determinare la richiesta
totale di frame, cioè D:
D = S wSSi.
ogni processo usa attivamente le pagine del proprio working set. Quindi, il processo
i necessita di wSSi frame. Se la richiesta totale è maggiore del numero totale di frame
liberi (D > m), si avrà thrashing, poiché alcuni processi non dispongono di un numero
sufficiente di frame.
Una volta scelto Δ , l’uso del modello del working set è abbastanza semplice. Il si-
stema operativo controlla il working set di ogni processo e gli assegna un numero di
frame sufficiente, rispetto alle dimensioni del suo working set. Se i frame ancora li-
470 Capitolo 9– Memoria virtuale
beri sono in numero sufficiente, si può iniziare un altro processo. Se la somma delle
dimensioni dei working set aumenta, superando il numero totale dei frame disponi-
bili, il sistema operativo individua un processo da sospendere. Scrive in memoria se-
condaria le pagine di quel processo e assegna i suoi frame ad altri processi. Il processo
sospeso può essere ripreso successivamente.
Questa strategia impedisce il thrashing, mantenendo il grado di multiprogramma-
zione più alto possibile, quindi ottimizza l’utilizzo della CPU.
Poiché la finestra del working set è una finestra dinamica, la difficoltà insita in
questo modello consiste nel tener traccia degli elementi che compongono il working
set stesso. A ogni riferimento alla memoria, a un’estremità appare un riferimento nuo-
vo e il riferimento più vecchio fuoriesce dall’altra estremità. Una pagina si trova nel
working set se esiste un riferimento a essa in qualsiasi punto della finestra del
working set.
Si può approssimare il modello con un interrupt da timer ad intervalli fissi ed un
bit di riferimento. Si supponga, per esempio, che Δsia pari a 10.000 riferimenti e che
sia possibile ottenere un segnale d’interruzione dal timer ogni 5000 riferimenti. Quan-
do si verifica uno di tali segnali d’interruzione, i valori dei bit di riferimento di cia-
scuna pagina vengono copiati in memoria e poi azzerati. Così, quando si verifica un
page fault è possibile esaminare il bit di riferimento corrente e 2 bit in memoria per
stabilire se una pagina sia stata usata entro gli ultimi 10.000-15.000 riferimenti. Se
lo è stata, almeno uno di questi bit è attivo. Se non lo è stata, questi bit sono tutti inat-
tivi. Le pagine con almeno un bit attivo si considerano appartenenti al working set.
occorre notare che questo schema non è del tutto preciso, poiché non è possibile sta-
bilire dove si è verificato un riferimento entro un intervallo di 5000. L’incertezza si
può ridurre aumentando il numero dei bit di cronologia e la frequenza dei segnali
d’interruzione, per esempio, 10 bit e un’interruzione ogni 1000 riferimenti. Tuttavia,
il costo per servire questi segnali d’interruzione più frequenti aumenta in modo cor-
rispondente.
9.6.3 Frequenza dei page fault
Il modello del working set ha avuto successo, e la sua conoscenza può servire per la
prepaginazione (Paragrafo 9.9.1), ma appare un modo alquanto goffo per controllare
il thrashing. La strategia basata sulla frequenza dei page fault (page fault frequency,
PFF) è più diretta.
Il problema specifico è la prevenzione del thrashing. La frequenza dei page fault
in tale situazione è alta, ed è proprio questa che si deve controllare. Se la frequenza
è eccessiva, significa che il processo necessita di più frame. Analogamente, se la fre-
quenza dei page fault è molto bassa, il processo potrebbe disporre di troppi frame. Si
può fissare un limite inferiore e un limite superiore per la frequenza desiderata dei
page fault (Figura 9.21). Se la frequenza effettiva dei page fault per un processo ol-
trepassa il limite superiore, occorre allocare a quel processo un altro frame; se la fre-
quenza scende sotto il limite inferiore, si sottrae un frame a quel processo. Quindi,
9.7 File mappati in memoria 471
frequenza di page fault
si aumenta il numero
dei frame
limite superiore
limite inferiore
si riduce il numero
dei frame
numero dei frame
Figura 9.21 Frequenza dei page fault.
per prevenire il thrashing, si può misurare e controllare direttamente la frequenza dei
page fault.
Come nel caso della strategia del working set, può essere necessaria lo swapping
di un processo. Se la frequenza dei page fault aumenta e non ci sono frame disponi-
bili, occorre selezionare un processo e spostarlo sul backing store. I frame liberati si
distribuiscono ai processi con elevate frequenze di page fault.

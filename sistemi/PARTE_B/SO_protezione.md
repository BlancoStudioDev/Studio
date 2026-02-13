
Domanda:
La protezione dei ﬁile in un sistema di elaborazione monoprocessore: si descrivano il concetto di
protezione dei ﬁile e sue principali realizzazioni, evidenziandone caratteristiche, vantaggi e limiti.

### Domanda
La protezione dei file in un sistema di elaborazione monoprocessore: si descrivano il concetto di protezione dei file e sue principali realizzazioni, evidenziandone caratteristiche, vantaggi e limiti.

### Risposta
#### Criteri e Meccanismi di Protezione
- **Criteri di protezione** -> decidono che cosa debba fare  
- **Meccanismi di protezione** -> come qualcosa debba essere eseguito  

#### Principi di protezione (semplificano le decisioni relative al progetto)
- **Principio del privilegio minimo** -> i processi, programmi e sistemi utenti devono ricevere solamente le risorse minime necessarie all'esecuzione, questo permette al sistema di dare i privilegi minimi ai processi per la loro esecuzione. Questo ha il vantaggio nella protezione, se un componente dovesse fallire si avrebbe un danno limitato. Un sistema del genere deve permettere di abilitare e disattivare i privilegi ai processi e programmi. All'interno di questo sistema operativo sono presenti anche gli audit trails, ovvero un sistema di tracciamento di tutte le attività di protezione e sicurezza del sistema. Svantaggio, bisogna creare un account per ciascun utente.

#### Domini di protezione
Un sistema elaboratico è un insieme di processi e oggetti, gli oggetti fisici sono componenti come CPU, segmenti di memoria, stampanti, dischi e unità a nastri, gli oggetti logici invece sono componenti come file, programmi e semafori. In ogni dato momento un processo deve poter accedere solamente alle risorse di cui ha bisogno, questo viene fatto con il principio di necessità di sapere. Esso è utile per limitare i danni che possono essere causati al sistema da un processo difettoso.

#### Struttura dei domini di protezione
Esso specifica le risorse accedibili dal processo durante la sua esecuzione. La possibilità di eseguire una operazione su un oggetto è detta diritto d'accesso. Un dominio è quindi un insieme di diritti d'accesso ciascuno dei quali è composto da una coppia ordinata:


Questa associazione tra un processo e un dominio può essere statica o dinamica, la statica permette di tenere il dominio del processo costante.

#### Matrice d'accesso
Per associare i domini ai processi vi è la possibilità di usare una matrice d'accesso che associa alle righe della matrice i domini e alle colonne gli oggetti. All'interno della matrice è possibile associare alla colonna anche un dominio e quindi andare a creare delle celle dominio-dominio che permettono di attuare lo switching, consentendo il cambiamento dinamico dei domini. Vi sono delle corrispondenze che possono indicare se un processo è l'owner di un dominio o di una risorsa e pertanto ha la possibilità di amministrare quella risorsa. La sua realizzazione può essere fatta in diversi modi:

- **Tabella globale** -> un insieme di triple:

- **Lista d'accesso per oggetti** -> ogni colonna è una lista d'accesso per oggetto  

- **Lista delle abilitazioni per domini** -> ogni riga è una lista di oggetti con le operazioni ammesse su quegli oggetti  

- **Meccanismo chiave-serratura** -> misto tra le liste d'accesso e le liste di abilitazione, ogni oggetto ha una lista di sequenze di bit uniche chiamate serrature, stessa cosa per i domini che possiedono chiavi, un processo in esecuzione in un dominio può accedere a un oggetto solo se quel dominio ha una chiave che corrisponde a una delle serrature.

#### Revoca dei diritti d'accesso
Quando parliamo di protezione dinamica vi è la possibilità che un processo non debba più avere certi diritti su un file, pertanto si utilizza un meccanismo di revoca dei diritti d'accesso. Essa può essere:
- Immediata o Ritardata  
- Selettiva o Generale  
- Parziale o Totale  
- Temporanea o Permanente  

La revoca dei permessi per sistemi basati su lista d'accesso è immediata, mentre su lista di abilitazione è più complessa in quanto si deve andare a cercare all'interno delle liste dei domini i processi, per questo ci sono diversi metodi:

- **Riacquisizione** -> le abilitazioni vengono cancellate periodicamente e il processo deve tentare di riottenerle; se il diritto è stato revocato, la riacquisizione fallisce.

- **Puntatori all'indietro** -> l'oggetto mantiene una lista di puntatori a tutte le abilitazioni associate; per la revoca si seguono i puntatori per modificarle o eliminarle.

- **Riferimento indiretto** -> l'abilitazione punta a un elemento di una tabella globale che rimanda all'oggetto; la revoca avviene cancellando l'elemento nella tabella, rendendo illegale il puntatore dell'abilitazione.

- **Chiavi** -> ogni abilitazione ha una chiave che deve coincidere con la master key dell'oggetto; cambiando la master key si invalidano istantaneamente tutte le abilitazioni precedenti.


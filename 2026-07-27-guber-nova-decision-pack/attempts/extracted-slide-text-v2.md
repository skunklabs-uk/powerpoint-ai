## Slide 1
NOVA
Alternative infrastrutturalie modelli operativi
Guber
31 luglio 2026

## Slide 2
NOVA | Contesto, esigenza e obiettivi
2
Contesto
Guber richiede un accesso SQL governato ai dati NOVA
L'esigenza riguarda verifiche ed estrazioni, mantenendo continuità operativa e tracciabilità degli accessi.
Esigenza
Separare l'autonomia sui dati dal rischio sul transazionale
La collocazione deve bilanciare controllo Guber, sicurezza, responsabilità operative e impatto della transizione.
Obiettivi
Confrontare sei alternative su criteri omogenei
Il confronto considera collocazione, accesso SQL, modello operativo, rischio, reversibilità ed economics.

## Slide 3
NOVA | Situazione attuale e requisito dati
3
Il requisito SQL si innesta su una piattaforma oggi concentrata nell'ambiente corrente
NOVA gestisce history e consolidamento; l'accesso Guber deve essere separato dal workload applicativo.
FLUSSO OPERATIVO
Sorgenti
ODT · AV · Loan Data Tape
NOVA
history · working row · consolidamento
Database primario
servizio applicativo
REQUISITO GUBER
•  Interrogazioni SQL per verifiche ed estrazioni | •  Profili read-only come configurazione ordinaria | •  Accessi, query e operazioni amministrative tracciati
IMPLICAZIONE ARCHITETTURALE
•  Il requisito può essere soddisfatto sul primario o su una replica | •  Una replica evita query dirette sul transazionale | •  Frequenza, lag e oggetti esposti diventano requisiti di servizio

## Slide 4
NOVA | Alternative di collocazione
4
Le sei alternative distinguono la collocazione del primario dalla replica presso Guber
Quattro opzioni intervengono sul database primario; due mantengono il primario e aggiungono una replica read-only.
COLLOCAZIONE DEL DATABASE PRIMARIO
01
Infrastruttura attuale
Continuità e cambiamento minimo
02
Primario su Azure Guber
Ownership Guber e governance Azure
03
Primario su AWS Guber
Ownership Guber e target AWS Francoforte
04
Primario on-premise Guber
Controllo infrastrutturale diretto
PRIMARIO ATTUALE + REPLICA READ-ONLY
05
Replica on-premise Guber
Accesso SQL presso Guber
06
Replica su Azure Guber
Accesso SQL presso Guber

## Slide 5
Scenario 01 | Infrastruttura attuale
5
La continuità riduce il rischio di transizione, ma limita il controllo infrastrutturale di Guber
Il database primario resta nell'ambiente corrente; l'accesso SQL viene segregato e tracciato.
ARCHITETTURA DI RIFERIMENTO
Guber
Accesso SQL governato
NOVA attuale
PERCHÉ CONSIDERARLO
•  Tempi più rapidi | •  Rischio migrazione contenuto | •  Alta reversibilità
PUNTI DI ATTENZIONE
•  Ownership Guber limitata | •  Accesso da segregare | •  Dipendenza dall'ambiente corrente
CONDIZIONI
Viste / schema read-only · Audit e capacità · SLA operativo
TCO PIATTAFORMA · 3 ANNI
€ 40k–124k
Una tantum € 15k–38k  |  piattaforma mensile € 0,7k–2,4k

## Slide 6
Scenario 02 | Primario su Azure Guber
6
Azure trasferisce il controllo a Guber e richiede una migrazione governata del primario
Il database primario migra nella subscription Azure di Guber, su servizio gestito o VM compatibile.
ARCHITETTURA DI RIFERIMENTO
Utenti / sistemi
Azure Guber
DB NOVA primario
PERCHÉ CONSIDERARLO
•  Account e chiavi Guber | •  Elasticità | •  PaaS se compatibile
PUNTI DI ATTENZIONE
•  Migrazione del primario | •  Dipendenza dalla rete | •  Run da assegnare
CONDIZIONI
Landing zone · Compatibilità DB · Networking privato
TCO PIATTAFORMA · 3 ANNI
€ 112k–319k
Una tantum € 49k–128k  |  piattaforma mensile € 1,75k–5,3k

## Slide 7
Scenario 03 | Primario su AWS Guber
7
AWS trasferisce il controllo a Guber e valorizza i servizi della regione Francoforte
Il database primario migra nell'account AWS di Guber, in regione Europe (Frankfurt).
ARCHITETTURA DI RIFERIMENTO
Utenti / sistemi
AWS eu-central-1
DB NOVA primario
PERCHÉ CONSIDERARLO
•  Account e chiavi Guber | •  Servizi gestiti | •  Coerenza con S3
PUNTI DI ATTENZIONE
•  Migrazione del primario | •  Compatibilità RDS | •  Responsabilità operative
CONDIZIONI
Standard AWS Guber · VPC e connettività · Motore / licensing
TCO PIATTAFORMA · 3 ANNI
€ 108k–315k
Una tantum € 49k–128k  |  piattaforma mensile € 1,65k–5,2k

## Slide 8
Scenario 04 | Primario on-premise Guber
8
L'on-premise massimizza il controllo diretto e concentra su Guber capacità e continuità operativa
Il database primario migra nell'infrastruttura Guber, con HA, backup e operations da dimensionare.
ARCHITETTURA DI RIFERIMENTO
Utenti / sistemi
Data center Guber
DB NOVA primario
PERCHÉ CONSIDERARLO
•  Ownership Guber | •  Integrazione con rete interna | •  Controllo diretto
PUNTI DI ATTENZIONE
•  Capacità e licensing | •  HA / DR | •  Carico operativo
CONDIZIONI
Infrastruttura disponibile · Competenze · Backup e secondo sito
TCO PIATTAFORMA · 3 ANNI
€ 121k–370k
Una tantum € 71k–208k  |  piattaforma mensile € 1,4k–4,5k

## Slide 9
Scenario 05 | Replica on-premise Guber
9
La replica on-premise abilita l'accesso locale senza spostare il database transazionale
Il primario resta nell'ambiente corrente e alimenta una replica read-only nell'infrastruttura Guber.
ARCHITETTURA DI RIFERIMENTO
Primario attuale
Replica asincrona
On-premise Guber
PERCHÉ CONSIDERARLO
•  Migrazione contenuta | •  Accesso locale | •  Alta reversibilità
PUNTI DI ATTENZIONE
•  Lag e riconciliazione | •  Ownership divisa | •  Compatibilità replica
CONDIZIONI
Motore / licenze · Frequenza e SLA · Viste e monitoring
TCO PIATTAFORMA · 3 ANNI
€ 57k–179k
Una tantum € 25k–64k  |  piattaforma mensile € 0,9k–3,2k

## Slide 10
Scenario 06 | Replica su Azure Guber
10
La replica Azure abilita accesso e governance cloud senza migrare il database transazionale
Il primario resta nell'ambiente corrente e alimenta una replica read-only nella subscription Azure Guber.
ARCHITETTURA DI RIFERIMENTO
Primario attuale
Replica asincrona
Azure Guber
PERCHÉ CONSIDERARLO
•  Autonomia sui dati | •  Identity e audit Azure | •  Scalabilità
PUNTI DI ATTENZIONE
•  Connettività cross-environment | •  Lag ed egress | •  Compatibilità replica
CONDIZIONI
Subscription e rete privata · Replica supportata · Retention
TCO PIATTAFORMA · 3 ANNI
€ 57k–179k
Una tantum € 25k–64k  |  piattaforma mensile € 0,9k–3,2k

## Slide 11
NOVA | Modello operativo
11
Account e chiavi possono restare Guber anche quando il run è affidato a Novigo
Il modello operativo è indipendente dalla collocazione e deve coprire l'intero servizio NOVA.
AM NOVIGO END-TO-END
GUBER / TERZA PARTE
Presidio
Coordinato da un unico fornitore
Distribuito tra owner e fornitori
Perimetro
Applicazione, DB, infrastruttura e orchestratore
Da ricomporre nel contratto operativo
Operations
Monitor, backup, patching, incident e release
Competenze e copertura da garantire
Governance
Account e approvazioni Guber
Account e approvazioni Guber
Handover
Exit plan contrattuale
Processo interno o di sourcing

## Slide 12
NOVA | Economics
12
I range TCO rendono confrontabili le alternative su un orizzonte di tre anni
TCO piattaforma: costi una tantum più 36 mesi di costi ricorrenti.
Infrastruttura attuale
UNA TANTUM
MENSILE
€ 15k–38k
€ 0,7k–2,4k
TCO 3 ANNI
€ 40k–124k
Primario su Azure Guber
UNA TANTUM
MENSILE
€ 49k–128k
€ 1,75k–5,3k
TCO 3 ANNI
€ 112k–319k
Primario su AWS Guber
UNA TANTUM
MENSILE
€ 49k–128k
€ 1,65k–5,2k
TCO 3 ANNI
€ 108k–315k
Primario on-premise Guber
UNA TANTUM
MENSILE
€ 71k–208k
€ 1,4k–4,5k
TCO 3 ANNI
€ 121k–370k
Replica on-premise Guber
UNA TANTUM
MENSILE
€ 25k–64k
€ 0,9k–3,2k
TCO 3 ANNI
€ 57k–179k
Replica su Azure Guber
UNA TANTUM
MENSILE
€ 25k–64k
€ 0,9k–3,2k
TCO 3 ANNI
€ 57k–179k
AM Novigo, team sostitutivo, licenze non note e disaster recovery geografico non inclusi.

## Slide 13
NOVA | Confronto delle alternative
13
Le alternative cambiano il punto di equilibrio tra velocità, controllo e complessità
Scenario
Rapidità
Rischiomigrazione
OwnershipGuber
AccessoSQL
Elasticità
Semplicitàoperativa
Reversibilità
Infrastruttura attuale
Alta
Alta
Bassa
Medio-alta
Media
Medio-alta
Alta
Primario su Azure Guber
Medio-bassa
Medio-bassa
Alta
Alta
Alta
Media
Media
Primario su AWS Guber
Medio-bassa
Medio-bassa
Alta
Alta
Alta
Media
Media
Primario on-premise Guber
Bassa
Bassa
Alta
Alta
Medio-bassa
Bassa
Medio-bassa
Replica on-premise Guber
Medio-alta
Medio-alta
Medio-alta
Alta
Medio-bassa
Media
Alta
Replica su Azure Guber
Medio-alta
Medio-alta
Medio-alta
Alta
Medio-alta
Media
Alta
Valutazione qualitativa basata sulle informazioni disponibili.

## Slide 14
NOVA | Sintesi
14
Le alternative rispondono a tre orientamenti infrastrutturali distinti
CONTINUITÀ
Scenario 1
Mantenere il primario nell'ambiente corrente
TRASFERIMENTO DEL PRIMARIO
Scenari 2–4
Azure, AWS o infrastruttura on-premise Guber
ACCESSO DATI CON REPLICA
Scenari 5–6
Replica read-only on-premise o Azure Guber
INFORMAZIONI CHE MODIFICANO IL CONFRONTO
Motore e versione DB
Sizing e crescita
SLA / RPO / RTO
Standard cloud Guber
Capacità on-premise
Connettività
Licensing

## Slide 15
APPENDICE
Assunzioni, economics eapprofondimenti tecnici

## Slide 16
Appendice | Evidenze e informazioni mancanti
16
Fatti, deduzioni e dati mancanti restano separati
FATTI CONFERMATI
•  Accesso SQL richiesto | •  Replica read-only accettata | •  Azure e on-premise in agenda | •  AWS confermato dall'utente | •  AM Novigo end-to-end
DEDUZIONI
•  Migrare il primario non è l'unico modo | •  La replica riduce il rischio sul transazionale | •  La rete diventa parte dell'architettura | •  Key ownership è una scelta di governance
DATI MANCANTI
•  Motore e licensing | •  Sizing, crescita e IOPS | •  SLA, RPO / RTO | •  Landing zone e connettività | •  Capacità on-premise e contratti

## Slide 17
Appendice | Assunzioni economiche
17
Il confronto usa un carico di riferimento comune
Produzione
4–8 vCPU · 16–32 GB RAM · 24x7 · alta disponibilità
Database
500 GB iniziali · crescita 20% annuo
Non produzione
1 ambiente al 50% della produzione
Backup
30 giorni · restore periodicamente testato
Documentale
1 TB iniziale
Accesso SQL
20 utenti autorizzati · massimo 5 concorrenti
TCO
Una tantum + 36 mesi di piattaforma
ESCLUSIONI
•  AM Novigo | •  Team sostitutivo | •  Licenze non note | •  DR geografico | •  Costi interni Guber | •  IVA e sconti

## Slide 18
Appendice | Scenario 01 — economics
18
Infrastruttura attuale — componenti del range
UNA TANTUM
•  Assessment e hardening | •  Viste / accesso SQL | •  Audit e test | •  Documentazione
RICORRENTE
•  Capacità incrementale | •  Backup e logging | •  Monitoring | •  Networking
VARIABILI PRINCIPALI
•  Motore e compatibilità | •  HA / DR e SLA | •  Volumi e IOPS | •  Licenze e contratti
UNA TANTUM
€ 15k–38k
MENSILE
€ 0,7k–2,4k
TCO 3 ANNI
€ 40k–124k

## Slide 19
Appendice | Scenario 02 — economics
19
Primario su Azure Guber — componenti del range
UNA TANTUM
•  Assessment PaaS / IaaS | •  Landing zone e rete | •  Migrazione e test | •  Cutover e rollback
RICORRENTE
•  Compute / database | •  Storage e backup | •  Logging e security | •  Networking
VARIABILI PRINCIPALI
•  Motore e compatibilità | •  HA / DR e SLA | •  Volumi e IOPS | •  Licenze e contratti
UNA TANTUM
€ 49k–128k
MENSILE
€ 1,75k–5,3k
TCO 3 ANNI
€ 112k–319k

## Slide 20
Appendice | Scenario 03 — economics
20
Primario su AWS Guber — componenti del range
UNA TANTUM
•  Assessment RDS / EC2 | •  Landing zone e VPC | •  Migrazione e test | •  Cutover e rollback
RICORRENTE
•  RDS / EC2 | •  Storage e backup | •  CloudWatch / security | •  Networking
VARIABILI PRINCIPALI
•  Motore e compatibilità | •  HA / DR e SLA | •  Volumi e IOPS | •  Licenze e contratti
UNA TANTUM
€ 49k–128k
MENSILE
€ 1,65k–5,2k
TCO 3 ANNI
€ 108k–315k

## Slide 21
Appendice | Scenario 04 — economics
21
Primario on-premise Guber — componenti del range
UNA TANTUM
•  Assessment e capacity | •  Provisioning e licensing | •  Migrazione e test | •  HA, backup e cutover
RICORRENTE
•  Capacità e manutenzione | •  Backup | •  Monitoring | •  Data center
VARIABILI PRINCIPALI
•  Motore e compatibilità | •  HA / DR e SLA | •  Volumi e IOPS | •  Licenze e contratti
UNA TANTUM
€ 71k–208k
MENSILE
€ 1,4k–4,5k
TCO 3 ANNI
€ 121k–370k

## Slide 22
Appendice | Scenario 05 — economics
22
Replica on-premise Guber — componenti del range
UNA TANTUM
•  Assessment replica | •  Provisioning on-premise | •  Setup e riconciliazione | •  Accessi e monitor
RICORRENTE
•  Compute replica | •  Storage e backup | •  Monitor del lag | •  Connettività
VARIABILI PRINCIPALI
•  Motore e compatibilità | •  HA / DR e SLA | •  Volumi e IOPS | •  Licenze e contratti
UNA TANTUM
€ 25k–64k
MENSILE
€ 0,9k–3,2k
TCO 3 ANNI
€ 57k–179k

## Slide 23
Appendice | Scenario 06 — economics
23
Replica su Azure Guber — componenti del range
UNA TANTUM
•  Assessment replica | •  Subscription e rete | •  Setup e riconciliazione | •  Accessi e monitor
RICORRENTE
•  Database replica | •  Storage e backup | •  Monitor e audit | •  Rete / egress
VARIABILI PRINCIPALI
•  Motore e compatibilità | •  HA / DR e SLA | •  Volumi e IOPS | •  Licenze e contratti
UNA TANTUM
€ 25k–64k
MENSILE
€ 0,9k–3,2k
TCO 3 ANNI
€ 57k–179k

## Slide 24
Appendice | Sicurezza e governance
24
Ownership e responsabilità devono restare esplicite
GUBER
•  Account e infrastruttura | •  Key ownership e policy | •  Approvazioni e audit
NOVIGO O ALTRO OPERATORE
•  Run operativo delegato | •  Backup, patching e monitor | •  Incident e release
CONTROLLO COMUNE
•  Accesso privato e MFA | •  Segregazione dei ruoli | •  Logging, revoca ed exit plan

## Slide 25
Appendice | Storage documentale
25
La tecnologia dipende dal requisito di storage e dalla collocazione
AWS S3
•  Lifecycle e versioning | •  KMS e policy | •  Egress da valutare
AZURE STORAGE
•  Identity e policy Azure | •  Tier e retention | •  Connettività privata
OBJECT STORAGE ON-PREMISE
•  Controllo locale | •  Capacity e operations | •  Durabilità da progettare

## Slide 26
Appendice | Orchestratore e rete
26
La separazione dei componenti modifica dipendenze e responsabilità
DB-ONLY
•  Database o replica spostati | •  Applicazione e orchestratore invariati | •  Dipendenza dalla WAN
PERCORSO PER FASI
•  Replica o DB come primo passo | •  Verifica prima di estendere lo scope | •  Transitorio da governare
FULL-STACK
•  Applicazione, DB e orchestratore | •  Target più coerente | •  Scope e cutover maggiori

## Slide 27
Appendice | Deployment database
27
La compatibilità del motore determina il livello di servizio gestito
SERVIZIO GESTITO · PAAS / RDS
•  Patching e backup maggiormente gestiti | •  Alta disponibilità standardizzata | •  Minore carico operativo | •  Compatibilità e feature da verificare
VM / EC2 · SELF-MANAGED
•  Maggiore controllo e compatibilità | •  Responsabilità DBA e sistema operativo | •  Backup, HA e patching da costruire | •  Licensing e TCO operativo da verificare

## Slide 28
Appendice | Modello operativo
28
Il run deve coprire applicazione, database e ambiente
Ambito
AM Novigo end-to-end
Guber / terza parte
Applicazione e release
Novigo esegue
Owner designato esegue
Database e performance
Novigo esegue
DBA Guber / terzo
Infrastruttura / cloud
Novigo opera con delega
Guber / terzo
Backup e restore
Novigo esegue e testa
Guber / terzo
Security operations
Novigo opera; Guber governa
Guber / terzo
Account e chiavi
Guber governa
Guber governa
Incident e problem
Presidio coordinato
Coordinamento multi-owner

## Slide 29
Appendice | Percorso di approfondimento
29
Quattro approfondimenti riducono l'incertezza tecnica ed economica
1
Assessment
Motore, sizing, licenze e compatibilità
2
Economics
Contratti, TCO e modello operativo
3
Prova tecnica
Replica o migrazione pilota
4
Piano di transizione
Cutover, rollback, RACI e SLA
Sequenza indicativa, attivabile sulle alternative che Guber sceglierà di approfondire.
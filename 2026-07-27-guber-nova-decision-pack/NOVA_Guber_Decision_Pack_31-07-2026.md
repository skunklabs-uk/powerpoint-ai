# NOVA – Decision Pack per la presentazione Guber del 31 luglio 2026

**Versione:** finale – sei scenari organizzati in due strategie, replica read-only accettata da Guber e integrazione grill-with-docs
**Data di preparazione:** 27 luglio 2026  
**Destinazione:** materiale sorgente per presentazione PowerPoint e successivo modello economico  
**Focus:** confronto di sei scenari organizzati in due strategie: collocazione del database primario oppure mantenimento del primario attuale con replica read-only presso Guber; l’Application Maintenance è applicata trasversalmente a ciascuno scenario, con costi, vantaggi, svantaggi, rischi e decisioni richieste

> **Avvertenza economica:** gli importi riportati sono **range di pianificazione**, non preventivi. Sono costruiti su ipotesi esplicite e fonti pubbliche ufficiali per i servizi cloud. Devono essere ricalcolati quando saranno disponibili motore e versione del database, dimensionamento, SLA, volumi, licenze, contratti Azure/AWS e capacità infrastrutturale Guber.

---

# 1. Scopo del documento

Questo documento raccoglie e organizza tutte le informazioni disponibili per costruire una presentazione che consenta, durante l'incontro del **31 luglio 2026**, di:

1. rappresentare la richiesta di Guber sull'accesso diretto ai dati NOVA, assumendo come accettato l'accesso a una replica read-only;
2. confrontare in modo omogeneo **sei scenari organizzati in due strategie**: la Strategia A confronta la collocazione del database primario (infrastruttura attuale, Azure Guber, AWS Guber e on-premise Guber); la Strategia B mantiene il primario attuale e colloca una replica read-only presso Guber, rispettivamente on-premise o su Azure Guber;
3. valutare impatti su storage documentale, sicurezza, gestione delle chiavi e orchestratore;
4. fornire una prima quantificazione economica, distinguendo costi una tantum, costi ricorrenti e voci ancora da stimare;
5. arrivare a decisioni, oppure almeno a una selezione preferenziale e a un piano di approfondimento con responsabilità e tempi;
6. evitare che la riunione rimanga una discussione generica tra “cloud”, “attuale” e “on-premise”, senza criteri di scelta.

La presentazione dovrà quindi essere un **supporto decisionale**, non una descrizione puramente tecnica.

---

# 2. Reality check: fatti, deduzioni e informazioni mancanti

## 2.1 Fatti confermati dalle fonti disponibili

- Guber considera essenziale poter utilizzare direttamente il database dell'applicativo per verifiche ed estrazioni, anche mediante interrogazioni SQL.
- **Conferma successiva di Carmen:** Guber accetta che tale esigenza sia soddisfatta tramite accesso SQL a una **replica read-only** del database NOVA collocata presso Guber.
- L'agenda ufficiale richiede di valutare tre scenari per il database NOVA:
  1. permanenza sull'infrastruttura attuale;
  2. migrazione su Azure Guber;
  3. migrazione su infrastruttura Guber on-premise.
- **Integrazione fornita da Carmen il 27 luglio 2026:** tra le ipotesi discusse deve essere incluso anche l'uso di un **account/tenant AWS di proprietà Guber**, distinguendo il modello con servizio Novigo dal modello gestito da Guber o da un terzo.
- **Conferma successiva di Carmen:** l'Application Maintenance Novigo comprende la **gestione completa dell'ambiente e dei servizi**, non soltanto il supporto applicativo. Il perimetro operativo deve quindi includere, salvo esclusioni contrattuali da esplicitare, applicazione, database, componenti infrastrutturali/cloud, orchestratore, monitoraggio, backup e restore, patching, sicurezza operativa, incident e problem management, capacity/performance management e gestione delle release.
- L'ipotesi AWS non è esplicitata nel markdown sorgente caricato e non è stata ritrovata nelle fonti GitHub indicizzate consultate; viene quindi trattata come requisito confermato in conversazione, da riallineare formalmente con Gianfranco Ballerini e con il verbale/invito originario.
- Per ciascuno scenario devono essere valutati fattibilità, requisiti e costi di migrazione.
- Deve essere valutato uno storage documentale con bucket S3 dedicato a Guber e i relativi costi.
- Devono essere affrontate cifratura dei dati e gestione delle chiavi di cifratura.
- Devono essere incluse considerazioni sull'orchestratore e sulle possibili evoluzioni a supporto dei processi Guber.
- È stata richiesta una presentazione PowerPoint e, se disponibili i dati, un file Excel con costi e ricavi previsti della commessa.
- La documentazione sul processo di gestione della history cita ODT, AV, Working Row e integrazione con Loan Data Tape; NOVA tratta quindi dati storicizzati e consolidati provenienti da più sorgenti.

## 2.2 Deduzioni ragionevoli, da dichiarare come tali

- La richiesta di accesso SQL non implica accesso diretto al database transazionale di produzione: l’accesso a una replica read-only presso Guber è stato accettato. Un database di reporting o un livello dati segregato restano varianti tecniche da valutare con un rischio operativo inferiore.
- La presenza di versionamento, working row e consolidamento da LDT rende la migrazione più delicata di una semplice copia di tabelle: devono essere verificati semantica della history, consistenza, riconciliazione e comportamento dei processi di caricamento.
- Se database, applicazione e orchestratore vengono collocati in infrastrutture differenti, rete, latenza, disponibilità del collegamento e responsabilità operative diventano parte dell'architettura applicativa, non meri dettagli infrastrutturali.
- Un bucket S3 collocato in un cloud diverso dal database o dall'orchestratore può generare costi di traffico, maggiore complessità di identity management e una superficie operativa multi-cloud.
- La gestione delle chiavi è anche una decisione di governance: chi possiede la chiave può, in ultima istanza, abilitare o impedire l'accesso ai dati.

## 2.3 Informazioni mancanti che impediscono un preventivo difendibile

Le informazioni seguenti non risultano nelle evidenze disponibili:

- motore e versione del database NOVA;
- sistema operativo e modalità di installazione attuale;
- dimensione attuale del database, crescita mensile/annua e picchi di I/O;
- numero e dimensione degli ambienti: produzione, collaudo, sviluppo, disaster recovery;
- dimensione e crescita dello storage documentale;
- volumi di lettura/scrittura e numero di connessioni concorrenti;
- numero e profilo degli utenti Guber che devono interrogare il database;
- strumenti utilizzati per SQL, BI o data extraction;
- dettaglio del livello read-only accettato: viste controllate, accesso a tabelle, stored procedure consentite ed eventuali eccezioni amministrative;
- SLA, RPO e RTO richiesti;
- finestra di fermo accettabile per la migrazione;
- collocazione attuale di applicazione, orchestratore e sistemi sorgente/destinazione;
- disponibilità di VPN, ExpressRoute, private peering o collegamenti dedicati;
- capacità già disponibile nell'infrastruttura Guber on-premise;
- tenant, subscription, landing zone e contratti Azure già disponibili a Guber;
- AWS Organization/account, landing zone, VPC, regione, connettività privata e contratti AWS già disponibili a Guber;
- finestra di servizio, SLA, severità, tempi di presa in carico/ripristino, reperibilità, capacità inclusa, esclusioni e prezzo del servizio AM Novigo end-to-end;
- licenze database possedute e presenza di Software Assurance o altri diritti di mobilità;
- modello di supporto 24x7 e responsabilità di DBA, patching, backup, security monitoring e incident management;
- requisiti di data residency, compliance, segregazione dei compiti e conservazione;
- costi interni, tariffe professionali e ricavi attesi della commessa.

## 2.4 Stress test applicato: zoom-out, critic, review e challenge-me

Le quattro modalità sono state usate come controlli distinti.

### Zoom-out – la decisione non è monodimensionale

Il problema non è soltanto “dove mettere il database”. Le decisioni indipendenti sono almeno cinque:

| Asse | Domanda | Alternative principali |
|---|---|---|
| Hosting e ownership | Dove risiedono account, compute, DB e storage? | attuale/Novigo, AWS Guber, Azure Guber, on-premise Guber, ambiente dedicato |
| Accesso ai dati | Come ottiene Guber SQL e dati verificabili? | accesso al database primario read-only oppure replica read-only presso Guber |
| Modello operativo | Chi esegue il run completo? | AM Novigo end-to-end, Guber/terza parte |
| Deployment DB | Quanto è gestito il motore? | PaaS/RDS/Managed Instance, VM/EC2 self-managed, ibrido gestito |
| Scope di migrazione | Cosa si sposta e quando? | solo data plane, DB+storage, full stack con applicazione/orchestratore, percorso per fasi |

La presentazione deve evitare il prodotto cartesiano di tutte le combinazioni, ma deve rendere espliciti questi assi prima di proporre scenari coerenti.

### Critic – debolezze rilevate nella versione 0.2

1. **L'AM era trattata quasi soltanto come variante AWS.** In realtà, essendo gestione completa dell'ambiente, è un modello operativo applicabile anche ad Azure, on-premise e a un ambiente dedicato.
2. **Rischio di doppio conteggio.** Alcuni TCO includevano già DBA/cloud operations e aggiungevano poi l'AM. Nella versione finale i costi di piattaforma sono separati dal canone AM o dal costo del team sostitutivo.
3. **Migrazione anticipata rispetto al requisito.** L'esigenza confermata è accesso SQL per verifiche ed estrazioni; non è ancora dimostrato che richieda il trasferimento del database transazionale.
4. **L’ambiguità su “accesso diretto” è stata risolta.** Guber accetta accesso SQL a una replica read-only; non sono richieste query libere sulla produzione.
5. **PaaS e IaaS erano compressi nello stesso scenario.** La compatibilità del motore può cambiare radicalmente rischio, costi e responsabilità operative.
6. **DB-only su cloud remoto rischia di diventare un'architettura permanentemente dipendente dalla WAN.** Deve essere una fase controllata, non un target implicito.

### Review – copertura dopo la correzione

| Area da coprire | Stato finale |
|---|---|
| Hosting/ownership | coperta con sei scenari organizzati in due strategie |
| Accesso SQL | coperto con database primario read-only oppure con replica read-only on-premise Guber o su Azure Guber |
| Run operativo | coperto trasversalmente con AM completa e gestione Guber/terzo |
| Compatibilità DB | coperta tramite gate PaaS vs VM/self-managed |
| Storage documentale | coperto come decisione AWS S3 vs requisito generico object storage |
| Orchestratore | coperto come scope DB-only, phased o full-stack |
| Sicurezza/chiavi | coperta con ownership Guber e accessi delegati tracciati |
| Economics | normalizzati per evitare doppio conteggio; restano parametrici |
| Exit strategy | inclusa nel modello operativo e contrattuale |

### Challenge-me – domande avversariali che cambiano la valutazione

- **Guber vuole verificare ed estrarre dati senza interrogare direttamente il transazionale.** La replica read-only presso Guber diventa quindi un vero scenario della comparativa.
- **E se Guber volesse possedere account e chiavi, ma non gestire il run?** Il modello naturale è customer-owned/provider-operated: AWS o Azure Guber con AM Novigo end-to-end.
- **E se il DB non fosse compatibile con i servizi gestiti?** Serve una variante VM/EC2 con TCO e rischio operativo più elevati, oppure una remediation applicativa prima della migrazione.
- **E se Guber volesse autonomia futura?** Va progettato un percorso contrattuale di trasferimento delle responsabilità, non un taglio immediato dell'AM.
- **E se S3 fosse soltanto un modo colloquiale per dire object storage?** Il vantaggio AWS diminuisce e vanno confrontati S3, Azure Storage e object storage on-premise sulla base dei requisiti reali.

---

# 3. Esito grill-with-docs sul perimetro della decisione

## 3.1 Regola di perimetro

La ricerca di ipotesi mancanti resta limitata alla **collocazione fisica o logica del database NOVA** e alle modalità di replica e accesso ai suoi dati. Non costituiscono scenari autonomi nuovi applicativi, orchestratori aggiuntivi, sistemi di ingestion o evoluzioni funzionali di NOVA.

L’Application Maintenance è un **asse operativo trasversale**: per ciascuno dei sei scenari devono essere valutati costi, vantaggi e svantaggi della gestione completa Novigo e della gestione Guber o di un terzo.

## 3.2 Classificazione delle evidenze

| Scenario | Provenienza | Classificazione |
|---|---|---|
| Infrastruttura attuale | agenda: «permanenza sull’infrastruttura attuale» | esplicitamente derivato dai documenti |
| Azure Guber | agenda: «migrazione su Azure Guber» | esplicitamente derivato dai documenti |
| AWS Guber | conferma fornita in conversazione | scenario confermato dall’utente, non ritrovato nel corpus GitHub disponibile |
| On-premise Guber | agenda: «migrazione su infrastruttura Guber on-premise» | esplicitamente derivato dai documenti |
| Replica read-only on-premise Guber | combinazione tra permanenza attuale e requisito di accesso SQL; replica collocata nell’infrastruttura on-premise Guber | deduzione architetturale inizialmente proposta come speculazione; accesso alla replica read-only successivamente accettato da Guber |
| Replica read-only su Azure Guber | combinazione tra permanenza attuale e requisito di accesso SQL; replica collocata nel tenant Azure Guber | deduzione architetturale inizialmente proposta come speculazione; accesso alla replica read-only successivamente accettato da Guber |

## 3.3 Esito della verifica documentale

Non sono emerse altre collocazioni del database esplicitamente richieste dalle fonti disponibili. La Strategia B separa l’unica alternativa aggiuntiva direttamente pertinente al perimetro in due scenari: mantiene il database transazionale nell’infrastruttura attuale e colloca una replica read-only interrogabile via SQL nell’infrastruttura on-premise Guber oppure nel tenant Azure Guber.

Restano varianti implementative, e non scenari ulteriori:

- servizio database gestito oppure database su VM/EC2;
- replica completa, schema di reporting o viste certificate;
- collocazione on-premise oppure Azure della replica Guber;
- gestione completa Novigo oppure gestione Guber/terza parte;
- gestione delle chiavi, networking, SLA, backup e disaster recovery.

## 3.4 Decisione considerata acquisita

Per il presente decision pack si assume come **accettato da Guber** l’accesso SQL alla replica read-only. Restano da definire la frequenza di aggiornamento, lo SLA di sincronizzazione, la granularità degli oggetti esposti, la modalità di autenticazione e il perimetro delle eventuali attività amministrative eccezionali.

---

# 4. Obiettivo decisionale dell'incontro

La presentazione dovrebbe chiedere al tavolo di decidere, o almeno indirizzare, i seguenti punti:

1. **Target preferito** tra i sei scenari organizzati in due strategie: primario su infrastruttura attuale, Azure Guber, AWS Guber o on-premise Guber; oppure primario attuale con replica read-only on-premise Guber o su Azure Guber.
2. **Modalità di accesso SQL**: la replica read-only è accettata; devono essere definiti aggiornamento, viste/schema esposti, auditing e accessi amministrativi eccezionali.
3. **Ownership operativa e modello di servizio**: chi gestisce database, backup, monitoraggio, patch, incidenti, capacity planning e Application Maintenance; per AWS, scegliere esplicitamente tra AM Novigo e gestione Guber/terza parte.
4. **Ownership delle chiavi**: Guber, fornitore, responsabilità condivisa o modello con doppio controllo.
5. **Strategia per lo storage documentale**: S3 dedicato, regione, cifratura, versioning, retention, immutabilità e lifecycle.
6. **Collocazione e ruolo dell'orchestratore**: resta dov'è, migra insieme al database o viene evoluto in modo disaccoppiato.
7. **Percorso di approfondimento**: assessment tecnico, benchmark, proof of connectivity, prova di migrazione e modello economico definitivo.

---

# 5. Requisiti minimi da usare per confrontare i sei scenari

## 5.1 Accesso ai dati

- Accesso SQL per utenti e strumenti autorizzati Guber.
- Ruoli **read-only** come impostazione predefinita.
- Viste o schema di reporting per evitare dipendenza dalla struttura interna e ridurre l'esposizione di dati non necessari.
- Tracciamento degli accessi e delle query amministrative.
- Separazione tra accesso operativo dell'applicazione e accesso analitico/manuale.
- Possibilità di esportazione controllata e riconciliazione dei dati.

## 5.2 Sicurezza

- Cifratura in transito con TLS.
- Cifratura a riposo per database, backup, snapshot e documenti.
- Gestione centralizzata delle chiavi con rotazione, revoca, audit e segregazione dei ruoli.
- Accesso privato, senza esposizione pubblica del database, salvo eccezione formalmente approvata.
- MFA e identity federation per gli amministratori.
- Logging di sicurezza e integrazione con i sistemi di monitoraggio/SIEM.
- Backup protetti da cancellazioni accidentali o malevole.
- Policy di retention e cancellazione coerenti con gli obblighi Guber.

## 5.3 Continuità operativa

- Backup automatizzati e restore testati.
- RPO e RTO definiti e misurabili.
- Alta disponibilità coerente con la criticità di NOVA.
- Procedure di rollback e cutover.
- Monitoraggio di capacità, prestazioni, errori e saturazione.

## 5.4 Governance e operatività

- RACI chiara tra Guber, Novigo, eventuale provider operativo e provider infrastrutturale.
- Il servizio **Application Maintenance Novigo**, quando selezionato, comprende la gestione completa dell'ambiente e dei servizi; il contratto deve comunque distinguere responsabilità esecutive Novigo da governance, approvazioni, key ownership e vendor management Guber.
- In caso di assenza di AM Novigo, identificazione del soggetto che assume integralmente applicazione, DBA, cloud/system operations, orchestratore, monitoring, backup/restore, patching, sicurezza operativa, incidenti, capacity e release.
- Change management, patching e vulnerability management.
- Gestione credenziali e segreti dell'orchestratore.
- Processo per richieste di accesso, revoca e revisione periodica dei privilegi.
- Cost allocation e reporting economico.

## 5.5 Modello decisionale da mostrare prima degli scenari

Per evitare una falsa scelta tra nomi di provider, la presentazione deve costruire gli scenari selezionando una voce per ciascun asse:

1. **Ownership:** Guber oppure Novigo.
2. **Hosting:** attuale, AWS, Azure, on-premise o ambiente dedicato.
3. **Data access:** replica read-only presso Guber oppure accesso controllato al database primario.
4. **Run:** AM Novigo end-to-end oppure Guber/terza parte.
5. **Scope:** data plane, DB+storage o full stack.
6. **Resilienza:** singola regione/sito, HA locale oppure DR geografico.

Il confronto economico deve essere eseguito sugli **scenari completi**, non sulla sola riga del servizio database.

---

# 6. Assunzioni usate esclusivamente per costruire i range di costo

Per rendere confrontabili gli scenari viene adottato un **carico di riferimento**, da sostituire con dati reali:

| Voce | Assunzione di lavoro |
|---|---:|
| Database relazionale | 1 istanza di produzione |
| Dimensionamento produzione | 4–8 vCPU, 16–32 GB RAM |
| Dati DB iniziali | 500 GB |
| Crescita dati | 20% annuo |
| Ambiente non produzione | 1 ambiente al 50% della produzione |
| Operatività | 24x7 |
| Alta disponibilità | richiesta in produzione |
| Backup | 30 giorni, restore periodicamente testato |
| Storage documentale | 1 TB iniziale |
| Accesso SQL | 20 utenti autorizzati, massimo 5 concorrenti |
| Disaster recovery geografico | non incluso nel range base |
| Supporto infrastrutturale | fascia business, non pieno 24x7 enterprise |
| Application Maintenance Novigo | gestione end-to-end confermata; esclusa dai TCO di piattaforma e valorizzata come canone gestito separato |
| IVA | esclusa |
| Licenze proprietarie | escluse salvo indicazione |

## 6.1 Cosa può cambiare drasticamente i numeri

- motore database e licensing;
- compatibilità con servizi PaaS;
- necessità di alta disponibilità multi-zona;
- necessità di disaster recovery geografico;
- retention backup e snapshot;
- volume documentale;
- traffico tra ambienti e cloud differenti;
- livello di supporto 8x5 o 24x7;
- presenza o assenza dell'AM Novigo;
- capacità già disponibile negli ambienti Guber.

---

# 7. Strategia A — Collocazione del database primario

Questa strategia confronta quattro possibili collocazioni del database primario NOVA. Non confronta quattro cloud: distingue il mantenimento nell’infrastruttura attuale dal trasferimento del primario nel perimetro Azure Guber, AWS Guber o on-premise Guber.

## Scenario 01 — Permanenza sull'infrastruttura attuale

## 7.1 Provenienza e classificazione

**Testo di partenza:** «permanenza sull'infrastruttura attuale».

**Classificazione:** esplicitamente derivato dai documenti.

## 7.2 Architettura proposta

Il database NOVA resta sull'infrastruttura attuale. Applicazione, orchestratore e dipendenze mantengono la collocazione esistente.

### Variante raccomandata

- accesso SQL read-only controllato;
- eventuali viste dedicate a Guber;
- rete privata o VPN;
- audit delle connessioni e delle query;
- segregazione tra account applicativi, amministrativi e di consultazione;
- backup e restore verificati;
- mantenimento dell'AM completa Novigo.

## 7.3 Modalità di accesso SQL

Possibili modalità interne allo stesso scenario:

1. accesso read-only al database primario;
2. replica read-only nell'ambiente attuale;
3. schema o viste certificate per Guber.

Le repliche presso Guber sono trattate separatamente negli scenari 05 e 06.

## 7.4 Sicurezza e chiavi

- cifratura a riposo e in transito;
- gestione chiavi nell'ambiente attuale;
- accesso Guber con identità nominali;
- logging e revisione periodica dei privilegi;
- definizione delle responsabilità di approvazione e revoca.

## 7.5 Impatto sull'orchestratore

Impatto minimo. Devono comunque essere verificati:

- eventuali carichi aggiuntivi generati dalle query Guber;
- dipendenze da schema e stored procedure;
- concorrenza tra processi batch e interrogazioni manuali;
- necessità di separare workload operativi e di reporting.

## 7.6 Costi di pianificazione

### Costi una tantum

| Voce | Range indicativo |
|---|---:|
| Assessment e hardening accesso SQL | € 5.000–12.000 |
| Ruoli, viste, auditing e segregazione | € 4.000–10.000 |
| Networking/VPN e test | € 3.000–8.000 |
| Test prestazionali e restore | € 3.000–8.000 |
| **Totale una tantum** | **€ 15.000–38.000** |

### Costi ricorrenti mensili incrementali

| Voce | Range indicativo |
|---|---:|
| capacità aggiuntiva e backup | € 300–1.000 |
| logging e monitoraggio | € 100–400 |
| supporto operativo incrementale | € 300–1.000 |
| **Totale mensile incrementale** | **€ 700–2.400** |

### TCO di piattaforma indicativo a 3 anni

**€ 40.000–124.000**, escluso il canone AM esistente o rivisto.

## 7.7 Vantaggi

- nessuna migrazione del database;
- continuità operativa;
- minor rischio di cutover;
- tempi di attivazione più rapidi;
- conoscenza dell'ambiente già disponibile;
- AM Novigo già coerente con il modello operativo.

## 7.8 Svantaggi

- ownership infrastrutturale non trasferita a Guber;
- possibile dipendenza dal fornitore;
- accesso SQL da governare con particolare attenzione;
- rischio di impatto sul transazionale se le query non sono isolate;
- minore autonomia Guber.

## 7.9 Rischi e mitigazioni

| Rischio | Mitigazione |
|---|---|
| query pesanti sul primario | viste, limiti, replica locale, workload governance |
| privilegi eccessivi | ruoli read-only, approvazioni e audit |
| dipendenza dal fornitore | documentazione, export, clausole di uscita |
| capacità insufficiente | benchmark e capacity planning |

## 7.10 Application Maintenance applicata allo scenario

L'AM Novigo comprende l'intera gestione dell'ambiente e dei servizi. Va valorizzato soltanto l'eventuale incremento per:

- nuovi accessi e auditing;
- monitoraggio dei carichi SQL;
- gestione di viste o replica;
- supporto a utenti e strumenti Guber;
- capacità aggiuntiva.

## 7.11 Quando scegliere questo scenario

- quando la priorità è rapidità e riduzione del rischio;
- quando Guber accetta che l'infrastruttura resti presso l'ambiente attuale;
- quando l'accesso SQL controllato soddisfa il requisito;
- quando la migrazione completa non è ancora giustificata.

---

## Scenario 02 — Migrazione su Azure Guber

## 8.1 Provenienza e classificazione

**Testo di partenza:** «migrazione su Azure Guber».

**Classificazione:** esplicitamente derivato dai documenti.

## 8.2 Architettura proposta

Database NOVA collocato in subscription e landing zone Guber.

Possibili varianti tecniche:

- servizio database gestito Azure compatibile con il motore;
- database su VM Azure se il PaaS non è compatibile;
- alta disponibilità zonale;
- backup e chiavi sotto governance Guber;
- accesso privato tramite Private Endpoint;
- integrazione con identity e monitoring Guber.

## 8.3 Modalità di accesso SQL

- accesso read-only tramite rete privata;
- identità nominali e gruppi Guber;
- schema o viste dedicate;
- auditing centralizzato;
- separazione tra utenti di consultazione e amministratori.

## 8.4 Sicurezza e chiavi

- TLS;
- cifratura a riposo;
- Key Vault Guber;
- customer-managed keys se richiesto;
- Private Endpoint;
- Defender/monitoring secondo standard Guber;
- segregazione tra operatori Novigo e owner Guber.

## 8.5 Impatto sull'orchestratore

### Orchestratore resta nell'ambiente attuale

- dipendenza dalla WAN;
- latenza e disponibilità del collegamento;
- gestione segreti cross-environment;
- rischio di architettura ibrida permanente.

### Orchestratore migra su Azure Guber

- maggiore coerenza operativa;
- scope e costo di migrazione più ampi;
- necessità di trasferire integrazioni e monitoring.

### Evoluzione consigliata

Evitare un target permanente con database remoto e orchestratore separato senza requisiti e SLA espliciti.

## 8.6 Costi di pianificazione

### Costi una tantum

| Voce | Range indicativo |
|---|---:|
| assessment e landing zone | € 8.000–18.000 |
| migrazione database | € 15.000–35.000 |
| networking e sicurezza | € 8.000–20.000 |
| test, cutover e rollback | € 8.000–20.000 |
| eventuale adeguamento applicativo | € 10.000–35.000 |
| **Totale una tantum** | **€ 49.000–128.000** |

### Costi ricorrenti mensili

| Voce | Range indicativo |
|---|---:|
| database gestito o VM HA | € 1.200–3.500 |
| storage e backup | € 250–800 |
| networking, logging e sicurezza | € 300–1.000 |
| **Totale piattaforma mensile** | **€ 1.750–5.300** |

### TCO indicativo a 3 anni

**€ 112.000–319.000**, escluso AM Novigo o team operativo sostitutivo.

## 8.7 Vantaggi

- ownership cloud Guber;
- integrazione con governance e security Azure;
- servizi gestiti disponibili;
- scalabilità;
- chiavi e auditing sotto controllo Guber;
- possibilità di AM Novigo su ambiente customer-owned.

## 8.8 Svantaggi

- migrazione e cutover;
- possibile incompatibilità con servizi PaaS;
- costi cloud ricorrenti;
- rischio di dipendenza dalla WAN se il resto dello stack non migra;
- necessità di chiarire responsabilità operative.

## 8.9 Rischi e mitigazioni

| Rischio | Mitigazione |
|---|---|
| incompatibilità DB | assessment e prova tecnica |
| costi superiori alle attese | sizing, budget alert, reserved capacity |
| latenza | test rete e collocazione coerente dello stack |
| responsabilità ambigue | RACI e contratto AM |
| lock-in | export, backup portabili, documentazione |

## 8.10 Application Maintenance applicata allo scenario

Con AM Novigo:

- Guber possiede subscription, dati e chiavi;
- Novigo esegue gestione end-to-end;
- accessi delegati e tracciati;
- contratto con SLA e responsabilità chiare.

Senza AM:

- Guber o un terzo deve coprire applicazione, DBA, cloud operations, monitoring, backup, patching, sicurezza, incidenti e release.

## 8.11 Quando scegliere questo scenario

- quando Azure è lo standard strategico Guber;
- quando esistono landing zone e competenze;
- quando ownership e integrazione con servizi Microsoft sono prioritarie;
- quando la migrazione dello stack è sostenibile.

---

## Scenario 03 — Account AWS di proprietà Guber

## 9.1 Provenienza e classificazione

**Provenienza:** conferma fornita in conversazione.

**Classificazione:** scenario reale, non ritrovato nel corpus GitHub disponibile.

## 9.2 Chiarimento: hosting e servizio sono due decisioni diverse

- **Hosting:** database e servizi risiedono in account AWS Guber.
- **Servizio:** l'ambiente può essere gestito end-to-end da Novigo oppure da Guber/terza parte.

La proprietà AWS non implica automaticamente gestione Guber.

## 9.3 Architettura proposta

- account AWS Guber;
- VPC privato;
- database su RDS/Aurora se compatibile;
- EC2 self-managed se necessario;
- KMS Guber;
- Secrets Manager;
- CloudWatch e logging;
- S3 per documenti e backup secondo requisiti;
- connettività privata verso applicazione e orchestratore.

### Collocazione di applicazione e orchestratore

Devono essere valutate:

- permanenza nell'ambiente attuale;
- migrazione progressiva su AWS Guber;
- migrazione full-stack.

## 9.4 Variante A – AWS Guber con Application Maintenance Novigo end-to-end

### Responsabilità proposte

**Guber:**

- ownership account, dati e chiavi;
- approvazioni e governance;
- vendor management;
- policy di sicurezza.

**Novigo:**

- applicazione;
- database e infrastruttura;
- monitoring;
- backup e restore;
- patching;
- sicurezza operativa;
- incident e problem management;
- capacity e performance;
- orchestratore;
- release.

### Vantaggi

- ownership Guber;
- un unico responsabile operativo;
- integrazione naturale con S3;
- minore rischio di transizione operativa;
- continuità di competenze Novigo.

### Svantaggi

- canone AM;
- dipendenza operativa da Novigo;
- necessità di accessi privilegiati delegati;
- confini di responsabilità da formalizzare.

## 9.5 Variante B – AWS Guber senza Application Maintenance Novigo

### Condizioni minime

Guber o il fornitore scelto deve garantire:

- DBA;
- cloud operations;
- supporto applicativo;
- gestione orchestratore;
- monitoring e on-call;
- backup/restore;
- patching;
- vulnerability management;
- incident/problem management;
- release management.

### Vantaggi

- maggiore autonomia;
- libertà di scelta del fornitore;
- possibile riduzione del canone esterno se esistono capacità interne reali.

### Svantaggi

- rischio di gap di competenze;
- costo interno spesso sottostimato;
- frammentazione delle responsabilità;
- handover e documentazione necessari;
- maggiore rischio operativo iniziale.

## 9.6 Modalità di accesso SQL

- read-only via rete privata;
- IAM/federation per accessi amministrativi;
- credenziali DB separate;
- auditing;
- viste o schema dedicato;
- replica read-only se necessaria.

## 9.7 Sicurezza e chiavi

- KMS customer-managed;
- key ownership Guber;
- grant temporanei a Novigo;
- rotazione e revoca;
- CloudTrail;
- accesso privato;
- cifratura backup e snapshot;
- Secrets Manager.

## 9.8 Costi infrastrutturali di pianificazione

### Costi una tantum

| Voce | Range indicativo |
|---|---:|
| landing zone e VPC | € 8.000–18.000 |
| migrazione database | € 15.000–35.000 |
| networking e sicurezza | € 8.000–20.000 |
| test, cutover e rollback | € 8.000–20.000 |
| adeguamenti applicativi | € 10.000–35.000 |
| **Totale una tantum** | **€ 49.000–128.000** |

### Costi cloud ricorrenti mensili

| Voce | Range indicativo |
|---|---:|
| RDS/Aurora o EC2 HA | € 1.100–3.400 |
| storage, backup e snapshot | € 250–800 |
| networking, logging e sicurezza | € 300–1.000 |
| **Totale piattaforma mensile** | **€ 1.650–5.200** |

### TCO infrastrutturale indicativo a 3 anni

**€ 108.000–315.000**, escluso AM Novigo o team sostitutivo.

## 9.9 Valorizzazione dell'Application Maintenance Novigo end-to-end

### Struttura economica raccomandata

- setup e presa in carico;
- canone mensile base;
- fascia SLA;
- reperibilità;
- capacità inclusa;
- change e release incluse o a consumo;
- attività straordinarie;
- exit/handover.

### Dati necessari per il prezzo

- orari di copertura;
- SLA;
- numero ambienti;
- volume ticket;
- frequenza release;
- necessità 24x7;
- perimetro security operations;
- capacity management;
- responsabilità su applicazione e orchestratore.

Il TCO deve usare una sola delle due righe alternative:

1. canone AM Novigo;
2. costo completo del team Guber/terzo.

## 9.10 Rischi e mitigazioni

| Rischio | Mitigazione |
|---|---|
| lock-in operativo | documentazione, automazione, exit plan |
| privilegi Novigo | accessi temporanei, least privilege, audit |
| costo AM non definito | servizio catalogato e metriche |
| incompatibilità RDS | assessment e fallback EC2 |
| dipendenza WAN | migrazione coerente dello stack o SLA rete |

## 9.11 Quando scegliere questo scenario

- quando AWS è già standard Guber;
- quando S3 è un requisito reale;
- quando Guber vuole ownership dell'account;
- quando Novigo può gestire end-to-end senza trasferire subito il run;
- quando la landing zone AWS è disponibile.

---

## Scenario 04 — Migrazione su infrastruttura Guber on-premise

## 10.1 Provenienza e classificazione

**Testo di partenza:** «migrazione su infrastruttura Guber on-premise».

**Classificazione:** esplicitamente derivato dai documenti.

## 10.2 Architettura proposta

- database in data center Guber;
- VM o server dedicati;
- cluster HA;
- storage enterprise;
- backup separato e immutabile;
- rete interna;
- monitoring Guber o Novigo;
- eventuale replica su secondo sito.

## 10.3 Modalità di accesso SQL

- accesso dalla rete Guber;
- ruoli read-only;
- audit;
- viste dedicate;
- eventuale bastion o PAM per amministratori;
- segregazione tra DBA e utenti di consultazione.

## 10.4 Sicurezza e chiavi

- cifratura storage e backup;
- TLS;
- HSM o key management Guber;
- PAM;
- vulnerability management;
- logging e SIEM;
- protezione fisica e continuità del data center.

## 10.5 Impatto sull'orchestratore

Se l'orchestratore resta fuori dall'on-premise:

- dipendenza dalla connettività;
- latenza;
- gestione segreti;
- troubleshooting cross-domain.

La migrazione full-stack riduce tali rischi ma aumenta scope e costi.

## 10.6 Costi di pianificazione

### Costi una tantum, senza licenze database proprietarie

| Voce | Range indicativo |
|---|---:|
| assessment e design | € 8.000–18.000 |
| hardware/virtualizzazione incrementale | € 20.000–70.000 |
| storage e backup | € 15.000–50.000 |
| migrazione e test | € 20.000–45.000 |
| sicurezza e monitoring | € 8.000–25.000 |
| **Totale una tantum** | **€ 71.000–208.000** |

### Costi ricorrenti mensili

| Voce | Range indicativo |
|---|---:|
| energia, data center e ammortamento | € 700–2.000 |
| supporto hardware/software | € 400–1.500 |
| backup, monitoring e sicurezza | € 300–1.000 |
| **Totale piattaforma mensile** | **€ 1.400–4.500** |

### Licenze da aggiungere

Eventuali licenze database, sistema operativo, virtualizzazione e backup possono modificare drasticamente il TCO.

### TCO indicativo a 3 anni

**€ 121.000–370.000**, escluso AM Novigo o team operativo sostitutivo e licenze proprietarie non note.

## 10.7 Vantaggi

- controllo fisico e logico Guber;
- accesso SQL interno;
- possibile riuso di capacità esistente;
- integrazione con rete e security Guber;
- minore dipendenza da provider cloud.

## 10.8 Svantaggi

- investimento iniziale;
- responsabilità su hardware e data center;
- scalabilità meno elastica;
- complessità HA e DR;
- necessità di competenze operative;
- rischio di sottostimare costi interni.

## 10.9 Rischi e mitigazioni

| Rischio | Mitigazione |
|---|---|
| capacità insufficiente | assessment infrastrutturale |
| single site | secondo sito o DR |
| competenze | AM Novigo o fornitore qualificato |
| hardware lifecycle | piano di rinnovo |
| licenze | inventory e verifica contrattuale |

## 10.10 Application Maintenance applicata allo scenario

Con AM Novigo:

- Novigo gestisce end-to-end ambiente e servizi;
- Guber mantiene ownership fisica, dati e governance;
- accessi e responsabilità devono essere formalizzati.

Senza AM:

- Guber o un terzo assume integralmente run e supporto.

## 10.11 Quando scegliere questo scenario

- quando esiste un vincolo di data center;
- quando Guber dispone già di capacità e competenze;
- quando il controllo on-premise è prioritario;
- quando il TCO reale è competitivo dopo licenze e DR.

---

# 11. Strategia B — Primario attuale + replica read-only presso Guber

Questa strategia non confronta ulteriori cloud: mantiene invariato il database primario nell’infrastruttura attuale e soddisfa il requisito dati con una replica read-only presso Guber. Le sole collocazioni valutate per la replica sono on-premise Guber e Azure Guber.

## Scenario 05 — Replica read-only on-premise Guber

### 11.1 Provenienza e classificazione

Lo scenario deriva dalla combinazione tra permanenza sull'infrastruttura attuale, esigenza di accesso SQL e accettazione Guber dell'accesso a replica read-only.

**Classificazione:** deduzione architetturale successivamente accettata da Guber.

### 11.2 Architettura e collocazione

- database primario NOVA nell'infrastruttura attuale, invariato;
- replica read-only nell'infrastruttura on-premise Guber;
- Guber accede localmente via SQL esclusivamente alla replica;
- sincronizzazione tramite tecnologia compatibile con il motore;
- monitoring di replica, lag e consistenza;
- procedure di rebuild e recovery.

### 11.3 Accesso SQL, costi e condizioni

Guber accede con ruoli read-only, identità nominali, auditing, viste o schema certificato se necessario, limitazioni su query e risorse e separazione completa dal database primario.

| Voce | Range indicativo |
|---|---:|
| assessment replica e compatibilità | € 5.000–12.000 |
| implementazione e configurazione | € 10.000–25.000 |
| networking e sicurezza | € 5.000–15.000 |
| test consistenza e performance | € 5.000–12.000 |
| **Totale una tantum** | **€ 25.000–64.000** |

| Voce | Range indicativo mensile |
|---|---:|
| compute/database replica | € 600–2.000 |
| storage e backup | € 150–600 |
| rete, logging e monitoring | € 150–600 |
| **Totale mensile** | **€ 900–3.200** |

**TCO indicativo a 3 anni:** **€ 57.000–179.000**, escluso AM Novigo. La stima resta parametrica e dipende da capacità on-premise Guber, connettività, licenze, SLA, dimensionamento e AM; non introduce costi aggiuntivi rispetto al precedente scenario replica.

### 11.4 Vantaggi, limiti e AM

- soddisfa il requisito SQL accettato senza migrazione immediata del primario;
- isola i carichi di consultazione, mantiene ownership della replica Guber, riduce il rischio di cutover e mantiene un percorso graduale e reversibile;
- dati non necessariamente in tempo reale, dipendenza dalla tecnologia di replica, gestione del lag e della consistenza, doppio ambiente, mancato trasferimento della piena ownership del transazionale e possibili limitazioni su stored procedure o funzionalità specifiche restano da governare.

Con AM Novigo, Novigo gestisce primario, replica, sincronizzazione, troubleshooting end-to-end, backup/recovery, accessi e auditing. Con gestione Guber o terzo, devono essere separati chiaramente gli owner del primario e della replica; il troubleshooting cross-environment può essere più complesso.

## Scenario 06 — Replica read-only su Azure Guber

### 11.5 Provenienza e classificazione

Lo scenario deriva dalla medesima deduzione architetturale successivamente accettata da Guber: permanenza del primario, requisito SQL e replica read-only.

### 11.6 Architettura e collocazione

- database primario NOVA nell'infrastruttura attuale, invariato;
- replica read-only nel tenant Azure Guber;
- Guber accede via SQL esclusivamente alla replica;
- identity, audit, accessi e chiavi sono gestiti nel perimetro Azure Guber;
- sincronizzazione tramite tecnologia compatibile con il motore;
- monitoring di replica, lag e consistenza;
- procedure di rebuild e recovery.

### 11.7 Accesso SQL, costi e condizioni

Guber accede con ruoli read-only, identità nominali, auditing, viste o schema certificato se necessario, limitazioni su query e risorse e separazione completa dal database primario.

| Voce | Range indicativo |
|---|---:|
| assessment replica e compatibilità | € 5.000–12.000 |
| implementazione e configurazione | € 10.000–25.000 |
| networking e sicurezza | € 5.000–15.000 |
| test consistenza e performance | € 5.000–12.000 |
| **Totale una tantum** | **€ 25.000–64.000** |

| Voce | Range indicativo mensile |
|---|---:|
| compute/database replica | € 600–2.000 |
| storage e backup | € 150–600 |
| rete, logging e monitoring | € 150–600 |
| **Totale mensile** | **€ 900–3.200** |

**TCO indicativo a 3 anni:** **€ 57.000–179.000**, escluso AM Novigo. La stima resta parametrica e dipende da servizi Azure, connettività, licenze, SLA, dimensionamento e AM; non introduce costi aggiuntivi rispetto al precedente scenario replica.

### 11.8 Vantaggi, limiti e AM

- soddisfa il requisito SQL accettato senza migrazione immediata del primario;
- isola i carichi di consultazione, mantiene ownership della replica Guber, riduce il rischio di cutover e mantiene un percorso graduale e reversibile;
- dati non necessariamente in tempo reale, dipendenza dalla tecnologia di replica, gestione del lag e della consistenza, doppio ambiente, mancato trasferimento della piena ownership del transazionale e possibili limitazioni su stored procedure o funzionalità specifiche restano da governare.

Con AM Novigo, Novigo gestisce primario, replica, sincronizzazione, troubleshooting end-to-end, backup/recovery, accessi e auditing. Con gestione Guber o terzo, devono essere separati chiaramente gli owner del primario e della replica; il troubleshooting cross-environment può essere più complesso.

### 11.9 Rischi e condizioni comuni agli scenari 05 e 06

| Rischio | Condizione/Mitigazione |
|---|---|
| replica non supportata | verifica motore e licenze |
| lag e dati non aggiornati | SLA di sincronizzazione |
| divergenza semantica | riconciliazioni e controlli |
| rete instabile | connettività ridondata |
| query pesanti | sizing e workload governance |

Gli scenari 05 e 06 sono appropriati quando Guber accetta dati read-only replicati, si vuole ridurre il rischio di migrazione, l'ownership immediata del primario non è indispensabile e serve una soluzione rapida e reversibile.

---

# 12. Modello operativo trasversale – gestione completa Novigo

## 12.1 Principio

L'Application Maintenance Novigo è applicabile a tutti i sei scenari. Non rappresenta una collocazione del database, ma un modello operativo. Negli scenari 05 e 06 deve essere confrontata esplicitamente con la gestione Guber o di un terzo.

Il servizio comprende la gestione completa dell'ambiente e dei servizi, salvo esclusioni esplicite.

## 12.2 RACI di riferimento

| Attività | Guber | Novigo con AM | Guber/terzo senza AM |
|---|---:|---:|---:|
| ownership dati e approvazioni | A | C | A |
| ownership account/tenant Guber | A | C | A |
| applicazione e release | C/A | R | R |
| database administration | C/A | R | R |
| cloud/system operations | C/A | R | R |
| orchestratore e batch | C/A | R | R |
| monitoring e on-call | C/A | R | R |
| backup e restore | C/A | R | R |
| patching e vulnerability | C/A | R | R |
| incident/problem management | C/A | R | R |
| capacity/performance | C/A | R | R |
| key ownership | A | C/R delegato | A/R |
| audit e compliance | A | R/C | A/R |

## 12.3 Due modelli operativi da confrontare

1. **AM Novigo end-to-end**;
2. **gestione Guber o terza parte**.

## 12.4 Regola economica anti-doppio conteggio

Per ciascuno scenario:

**TCO = costi una tantum + costi piattaforma + una sola voce operativa**

La voce operativa deve essere:

- canone AM Novigo;
- oppure costo del team Guber/terzo.

Non devono essere sommati entrambi.

## 12.5 Implicazione sulla decisione

Un ambiente di proprietà Guber può essere gestito completamente da Novigo. Ownership e gestione sono decisioni separate.

---

# 13. Storage documentale – bucket S3 dedicato a Guber

## 13.1 Requisiti minimi

- bucket dedicato;
- cifratura;
- key ownership;
- versioning;
- lifecycle;
- retention;
- eventuale immutabilità;
- logging accessi;
- segregazione tra applicazione, utenti e amministratori;
- classificazione dati;
- regione e data residency.

## 13.2 Componenti di costo

- storage;
- richieste API;
- retrieval;
- versioni;
- backup/replica;
- egress;
- KMS;
- logging;
- servizi di sicurezza.

## 13.3 Range usato nel decision pack

Per 1 TB iniziale con crescita moderata:

- costo base storage: basso rispetto al database;
- costo reale dipendente da versioning, retrieval, egress e retention;
- range di pianificazione: **€ 30–200/mese**, esclusi trasferimenti intensivi e replica geografica.

## 13.4 Decisione da prendere

Chiarire se “S3” è:

- requisito AWS specifico;
- oppure sinonimo di object storage.

La risposta influenza la comparazione AWS/Azure/on-premise.

---

# 14. Sicurezza e gestione delle chiavi – modello comune

## 14.1 Principio proposto

Guber dovrebbe mantenere ownership o controllo finale delle chiavi per gli ambienti di propria proprietà.

## 14.2 Modello di responsabilità

- Guber approva policy, accessi e revoche;
- Novigo opera con grant delegati e tracciati;
- rotazione e revoca sono automatizzate;
- accessi amministrativi sono temporanei;
- backup e snapshot sono cifrati;
- procedure di emergenza sono documentate.

## 14.3 Controlli da mostrare in presentazione

- TLS;
- encryption at rest;
- customer-managed keys;
- private networking;
- MFA;
- PAM o accesso just-in-time;
- audit log;
- segregazione dei ruoli;
- backup immutabili;
- restore test;
- vulnerability management;
- incident response.

---

# 15. Evoluzione dell'orchestratore

## 15.1 Domanda architetturale reale

L'orchestratore deve restare vicino all'applicazione e al database oppure può operare attraverso una rete ibrida?

## 15.2 Requisiti minimi

- gestione sicura dei segreti;
- retry e idempotenza;
- logging e tracciamento;
- controllo del lag;
- gestione degli errori;
- monitoring end-to-end;
- compatibilità con la nuova collocazione;
- SLA di rete.

## 15.3 Impatto degli scenari

- scenario attuale: impatto minimo;
- Azure/AWS DB-only: forte dipendenza dalla WAN;
- on-premise DB-only: dipendenza dalla connettività verso Guber;
- scenari 05 e 06: replica asincrona e monitoring della consistenza;
- full-stack: maggiore costo iniziale ma minore accoppiamento cross-environment.

## 15.4 Proposta evolutiva indipendente dallo scenario

L'orchestratore dovrebbe essere reso più osservabile, configurabile e resiliente, ma non deve diventare un nuovo scenario autonomo.

---

# 16. Confronto sintetico degli scenari decisionali

## 16.1 Matrice qualitativa

| Criterio | 01 Attuale | 02 Azure primario | 03 AWS primario | 04 On-premise primario | 05 Replica on-premise | 06 Replica Azure |
|---|---:|---:|---:|---:|---:|---:|
| rapidità | alta | media-bassa | media-bassa | bassa | alta-media | alta-media |
| rischio migrazione | basso | medio-alto | medio-alto | alto | basso-medio | basso-medio |
| ownership Guber | bassa | alta | alta | alta | media-alta sulla replica | media-alta sulla replica |
| accesso SQL | medio-alto | alto | alto | alto | alto | alto |
| elasticità | media | alta | alta | bassa-media | dipende dalla replica | dipende dalla replica |
| complessità operativa | bassa-media | media | media | alta | media | media |
| compatibilità con AM Novigo | alta | alta | alta | alta | alta | alta |
| reversibilità | alta | media | media | bassa | alta | alta |

## 16.2 Confronto dei modelli operativi

| Modello | Pro | Contro |
|---|---|---|
| AM Novigo end-to-end | continuità, un solo responsabile, competenze | canone, dipendenza operativa |
| Guber/terzo | autonomia, libertà di sourcing | handover, competenze, rischio frammentazione |

## 16.3 Confronto economico normalizzato

| Scenario | Una tantum | Piattaforma mensile | TCO 3 anni piattaforma |
|---|---:|---:|---:|
| Attuale | € 15k–38k | € 0,7k–2,4k | € 40k–124k |
| Azure Guber | € 49k–128k | € 1,75k–5,3k | € 112k–319k |
| AWS Guber | € 49k–128k | € 1,65k–5,2k | € 108k–315k |
| On-premise Guber | € 71k–208k | € 1,4k–4,5k | € 121k–370k |
| Replica on-premise Guber | € 25k–64k | € 0,9k–3,2k | € 57k–179k |
| Replica Azure Guber | € 25k–64k | € 0,9k–3,2k | € 57k–179k |

### Lettura corretta dei numeri

- i range sono parametrici;
- non includono licenze non note;
- non includono AM Novigo;
- non includono il costo del team sostitutivo;
- non includono DR geografico;
- devono essere aggiornati con dati reali.

Per gli scenari 05 e 06 gli stessi range sono mantenuti come stima parametrica: il primo dipende dalla capacità on-premise Guber, il secondo dai servizi Azure; entrambi dipendono anche da connettività, licenze, SLA, dimensionamento e AM. Le righe restano alternative e non vanno sommate tra loro né con i costi del primario.

---

# 17. Gate decisionali prima del punteggio

| Gate | Impatto |
|---|---|
| accesso read-only alla replica accettato da Guber | scenari 05 e 06 pienamente valutabili |
| AWS standard Guber | rafforza scenario 03 |
| Azure standard Guber | rafforza scenario 02 |
| capacità on-premise esistente | può ridurre costi scenario 04 |
| compatibilità PaaS | riduce costi e rischio cloud |
| ownership account obbligatoria | penalizza scenario attuale |
| AM Novigo richiesta | uniforma il run nei diversi scenari |
| full-stack necessario | aumenta scope di Azure/AWS/on-premise |

---

# 18. Raccomandazione preliminare

## 18.1 Raccomandazione a due velocità

### Velocità 1 – soddisfare il requisito dati

Guber ha accettato l’accesso SQL a una replica read-only sotto propria governance. Privilegiare quindi gli **scenari 05 e 06** come alternative pienamente comparabili: replica on-premise Guber oppure su Azure Guber, gestibili end-to-end da Novigo. Sono meno rischiosi di una migrazione immediata e possono restare target stabili.

### Velocità 2 – decidere il target della piattaforma

Confrontare AWS, Azure e on-premise sulla base di:

- standard Guber;
- compatibilità del database;
- costi reali;
- connettività;
- ownership;
- AM Novigo;
- scope full-stack.

## 18.2 Regole di scelta

- scegliere AWS se è standard Guber e S3 è requisito reale;
- scegliere Azure se è standard strategico Guber;
- scegliere on-premise solo con capacità, competenze o vincoli specifici;
- scegliere scenario attuale per rapidità e rischio minimo;
- scegliere gli scenari 05 o 06 per accesso SQL senza migrazione immediata, in funzione della collocazione on-premise o Azure della replica.

## 18.3 Baseline operativa raccomandata

Per ambienti Guber:

- account e chiavi Guber;
- AM Novigo end-to-end;
- accessi delegati e audit;
- RACI;
- exit plan;
- TCO separato tra piattaforma e servizio.

## 18.4 Decisione minima attesa il 31 luglio

1. confermare i sei scenari organizzati nelle due strategie;
2. scegliere la collocazione preferita della replica read-only: on-premise Guber o Azure Guber;
3. confermare il modello AM;
4. autorizzare assessment tecnico ed economico;
5. definire owner e tempi.

---

# 19. Roadmap proposta

| Fase | Durata indicativa | Output |
|---|---:|---|
| raccolta dati tecnici | 1–2 settimane | inventory DB, volumi, SLA, rete |
| assessment compatibilità | 1–2 settimane | PaaS/IaaS, replica, licenze |
| modello economico | 1 settimana | TCO e AM |
| prova tecnica | 2–4 settimane | replica o migrazione pilota |
| decisione target | 1 settimana | scenario approvato |
| implementazione | 6–16 settimane | ambiente operativo |
| cutover/handover | 1–3 settimane | go-live e stabilizzazione |

---

# 20. Struttura consigliata della presentazione

## Slide 1 – Titolo

NOVA – Evoluzione dell'architettura della piattaforma.

## Slide 2 – La decisione reale

Collocazione del database, accesso SQL, ownership e modello operativo.

## Slide 3 – Il requisito chiarito

Accesso SQL a replica read-only accettato da Guber.

## Slide 4 – I cinque assi decisionali

Hosting, accesso, run, deployment, scope.

## Slide 5 – Fatti confermati e dati mancanti

Distinguere evidenze e assunzioni.

## Slide 6 – Sei scenari, due strategie per rispondere al requisito dati

Un unico requisito dati può essere soddisfatto trasferendo il primario oppure replicando i dati presso Guber. Distinguere visivamente Strategia A: collocazione del primario (01–04) e Strategia B: replica read-only (05–06), senza ranking o raccomandazioni nella mappa.

## Slide 7 – Scenari 05 e 06: replica read-only presso Guber

Confrontare replica on-premise Guber e replica su Azure Guber: primario invariato, architettura, costi parametrici, pro e contro.

## Slide 8 – Scenario 01: infrastruttura attuale

Costi, pro e contro.

## Slide 9 – AWS Guber + AM Novigo end-to-end

Ownership e gestione.

## Slide 10 – Azure Guber + AM Novigo end-to-end

Ownership e gestione.

## Slide 11 – Scenario 04: on-premise Guber

Costi, pro e contro.

## Slide 12 – Cosa comprende l'AM Novigo

Perimetro completo.

## Slide 13 – Con AM o senza AM

Confrontare per ciascuno scenario la gestione completa Novigo con la gestione Guber o di un terzo.

## Slide 14 – PaaS vs IaaS

Gate di compatibilità.

## Slide 15 – Accesso SQL sicuro

Database primario e replica read-only accettata presso Guber, con ruoli, auditing e segregazione degli accessi.

## Slide 16 – Storage documentale

S3 e alternative object storage.

## Slide 17 – Orchestratore e scope full-stack

Impatto della collocazione.

## Slide 18 – Economics senza doppio conteggio

Piattaforma più una sola voce operativa.

## Slide 19 – Gate decisionali

Criteri che cambiano la scelta.

## Slide 20 – Raccomandazione

Scenari 05 e 06 per il requisito dati; target del primario da scegliere tra infrastruttura attuale, AWS, Azure e on-premise.

## Slide 21 – Decisioni e prossimi passi

Owner, tempi, assessment.

---

# 21. Informazioni da chiedere a Carmen/Ignazio e al team prima della versione definitiva

## Priorità 1 – bloccanti per costi e architettura

- motore e versione DB;
- dimensione e crescita;
- ambienti;
- SLA, RPO, RTO;
- disponibilità Azure/AWS/on-premise;
- connettività;
- licenze;
- dettaglio della replica read-only;
- collocazione desiderata della replica.

## Priorità 2 – necessarie per la proposta commerciale

- perimetro e prezzo AM;
- orari e SLA;
- ticket e release;
- costi interni;
- tariffe professionali;
- ricavi e margini;
- durata contrattuale;
- exit/handover.

## Priorità 3 – affinamento della presentazione

- template PowerPoint;
- logo e visual identity;
- audience;
- durata dell'incontro;
- livello tecnico;
- decisioni già orientate informalmente.

---

# 22. Struttura del modello Excel da predisporre dopo la raccolta dati

## Foglio 1 – Assunzioni

- motore;
- sizing;
- volumi;
- crescita;
- SLA;
- ambienti;
- licenze;
- costo unitario cloud;
- tariffa giornaliera;
- AM.

## Foglio 2 – Scenario 01: infrastruttura attuale

- una tantum;
- costi incrementali;
- AM;
- TCO;
- ricavi;
- margine.

## Foglio 3 – Scenario 02: Azure Guber

- migrazione;
- servizi Azure;
- networking;
- sicurezza;
- AM;
- TCO;
- ricavi;
- margine.

## Foglio 4 – Scenario 03: AWS Guber

- migrazione;
- RDS/EC2;
- S3;
- networking;
- sicurezza;
- AM o team sostitutivo;
- TCO;
- ricavi;
- margine.

## Foglio 5 – Scenario 05: replica read-only on-premise Guber

- implementazione replica;
- capacità on-premise Guber;
- networking;
- monitoring;
- AM;
- TCO;
- ricavi;
- margine.

## Foglio 6 – Scenario 06: replica read-only su Azure Guber

- implementazione replica;
- servizi Azure;
- networking;
- monitoring;
- AM;
- TCO;
- ricavi;
- margine.

## Foglio 7 – Application Maintenance end-to-end

- setup;
- canone;
- SLA;
- copertura;
- capacità;
- extra;
- exit.

## Foglio 8 – Scenario 04: on-premise Guber

- hardware;
- storage;
- backup;
- licenze;
- migrazione;
- AM;
- TCO;
- ricavi;
- margine.

## Foglio 9 – Ricavi e margini

- ricavi una tantum;
- ricavi ricorrenti;
- costi interni;
- margine lordo;
- cash flow.

## Foglio 10 – Comparativa

- TCO;
- score;
- rischio;
- time-to-value;
- ownership;
- AM;
- raccomandazione.

---

# 23. Fonti e provenienza

## 23.1 Fonte interna principale

- markdown NOVA – Database Esterno e Architettura Target – Meeting 31/07/2026.

## 23.2 Materiale GitHub e skill metodologiche consultate

- repository `synthesize-guber-knowledge`;
- `summary.md`;
- `ask-skills`;
- `reality-check`;
- `research`;
- `grill-with-docs`;
- `zoom-out`;
- lenti critic, review e challenge-me.

## 23.3 Fonti esterne ufficiali usate per architettura e costi

- documentazione e pricing ufficiali Microsoft Azure;
- documentazione e pricing ufficiali AWS;
- documentazione ufficiale su database gestiti, private networking, key management, backup e object storage.

Le fonti esterne supportano fattibilità e struttura dei costi, non costituiscono preventivi.

## 23.4 Classificazione delle stime

- **fatti:** richieste e agenda;
- **conferme conversazionali:** AWS, AM completa, replica read-only accettata;
- **deduzioni:** impatti architetturali e rischi;
- **stime:** range economici parametrici;
- **da validare:** sizing, licenze, SLA, contratti e capacità.

---

# 24. Conclusione da usare come messaggio finale della presentazione

Guber dispone di sei scenari organizzati in due strategie: collocazione del database primario oppure mantenimento del primario attuale con replica read-only presso Guber.

Gli scenari 05 e 06 consentono di soddisfare il requisito SQL accettato senza migrare immediatamente il database primario: il primo colloca la replica on-premise Guber, il secondo su Azure Guber. Rappresentano le opzioni con il miglior equilibrio iniziale tra rischio, reversibilità e time-to-value.

AWS e Azure devono essere confrontati come target strategici sulla base degli standard Guber, della compatibilità del database e del TCO completo. L’on-premise resta uno scenario condizionato dalla disponibilità di capacità, competenze e requisiti di continuità operativa presso Guber.

L'Application Maintenance Novigo deve essere valutata trasversalmente a tutti gli scenari, separando sempre il costo della piattaforma dal costo del servizio operativo.

# NOVA Guber — executive storyline

## Corpo principale

### 1. Cover

**NOVA — alternative infrastrutturali e modelli operativi**

Confronto preliminare per Guber · 31 luglio 2026

### 2. Il perimetro: accesso ai dati, controllo e continuità

- **Contesto:** Guber richiede accesso SQL ai dati NOVA per verifiche ed estrazioni.
- **Esigenza:** rendere i dati accessibili senza compromettere operatività, sicurezza e responsabilità.
- **Obiettivo:** rendere confrontabili sei alternative di collocazione e gestione, senza anticipare la scelta.

Nota: la replica read-only presso Guber è considerata accettabile.

### 3. Oggi NOVA concentra dati e operatività sull'ambiente corrente

- Il database primario supporta applicazione, history e consolidamento.
- Guber richiede un accesso SQL governato e tracciabile.
- Mancano ancora dimensionamento, SLA, licensing, connettività e standard cloud Guber.

Messaggio: il requisito dati è confermato; la necessità di migrare il primario non è ancora dimostrata.

### 4. Sei alternative separano due scelte: primario e replica

1. mantenere l'infrastruttura attuale;
2. migrare il primario su Azure Guber;
3. migrare il primario su AWS Guber;
4. migrare il primario on-premise Guber;
5. mantenere il primario e creare una replica on-premise Guber;
6. mantenere il primario e creare una replica su Azure Guber.

Messaggio: le alternative coprono sia il trasferimento della piattaforma sia il solo requisito di accesso.

### 5. Scenario 1 — continuità sull'infrastruttura attuale

**Profilo:** cambiamento minimo e tempi più rapidi.

- Pro: rischio di migrazione contenuto; continuità operativa; alta reversibilità.
- Attenzioni: ownership Guber limitata; accesso SQL da segregare; dipendenza dall'ambiente corrente.
- Gate: schema/vista read-only, audit, capacità e SLA.
- TCO piattaforma 3 anni: **€ 40k–124k**.

### 6. Scenario 2 — primario su Azure Guber

**Profilo:** ownership Guber e integrazione con governance Azure.

- Pro: controllo account e chiavi; elasticità; servizi gestiti se compatibili.
- Attenzioni: migrazione e dipendenza dalla connettività; compatibilità PaaS; run da assegnare.
- Gate: landing zone, motore DB, networking privato e contratti.
- TCO piattaforma 3 anni: **€ 112k–319k**.

### 7. Scenario 3 — primario su AWS Guber

**Profilo:** ownership Guber con target cloud in regione Francoforte.

- Pro: elasticità; servizi gestiti; coerenza con S3 se requisito effettivo.
- Attenzioni: migrazione, compatibilità RDS, landing zone e responsabilità operative.
- Gate: standard AWS Guber, motore DB, VPC e connettività privata.
- TCO piattaforma 3 anni: **€ 108k–315k**.

### 8. Scenario 4 — primario on-premise Guber

**Profilo:** massimo controllo infrastrutturale diretto.

- Pro: ownership Guber; integrazione con rete e processi interni.
- Attenzioni: capacità, licensing, HA/DR e carico operativo.
- Gate: infrastruttura disponibile, competenze, secondo sito e backup.
- TCO piattaforma 3 anni: **€ 121k–370k**.

### 9. Scenario 5 — replica read-only on-premise Guber

**Profilo:** autonomia sui dati senza spostare il transazionale.

- Pro: migrazione contenuta; accesso locale; alta reversibilità.
- Attenzioni: lag, compatibilità della replica, ownership divisa e riconciliazione.
- Gate: motore/licenze, frequenza, viste esposte e monitoring.
- TCO piattaforma 3 anni: **€ 57k–179k**.

### 10. Scenario 6 — replica read-only su Azure Guber

**Profilo:** accesso governato ai dati con servizi Azure.

- Pro: autonomia dati; identity e audit Azure; scalabilità della replica.
- Attenzioni: connettività cross-environment, lag, egress e compatibilità.
- Gate: subscription, networking privato, replica supportata e retention.
- TCO piattaforma 3 anni: **€ 57k–179k**.

### 11. Il modello operativo resta una scelta trasversale

- **AM Novigo end-to-end:** un solo presidio operativo su applicazione, database, infrastruttura, orchestratore, monitoring, backup, patching, sicurezza e release.
- **Guber / terza parte:** maggiore autonomia di sourcing, con handover, competenze e rischio di frammentazione da gestire.

Messaggio: account e chiavi possono restare Guber anche con run delegato e tracciato.

### 12. I range economici delimitano il confronto, non sostituiscono il sizing

Tabella dei sei scenari con una tantum, piattaforma mensile e TCO a tre anni.

Note:

- AM esclusa e separata;
- DR geografico e licenze non note esclusi;
- AWS verificato su `eu-central-1`;
- confidenza bassa finché non sono disponibili dati reali.

### 13. La matrice evidenzia trade-off differenti, non un vincitore

Criteri: rapidità, rischio migrazione, ownership Guber, accesso SQL, elasticità, complessità operativa e reversibilità.

Messaggio: il posizionamento cambia in funzione degli standard Guber e dei gate tecnici.

### 14. Le alternative restano aperte; cambiano le informazioni necessarie

- **Continuità:** scenario attuale.
- **Trasferimento del primario:** Azure, AWS o on-premise.
- **Accesso dati senza migrazione del primario:** replica on-premise o Azure.

Da validare: motore e sizing, standard cloud, capacità on-premise, SLA/RPO/RTO, connettività, licensing e modello operativo.

## Appendice

### A1. Evidenze, deduzioni e dati mancanti

Separare fatti confermati, deduzioni dichiarate e informazioni mancanti.

### A2. Assunzioni economiche e formula TCO

Carico di riferimento, esclusioni e sensibilità.

### A3–A8. Dettaglio costi dei sei scenari

Una slide per scenario con componenti una tantum, ricorrenti e principali variabili.

### A9. Sicurezza e ownership delle chiavi

Account, chiavi, accessi delegati, audit, backup e segregazione.

### A10. Storage documentale

S3, Azure Storage o object storage on-premise come alternative dipendenti dal requisito reale.

### A11. Orchestratore e dipendenza dalla rete

DB-only, phased o full-stack; evitare un target permanentemente fragile sulla WAN.

### A12. PaaS o IaaS è un gate di compatibilità

Servizio gestito se compatibile; VM/EC2 se necessario, con maggiore onere operativo.

### A13. RACI sintetica del run

Confronto AM Novigo end-to-end vs Guber/terza parte.

### A14. Percorso indicativo di approfondimento

Assessment, modello economico, prova tecnica e piano di migrazione — senza trasformarlo in un obiettivo immediato.


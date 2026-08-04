# NOVA Guber — executive storyline

## Corpo principale

### 1. Cover

**NOVA — alternative infrastrutturali e modelli operativi**

Confronto preliminare per Guber · 31 luglio 2026

### 2. Il perimetro: una base dati comune per NOVA e le possibili automazioni

- **Contesto:** Novigo ha sviluppato NOVA, soluzione per la gestione dei portafogli NPL realizzata con OutSystems. Il database è oggi collocato nell'ambiente OutSystems.
- **Contesto evolutivo:** parallelamente, Novigo sta razionalizzando alcuni processi Guber; questa attività potrebbe portare a nuove automazioni che potrebbero utilizzare lo stesso patrimonio dati di NOVA, condividendo almeno la stessa istanza database anche con schemi distinti.
- **Esigenza:** individuare collocazione e modello di gestione del database più adatti a garantire accesso SQL governato, continuità operativa, sicurezza, tracciabilità e supporto alle possibili evoluzioni.
- **Obiettivo:** rendere confrontabili sei alternative di collocazione e gestione, senza anticipare la scelta.

Nota di grounding: le automazioni e il riuso della stessa istanza sono possibilità architetturali da valutare, non decisioni già assunte.

### 3. Oggi NOVA e il database risiedono nell'ambiente OutSystems

- NOVA gestisce i portafogli NPL ed è realizzato sulla piattaforma OutSystems.
- Il database primario è attualmente collocato nell'ambiente OutSystems e supporta l'operatività applicativa.
- La razionalizzazione dei processi Guber può generare automazioni con esigenze dati coerenti con quelle di NOVA.
- La futura architettura deve valutare se condividere la stessa istanza database, mantenendo eventualmente schemi separati e responsabilità chiare.
- Guber richiede inoltre un accesso SQL governato e tracciabile.

Messaggio: la decisione sulla collocazione del database deve tenere insieme l'operatività attuale di NOVA e le possibili evoluzioni derivanti dalla razionalizzazione dei processi Guber.

### 4. Sei alternative separano due scelte: primario e replica

1. mantenere l'infrastruttura attuale;
2. migrare il primario su Azure Guber;
3. migrare il primario su AWS Guber;
4. migrare il primario on-premise Guber;
5. mantenere il primario e creare una replica on-premise Guber;
6. mantenere il primario e creare una replica su Azure Guber.

Messaggio: le alternative coprono sia il trasferimento della piattaforma sia il solo requisito di accesso, e devono essere valutate anche rispetto alle possibili automazioni future.

### 5. Scenario 1 — continuità sull'infrastruttura attuale

**Profilo:** cambiamento minimo e tempi più rapidi.

- Pro: rischio di migrazione contenuto; continuità operativa; alta reversibilità.
- Attenzioni: ownership Guber limitata; accesso SQL da segregare; dipendenza dall'ambiente corrente.
- Gate: schema/vista read-only, audit, capacità e SLA.
- TCO piattaforma 3 anni: **€ 40k–124k**.

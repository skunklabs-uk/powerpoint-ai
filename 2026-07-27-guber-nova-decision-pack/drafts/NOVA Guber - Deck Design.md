# NOVA Guber — Deck Design

**Stato:** design approvato in conversazione, da revisionare prima della produzione  
**Data:** 27 luglio 2026  
**Audience:** C-level Guber  
**Output:** PowerPoint modificabile  
**Fonte primaria:** `../NOVA_Guber_Decision_Pack_31-07-2026.md`

## 1. Obiettivo

Presentare in modo neutrale e confrontabile le alternative di collocazione del database NOVA e i relativi modelli operativi.

Il deck non deve:

- raccomandare uno scenario;
- chiedere una decisione, una shortlist o un'approvazione immediata;
- presentare i range economici come preventivi;
- confondere ownership dell'infrastruttura e gestione operativa.

Il risultato atteso è una comprensione condivisa delle alternative, dei trade-off e delle condizioni che influenzano costi, rischio e time-to-value.

## 2. Scenari confermati

1. Permanenza sull'infrastruttura attuale.
2. Migrazione su Azure Guber.
3. Account AWS di proprietà Guber.
4. Migrazione completa on-premise Guber.
5. Database primario attuale con replica read-only on-premise Guber.
6. Database primario attuale con replica read-only su Azure Guber.

Ogni scenario deve ricevere un trattamento paritario. Le sei slide scenario useranno la stessa grammatica:

- schema architetturale essenziale;
- collocazione e ownership;
- modalità di accesso SQL;
- vantaggi;
- limiti e rischi;
- time-to-value qualitativo;
- range TCO a tre anni.

Se il contenuto non entra mantenendo leggibilità C-level, il dettaglio passa in appendice.

## 3. Storyline principale

Il corpo principale è composto da 14 slide.

| # | Sezione | Titolo messaggio | Contenuto e forma visuale |
|---:|---|---|---|
| 1 | Cover | `NOVA — Sei scenari per l'evoluzione dell'architettura` | Cover istituzionale TXT/Novigo; sottotitolo sul confronto tra collocazione, accesso ai dati e gestione operativa. |
| 2 | Contesto / Esigenza / Obiettivi | `Il confronto deve separare collocazione, accesso ai dati e responsabilità operative` | Tre blocchi espliciti: contesto, esigenza, obiettivo informativo. |
| 3 | AS IS | `Il requisito dati può essere soddisfatto senza confondere consultazione e transazionale` | Schema dello stato corrente e del requisito SQL read-only; fatti confermati e principali dati mancanti. |
| 4 | TO BE | `Sei configurazioni combinano in modo diverso ownership, migrazione e accesso SQL` | Mappa sintetica dei sei scenari con assi comuni; nessun ranking. |
| 5 | Scenario 1 | `Restare sull'infrastruttura attuale minimizza la discontinuità` | Scheda scenario standard. |
| 6 | Scenario 2 | `Azure Guber porta ownership e governance nel cloud del cliente` | Scheda scenario standard. |
| 7 | Scenario 3 | `AWS Guber separa ownership dell'account e gestione operativa` | Scheda scenario standard; costi AWS basati su Francoforte `eu-central-1`. |
| 8 | Scenario 4 | `L'on-premise Guber massimizza il controllo ma concentra responsabilità e investimento` | Scheda scenario standard. |
| 9 | Scenario 5 | `La replica on-premise abilita accesso SQL senza migrare il primario` | Scheda scenario standard. |
| 10 | Scenario 6 | `La replica su Azure abilita accesso SQL e governance cloud senza migrare il primario` | Scheda scenario standard. |
| 11 | Modello operativo | `Ownership e gestione sono due scelte distinte` | Confronto AM Novigo end-to-end vs gestione Guber/terza parte; RACI executive. |
| 12 | Economics | `I range TCO rendono confrontabili gli scenari senza simulare un preventivo` | Tabella normalizzata: una tantum, ricorrente, TCO 3 anni; AM separata. |
| 13 | Confronto | `Ogni alternativa sposta il compromesso tra rapidità, controllo, rischio e reversibilità` | Matrice comparativa dei sei scenari, con scala qualitativa coerente. |
| 14 | Sintesi | `Le alternative sono leggibili attraverso pochi trade-off comuni` | Sintesi neutrale per hosting, accesso, run, compatibilità, resilienza e informazioni da validare; nessuna call to action. |

## 4. Appendice

L'appendice conserva il dettaglio necessario senza appesantire il corpo principale:

1. fatti confermati, deduzioni e informazioni mancanti;
2. assunzioni economiche;
3. dettaglio costi scenario 1;
4. dettaglio costi scenario 2;
5. dettaglio costi scenario 3;
6. dettaglio costi scenario 4;
7. dettaglio costi scenario 5;
8. dettaglio costi scenario 6;
9. sicurezza e gestione delle chiavi;
10. storage documentale;
11. orchestratore e scope full-stack;
12. PaaS vs IaaS;
13. RACI Application Maintenance;
14. percorso indicativo di assessment e implementazione.

## 5. Adattamento dello standard aziendale

Le cinque sezioni cardine vengono mantenute con un adattamento coerente con la natura informativa del deck:

- `Contesto / Esigenza / Obiettivi`: slide 2;
- `AS IS`: slide 3;
- `TO BE`: slide 4 e slide 5–11;
- `Piano di lavoro`: appendice, perché non viene richiesto un avvio immediato;
- `Economics`: slide 12 e appendice.

La WBS non entra nel corpo principale. Il percorso di assessment e implementazione viene rappresentato in appendice come vista sintetica dei deliverable, senza trasformarlo in impegno progettuale.

## 6. Regole economiche

- Orizzonte TCO: tre anni.
- Formula: costi una tantum + 36 mesi di costi ricorrenti.
- Application Maintenance separata dai costi di piattaforma.
- Mai sommare AM Novigo e costo completo del team Guber/terza parte.
- Usare range arrotondati e leggibili.
- Evitare precisione artificiale.
- Per AWS usare prezzi ufficiali della regione Francoforte, `eu-central-1`.
- Dichiarare che motore DB, sizing, licenze, SLA, volumi e capacità esistente possono cambiare materialmente i range.

## 7. Direzione visuale

- Formato 16:9.
- Font Poppins.
- Sfondo bianco, testo nero/grigio, accenti teal e azzurro.
- Header TXT/Novigo, numero pagina e barre sottili coerenti con `docs/template.pdf`.
- Molto spazio bianco.
- Tabelle per confronti.
- Checklist o bullet brevi per elenchi.
- Schemi e infografiche per architettura, accesso SQL e responsabilità.
- Oggetti PowerPoint nativi e modificabili.
- Immagini generate soltanto quando un diagramma nativo diventerebbe eccessivamente complesso.
- In caso di placeholder visuale, includere un prompt completo per generazione esterna.

### Reference principali

- `docs/template.pdf` e `docs/template.pptx`;
- `docs/ui/`;
- `2026-06-30-data-pipeline/` per matrici, scenari e confronto neutrale;
- `2026-06-07-cantieri-protetti-ai/` per schemi, architetture, economics e contenimento del dettaglio.

### Libertà creativa

- Cover: Low.
- Contesto / Esigenza / Obiettivi: Low.
- AS IS e mappa scenari: Medium.
- Sei slide scenario: Medium, con struttura identica.
- Modello operativo: Medium.
- Economics: Low.
- Matrice comparativa: Low.
- Sintesi finale: Medium.
- Appendice: Medium.

## 8. Grounding e claim

- Il decision pack è la fonte primaria dei contenuti.
- Le reference visuali non autorizzano il riuso di fatti, importi o claim cliente.
- Le conferme conversazionali riportate nel decision pack restano identificate come tali.
- I range economici sono stime di pianificazione.
- I prezzi AWS devono essere verificati su fonti ufficiali prima della produzione.
- Nessun dettaglio mancante viene ricostruito come fatto.

## 9. Criteri di accettazione

Il deck è accettabile quando:

- i sei scenari sono distinti e trattati in modo paritario;
- il lettore comprende differenze e trade-off senza una raccomandazione implicita;
- ogni slide principale è leggibile in meno di venti secondi;
- economics e AM non contengono doppi conteggi;
- il corpo principale resta entro 14 slide;
- il dettaglio tecnico è confinato in appendice;
- il file è modificabile e coerente con il template TXT/Novigo;
- il package PPTX supera i controlli di integrità;
- sono stati completati `Critic`, `Review` e `Humanize`.

## 10. Rischi residui non bloccanti per la prima versione

- motore e versione del database non confermati;
- sizing, crescita e profilo I/O non confermati;
- ambienti, SLA, RPO e RTO non confermati;
- licenze proprietarie non confermate;
- capacità Azure e on-premise già disponibile non confermata;
- perimetro e prezzo AM non confermati;
- collocazione attuale dettagliata di applicazione e orchestratore non confermata.

Questi punti impediscono un preventivo definitivo, ma non impediscono una prima presentazione comparativa se rimangono espliciti.

# Slide di copertura del processo

## Obiettivo

Aggiungere una sola slide alla presentazione `Data pipeline blueprint v2.pptx` per mostrare, con linguaggio C-level, quanto del processo end-to-end sia copribile dalle due soluzioni in confronto:

- AWS, abbreviazione usata nel deck per lo stack componibile Dagster, dbt, PostgreSQL, object storage e Metabase;
- Qlik, abbreviazione usata nel deck per la piattaforma Qlik + Talend, con storage storico da confermare.

## Esito del grill-with-docs

- **Copertura non equivale a readiness.** La slide confronta la capacità tecnologica di supportare i passaggi; non considera chiusi contratti delle fonti, formule, soglie, test o responsabilità.
- **Nessuna percentuale artificiosa.** Le fonti sostengono che entrambe le alternative possano coprire l'intero processo, ma non permettono di attribuire percentuali quantitative affidabili.
- **Confronto neutrale.** Entrambe mostrano `8/8 passaggi copribili`; cambia il grado di integrazione, configurazione e dipendenza dalla piattaforma.
- **Terminologia precisa.** `AWS` non indica un singolo prodotto; indica lo stack componibile. `Qlik` comprende Qlik Talend Cloud e Qlik Cloud Analytics, oltre a componenti da completare o verificare.
- **Aggregazione executive.** Gli undici passaggi della base funzionale sono raggruppati in otto righe per mantenere la slide leggibile senza eliminare funzioni.

## Messaggio della slide

**Il processo è coperto da entrambe; cambia il livello di integrazione.**

- AWS concentra più lavoro su integrazione, configurazione e gestione dei componenti.
- Qlik concentra più funzioni nella suite, ma storage storico, parti personalizzate e copertura di audit/lineage dipendono dal disegno e dall'edizione disponibile.

## Fonte principale

`../kiron-cdg/ai-runs/2026-07-10-cdg-assessment-v4/07-common-architecture-options.md`, in particolare:

- sezione 2, base funzionale comune;
- sezioni 5 e 6, stack componibile e piattaforma Qlik + Talend;
- sezione 8, confronto;
- sezione 12, fonti, deduzioni e informazioni non verificate.

Fonte di controllo: `01-architecture-assessment.md`, sezioni 3-7.

## Collocazione e visual

- Posizione: dopo `Un modello, due modi per realizzarla` e prima di `Criteri di scelta`.
- Pattern: matrice comparativa a due colonne, coerente con le slide di confronto della v2.
- Libertà creativa: Medium.
- Output: forme, testi e indicatori PowerPoint modificabili; nessun testo rasterizzato.

## Assunzioni usate per procedere

- `8/8 passaggi copribili` indica copertura potenziale della soluzione, non disponibilità immediata o completezza progettuale.
- Gli undici passaggi della fonte sono stati raggruppati in otto aree executive senza eliminarne la sostanza.
- La configurazione AWS rappresenta lo stack già proposto nel deck; la configurazione Qlik comprende Qlik Talend Cloud e Qlik Cloud Analytics.

Queste assunzioni non sono bloccanti per la slide perché sono dichiarate nel messaggio, nella legenda e negli stati `Da completare` / `Da verificare`.

## Critic

- Nessuna delle due soluzioni viene presentata come vincitrice.
- Non sono usate percentuali o punteggi non supportati.
- Il titolo comunica la conclusione senza confondere copertura con readiness.
- I limiti comuni restano visibili: fonti, regole, soglie e responsabilità non sono risolti dalla tecnologia.
- Il termine `AWS` è ricondotto allo stack componibile; `Qlik` è ricondotto alla piattaforma Qlik + Talend.

Esito: nessun problema materiale dopo l'accorciamento del titolo e la semplificazione dei termini più tecnici.

## Review

- Una sola slide aggiunta: il deck passa da 19 a 20 pagine.
- Posizione verificata tra le slide `Un modello, due modi per realizzarla` e `Criteri di scelta`.
- Coerenza visuale verificata su export PDF e contact sheet completa.
- Tutti gli elementi aggiunti sono forme o testi PowerPoint modificabili.
- Package Office Open XML valido: archivio integro, XML leggibili, riferimenti e content type risolti, nessuna estensione negativa.

Esito: superato.

## Humanize

- Titolo ridotto a una frase breve e orientata alla decisione.
- Sostituiti `object storage`, `custom` e altre formule tecniche non necessarie con espressioni italiane più immediate.
- Mantenuti i nomi dei prodotti solo dove servono a distinguere concretamente le due soluzioni.
- Punteggiatura e accenti rivisti senza modificare fatti, limiti o assunzioni.

Esito: superato.

## Domande da porre prima del prossimo approfondimento

- Quali edizioni e licenze Qlik/Talend sono effettivamente disponibili?
- Quale archivio storico deve essere usato nello scenario Qlik?
- Quali connettori sono disponibili per le fonti reali dei progetti?
- Quali regole, soglie, test e responsabilità devono essere approvati prima della progettazione esecutiva?

## Revisione dell'asse di copertura

La revisione approvata separa la modalità di copertura dal grado di certezza.

### Asse principale

- `DIRETTA`: capacità disponibile con i componenti previsti.
- `CONFIGURAZIONE`: richiede parametri, regole o impostazioni.
- `ESTENSIONE`: richiede sviluppo, connettori o integrazioni aggiuntive.
- `NON COPERTO`: funzione esterna al perimetro della soluzione.

### Indicatore separato

L'asterisco `*` indica una capacità da verificare rispetto a edizione, licenza o componente scelto. Non costituisce una quinta modalità di copertura.

### Classificazione applicata

| Processo | AWS | Qlik |
|---|---|---|
| Fonti e acquisizione | Estensione | Diretta |
| Conservazione degli input | Diretta | Estensione* |
| Preparazione e mapping | Diretta | Diretta |
| Regole, allocazioni e calcoli | Estensione | Estensione |
| Qualità e riconciliazione | Configurazione | Configurazione |
| Actual, Forecast e versioni | Estensione | Estensione |
| Reporting e distribuzione | Diretta | Diretta |
| Monitoraggio, audit e lineage | Configurazione | Configurazione* |

Il titolo della slide diventa `Modalità di copertura di ciascuna soluzione`, coerente con l'asse rappresentato.

### Gate finale della revisione

- **Critic:** le quattro modalità sono mutuamente esclusive; l'asterisco non è trattato come uno stato alternativo; non sono introdotti punteggi o percentuali.
- **Review:** la classificazione mantiene la stessa scala per AWS e Qlik e conserva il layout alleggerito dall'utente.
- **Humanize:** etichette brevi, nominali e leggibili; eliminati `Da completare` e `Da verificare` come stati concorrenti.

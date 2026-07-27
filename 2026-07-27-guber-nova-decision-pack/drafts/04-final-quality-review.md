# NOVA Guber — final quality review

## Critic

### Problemi individuati e corretti

1. La prima mappa scenari collocava visivamente lo scenario attuale sotto “spostare il primario”. La tassonomia è stata corretta in:
   - collocazione del primario;
   - primario attuale + replica.
2. La prima matrice usava punteggi 1–5, dando una precisione eccessiva a valutazioni ancora preliminari. È stata convertita in scala qualitativa.
3. Il numero pagina era duplicato dal master. La numerazione aggiunta dal generatore è stata rimossa.
4. I due scenari di replica rischiavano di ricevere differenziali economici inventati. Mantengono lo stesso envelope sorgente, con driver tecnici distinti.

### Stress test C-level

- È chiaro cosa deve essere confrontato: sì, sei alternative distinte.
- È chiaro che la replica è accettata: sì, nelle slide 2, 3, 4, 9 e 10.
- È chiaro che non si sta raccomandando una soluzione: sì, titoli e chiusura mantengono la scelta aperta.
- È chiaro cosa includono i TCO: sì, formula, esclusioni e confidenza sono esplicite.
- È chiaro che AM è trasversale: sì, slide 11 e appendice RACI.
- Un executive può cogliere rapidamente pro, attenzioni e gate: sì, le sei slide scenario hanno struttura identica.

## Review

### Grounding

- Fonte primaria: `NOVA_Guber_Decision_Pack_31-07-2026.md`.
- Sei scenari allineati alle conferme dell'utente.
- AWS verificato su `eu-central-1`.
- Nessun costo, data, impegno o tecnologia aggiuntiva presentata come fatto.
- I due scenari di replica condividono deliberatamente il range sorgente.

### Struttura

- Contesto, Esigenza e Obiettivi: espliciti nella slide 2.
- AS IS: slide 3.
- TO BE / alternative: slide 4 e slide 5–10.
- Piano: adattato intenzionalmente come percorso indicativo in appendice, perché non è richiesto un obiettivo immediato.
- Economics: slide 12 e appendice.
- Modello operativo: slide 11 e appendice RACI.

### Visual

- Formato 16:9.
- Font dichiarato Poppins.
- Palette, logo, master e numerazione ereditati dal template aziendale.
- Contenuti sostanziali editabili: testo, forme, tabelle e matrice.
- Nessuna immagine generata necessaria.
- Nessun placeholder necessario.
- Export PDF completato e contact sheet ispezionato.

### Package

- 29 slide: 14 principali, 1 separatore, 14 di appendice.
- Archivio ZIP integro.
- XML e relazioni interne validi.
- Nessuna estensione negativa.
- Apertura ed export headless con LibreOffice riusciti.

## Humanize

Ultima passata applicata per:

- ridurre ripetizioni tra scenari;
- usare titoli che esprimono il messaggio;
- sostituire tecnicismi non necessari con implicazioni operative;
- mantenere termini tecnici soltanto quando distinguono rischio, costo o governance;
- evitare formule prescrittive e call to action immediate.

## Rischi residui

- Il font Poppins non è installato nell'ambiente di rendering; il PPTX lo dichiara correttamente, ma LibreOffice usa una sostituzione locale. La resa definitiva va verificata su un PC aziendale con Poppins.
- Motore DB, licensing, sizing, SLA, connettività, contratti cloud e capacità on-premise non sono disponibili: i range restano a bassa confidenza.
- La matrice qualitativa è un supporto alla discussione, non uno scoring approvato da Guber.


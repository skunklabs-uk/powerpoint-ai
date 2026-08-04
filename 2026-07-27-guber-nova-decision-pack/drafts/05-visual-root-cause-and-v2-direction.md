# NOVA Guber — root cause e direzione visuale v2

## Root cause

La v1 ha usato `docs/template.pptx` come contenitore, ma ha cancellato le slide esistenti e ricostruito i contenuti su layout vuoti. In questo modo ha preservato tema e master, ma non i pattern compositivi reali.

Problemi conseguenti:

- logo aggiunto sopra elementi già ereditati dal master;
- titoli interni troppo grandi rispetto alle reference;
- uso ripetuto di tre card equivalenti, non presente nei deck indicati;
- scenari costruiti come dashboard anziché schema a sinistra e lettura executive a destra;
- economics formalmente ordinati, ma non nel pattern a card e tabelle leggere delle reference;
- validazione visuale eseguita sul solo deck generato, senza confronto affiancato;
- sottotitoli e caveat di lavorazione trasformati in testo cliente.

## Baseline effettiva

- Cover: `cantieri-protetti-01` e `bernadelli-01`.
- Contesto / Esigenza / Obiettivi: `cantieri-protetti-02` e Data Pipeline slide 2.
- AS IS: `cantieri-protetti-12` e `bernadelli-05`.
- Scenari: `bernadelli-06`, `bernadelli-07` e Data Pipeline slide 5/8.
- Confronto: `bernadelli-08`.
- Economics: `bernadelli-10` e `cantieri-protetti-20`.
- Chiusura: template / `cantieri-protetti-23`.

## Regole v2

- Riutilizzare logo header, wave cover e star footer estratti dal template.
- Titolo interno 17–19 pt; header di sezione piccolo e discreto.
- Preferire strutture asimmetriche: visuale 40–45%, testo 50–55%.
- Usare bordi sottili e sfondi bianchi; limitare le card piene.
- Usare teal e azzurro per parole chiave e linee, non come grandi campiture ripetute.
- Inserire solo messaggi destinati all'audience.
- Spostare assunzioni, caveat e note metodologiche in appendice o note a piè pagina.
- Eliminare frasi come “la scelta resta aperta”, “profilo preliminare” e “da validare” quando sono commenti sul processo e non informazioni.
- Ogni sottotitolo deve spiegare l'implicazione dello scenario, non lo stato di lavorazione del deck.

## Test minimo

Prima della ricostruzione completa verificare tre pattern:

1. cover;
2. Contesto / Esigenza / Obiettivi;
3. scenario singolo con schema a sinistra e contenuti a destra.


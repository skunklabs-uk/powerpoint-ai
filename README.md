# PowerPoint Deck Workflow

Questo repository serve a produrre presentazioni commerciali, business case e deck PMO in PowerPoint, con contenuti fondati sulle fonti e stile coerente con le reference TXT/Novigo.

Usalo quando parti da repository software, appunti, documenti, immagini, transcript, deck sorgenti o template. Il risultato tipico è:

- un brief fondato sulle fonti in Markdown;
- una storyline executive;
- un creative handoff per tool/modelli di generazione slide;
- un `.pptx` finale nella cartella dedicata alla presentazione;
- un eventuale `.pdf` solo quando richiesto.

Ogni artefatto finale deve passare da `Critic`, `Review` e ultima passata `humanize` prima dell'handoff.

## Regole Minime

- Non inventare fatti, costi, date, scope, commitment, benefici, contenuti o informazioni non presenti nelle fonti o non richiesti esplicitamente.
- Se un documento, link o allegato citato non e' raggiungibile, chiedere all'utente di recuperarlo o fornirlo; non ricostruirne il contenuto per inferenza.
- Marca sempre **fatti confermati**, **inferenze**, **stime**, **assunzioni** e **domande aperte**.
- Se procedi usando assunzioni, dichiarale anche nel messaggio all'utente.
- Mantieni le cinque sezioni cardine: `Contesto / Esigenza / Obiettivi`, `AS IS`, `TO BE`, `Piano di lavoro`, `Economics`.
- Nei deck basati su POC o repository software, spiega sempre cosa fa oggi la soluzione, come funziona, cosa produce, quali limiti ha e in cosa può evolvere.
- Usa `docs/ui/` e `docs/template.pptx` come riferimento visuale, non come fonte di contenuti cliente.
- Se `docs/template.pdf` e' disponibile, confronta la fedelta' visuale con il PDF; usa il `.pptx` come sorgente editabile.
- Usa aderenza stretta ai pattern visuali solo per slide marcate `Creative freedom: Low`.

## Struttura Del Repo

| Path | Uso |
|---|---|
| `AGENTS.md` | Regole operative principali |
| `.codex/deck-pipeline.md` | Pipeline end-to-end |
| `skunklabs-uk/codex-skills/projects/powerpoint/` | Fonte unica delle skill riusabili per le fasi del workflow |
| `CONTEXT.md` | Glossario del dominio deck |
| `docs/reference*.md` | Metodo commerciale e storyline standard |
| `docs/ui/` | Reference visuali |
| `docs/template.pptx` | Template/base PowerPoint |
| `template-references/` | Slide reference estratte da `docs/template.pdf` per fedelta' visuale |
| `prompt.repo-analysis-for-deck.md` | Prompt per analizzare repo software |
| `yyyy-mm-dd-<nome-progetto>/` | Materiali, draft, prompt, asset, tentativi e deliverable di una singola presentazione |

## Convenzione Cartelle Presentazione

Ogni presentazione deve stare in una cartella dedicata nella root:

```text
yyyy-mm-dd-<nome-progetto>/
```

Esempio:

```text
2026-06-07-cantieri-protetti-ai/
```

Struttura standard obbligatoria:

```text
yyyy-mm-dd-<nome-progetto>/
  drafts/
  prompts/
  source-materials/
  visual-references/
  generated-assets/
  attempts/
```

Uso previsto:

| Sottocartella | Contenuto |
|---|---|
| `drafts/` | Brief, storyline, creative handoff, visual plan e note testuali di lavoro |
| `prompts/` | Prompt usati per generare, recuperare o passare il lavoro ad altri tool |
| `source-materials/` | Materiali sorgente ricevuti o usati per la presentazione |
| `visual-references/` | Reference visive specifiche della presentazione |
| `generated-assets/` | Asset, script o package generati per quella presentazione |
| `attempts/` | Tentativi, preview, export intermedi e output non finali |

Usare la cartella progetto per tutto ciò che appartiene a una singola presentazione: materiali sorgente, brief, storyline, creative handoff, prompt, reference specifiche, asset generati, preview, `.pptx` e `.pdf`. Lasciare in root solo regole comuni, template comuni, prompt riusabili e cartelle progetto.

## Comandi Rapidi

Usali all'inizio o durante il lavoro, in base alla fase:

```bash
git status --short
find docs/ui -maxdepth 1 -type f | sort
find "<cartella-presentazione>/visual-references" -maxdepth 1 -type f | sort
pdfinfo docs/template.pdf
unzip -l docs/template.pptx | sed -n '1,80p'
unzip -t "<deck>.pptx"
```

Per esportare un PPTX in PDF quando serve una revisione visuale:

```bash
libreoffice --headless --convert-to pdf --outdir /tmp/deck-review "<deck>.pptx"
```

## Workflow Pratico

### 1. Raccogli input e obiettivo

Prima di generare qualunque artefatto, chiarisci:

- progetto o cliente;
- materiali disponibili;
- audience;
- decisione che il deck deve abilitare;
- vincoli commerciali, privacy o tecnici;
- output desiderato: brief, storyline, handoff, PPTX o PDF.

Prompt utile:

```text
Voglio creare una proposta/business case per <progetto>.
Materiali disponibili: <lista>.
Audience: <audience>.
Decisione che il deck deve abilitare: <decisione>.
Usa la pipeline del repo PowerPoint e fammi prima le domande bloccanti.
```

Fermati e chiedi se mancano informazioni critiche su valore, perimetro, economics, date, commitment o claim cliente.

### 2. Analizza le fonti

Se parti da un repository software, usa il prompt dedicato:

```text
Analizza il repository <path_repo> usando prompt.repo-analysis-for-deck.md.
Produci un dossier fondato sulle fonti per proposta commerciale/business case.
Includi contesto, AS IS, TO BE, piano, effort, benefici, economics driver, rischi e domande.
Non creare ancora il PowerPoint.
```

Output atteso:

```text
yyyy-mm-dd-<nome-progetto>/drafts/<Nome progetto> - Repo to Deck Brief.md
```

Il brief deve contenere:

- inventario fonti;
- cosa fa il prodotto/sistema;
- se è una POC: cosa fa oggi, come funziona, cosa produce, limiti ed evoluzione;
- baseline o metriche, se disponibili;
- stime e benefici marcati come tali;
- rischi e domande aperte.

### 3. Crea la storyline executive

Trasforma il brief in una struttura slide-by-slide.

Prompt utile:

```text
Usa <Nome progetto> - Repo to Deck Brief.md per creare una executive storyline.
Mantieni le cinque sezioni cardine.
Usa titoli slide che comunichino il messaggio.
Applica il CEO-readiness check: risultati visibili, sizing, economics, owner, decisioni.
Non generare ancora il PPTX.
```

Output atteso:

```text
yyyy-mm-dd-<nome-progetto>/drafts/<Nome progetto> - Executive Storyline v1.md
```

Controlla che:

- ogni slide abbia un ruolo distinto;
- `Contesto / Esigenza / Obiettivi` sia esplicito;
- per POC/repo software non manchi il ponte `cosa fa / come funziona / cosa produce / limiti / evoluzione`;
- le metriche operative non siano presentate come accuratezza validata;
- economics e benefici non sembrino promesse non supportate.

### 4. Crea il creative handoff

Usa il creative handoff quando il deck verrà generato da altri modelli, tool visuali o designer. Serve a dare contenuto e guardrail senza bloccare la composizione.

Prompt utile:

```text
Crea il creative handoff slide-by-slide per <Nome progetto>.
Per ogni slide includi:
- ruolo narrativo;
- contenuti obbligatori;
- contenuti opzionali;
- cosa non dichiarare;
- fonti;
- guardrail visuali;
- forme visuali possibili;
- Creative freedom: High/Medium/Low.

Usa docs/template.pptx e docs/ui/ come reference visuali, ma non prescrivere layout rigidi salvo slide a bassa libertà.
Se docs/template.pdf e' disponibile, confronta la direzione visuale con il PDF e cita i pattern del template usati.
Non generare ancora il PPTX.
```

Output atteso:

```text
yyyy-mm-dd-<nome-progetto>/drafts/<Nome progetto> - Creative Handoff.md
```

Usa questi livelli:

- `High`: libertà compositiva ampia, purché il messaggio resti corretto.
- `Medium`: restare vicino a una famiglia visuale, ma con layout variabile.
- `Low`: seguire da vicino una reference. Tipico per copertina, `Contesto / Esigenza / Obiettivi`, economics/offerta, chiusura.

Se serve una generazione diretta e molto vincolata, puoi creare anche:

```text
yyyy-mm-dd-<nome-progetto>/drafts/<Nome progetto> - Visual Plan.md
```

### 5. Passa il lavoro ad altri modelli o tool

Quando devi passare il lavoro a modelli o tool esterni, crea un prompt specifico per quello strumento partendo da:

- `<Nome progetto> - Repo to Deck Brief.md`
- `<Nome progetto> - Executive Storyline v1.md`
- `<Nome progetto> - Creative Handoff.md`
- `docs/template.pptx`
- `docs/template.pdf`
- `template-references/`
- reference in `docs/ui/`
- reference specifiche in `yyyy-mm-dd-<nome-progetto>/visual-references/`

Prompt sintetico di base:

```text
Genera un deck PowerPoint pronto per una lettura executive usando:
- <Nome progetto> - Repo to Deck Brief.md
- <Nome progetto> - Executive Storyline v1.md
- <Nome progetto> - Creative Handoff.md
- docs/template.pptx
- docs/template.pdf
- template-references/
- docs/ui/
- yyyy-mm-dd-<nome-progetto>/visual-references/

Rispetta contenuti obbligatori, guardrail e livelli Creative freedom.
Non inventare claim, prezzi, date, commitment, contenuti o informazioni non presenti nelle fonti o non richiesti esplicitamente.
Se una fonte citata non e' raggiungibile, segnalarla come mancante e chiedere all'utente di recuperarla prima di usarne il contenuto.
```

### 6. Genera il PPTX con Codex

Quando vuoi che Codex generi direttamente il deck:

```text
Genera una prima versione PPTX editabile usando:
- <Nome progetto> - Repo to Deck Brief.md
- <Nome progetto> - Executive Storyline v1.md
- <Nome progetto> - Creative Handoff.md

Usa docs/template.pptx e docs/ui/ come baseline visuale.
Salva il file nella cartella della presentazione.
Non sovrascrivere file esistenti.
```

Output atteso:

```text
YYYY_CLIENTE_001 - Cliente - Titolo proposta.pptx
```

Se si aggiunge uno script riusabile, metterlo sotto `scripts/`. Se servono dipendenze Python, usare `uv`.

### 7. Valida il deliverable

Ogni consegna deve passare questi tre step, in ordine:

1. `Critic`: cerca contenuti mancanti, assunzioni nascoste, passaggi deboli, claim non supportati e punti poco chiari per CEO/CTO.
2. `Review`: applica la qualità del processo con `commercial-deck-quality-review` e, per PPTX, `pptx-package-validation`.
3. `humanize`: ultima passata sui testi per renderli naturali e leggibili senza cambiare fatti, fonti o vincoli.

Per PPTX, almeno:

```bash
unzip -t "<deck>.pptx"
```

Quando utile:

```bash
libreoffice --headless --convert-to pdf --outdir /tmp/deck-review "<deck>.pptx"
```

Checklist:

- sezioni cardine presenti;
- `Contesto / Esigenza / Obiettivi` esplicito;
- POC/repo software spiegato prima di roadmap/economics;
- fonti e assunzioni visibili;
- economics senza prezzi se non autorizzati;
- baseline non spacciata per accuratezza;
- guardrail visuali rispettati;
- package PPTX integro;
- testi leggibili e non meccanici.

### 8. Handoff finale

Il messaggio finale deve includere:

- path degli output;
- principali decisioni contenutistiche;
- assunzioni rimaste;
- domande aperte;
- verifiche eseguite;
- rischi residui o controlli manuali PowerPoint.

## Prompt Completo Per Un Nuovo Deck Da Repository

```text
Voglio creare una presentazione business case/proposta commerciale a partire da questo repository:
<path_repo>

Obiettivo business:
<obiettivo>

Audience:
<audience>

Cliente/sponsor:
<cliente o sponsor, se noto>

Vincoli:
<vincoli privacy, economici, tecnici, commerciali>

Usa il workflow di questo repo PowerPoint:
1. leggi AGENTS.md, .codex/deck-pipeline.md, CONTEXT.md, docs/reference*.md;
2. usa prompt.repo-analysis-for-deck.md;
3. crea prima il Repo to Deck Brief;
4. poi crea Executive Storyline;
5. poi Creative Handoff;
6. aspetta approvazione prima di generare il PPTX.

Non inventare dati, costi, date, benefici, commitment, contenuti o informazioni non presenti nelle fonti o non richiesti esplicitamente.
Se un documento necessario non e' raggiungibile, chiedere all'utente di recuperarlo o fornirlo; non sostituirlo con contenuto plausibile.
Se usi assunzioni per procedere, dichiarale nella risposta prima di generare l'artefatto.
Se mancano informazioni critiche, chiedi.
```

## Convenzioni Nome File

Working draft:

```text
yyyy-mm-dd-<nome-progetto>/drafts/<Nome progetto> - Repo to Deck Brief.md
yyyy-mm-dd-<nome-progetto>/drafts/<Nome progetto> - Executive Storyline v1.md
yyyy-mm-dd-<nome-progetto>/drafts/<Nome progetto> - Creative Handoff.md
yyyy-mm-dd-<nome-progetto>/drafts/<Nome progetto> - Visual Plan.md, solo per generazione diretta vincolata
```

Deliverable finali:

```text
yyyy-mm-dd-<nome-progetto>/2026_CLIENTE_001 - Cliente - Titolo proposta.pptx
yyyy-mm-dd-<nome-progetto>/2026_CLIENTE_001 - Cliente - Titolo proposta.pdf
```

## Note Operative

- Ogni presentazione e i suoi deliverable finali vanno nella cartella `yyyy-mm-dd-<nome-progetto>/`.
- `docs/ui/` non deve contenere output generati.
- Le reference specifiche di una presentazione vanno in `yyyy-mm-dd-<nome-progetto>/visual-references/`.
- `docs/template.pptx` non va sovrascritto.
- Non installare dipendenze se non servono davvero.
- Non usare reference visuali come fonte di fatti cliente.
- Non usare GitNexus per questo repo, salvo introduzione futura di codice riusabile complesso.

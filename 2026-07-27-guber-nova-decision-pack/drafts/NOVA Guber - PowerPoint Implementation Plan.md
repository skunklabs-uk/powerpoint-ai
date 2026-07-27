# NOVA Guber PowerPoint Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use `superpowers:executing-plans` to implement this plan task-by-task. Subagent execution is intentionally not required because content, layout, economics and validation share the same source contract and integration sequence.

**Goal:** produrre un PowerPoint modificabile, executive-ready e conforme allo standard TXT/Novigo che presenti in modo neutrale sei scenari infrastrutturali NOVA.

**Architecture:** il decision pack resta la fonte contenutistica primaria. Tre artifact Markdown separano economics, storyline e direzione creativa; un generatore Python basato su `python-pptx` costruisce il deck usando `docs/template.pptx` come baseline. Un validatore indipendente controlla package OOXML, relazioni, content type e geometrie prima della review visuale.

**Tech Stack:** Python 3.12, `python-pptx` 1.0.2, `uv`, Office Open XML, LibreOffice headless, Poppler, ImageMagick.

## Global Constraints

- Audience: C-level Guber.
- Lingua: italiano.
- Output finale: solo `.pptx` modificabile.
- Corpo principale: 14 slide.
- Appendice: dettaglio tecnico ed economico.
- Scenari: sei, distinti e trattati in modo paritario.
- Posizionamento: neutrale; nessuna raccomandazione o richiesta di decisione immediata.
- TCO: range a tre anni, con costi una tantum e 36 mesi di costi ricorrenti.
- Application Maintenance: separata dai costi di piattaforma; nessun doppio conteggio.
- AWS: prezzi ufficiali della regione Francoforte `eu-central-1`.
- Visual: 16:9, Poppins, palette TXT/Novigo, header/footer e asset del template.
- Editabilità: testo, tabelle, diagrammi e connettori PowerPoint nativi.
- Fallback visuale: se una composizione nativa non raggiunge una resa coerente con stile e layout aziendali, è accettabile usare un'immagine dedicata oppure inserire un placeholder PowerPoint con il prompt completo per generarla.
- Le immagini di fallback non devono rasterizzare testi, tabelle o dati che devono restare modificabili.
- Non sovrascrivere il decision pack, `docs/template.pptx` o altri deck esistenti.
- File finale: `2026-07-27-guber-nova-decision-pack/2026_GUBER_001 - Guber - NOVA Scenari infrastrutturali.pptx`.

---

## File Map

| File | Responsabilità |
|---|---|
| `2026-07-27-guber-nova-decision-pack/drafts/01-economics-source-note.md` | Fonti ufficiali, parametri e range economici normalizzati. |
| `2026-07-27-guber-nova-decision-pack/drafts/02-executive-storyline.md` | Messaggio, contenuto, fonti e assunzioni slide-by-slide. |
| `2026-07-27-guber-nova-decision-pack/drafts/03-creative-handoff.md` | Pattern visuali, densità, reference e libertà creativa per ogni slide. |
| `2026-07-27-guber-nova-decision-pack/prompts/visual-placeholder-prompts.md` | Prompt completi per gli asset visuali non prodotti direttamente o sostituiti da placeholder. |
| `2026-07-27-guber-nova-decision-pack/generated-assets/build_nova_guber_deck.py` | Generazione deterministica del PPTX editabile dal template. |
| `2026-07-27-guber-nova-decision-pack/generated-assets/validate_nova_guber_pptx.py` | Validazione indipendente del package OOXML. |
| `2026-07-27-guber-nova-decision-pack/attempts/NOVA Guber v0.1.pdf` | Export temporaneo per review visuale. |
| `2026-07-27-guber-nova-decision-pack/attempts/NOVA Guber v0.1 - contact-sheet.png` | Vista completa del deck per Critic e Review. |
| `2026-07-27-guber-nova-decision-pack/drafts/04-final-review.md` | Critic, Review, Humanize, verifiche e rischi residui. |
| `2026-07-27-guber-nova-decision-pack/2026_GUBER_001 - Guber - NOVA Scenari infrastrutturali.pptx` | Deliverable finale. |

---

### Task 1: Verificare economics e fonti AWS Francoforte

**Files:**
- Read: `2026-07-27-guber-nova-decision-pack/NOVA_Guber_Decision_Pack_31-07-2026.md`
- Create: `2026-07-27-guber-nova-decision-pack/drafts/01-economics-source-note.md`

**Interfaces:**
- Consumes: assunzioni di carico e range riportati nel decision pack.
- Produces: tabella normalizzata `scenario_cost_ranges` con `one_off`, `monthly_platform`, `tco_36m`, `exclusions`, `confidence`, usata da storyline e generatore.

- [ ] **Step 1: recuperare documentazione corrente**

Usare Context7 con la domanda completa relativa ad AWS Price List, Amazon RDS/EC2/S3 e regione `eu-central-1`. Usare soltanto documentazione ufficiale AWS per sintassi e significato delle dimensioni di prezzo.

- [ ] **Step 2: scaricare i listini ufficiali regionali**

```bash
mkdir -p /tmp/nova-guber-pricing
curl -fsSL https://pricing.us-east-1.amazonaws.com/offers/v1.0/aws/AmazonRDS/current/eu-central-1/index.json -o /tmp/nova-guber-pricing/rds-eu-central-1.json
curl -fsSL https://pricing.us-east-1.amazonaws.com/offers/v1.0/aws/AmazonEC2/current/eu-central-1/index.json -o /tmp/nova-guber-pricing/ec2-eu-central-1.json
curl -fsSL https://pricing.us-east-1.amazonaws.com/offers/v1.0/aws/AmazonS3/current/eu-central-1/index.json -o /tmp/nova-guber-pricing/s3-eu-central-1.json
```

Expected: tre JSON non vuoti con `formatVersion`, `products` e `terms`.

- [ ] **Step 3: verificare regione e data dei listini**

```bash
jq '{publicationDate, offerCode, version}' /tmp/nova-guber-pricing/rds-eu-central-1.json
jq '{publicationDate, offerCode, version}' /tmp/nova-guber-pricing/ec2-eu-central-1.json
jq '{publicationDate, offerCode, version}' /tmp/nova-guber-pricing/s3-eu-central-1.json
```

Expected: `offerCode` coerente con il servizio e `publicationDate` valorizzata.

- [ ] **Step 4: costruire la nota economica**

Creare `01-economics-source-note.md` con:

- data di verifica;
- URL ufficiali;
- assunzioni del decision pack: 4–8 vCPU, 16–32 GB RAM, 500 GB DB, 20% crescita annua, non-prod al 50%, 1 TB documenti;
- range originali per i sei scenari;
- per AWS, range ricalibrato su `eu-central-1`;
- formula `TCO 3 anni = una tantum + 36 × piattaforma mensile`;
- esclusioni: AM, licenze non note, DR geografico, IVA, team sostitutivo;
- confidenza `bassa` finché motore DB, sizing e licenze non sono confermati.

- [ ] **Step 5: verificare coerenza matematica**

Per ogni scenario verificare:

```text
tco_min = one_off_min + 36 * monthly_min
tco_max = one_off_max + 36 * monthly_max
```

Le cifre esposte nel deck devono essere arrotondate alle migliaia di euro.

- [ ] **Step 6: checkpoint**

```bash
rg -n 'preventivo|eu-central-1|36|Application Maintenance|licenze|confidenza' \
  2026-07-27-guber-nova-decision-pack/drafts/01-economics-source-note.md
```

Expected: tutte le cautele economiche risultano presenti.

---

### Task 2: Creare la storyline executive source-mapped

**Files:**
- Read: `2026-07-27-guber-nova-decision-pack/drafts/NOVA Guber - Deck Design.md`
- Read: `2026-07-27-guber-nova-decision-pack/drafts/01-economics-source-note.md`
- Create: `2026-07-27-guber-nova-decision-pack/drafts/02-executive-storyline.md`

**Interfaces:**
- Consumes: design approvato e `scenario_cost_ranges`.
- Produces: contratto contenutistico per tutte le slide con chiavi `slide`, `section`, `message`, `body`, `visual`, `source`, `assumptions`, `must_not_claim`.

- [ ] **Step 1: scrivere le 14 slide principali**

Usare la sequenza approvata:

1. cover;
2. Contesto / Esigenza / Obiettivi;
3. AS IS e requisito SQL;
4. mappa dei sei scenari;
5–10. una slide per scenario;
11. modello operativo;
12. economics;
13. matrice comparativa;
14. sintesi neutrale.

- [ ] **Step 2: applicare il limite di densità**

Per ogni slide:

- un solo messaggio guida;
- massimo 3–5 elementi testuali principali;
- massimo 65 parole nel corpo, esclusi header, label e note;
- titoli orientati all'implicazione;
- dettaglio eccedente spostato in appendice.

- [ ] **Step 3: scrivere l'appendice**

Includere 14 slide appendix:

1. evidenze e dati mancanti;
2. assunzioni economics;
3–8. dettaglio costi dei sei scenari;
9. sicurezza e chiavi;
10. storage;
11. orchestratore;
12. PaaS vs IaaS;
13. RACI AM;
14. percorso indicativo.

- [ ] **Step 4: verificare grounding**

Ogni slide deve citare una sezione del decision pack o `01-economics-source-note.md`. Nessuna slide può usare le reference visuali come fonte di fatti.

- [ ] **Step 5: eseguire Critic contenutistico**

Controllare:

- neutralità reale tra i sei scenari;
- assenza di raccomandazioni implicite;
- separazione tra migrazione completa e replica;
- assenza di doppio conteggio AM;
- adattamento esplicito della sezione Piano di lavoro in appendice.

- [ ] **Step 6: checkpoint**

```bash
rg -n '^## Slide|Source basis|Assunzioni|Non deve dichiarare' \
  2026-07-27-guber-nova-decision-pack/drafts/02-executive-storyline.md
```

Expected: 28 slide brief completi e source-mapped.

---

### Task 3: Creare il creative handoff

**Files:**
- Read: `docs/template.pdf`
- Read: `docs/template.pptx`
- Read: `docs/ui/README.md`
- Read: `2026-07-27-guber-nova-decision-pack/drafts/02-executive-storyline.md`
- Create: `2026-07-27-guber-nova-decision-pack/drafts/03-creative-handoff.md`

**Interfaces:**
- Consumes: contratto contenutistico slide-by-slide.
- Produces: `slide_visual_contracts` con `pattern`, `freedom`, `density`, `reference`, `editable_objects`, `visual_fallback`.

- [ ] **Step 1: mappare i pattern**

Usare:

- cover: `template-01-cover.png`;
- contesto: `docs/ui/bernadelli-02-contesto-esigenza-obiettivi.png`;
- scenari: famiglia `bernadelli-06/07/09` e Data Pipeline Blueprint;
- economics: `bernadelli-10-costi-simulazione-lungo-periodo.png`;
- confronto: `bernadelli-08-confronto-soluzioni.png`;
- sintesi: pattern decision/discussion del Data Pipeline Blueprint;
- appendix: card, tabelle e roadmap del template.

- [ ] **Step 2: definire la slide scenario standard**

Griglia:

- sinistra 45%: schema architetturale;
- destra alta: vantaggi e limiti;
- destra bassa: rischio, time-to-value e TCO;
- footer: disclaimer sintetico.

Tutte le sei slide devono usare geometria, ordine e label identici.

- [ ] **Step 3: definire libertà creativa**

- Low: cover, contesto, economics, matrice.
- Medium: AS IS, scenari, AM, sintesi, appendix.
- Nessuna slide High nel primo build: la comparabilità richiede disciplina formale.

- [ ] **Step 4: definire regole di editabilità**

Testo, tabelle, card, diagrammi, frecce e badge devono essere oggetti PowerPoint. Usare immagini solo per logo e decorazioni estratte dal template.

- [ ] **Step 5: definire il fallback visuale**

Per ogni slide con un diagramma potenzialmente complesso, il creative handoff deve indicare:

- `visual_fallback: none` quando la resa nativa è adeguata;
- `visual_fallback: generated-image` quando un asset bitmap migliora materialmente chiarezza e fedeltà;
- `visual_fallback: prompt-placeholder` quando l'immagine non viene prodotta nella sessione.

Il fallback è ammesso solo se la prima resa nativa non rispetta stile, gerarchia o layout TXT/Novigo. L'immagine deve contenere elementi visuali, non testo di contenuto, tabelle o economics.

- [ ] **Step 6: checkpoint**

```bash
rg -n 'Creative freedom|Reference|Editable|Scenario|visual_fallback' \
  2026-07-27-guber-nova-decision-pack/drafts/03-creative-handoff.md
```

Expected: mapping completo per 28 slide.

---

### Task 4: Implementare il generatore PowerPoint

**Files:**
- Create: `2026-07-27-guber-nova-decision-pack/generated-assets/build_nova_guber_deck.py`
- Read: `docs/template.pptx`
- Read: `2026-07-27-guber-nova-decision-pack/drafts/02-executive-storyline.md`
- Read: `2026-07-27-guber-nova-decision-pack/drafts/03-creative-handoff.md`
- Create: `2026-07-27-guber-nova-decision-pack/2026_GUBER_001 - Guber - NOVA Scenari infrastrutturali.pptx`

**Interfaces:**
- Consumes: storyline e visual contracts.
- Produces: `.pptx` 16:9 con 28 slide e oggetti editabili.
- Public functions:
  - `load_template() -> Presentation`
  - `add_cover(prs: Presentation) -> None`
  - `add_context_slide(prs: Presentation, number: int) -> None`
  - `add_scenario_map(prs: Presentation, number: int) -> None`
  - `add_scenario_slide(prs: Presentation, scenario: ScenarioSpec, number: int) -> None`
  - `add_economics_slide(prs: Presentation, ranges: list[CostRange], number: int) -> None`
  - `add_comparison_slide(prs: Presentation, scenarios: list[ScenarioSpec], number: int) -> None`
  - `add_appendix_slides(prs: Presentation) -> None`
  - `build(output_path: Path) -> None`

- [ ] **Step 1: definire i contratti dati**

Nel generatore definire:

```python
@dataclass(frozen=True)
class CostRange:
    one_off: str
    monthly: str
    tco_36m: str

@dataclass(frozen=True)
class ScenarioSpec:
    number: int
    name: str
    message: str
    architecture_nodes: tuple[str, ...]
    advantages: tuple[str, ...]
    limits: tuple[str, ...]
    risk: str
    time_to_value: str
    costs: CostRange
```

- [ ] **Step 2: caricare e proteggere il template**

`load_template()` deve aprire `docs/template.pptx`, estrarre logo e asset autorizzati, eliminare soltanto le slide dalla copia in memoria e conservare tema, master e layout. Il file sorgente non deve essere modificato.

- [ ] **Step 3: implementare primitive visuali**

Implementare:

- `add_header`;
- `add_message_title`;
- `add_text`;
- `add_bullet_list`;
- `add_card`;
- `add_badge`;
- `add_connector`;
- `add_architecture_node`;
- `add_footer_disclaimer`;
- `add_native_table`;
- `add_visual_placeholder`.

Tutte le primitive devono usare Poppins, palette del template e coordinate in centimetri.

`add_visual_placeholder` deve creare un riquadro PowerPoint coerente con il template, mostrare un identificativo breve del prompt e mantenere titolo, messaggio e dati della slide come oggetti nativi.

- [ ] **Step 4: implementare le slide principali**

Generare esattamente 14 slide secondo `02-executive-storyline.md`. Le sei slide scenario devono chiamare la stessa funzione `add_scenario_slide`.

- [ ] **Step 5: implementare l'appendice**

Generare le 14 slide appendix con tabelle e card native. Le tabelle costi devono riportare `Range di pianificazione — non preventivo`.

- [ ] **Step 6: aggiungere controlli pre-save**

Prima di salvare:

```python
assert len(prs.slides) == 28
assert prs.slide_width == 12192000
assert prs.slide_height == 6858000
```

Verificare inoltre che tutti i titoli attesi siano presenti e che nessuna stringa contenga `TBD` o `TODO`.

- [ ] **Step 7: generare il deck**

```bash
uv run python 2026-07-27-guber-nova-decision-pack/generated-assets/build_nova_guber_deck.py
```

Expected: file finale creato senza sovrascrivere sorgenti.

- [ ] **Step 8: checkpoint**

```bash
unzip -t '2026-07-27-guber-nova-decision-pack/2026_GUBER_001 - Guber - NOVA Scenari infrastrutturali.pptx'
```

Expected: `No errors detected`.

---

### Task 5: Implementare e usare il validatore OOXML

**Files:**
- Create: `2026-07-27-guber-nova-decision-pack/generated-assets/validate_nova_guber_pptx.py`
- Test: `2026-07-27-guber-nova-decision-pack/2026_GUBER_001 - Guber - NOVA Scenari infrastrutturali.pptx`

**Interfaces:**
- Consumes: path del PPTX.
- Produces: exit code `0` e report JSON su stdout quando tutti i controlli passano.

- [ ] **Step 1: implementare i controlli**

Il validatore deve:

- aprire il file come ZIP;
- parsare ogni XML;
- verificare gli override di `[Content_Types].xml`;
- risolvere ogni relazione interna `.rels`;
- verificare la presenza degli asset media;
- cercare estensioni negative;
- contare 28 slide;
- verificare formato 16:9;
- verificare assenza di `TBD`, `TODO` e marcatori di debug.

- [ ] **Step 2: eseguire il validatore**

```bash
uv run python 2026-07-27-guber-nova-decision-pack/generated-assets/validate_nova_guber_pptx.py \
  '2026-07-27-guber-nova-decision-pack/2026_GUBER_001 - Guber - NOVA Scenari infrastrutturali.pptx'
```

Expected:

```json
{"result":"pass","slides":28,"xml_errors":0,"missing_targets":0,"negative_extents":0}
```

---

### Task 6: Review visuale e correzione

**Files:**
- Create: `2026-07-27-guber-nova-decision-pack/attempts/NOVA Guber v0.1.pdf`
- Create: `2026-07-27-guber-nova-decision-pack/attempts/NOVA Guber v0.1 - contact-sheet.png`
- Modify: `2026-07-27-guber-nova-decision-pack/generated-assets/build_nova_guber_deck.py`
- Regenerate: final `.pptx`

**Interfaces:**
- Consumes: prima generazione validata.
- Produces: deck corretto dopo review visuale completa.

- [ ] **Step 1: esportare in PDF**

```bash
libreoffice --headless --convert-to pdf \
  --outdir 2026-07-27-guber-nova-decision-pack/attempts \
  '2026-07-27-guber-nova-decision-pack/2026_GUBER_001 - Guber - NOVA Scenari infrastrutturali.pptx'
```

Rinominare l'export in `NOVA Guber v0.1.pdf`.

- [ ] **Step 2: generare preview**

```bash
mkdir -p /tmp/nova-guber-preview
pdftoppm -png -r 96 \
  '2026-07-27-guber-nova-decision-pack/attempts/NOVA Guber v0.1.pdf' \
  /tmp/nova-guber-preview/slide
montage /tmp/nova-guber-preview/slide-*.png \
  -thumbnail 480x270 -tile 2x -geometry +12+12 \
  '2026-07-27-guber-nova-decision-pack/attempts/NOVA Guber v0.1 - contact-sheet.png'
```

- [ ] **Step 3: ispezionare**

Controllare contact sheet e singole slide chiave:

- slide 2;
- slide 4;
- slide 5–10;
- slide 12;
- slide 13;
- slide 14;
- appendix economics.

Verificare leggibilità, overflow, allineamenti, equilibrio, neutralità visiva e somiglianza con il template.

- [ ] **Step 4: applicare il fallback visuale quando necessario**

Se una slide non raggiunge una resa conforme dopo la prima correzione nativa:

1. preferire un'immagine generata e salvata sotto `generated-assets/`;
2. se l'immagine non viene generata, inserire un placeholder PowerPoint;
3. registrare il prompt completo in `prompts/visual-placeholder-prompts.md`.

Ogni prompt deve specificare:

- ruolo dell'immagine nella slide;
- composizione e soggetto;
- stile corporate TXT/Novigo;
- palette bianco, teal e azzurro;
- rapporto e area utile;
- assenza di testo incorporato, loghi inventati e dettagli cliente non autorizzati;
- elementi da evitare;
- nome del file atteso.

- [ ] **Step 5: correggere**

Correggere nel generatore, non direttamente nel PPTX:

- testi oltre 65 parole;
- font sotto 10 pt nel corpo principale;
- box sovrapposti;
- scenari con densità o enfasi diversa;
- tabelle illeggibili;
- disclaimer economici poco visibili.

- [ ] **Step 6: rigenerare e rivalidare**

Ripetere Task 4 Step 7 e Task 5 Step 2.

---

### Task 7: Critic, Review, Humanize e handoff

**Files:**
- Create: `2026-07-27-guber-nova-decision-pack/drafts/04-final-review.md`
- Final: `2026-07-27-guber-nova-decision-pack/2026_GUBER_001 - Guber - NOVA Scenari infrastrutturali.pptx`

**Interfaces:**
- Consumes: deck corretto e validato.
- Produces: review finale con risultato, evidenze e rischi residui.

- [ ] **Step 1: Critic**

Registrare solo problemi capaci di cambiare la lettura:

- scenario favorito implicitamente;
- costi presentati come certi;
- confusione tra ownership e AM;
- confusione tra migrazione e replica;
- conclusione che richiede una decisione non autorizzata.

- [ ] **Step 2: Review**

Verificare:

- cinque sezioni cardine o adattamento dichiarato;
- sei scenari;
- grounding;
- C-level readability;
- coerenza visuale;
- economics;
- package integrity;
- posizione e filename.

- [ ] **Step 3: Humanize**

Rileggere titoli e testi per eliminare:

- ripetizioni;
- nominalizzazioni pesanti;
- gergo non necessario;
- formule meccaniche;
- claim assoluti.

- [ ] **Step 4: rigenerare se necessario**

Ogni correzione testuale o visuale deve essere applicata al generatore, seguita da build e validazione completa.

- [ ] **Step 5: verifica finale**

```bash
unzip -t '2026-07-27-guber-nova-decision-pack/2026_GUBER_001 - Guber - NOVA Scenari infrastrutturali.pptx'
uv run python 2026-07-27-guber-nova-decision-pack/generated-assets/validate_nova_guber_pptx.py \
  '2026-07-27-guber-nova-decision-pack/2026_GUBER_001 - Guber - NOVA Scenari infrastrutturali.pptx'
git status --short
```

Expected: package valido, 28 slide, nessun target mancante, nessuna estensione negativa; modifiche limitate alla cartella della presentazione.

## Plan Self-Review

- Copertura design: tutte le sezioni del design hanno un task.
- Dipendenze: nessuna nuova dipendenza; viene riusato `python-pptx`.
- Grounding: contenuti e economics hanno artifact separati e source-mapped.
- Visual: sei scenari condividono una sola funzione e una sola geometria.
- Fallback visuale: immagini e placeholder sono ammessi solo dopo una review negativa della resa nativa e restano collegati a prompt tracciati.
- Validazione: generatore e validatore sono indipendenti.
- Deliverable: il solo output finale richiesto è il `.pptx`; PDF e PNG restano in `attempts/`.
- Placeholder: nessun `TBD` o `TODO` richiesto dall'implementazione.

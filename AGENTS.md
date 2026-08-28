# AGENTS.md

## Agent OS e lifecycle delle skill

- Prima di analizzare, pianificare, modificare o creare issue o pull request, si DEVE leggere integralmente la versione corrente di [RFC-0001 – Principi fondanti della Software Factory](https://github.com/skunklabs-uk/agent-os/blob/main/rfcs/RFC-0001-principles.md).
- Se la fonte non è accessibile, il lavoro DEVE fermarsi.
- Le regole locali possono restringere la RFC, ma non indebolirla; conflitti o deroghe richiedono l'autorizzazione esplicita dell'utente o di una fonte attiva approvata di autorità superiore.
- Il contenuto della RFC non DEVE essere duplicato in questo repository.
- Le skill riusabili hanno una sola sorgente nel [repository codex-skills](https://github.com/skunklabs-uk/codex-skills). Nei progetti vanno installate tramite symlink con `scripts/install-project.sh`, senza copiare o modificare manualmente le directory installate.

## Scopo

Questo repository serve a creare presentazioni commerciali e PMO, preferibilmente in formato PowerPoint.

Codex deve usare il repository come ambiente di produzione per deck:

- `docs/` definisce metodo, storyline e regole contenutistiche.
- `docs/ui/` fornisce riferimenti visivi e di layout.
- ogni presentazione vive in una cartella dedicata nella root del progetto.

## Agent OS / Codex OS

Questo repository adotta Agent OS / COS a livello **A3 Workflow-aware** per la produzione di deck.

Prima di lavori non banali, Codex deve leggere:

- `.codex/adoption.md`
- `.codex/routing.md`
- `.codex/authority.md`
- `.codex/execution.md`
- `.codex/knowledge-map.md`
- `.codex/deck-pipeline.md`
- `CONTEXT.md`

Usare questi file per scegliere route, autorità delle fonti, policy di esecuzione, quality gate e handoff.

Le skill riusabili della pipeline hanno come unica fonte
[`skunklabs-uk/codex-skills/projects/powerpoint`](https://github.com/skunklabs-uk/codex-skills/tree/main/projects/powerpoint):

- `proposal-intake`
- `repo-to-deck-brief`
- `business-case-storyline`
- `software-delivery-estimation`
- `executive-slide-writing`
- `deck-visual-grounding`
- `pptx-template-extraction`
- `powerpoint-manipulation`
- `pptx-package-validation`
- `commercial-deck-quality-review`

Usarle tramite i symlink installati quando sono disponibili e materialmente
utili. La pipeline descritta sotto resta applicabile anche mediante verifica
diretta equivalente; l'assenza di una skill non blocca da sola il lavoro.

Per proposte/business case di sviluppo software, usare una pipeline quality-first:

1. intake e inventario materiali;
2. grounding e gap assessment;
3. storyline sulle cinque sezioni cardine;
4. grounding visuale su `docs/template.pptx`, `docs/ui/` e deck sorgente;
5. manipolazione/produzione PowerPoint editabile;
6. passaggio finale `Critic`;
7. passaggio finale `Review`;
8. ultima passata `humanize`;
9. handoff con assunzioni, verifiche e rischi residui.

Se mancano informazioni critiche su valore, perimetro, economics, impegni, date o contenuti cliente, fermarsi e chiedere chiarimenti. Se mancano dettagli minori, procedere solo marcandoli come assunzioni o punti da validare.

Quando Codex procede usando assunzioni, deve renderlo noto esplicitamente anche nella conversazione, non solo nel documento generato. Il messaggio deve indicare:

- quali assunzioni sono state usate per proseguire;
- perche' non sono state considerate bloccanti;
- quali domande restano da porre prima del passaggio successivo.

Non inserire in un deliverable domande formulate come "approval questions" se non sono state effettivamente poste all'utente. Usare invece una sezione esplicita come "Domande da porre prima del prossimo step" o "Assunzioni usate per procedere".

## Arresto e prosecuzione

Le condizioni di stop e i livelli di conferma definiti in `.codex/execution.md` restano vincolanti per l'azione che li richiede. Il blocco di un deck, una fonte, un'operazione esterna o un passaggio non blocca automaticamente l'intera missione: il lavoro già autorizzato e determinato che non dipende da quella condizione deve proseguire.

Prima di fermarsi, indicare la condizione applicabile, il fatto osservato e la decisione o informazione necessaria.

Quando la fonte attiva o il task corrente identifica già il lavoro successivo necessario nella stessa missione, proseguire senza chiedere una conferma meccanica, salvo che si applichi una condizione di stop reale.

Non usare questa regola per aggirare i livelli E3-E5 di `.codex/execution.md`, le conferme su contenuti cliente o il divieto di inventare informazioni mancanti.

## Lettura Obbligatoria

Prima di creare o modificare una presentazione, leggere i file rilevanti in `docs/`.

Partire sempre da:

- tutti i file `docs/reference*.md`

Rileggere sempre il contenuto aggiornato delle cartelle di riferimento prima di lavorare. Non basarsi su letture precedenti, memoria della sessione o assunzioni su versioni passate, perché `docs/` e `docs/ui/` possono essere aggiornate nel tempo.

Considerare `docs/` come fonte primaria per struttura, metodo e contenuti della presentazione. Non inventare fatti, impegni, costi, date, perimetro progettuale, tecnologie, claim commerciali, esempi, dettagli cliente, dettagli implementativi, contenuti o informazioni che non siano presenti nei materiali sorgente o chiaramente forniti dall'utente.

Se un documento, link, allegato, deck, file SharePoint/Drive/OneDrive o altro materiale citato non e' raggiungibile, non ricostruirne il contenuto per inferenza e non sostituirlo con contenuti plausibili. Segnalarlo all'utente e chiedere di recuperare o fornire il documento, indicando esattamente quale fonte manca e perche' e' necessaria.

## Struttura Per Presentazione

Ogni nuova presentazione deve avere una cartella dedicata nella root del repository, con naming:

```text
yyyy-mm-dd-<nome-progetto>
```

Esempio:

```text
2026-06-07-cantieri-protetti-ai/
```

La cartella della presentazione deve contenere il materiale specifico di quel lavoro:

- sorgenti cliente o di progetto;
- brief, storyline, creative handoff, prompt e piani;
- reference visuali specifiche di quella presentazione;
- asset generati o scaricati per quella presentazione;
- output finali `.pptx` e `.pdf`;
- eventuali tentativi, anteprime o export intermedi quando utili a ricostruire il lavoro.

Ogni cartella presentazione deve usare queste sottocartelle standard:

```text
drafts/
prompts/
source-materials/
visual-references/
generated-assets/
attempts/
```

Uso previsto:

- `drafts/`: brief, storyline, creative handoff, visual plan e note testuali di lavoro;
- `prompts/`: prompt usati per generare, recuperare o passare il lavoro ad altri tool;
- `source-materials/`: materiali sorgente ricevuti o usati per la presentazione;
- `visual-references/`: reference visive specifiche della presentazione;
- `generated-assets/`: asset, script o package generati per quella presentazione;
- `attempts/`: tentativi, preview, export intermedi e output non finali.

La root deve restare l'indice dei progetti e delle regole comuni, non una destinazione per output o working draft di singole presentazioni.

Se un contenuto manca, è ambiguo, non è sufficientemente specificato o dipende da un documento non raggiungibile, chiedere all'utente prima di colmare il vuoto. Fare assunzioni o creare contenuti placeholder solo quando l'utente lo chiede esplicitamente. Quando le assunzioni sono richieste, dichiararle in modo esplicito e facilmente verificabile nel documento e nel messaggio di handoff.

## Storyline Standard

Ogni proposta o business case dovrebbe includere queste cinque sezioni cardine, salvo diversa richiesta esplicita dell'utente:

1. Contesto ed esigenza/obiettivi
2. AS IS
3. TO BE
4. Piano di lavoro
5. Economics

Usare i file `docs/reference*.md` come interpretazione di base di queste sezioni.

La storyline può essere adattata in base a dimensione e complessità del progetto, ma le cinque sezioni cardine non devono sparire senza un motivo chiaro.

La prima sezione cardine **Contesto ed esigenza/obiettivi** deve essere esplicita nel deck e nella storyline. Non basta una slide generica di contesto o pain point: deve risultare chiaro, anche a livello di titolo o struttura interna della slide, quali sono:

- **Contesto:** situazione di partenza e razionale business;
- **Esigenza:** bisogno, criticità, opportunità o trigger che rende utile il progetto;
- **Obiettivi:** cosa il deck/progetto deve abilitare o decidere.

Quando il deck è sintetico, questi tre elementi possono stare in una sola slide, ma non devono sparire o essere impliciti.

Per deck costruiti a partire da una POC, un prototipo o un repository software, la storyline deve includere anche un ponte esplicativo prima di passare a roadmap ed economics. Il deck deve far capire, in linguaggio executive:

- **cosa fa oggi la POC/soluzione:** input gestiti, principali funzioni e output prodotti;
- **come lo fa:** flusso operativo, componenti o logiche chiave, spiegati solo quanto serve a comprenderne valore, rischio e riusabilità;
- **cosa produce di misurabile:** evidenze, metriche, payload, report, dati, diagnostica o risultati osservabili;
- **quali limiti ha oggi:** gap funzionali, operativi, tecnici o di validazione;
- **in cosa può evolvere:** capability target, estensioni applicative, processi/funzioni futuri e business case abilitati.

La sintesi C-level non deve cancellare questo ponte. Può comprimerlo in una o due slide, ma non può lasciare il lettore senza una comprensione concreta dell'oggetto che si propone di finanziare, evolvere o industrializzare.

## Riferimenti Visivi

Usare `docs/ui/` solo come area di riferimento visivo e di layout comune.

Prima di creare o modificare un deck, rileggere sempre il contenuto aggiornato di `docs/ui/`, verificare quali file di riferimento comuni sono disponibili e controllare anche eventuali reference specifiche nella cartella della presentazione.

I file in `docs/ui/` possono includere PDF, immagini esportate da slide, screenshot o altri esempi che mostrano lo stile desiderato della presentazione. Usarli per dedurre:

- formato e proporzioni delle slide
- posizionamento dei titoli
- stile delle slide divisorie
- scala tipografica
- palette colori
- spaziature e griglia
- convenzioni di header e footer
- densità del testo
- trattamento di diagrammi, architetture, processi, tabelle, roadmap ed economics

Non scrivere deliverable generati dentro `docs/ui/`. Le reference visuali specifiche di una presentazione devono stare nella cartella della presentazione, ad esempio in `yyyy-mm-dd-<nome-progetto>/visual-references/`.

Quando si usano deck di riferimento, seguire il loro linguaggio visivo e il sistema di layout. Non copiare contenuti riservati o specifici di un cliente, salvo richiesta esplicita dell'utente.

Se `docs/template.pdf` e' disponibile, usarlo come riferimento visuale primario per la fedelta' grafica, perche' mostra la resa effettiva del template esportato. `docs/template.pptx` resta invece la base editabile da riusare o ispezionare per master, layout e asset PowerPoint.

La generazione visuale deve partire dai pattern effettivamente presenti in `docs/ui/`, non da layout generici. In particolare:

- per la slide iniziale di contenuto usare il pattern `Contesto / Esigenza / Obiettivi` quando disponibile;
- per roadmap e piano usare pattern a fasi/righe coerenti con le reference PMO;
- per economics usare tabelle o card comparabili alle reference economics;
- header, barre decorative, logo, colori, densità e spaziature devono richiamare le reference, salvo motivo esplicito.
- quando `docs/template.pdf` e' presente, confrontare cover, header/footer, card, colonne, roadmap, fascia `Valore generato`, chiusura e densita' del testo con le pagine del PDF prima di approvare la fedelta' visuale.

Se il deck generato si discosta dai pattern disponibili, la deviazione deve essere dichiarata e motivata nel visual plan o nell'handoff.

Quando il materiale viene passato ad altri modelli, tool di generazione slide o designer, preferire un **creative handoff** rispetto a un visual plan rigido. Il creative handoff deve preservare messaggio, contenuti obbligatori, fonti, assunzioni e guardrail visuali, ma lasciare libertà compositiva dove possibile.

Per ogni slide indicare un livello di libertà:

- **High:** il modello può scegliere la composizione visuale, se rispetta messaggio e guardrail.
- **Medium:** deve restare vicino a una famiglia di reference, ma può variare layout.
- **Low:** deve seguire un pattern specifico perché serve coerenza formale o riconoscibilità.

Usare `Low` soprattutto per copertina, `Contesto / Esigenza / Obiettivi`, economics/offerta formale e chiusura istituzionale. Per le altre slide, evitare di prescrivere coordinate, numero esatto di box, frecce o diagrammi se non necessario: indicare invece ruolo narrativo, contenuti obbligatori, alternative visuali ammesse e anti-pattern.

## Regole di Output

Salvare i deliverable finali nella cartella della presentazione, non nella root del progetto.

Output finali preferiti:

- `.pptx` come deliverable primario e modificabile
- `.pdf` come export per revisione o distribuzione, quando richiesto

Export opzionali, solo quando richiesti esplicitamente:

- immagini pagina per pagina, ad esempio `.png`
- asset di anteprima
- screenshot intermedi

Usare nomi file chiari e descrittivi, ad esempio:

- `2026_CLIENTE_001 - Cliente - Titolo proposta.pptx`
- `2026_CLIENTE_001 - Cliente - Titolo proposta.pdf`

Non posizionare output finali generati dentro `docs/`, `docs/ui/` o nella root se appartengono a una presentazione specifica.

## Generazione PowerPoint

Preferire la creazione di file PowerPoint modificabili rispetto a output solo statici.

Quando si implementa una pipeline di generazione, aggiungere una dipendenza solo se serve davvero al task. Se serve generare `.pptx` via script, preferire `pptxgenjs` salvo che il progetto usi già in modo consolidato un altro strumento. Tenere script e logica riutilizzabile fuori da `docs/` e `docs/ui/`, ad esempio sotto `scripts/`. Script e asset usa-e-getta di una singola presentazione possono stare nella cartella della presentazione.

I deck generati dovrebbero rimanere modificabili in PowerPoint quando possibile:

- usare vere caselle di testo invece di immagini con testo rasterizzato
- usare forme PowerPoint per diagrammi semplici e callout
- usare tabelle quando ci si aspetta che siano modificabili
- usare immagini solo per asset che devono rimanere visuali

## Stile dei Contenuti

Scrivere con tono commerciale, chiaro, sintetico e adatto a interlocutori C-level.

Il linguaggio deve essere comprensibile a lettori executive che devono cogliere rapidamente valore di business, impatto operativo, rischi, tempi ed economics. Evitare gergo tecnico non necessario; quando i dettagli tecnici servono, spiegarne la rilevanza business.

Preferire titoli slide che comunichino il messaggio della slide, non etichette generiche. Ad esempio, preferire un titolo che esprima l'implicazione business rispetto a un titolo che dica solo "TO BE" o "Architecture".

Mantenere il testo delle slide breve e leggibile. Evitare di trasformare le slide in documenti densi.

Quando utile, separare:

- contenuti di sintesi executive
- contenuti di dettaglio delivery o implementativi
- assunzioni e punti aperti
- economics e note commerciali

## Checklist Qualità

Prima di considerare una presentazione completa, verificare che:

- le cinque sezioni cardine siano presenti o adattate intenzionalmente
- la sezione `Contesto ed esigenza/obiettivi` sia esplicita, non solo implicita in una slide generica
- per deck basati su POC/repo software, sia chiaro cosa fa oggi la soluzione, come funziona a livello executive, cosa produce, quali limiti ha e in cosa può evolvere
- il deck usi `docs/` come fonte contenutistica e metodologica
- il deck usi `docs/ui/` solo come riferimento layout
- le slide rispettino i guardrail visuali e il livello di libertà creativa dichiarato; aderenza stretta ai pattern `docs/ui/` solo dove richiesta
- i deliverable finali siano salvati nella cartella della presentazione
- le assunzioni siano esplicite
- i titoli slide comunichino il messaggio
- il testo non sia sovraccarico
- diagrammi, tabelle e roadmap siano leggibili
- contenuti riservati provenienti da deck di riferimento non siano stati copiati accidentalmente

## Gate Finale Obbligatorio

Prima di consegnare un deck, una storyline, un creative handoff, un prompt o qualunque artifact testuale destinato a generare slide, eseguire sempre tre passaggi finali:

1. **Critic:** rileggere il lavoro in modo avversariale, cercando contenuti mancanti, assunzioni nascoste, passaggi narrativi deboli, claim non supportati e punti che un CEO/CTO non capirebbe.
2. **Review:** applicare la review qualità del processo, includendo grounding, sezioni cardine, POC narrative bridge, economics, assunzioni, guardrail visuali e completezza del deliverable.
3. **Humanize:** fare l'ultima passata sul testo per renderlo più naturale, leggibile e meno meccanico, senza cambiare fatti, assunzioni, vincoli o fonti.

Se uno dei tre passaggi trova un problema materiale, correggere l'artifact e ripetere almeno il controllo rilevante prima dell'handoff.

## Strumenti e Skill Utili

Usare GitNexus solo se il repository cresce con script, generatori riutilizzabili, template o altro codice di cui è necessario capire relazioni e impatto.

Comandi GitNexus tipici:

```bash
npx gitnexus analyze
npx gitnexus --help
```

Usare Playwright solo quando servono anteprime browser-based o controlli visuali.

Usare image generation solo per asset bitmap come illustrazioni, texture, sfondi o mockup visuali. Non usare immagini generate come sostituto della struttura modificabile in PowerPoint.

Se è disponibile un plugin di verifica o grounding documentale come `grill-with-docs`, usarlo per controllare che il contenuto del deck generato resti fedele a `docs/` e ai materiali sorgente forniti dall'utente.

## Regole di Fedeltà Visuale

Quando si modifica un deck esistente, preferire interventi conservativi:
- riusare master, layout, font, palette, header/footer e loghi del file originale;
- non inventare loghi, immagini, icone o elementi decorativi;
- non deformare o ricreare loghi;
- non cambiare famiglia font se non richiesto;
- non ricostruire da zero slide che possono essere adattate;
- creare nuove slide copiando layout esistenti simili e modificando solo contenuto necessario.

## GitNexus

Non usare GitNexus per questo repository nelle attività ordinarie di produzione, revisione o configurazione dei deck.

Questo repository contiene materiali PowerPoint, documenti di riferimento e immagini UI, non una codebase applicativa.
La review delle presentazioni deve basarsi su:
- `docs/`
- `docs/ui/`
- contenuto estratto dal `.pptx`
- eventuali plugin di grounding documentale come `grill-with-docs`

Usare GitNexus solo se in futuro vengono introdotti script, generatori o codice riutilizzabile da analizzare.

## Closeout terminale RFC-0001

Prima del merge terminale, del commit o push che conclude la missione oppure della chiusura dell'issue, completare il closeout previsto da RFC-0001.

Verificare tutte le fonti autorevoli e i documenti `Active` interessati. Aggiornare quelli che mantengono la stessa funzione; archiviare nella stessa modifica quelli conclusi, superati, sostituiti, obsoleti o non più operativi. Prima dell'archiviazione trasferire fatti, decisioni, limiti, requisiti e obblighi di verifica ancora durevoli nella fonte corrente; rimuovere poi il documento da puntatori, indici, tracker, code di lavoro, sezioni sullo stato corrente e istruzioni operative.

I commenti GitHub forniscono tracciabilità, ma non sostituiscono la documentazione autorevole. Quando un'evidenza runtime è un criterio di accettazione, mantenere la missione aperta e non usare `Closes #N` finché tale evidenza manca. `NON APPLICABILE` richiede una motivazione concreta e verificabile.

Commit e push intermedi restano consentiti; quello terminale deve includere il closeout completato.

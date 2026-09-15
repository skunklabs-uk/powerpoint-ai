# PowerPoint AI — proposta README di adozione

**Stato: Active**

## Incarico

Per [Homelab #1265](https://github.com/skunklabs-uk/homelab/issues/1265), produci soltanto un report italiano con una breve sezione proposta per il README esistente. Non modificare file e non generare presentazioni, storyline, creative handoff, asset o script.

Source `skunklabs-uk/powerpoint-ai@09dabfb8ee041bdd4951cc73f19f29b7b4c9536b`, tree `189f3b8eada423fe00d9fa9ef6ffe4b52fe38de9`. Branch/head dello snapshot saranno indicati nella richiesta verificata e sono distinti dal source. Non ricostruirli tramite rete; il branch senza parent non viene integrato.

Leggi la RFC corrente fornita dal coordinatore e le fonti complete qualificate: AGENTS.md, README.md, CONTEXT.md, le sette policy `.codex/{adoption,routing,authority,execution,knowledge-map,deck-pipeline,governance}.md`. AGENTS, README e CONTEXT sono file esatti nello snapshot. Le sette policy sono fornite integralmente qui sotto come contesto normativo, con percorso e blob della fonte: leggile tutte, senza ricreare `.codex` o trattarle come configurazione eseguibile. Questo trasporto temporaneo non cambia autorità, contenuto o applicabilità delle policy. La normale PR conserva tutti i file originali; al closeout questo prompt viene ritirato.

## Scope

Spiega il percorso documentato di produzione e verifica dei deck e il confine del collegamento senza cambiare regole durature, livelli E0–E6 o approvazioni. Questo è un report informativo E0: non sceglie contenuti o materiali per un cliente. Le letture deck/reference previste per lavori di presentazione non sono necessarie alla nota tecnica.

Non leggere cartelle cliente, template, reference deck, PDF, Office, immagini, materiale confidenziale, .codegraphcontext, configurazioni locali o credenziali. Non recuperare altri ref/oggetti, servizi o URL. Non usare Canva, Drive o API, non installare dipendenze, non aprire GUI e non lanciare altri modelli/consumer.

## Risultato

Restituisci una breve valutazione delle fonti e una sola sezione README proposta che descriva:

- incarico delimitato da repository/thread, branch/head e prompt; input qualificati e consumer seriale;
- report-only, verifica del coordinatore e RETURN distinti da eventuale applicazione della nota nel branch normale e merge;
- conservazione dei livelli di conferma per azioni esterne, dati riservati e produzione dei deck;
- rimando alla pipeline `.codex/deck-pipeline.md` già esistente, senza duplicarla;
- rimandi al [runbook del collegamento](https://github.com/skunklabs-uk/developer-workspace/blob/main/docs/WORKSPACE-HANDOFF.md) e al [README runtime Homelab](https://github.com/skunklabs-uk/homelab/blob/main/gitops/apps/developer-workspace/README.md), senza aprirli dalla sandbox o dichiararli letti;
- preview Kubernetes HTTP non applicabile al repository documentale, distinta dalle eventuali verifiche visuali di PPTX/PDF, che questo report non esegue.

Il collegamento non autorizza la trasmissione di dati cliente, la produzione di slide o nuove azioni esterne. Non dichiarare completati REQUEST, consegna, RETURN, verifiche deck, merge o adozione globale senza evidenze.

Rileggi il report per correttezza, chiarezza e assenza di claim non fondati; humanize-writing se disponibile nel perimetro, senza installazioni né falsa review indipendente. Indica source e snapshot separati, fonti effettivamente lette, verifiche documentali e limiti. Nessun test artificiale per prosa. Il coordinatore applicherà la proposta revisionata nella normale PR e completerà closeout, ritiro prompt/ref temporanei e conservazione delle evidenze.

## Fonti normative integrali fornite dal coordinatore

Fonte comune: `skunklabs-uk/powerpoint-ai@09dabfb8ee041bdd4951cc73f19f29b7b4c9536b`. Tutti i file sono mode `100644`. Le delimitazioni seguenti sono contenitori di trasporto: il contenuto fra i marcatori è la fonte integrale, non una nuova policy. L’obbligo RFC in AGENTS prevale sui riferimenti generici Agent OS.

### Fonte `.codex/adoption.md`

Blob `3873f23e7bb8a12f1eae08c251cc475f553a5f89`, 3132 byte.

<!-- BEGIN qualified source .codex/adoption.md -->
# Codex OS Adoption

Status: Active
Authority Class: Repository Policy
Owner: Repository Owner
Scope: Agent workflow for commercial and business-case PowerPoint production
Created: 2026-06-05
Last Reviewed: 2026-08-28
Review Cadence: Quarterly or when deck-production standards change
Supersedes: None
Superseded By: None
Related Artifacts: AGENTS.md, .codex/routing.md, .codex/deck-pipeline.md
Invalidation Triggers: new corporate deck standard, new template, new source-grounding policy, change of target deck type

# Adoption Level

This repository adopts Agent OS / COS at **A3 Workflow-aware** level for deck-production work.

The purpose is not to automate deck generation blindly. The purpose is to give Codex a quality-first operating model for producing editable PowerPoint proposals and business cases from heterogeneous source material.

# Agent OS Source

The design reference is the current [`skunklabs-uk/agent-os`](https://github.com/skunklabs-uk/agent-os) repository.

The repository-specific rules in this repo take precedence over the generic Agent OS reference when producing decks.

# Repository Mission

This repository is a production environment for:

- commercial proposals;
- software-development business cases;
- executive proposal narratives;
- proposal-to-PMO continuity artifacts when requested.

The primary quality bar is: a final deck should be credible as a consultant-grade, executive-ready TXT/Novigo proposal, with grounded content and visual coherence.

# Adoption Principles

- Quality is more important than speed.
- The pipeline must prefer controlled iteration over one-shot generation.
- Critical gaps must trigger questions before generation.
- Minor gaps may be carried as explicit assumptions or validation points.
- `docs/` and user-provided source material are content authorities.
- `docs/ui/` and `docs/template.pptx` are visual/layout authorities.
- Each presentation belongs in a dedicated root-level folder named `yyyy-mm-dd-<project-name>`.
- Generated deliverables belong in the relevant presentation folder, not in repository root, `docs/`, or `docs/ui/`.
- Handoff notes are continuity aids, not policy.

# High-Risk Confirmation Rule

Codex must ask for explicit confirmation before:

- overwriting any `.pptx`, `.pdf`, source document, template, or visual reference;
- inventing costs, dates, effort, scope, commitments, benefits, technologies, or customer facts;
- turning a hypothesis into a claim in the body of a proposal;
- using confidential content from a reference deck as reusable content;
- changing this repository's durable workflow policy;
- running external, privileged, destructive, or cost-incurring actions.

# Target State

The target operating model is a quality-first deck pipeline:

1. Intake and material inventory.
2. Source grounding and gap assessment.
3. Storyline design around the five required proposal sections.
4. Visual grounding against `docs/ui/` and `docs/template.pptx`.
5. Deck production as editable PowerPoint.
6. Quality review and validation.
7. Handoff with evidence, assumptions, open decisions, and the presentation folder path.
<!-- END qualified source .codex/adoption.md -->

### Fonte `.codex/routing.md`

Blob `70439e648ff2df1b4148a0e075b3d0f0b20213d4`, 4699 byte.

<!-- BEGIN qualified source .codex/routing.md -->
# Routing

Status: Active
Authority Class: Repository Policy
Owner: Repository Owner
Scope: How Codex routes requests in this deck-production repository
Created: 2026-06-05
Last Reviewed: 2026-08-28
Review Cadence: Quarterly
Supersedes: None
Superseded By: None
Related Artifacts: .codex/adoption.md, .codex/deck-pipeline.md, AGENTS.md
Invalidation Triggers: new deck type, new production workflow, new required review gate

# Default Lifecycle

Use the Agent OS lifecycle:

`Intake -> Understand -> Challenge -> Decide -> Plan -> Build -> Verify -> Handoff -> Maintain`

Skip stages only when the request is clearly low-risk and no durable artifact changes.

# Repository-Specific Routes

## Create Proposal or Business Case Deck

Use when the user asks to create a new commercial proposal or business case for a software-development project.

Route:

`Intake -> Understand -> Challenge -> Decide -> Plan -> Build -> Verify -> Handoff`

Required overlays:

- AI/Application overlay for agent behavior, prompt discipline, grounding, and generated deck quality.
- Research overlay only when external facts, vendors, technologies, market data, pricing, regulations, or current information are needed.
- Security/Privacy overlay when customer material, transcripts, confidential references, or personal data are present.

Preferred reusable skills are sourced from
`skunklabs-uk/codex-skills/projects/powerpoint`. Use installed symlinks when
available and materially useful; equivalent direct execution remains valid:

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

## Improve Existing Deck

Use when the user provides an existing `.pptx` and asks for improvement, restructuring, cleanup, or regeneration.

Route:

`Intake -> Understand -> Challenge -> Plan -> Build -> Verify -> Handoff`

Rules:

- Inspect the source deck directly.
- Preserve the original file unless the user explicitly asks to overwrite it.
- Reuse visual language from the source deck before introducing new layout patterns.
- Produce a review and remediation plan before generation when changes affect storyline, economics, scope, or executive message.

## Review Deck

Use when the user asks to inspect, validate, critique, or quality-check a deck.

Route:

`Intake -> Understand -> Challenge -> Verify -> Handoff`

Review lenses:

- content grounding;
- storyline completeness;
- executive clarity;
- commercial tone;
- visual consistency;
- deliverable hygiene.

No deck edits unless the user asks for implementation after the review.

## Configure Repository Workflow

Use when changing AGENTS, context, governance, routing, skills, or deck-production rules.

Route:

`Intake -> Understand -> Challenge -> Decide -> Plan -> Build -> Verify -> Handoff`

Rules:

- Read Agent OS reference material before changing workflow rules.
- Read `AGENTS.md` and relevant `docs/reference*.md`.
- Use `CONTEXT.md` for glossary terms only.
- Create ADRs only for durable, hard-to-reverse workflow decisions with real trade-offs.

## Simple Information Request

Use when the user asks a direct question and no files need to change.

Route:

`Intake -> Understand -> Handoff`

Use source-grounded answers when the question concerns repository rules or deck standards.

# Blast Radius

## Level 0: Informational

No file changes. Answer from current context or after reading relevant docs.

## Level 1: Local Reversible

Small text edits to one non-authoritative file or one reusable-skill reference.

Minimum rigor:

- read the file first;
- edit narrowly;
- run a targeted text/link check.

## Level 2: Workflow-Level

Changes to one workflow, reusable-skill integration, prompt, or checklist.

Minimum rigor:

- read `AGENTS.md`, `.codex/adoption.md`, and impacted files;
- update related knowledge map or references;
- verify required files and links.

## Level 3: Repository Policy

Changes to `AGENTS.md`, `.codex/routing.md`, `.codex/authority.md`, `.codex/governance.md`, or durable deck policy.

Minimum rigor:

- challenge assumptions before editing;
- preserve existing constraints unless intentionally superseded;
- update related governance files;
- verify policy consistency.

## Level 4: Sensitive or Irreversible

Actions involving confidential material, destructive edits, overwrites, external publication, production credentials, or customer commitments.

Minimum rigor:

- explicit user confirmation;
- backup or non-overwrite strategy;
- documented residual risks;
- verification evidence.
<!-- END qualified source .codex/routing.md -->

### Fonte `.codex/authority.md`

Blob `415b89f953618da7d49a870c6d9554c9308e602f`, 3242 byte.

<!-- BEGIN qualified source .codex/authority.md -->
# Authority Model

Status: Active
Authority Class: Repository Policy
Owner: Repository Owner
Scope: Source priority for deck-production work
Created: 2026-06-05
Last Reviewed: 2026-06-05
Review Cadence: Quarterly
Supersedes: None
Superseded By: None
Related Artifacts: AGENTS.md, .codex/knowledge-map.md, .codex/governance.md
Invalidation Triggers: conflicting instructions, new source hierarchy, new client confidentiality rule

# Authority Order

For this repository, use this order:

1. System, developer, safety, sandbox, and tool instructions.
2. Current user instruction.
3. `AGENTS.md`.
4. `.codex/*.md` repository workflow policy.
5. `CONTEXT.md` for glossary terms.
6. `docs/reference*.md` for proposal method and storyline.
7. User-provided source material for the specific deck, including material stored in the relevant presentation folder.
8. `docs/template.pptx` for editable PowerPoint baseline and reusable structure.
9. `docs/ui/README.md` and files under `docs/ui/` for common visual reference.
10. Presentation-folder visual references, normally under `yyyy-mm-dd-<project-name>/visual-references/`.
11. Existing deck source when the task is to revise a specific deck.
12. Durable decisions in `docs/adr/`.
13. Accepted research in `docs/research/accepted/`.
14. Prompt examples, old handoffs, generated decks, and historical artifacts.

# Conflict Rules

- Higher authority beats lower authority.
- Newer does not automatically mean more authoritative.
- A reference deck is visual guidance, not permission to reuse customer-specific content.
- A generated deck is evidence of prior execution, not proof of standard.
- Handoffs are continuity notes, not policy.
- If tool-specific instructions conflict with `AGENTS.md`, follow `AGENTS.md` for this repository.
- If a user asks for a claim that is not grounded in source material, ask for source or mark it as an assumption only with explicit approval.

# Content Authorities

## Proposal Method

Primary:

- `docs/reference.1.md`
- `docs/reference.2.md`

These define the five required business-case sections and the expected commercial framing.

## Deck-Specific Content

Primary:

- user-provided appunti;
- text documents;
- images;
- transcripts;
- source decks;
- explicit user clarifications.

Rules:

- Do not invent facts.
- Do not promote assumptions into claims.
- Do not imply customer commitment from exploratory material.
- Separate confirmed content, assumptions, and open questions.

## Visual System

Primary:

- `docs/template.pptx`
- `docs/ui/README.md`
- current files under `docs/ui/`
- project-specific visual references under the relevant presentation folder
- source deck visual language when revising a deck.

Rules:

- Keep PowerPoint editable.
- Prefer real text boxes, shapes, tables, connectors, and PowerPoint-native objects.
- Use bitmap images only for visual assets that should remain visual.
- Do not recreate logos manually if an authoritative asset exists.

# Low-Authority Artifacts

Low authority artifacts may be useful for context but must not create policy:

- `.codex-work/` handoffs;
- temporary extraction files;
- generated previews;
- old prompt examples;
- unreviewed generated decks;
- draft plans not accepted by the user.
<!-- END qualified source .codex/authority.md -->

### Fonte `.codex/execution.md`

Blob `aba856f52758b068db41af6a8daa491e5fb510bf`, 3692 byte.

<!-- BEGIN qualified source .codex/execution.md -->
# Execution Policy

Status: Active
Authority Class: Repository Policy
Owner: Repository Owner
Scope: What Codex may execute or modify while producing decks
Created: 2026-06-05
Last Reviewed: 2026-08-28
Review Cadence: Quarterly
Supersedes: None
Superseded By: None
Related Artifacts: .codex/routing.md, AGENTS.md
Invalidation Triggers: new automation, new external integration, new publication path

# Execution Levels

## E0: Read-Only Work

Allowed without confirmation:

- inspect markdown, scripts, templates, decks, PDFs, and images;
- list files in `docs/`, `docs/ui/`, root, presentation folders, scripts, and config folders;
- extract deck structure for analysis;
- produce review notes.

## E1: Local Reversible Edits

Allowed when requested or clearly implied:

- create or edit markdown guidance;
- update references to reusable skills; create or edit the skills themselves only through the separately authorized `skunklabs-uk/codex-skills` workflow;
- create non-deliverable working notes;
- update prompts or checklists.

Rules:

- never discard unrelated user changes;
- preserve current source files unless the task is to update them.

## E2: Local Deck Production

Allowed when the user asks to create or improve a deck:

- generate a new `.pptx` in the relevant `yyyy-mm-dd-<project-name>/` presentation folder;
- create and use the standard presentation subfolders `drafts/`, `prompts/`, `source-materials/`, `visual-references/`, `generated-assets/`, and `attempts/`;
- create temporary extraction or validation artifacts under `/tmp` or `.codex-work/`;
- update scripts under `scripts/` only when pipeline implementation is requested.

Rules:

- do not overwrite existing decks unless explicitly approved;
- keep output editable where practical;
- validate the generated package before claiming completion.

## E3: External or Privileged Action

Requires explicit confirmation:

- network calls for research or asset retrieval;
- installing dependencies;
- using external APIs;
- opening GUI applications;
- writing outside permitted workspace;
- publishing or sending files.

## E4: Sensitive or Customer-Impacting Action

Requires explicit confirmation and documented risk:

- handling confidential customer material beyond local analysis;
- using customer-specific content from reference decks;
- changing customer-facing commitments;
- creating final offer language around prices, effort, dates, or legal disclaimers without source confirmation.

## E5: Destructive or Irreversible Action

Requires explicit confirmation and a backup strategy:

- deleting source materials;
- overwriting decks or templates;
- removing visual references;
- destructive git operations;
- irreversible file transformations.

## E6: Forbidden

Never do:

- fabricate customer facts, economics, dates, or scope;
- hide assumptions in final proposal text;
- copy confidential content from a reference deck into a new customer deck without explicit permission;
- claim a deck is verified without fresh checks.

# Verification Commands

Use the smallest relevant set:

- `git status --short` before and after edits;
- `find docs/ui -maxdepth 1 -type f | sort` before visual work;
- package integrity checks for `.pptx` outputs;
- XML parse and relationship checks for generated decks when practical;
- PDF export checks only when requested or needed and the tool is available.

# Non-Overwrite Rule

When producing output:

- if the requested output filename exists, ask before overwriting or create a clearly suffixed version;
- never overwrite `docs/template.pptx`;
- never place final deliverables under repository root, `docs/`, or `docs/ui/` when they belong to a specific presentation.
<!-- END qualified source .codex/execution.md -->

### Fonte `.codex/knowledge-map.md`

Blob `627e8cbe9e48b1dc6927f6e18c99a9fef517a53f`, 3999 byte.

<!-- BEGIN qualified source .codex/knowledge-map.md -->
# Knowledge Map

Status: Active
Authority Class: Repository Policy
Owner: Repository Owner
Scope: Where agents find knowledge for deck-production work
Created: 2026-06-05
Last Reviewed: 2026-08-28
Review Cadence: Quarterly
Supersedes: None
Superseded By: None
Related Artifacts: .codex/authority.md, AGENTS.md
Invalidation Triggers: folder restructure, new artifact class, new source material policy

# Start Here

For any deck-production task, read in this order:

1. `AGENTS.md`
2. `.codex/adoption.md`
3. `.codex/routing.md`
4. `.codex/deck-pipeline.md`
5. `CONTEXT.md`
6. all `docs/reference*.md`
7. `docs/ui/README.md`
8. actual files under `docs/ui/`
9. `docs/template.pptx` when creating or revising deck layout
10. task-specific source material, drafts, prompts, and visual references inside the relevant `yyyy-mm-dd-<project-name>/` folder
11. task-specific source material supplied by the user outside the repository, when explicitly referenced

# Repository Policy

Location:

- `.codex/*.md`

Use for:

- routing;
- execution authority;
- knowledge authority;
- quality gates;
- deck pipeline.

# Reusable Skills

Canonical source: `skunklabs-uk/codex-skills/projects/powerpoint`.

Use installed symlinks when available and materially useful. Their absence does
not block equivalent direct execution of the repository pipeline:

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

Use for:

- proposal intake;
- repository-to-deck dossier extraction;
- commercial storyline design;
- software delivery phases, effort, timeline, role, dependency, and risk estimates;
- executive slide wording and message titles;
- visual grounding;
- template visual-system extraction;
- PowerPoint inspection, editing, validation, repair, and export;
- technical `.pptx` package validation;
- final deck review.

# Proposal Method

Location:

- `docs/reference.1.md`
- `docs/reference.2.md`

Use for:

- five required sections;
- proposal/business-case intent;
- proposal-to-PMO continuity.

# Visual System

Location:

- `docs/template.pptx`
- `docs/ui/README.md`
- `docs/ui/*`

Use for:

- slide proportions;
- title placement;
- header/footer conventions;
- color palette;
- typography cues;
- card, table, roadmap, architecture, and economics layout patterns.

Project-specific visual references belong in the relevant presentation folder, normally under `yyyy-mm-dd-<project-name>/visual-references/`.

# Presentation Folders

Location:

- `yyyy-mm-dd-<project-name>/`

Use for:

- `source-materials/`: project-specific source materials;
- `drafts/`: draft briefs, storylines, creative handoffs, visual plans, and working notes;
- `prompts/`: generation, recovery, and external handoff prompts;
- `visual-references/`: project-specific visual references;
- `generated-assets/`: generated or downloaded assets for that presentation;
- `attempts/`: intermediate attempts, previews, exports, and non-final outputs;
- final `.pptx` and optional `.pdf` deliverables.

Every presentation folder must contain the six standard subfolders above. Repository-wide method, template, common visual references, and reusable prompts stay outside them.

# Durable Decisions

Location:

- `docs/adr/`

Use for:

- accepted hard-to-reverse repository workflow decisions.

# Research

Location:

- `docs/research/active/`
- `docs/research/accepted/`
- `docs/research/archived/`

Use for:

- current vendor, technology, model, framework, or market research that may affect proposal content.

Research involving current facts must be freshly verified before being used in a customer-facing deck.

# Ephemeral Work

Location:

- `.codex-work/handoffs/`
- `.codex-work/verification/`

Use for:

- session continuity;
- validation evidence;
- temporary notes.

These files do not define policy.
<!-- END qualified source .codex/knowledge-map.md -->

### Fonte `.codex/deck-pipeline.md`

Blob `de8b12804b02ee1a220d8c58ac790734aa6bbd7d`, 12357 byte.

<!-- BEGIN qualified source .codex/deck-pipeline.md -->
# Quality-First Deck Pipeline

Status: Active
Authority Class: Repository Policy
Owner: Repository Owner
Scope: Pipeline for commercial proposals and business cases for software-development projects
Created: 2026-06-05
Last Reviewed: 2026-08-28
Review Cadence: Quarterly
Supersedes: None
Superseded By: None
Related Artifacts: AGENTS.md, .codex/routing.md, skunklabs-uk/codex-skills/projects/powerpoint/*
Invalidation Triggers: new deck standard, new template, recurring quality failure, new deck type

# Goal

Produce editable, executive-ready PowerPoint proposals and business cases for software-development projects, grounded in supplied materials and visually coherent with TXT/Novigo references.

# Primary Output

The primary deliverable is a `.pptx` saved in the dedicated presentation folder.

Presentation folders live in the repository root and use:

```text
yyyy-mm-dd-<project-name>/
```

Use that folder for all project-specific source materials, working drafts, prompts, visual references, generated assets, attempts, and final deliverables.

Every presentation folder must include these standard subfolders:

```text
drafts/
prompts/
source-materials/
visual-references/
generated-assets/
attempts/
```

Use them consistently:

- `drafts/`: briefs, storylines, creative handoffs, visual plans, and working notes;
- `prompts/`: prompts used for generation, recovery, or external handoff;
- `source-materials/`: source material received or used for the presentation;
- `visual-references/`: presentation-specific visual references;
- `generated-assets/`: generated assets, scripts, and packages for that presentation;
- `attempts/`: attempts, previews, intermediate exports, and non-final outputs.

Optional outputs:

- `.pdf` export when requested;
- slide images or previews when requested;
- review notes or handoff notes when useful.

# Pipeline

## 1. Intake

Inventory all supplied materials:

- appunti;
- text documents;
- customer documents;
- images;
- transcripts;
- source decks;
- requested output filename;
- target presentation folder;
- presence of the standard presentation subfolders;
- target audience;
- business objective;
- commercial constraints.

Classify missing information:

- critical gap: blocks storyline, value, scope, plan, economics, or customer commitment;
- minor gap: can be carried as an explicit assumption or validation point.

Critical gaps require questions before generation.

If Codex proceeds with minor assumptions, it must disclose them in the user-facing message before or during the step where they are used. Do not leave assumptions only inside the generated artifact.

Questions that were not actually asked must not be presented as approved gates. Label them as "questions to ask before the next step" or "open questions", and state whether Codex proceeded because they were non-blocking for the current phase.

When the input is a software repository, use `repo-to-deck-brief` before deck planning when the installed skill is available and materially useful.

## 2. Grounding

Create a source-grounded brief:

- confirmed facts;
- likely implications;
- unsupported claims;
- assumptions allowed by the user;
- open questions;
- material that must not be reused.

Never use a reference deck as a source for new customer facts.

## 3. Storyline

Build the proposal around the five standard sections unless the user explicitly asks otherwise:

1. Contesto ed esigenza/obiettivi.
2. AS IS.
3. TO BE.
4. Piano di lavoro.
5. Economics.

The first section, `Contesto ed esigenza/obiettivi`, must be explicit. Codex must not treat a generic context, pain-point, or opportunity slide as sufficient unless the slide clearly covers:

- context: starting situation and business rationale;
- need: pain, trigger, opportunity, or constraint that makes the project necessary;
- objectives: what the project/deck should enable, decide, or achieve.

For compact CEO decks, these three elements may be compressed into one slide, but the slide title, labels, or structure must make the three-part section visible.

For decks derived from a POC, prototype, or software repository, the storyline must include a concrete explanatory bridge before roadmap and economics. Executive compression must not remove the reader's understanding of the object being funded or evolved.

At minimum, the storyline must answer:

- what the POC/system does today: inputs, main functions, and outputs;
- how it works at executive level: operating flow, main components, decision logic, integrations, or data movement;
- what it produces that is observable or measurable: payloads, evidence, reports, metrics, diagnostics, run history, or business artifacts;
- where it is limited today: functional gaps, operational gaps, validation gaps, production-readiness gaps;
- what it can become: target capability, product/service evolution, application layers, workflows, or customer business cases.

These points may be covered in one or two slides in compact CEO decks, but they must not be silently collapsed into a generic "POC exists" or "technical architecture" slide.

For software-development projects, the TO BE should connect:

- proposed solution strategy;
- target architecture or application landscape;
- main capabilities/processes handled;
- delivery approach;
- operational and business impact.

For standard TXT/Novigo proposal and business-case decks, the TO BE must include a WBS view; use `wbs-generation` when the installed skill is available and materially useful:

- for a new application, create a new WBS;
- for an existing application, create a WBS focused on the modified section or affected scope;
- if source material is incomplete, keep the WBS slide in the plan and mark assumptions/open points instead of omitting it.

Slide titles must state the message of the slide, not only the section label.

Use `executive-slide-writing` when the installed skill is available and materially useful for drafting or compressing slide language.

For CEO, portfolio, or multi-initiative decks, apply a CEO-readiness pattern:

- avoid repeated slides unless each slide adds a new decision, evidence, or narrative step;
- use a visible navigator or recurring structure for macro-areas and initiatives;
- for each initiative, clarify current state, results achieved, next steps, value generated, open points, owner/funding when relevant;
- include sizing, timing, cost, benefit, or at least an explicit order-of-magnitude estimate when the slide asks for investment or prioritization;
- translate technical terms into business impact, risk, dependency, cost, or decision.

## 4. Creative Direction

Before producing slides:

- read `docs/ui/README.md`;
- list actual files under `docs/ui/`;
- list project-specific visual references under the presentation folder when present;
- inspect relevant visual references;
- inspect `docs/template.pptx` when creating a new deck;
- inspect the source deck when revising one.

Use `pptx-template-extraction` when the installed skill is available and materially useful for a reusable visual-system brief.

When `docs/template.pdf` exists, treat it as the primary visual fidelity reference because it captures the exported appearance of the PowerPoint template. Keep `docs/template.pptx` as the editable source for masters, layouts, theme parts, and reusable assets.

Derive:

- slide grid and whitespace;
- title/header/footer conventions;
- palette and gradients;
- typography scale;
- card/table/process/architecture/economics patterns;
- icon usage.
- visual patterns visible in `docs/template.pdf`, including cover, header/footer, three-column initiative slides, thin bordered cards, roadmap layouts, value-generated bands, page numbers, and closing slide.

Do not copy customer-specific content from visual references.

Creative direction must map the actual slide plan to `docs/ui/` reference families or guardrails before PPTX generation or external handoff. At minimum, identify the reference guardrail for:

- cover;
- `Contesto / Esigenza / Obiettivi`;
- AS IS / architecture or process;
- TO BE / target architecture or scenario;
- WBS / deliverable breakdown;
- roadmap / piano di lavoro;
- economics;
- decision / next steps.

For handoff to external design models or tools, do not turn the visual plan into a pixel-level or layout-prescriptive specification unless the user explicitly asks for strict recreation.

Use two layers instead:

1. `Slide Brief`: narrative intent, mandatory content, optional content, source grounding, assumptions, and what must not be claimed.
2. `Creative Direction`: visual references, brand guardrails, density, typography/palette constraints, suggested patterns, anti-patterns, and creative freedom.

Each slide should include a `Creative freedom` level:

- `High`: the model/tool may choose the visual composition as long as the message and guardrails are respected.
- `Medium`: the slide should stay close to a reference family, but composition alternatives are acceptable.
- `Low`: use a specific reference pattern or brand convention because consistency, recognizability, or commercial formality matters.

Typical low-freedom slides are cover, `Contesto / Esigenza / Obiettivi`, formal economics/offering, and institutional closing. For other slides, prefer giving the model a clear communicative goal and usable visual options over prescribing exact boxes, arrows, or coordinates.

When an available reference pattern matches the slide type, cite it as inspiration or guardrail. Require strict adaptation only when the slide has `Creative freedom: Low` or when the user asks for high fidelity.

## 5. Plan

Before generating or heavily editing a deck, produce a short plan when the change affects storyline, economics, scope, or executive message.

The plan should include:

- proposed slide structure;
- section coverage, including the WBS view required by the standard deck storyline;
- source mapping;
- assumptions;
- open questions;
- creative direction and freedom level;
- validation criteria.

Ask for approval when the plan changes commercial positioning, economics, or scope.

Before moving from Markdown planning artifacts to PPTX generation, ask the user any remaining questions that affect audience, positioning, economics, baseline metrics, output fidelity, or customer-facing claims. Do not generate the PPTX while those questions are only listed inside an artifact.

For software-development estimates, produce delivery phases, effort ranges, role mix, dependencies, risks, and estimate assumptions; use `software-delivery-estimation` when the installed skill is available and materially useful. These estimates are delivery inputs, not binding pricing.

During standard deck planning, create the WBS view required by the TXT/Novigo storyline; use `wbs-generation` when the installed skill is available and materially useful. The WBS must be source-grounded, deliverable-oriented, and distinct from roadmap, macro Gantt, backlog, and implementation task list. For small or early-stage decks, create a compact executive WBS with assumptions/open points rather than dropping the slide.

For executive proposal decks, distinguish the strategic evolution roadmap from the implementation macro plan. The roadmap explains how the product, service, or capability evolves over releases and business cases. The macro plan explains feasible delivery phases, indicative ranges, milestones, releases, replanning points, and run/maintenance where relevant. When `docs/gantt.pdf` is available, use it as the planning reference for the macro plan. Do not turn the macro-plan slide into a detailed WBS or a list of individual implementation tasks unless the user explicitly asks for an operational plan.

## 6. Build

Create or update the `.pptx`:

- keep it editable in PowerPoint;
- use real text boxes, shapes, tables, connectors, and PowerPoint-native objects;
- use images only for visual assets;
- use `powerpoint-manipulation` when the installed skill is available and materially useful for package inspection, editing, validation, repair, and export;
- prefer `pptxgenjs` for generated decks only when a generation script/dependency is intentionally added for the task;
- keep scripts under `scripts/`;
- save final deliverables in the relevant presentation folder.

Do not overwrite existing files without confirmation.
<!-- END qualified source .codex/deck-pipeline.md -->

### Fonte `.codex/governance.md`

Blob `0e651dce1abadf960f41043cfc758bd39b487b37`, 3388 byte.

<!-- BEGIN qualified source .codex/governance.md -->
# Governance

Status: Active
Authority Class: Repository Policy
Owner: Repository Owner
Scope: Lifecycle and maintenance of durable repository knowledge
Created: 2026-06-05
Last Reviewed: 2026-08-28
Review Cadence: Quarterly
Supersedes: None
Superseded By: None
Related Artifacts: .codex/authority.md, .codex/knowledge-map.md
Invalidation Triggers: new durable artifact type, stale deck standard, conflicting policy

# Artifact Classes

## Repository Policy

Files that define how agents must operate:

- `AGENTS.md`
- `.codex/adoption.md`
- `.codex/routing.md`
- `.codex/authority.md`
- `.codex/execution.md`
- `.codex/governance.md`
- `.codex/knowledge-map.md`
- `.codex/deck-pipeline.md`

Changes require careful review and consistency checks.

## Domain Glossary

`CONTEXT.md` defines domain terms only.

It must not become a spec, implementation plan, or dumping ground for prompts.

## Method References

`docs/reference*.md` define proposal method and expected storyline.

They are authoritative for content structure unless the user gives a task-specific exception.

## Visual References

`docs/template.pptx` and `docs/ui/` define common visual style, layout, and baseline patterns.

Presentation-specific visual references belong in the relevant `yyyy-mm-dd-<project-name>/visual-references/` folder.

They are not content sources unless the user explicitly authorizes reuse.

## Presentation Folders

Root-level folders named `yyyy-mm-dd-<project-name>/` contain all material for a single presentation and must use the standard subfolders:

- `drafts/`
- `prompts/`
- `source-materials/`
- `visual-references/`
- `generated-assets/`
- `attempts/`

They are delivery workspaces, not repository-wide policy.

## Working Notes

`.codex-work/` stores ephemeral handoffs, verification notes, and temporary investigation notes.

Important findings must be promoted into durable docs when they affect future work.

# Lifecycle States

Use these states in durable docs when relevant:

- Draft: useful but not yet accepted.
- Active: currently authoritative.
- Superseded: replaced by a newer artifact.
- Archived: retained for history only.

# Required Header

Durable repository policy and decision files should include:

- Status
- Authority Class
- Owner
- Scope
- Created
- Last Reviewed
- Review Cadence
- Supersedes
- Superseded By
- Related Artifacts
- Invalidation Triggers

# Promotion Rules

Promote a working note into durable docs when it:

- changes the deck-production workflow;
- changes the content or visual standard;
- resolves a recurring ambiguity;
- defines a reusable quality gate;
- records a hard-to-reverse decision.

Do not promote:

- task-specific assumptions;
- one-off deck decisions;
- temporary extraction notes;
- unreviewed generated content.

# ADR Rules

Create an ADR under `docs/adr/` only when the decision is:

- hard to reverse;
- surprising without context;
- based on a real trade-off.

Do not create ADRs for simple file additions, obvious policy clarifications, or one-off deck choices.

# Maintenance

Review these periodically:

- whether `AGENTS.md` points to the right folders;
- whether `docs/ui/README.md` matches actual visual references;
- whether installed skill links still resolve to the canonical `skunklabs-uk/codex-skills` source and match repository policy;
- whether generated scripts still match the current visual system.
<!-- END qualified source .codex/governance.md -->

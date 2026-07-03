---
name: wbs-generation
description: Use for every standard TXT/Novigo proposal or business-case deck to derive a Work Breakdown Structure from project documentation and create the WBS slide/section required by the standard storyline. Also use for PMO artifacts, deliverable breakdowns, work-package structures, or scope decompositions.
---

# WBS Generation

## Purpose

Create a source-grounded **Work Breakdown Structure (WBS)** from project documentation and convert it into an executive-ready slide brief for the WBS section of a standard TXT/Novigo deck.

Act as both:

- **Senior Project Manager**: protect scope, delivery logic, governance, estimability, traceability, and planning usefulness.
- **Senior Business Analyst**: extract requirements, clarify deliverables, identify missing information, and separate confirmed facts from assumptions.

The WBS must describe the **structure of work and deliverables**, not the chronological plan. It is not a Gantt, roadmap, backlog, task list, or meeting agenda.

## Standard Deck Rule

For standard TXT/Novigo proposals and business cases, produce a WBS view as part of the deck planning by default.

This follows `docs/reference.1.md`, where the standard storyline includes a WBS inside the TO BE section:

- for a **new application**, create a new WBS;
- for an **existing application**, create a WBS limited to the modified section or affected scope;
- in the work-plan section, releases and milestones should connect back to the WBS after analysis.

The WBS slide may be compact, executive, or appendix-level depending on project size, but it must not disappear silently from the deck plan. If the source material is too thin to build a credible WBS, create a placeholder WBS slide brief with explicit assumptions and open questions rather than inventing scope.

## Required Reads

Read:

1. `AGENTS.md`
2. `docs/reference.1.md`
3. `.codex/deck-pipeline.md`
4. `.codex/skills/business-case-storyline/SKILL.md`
5. `.codex/skills/software-delivery-estimation/SKILL.md` when the WBS affects effort, timeline, or economics
6. `.codex/skills/executive-slide-writing/SKILL.md` when turning the WBS into slide text
7. project-specific source materials in the relevant `yyyy-mm-dd-<project-name>/source-materials/` folder
8. project-specific drafts, briefs, handoffs, or prompts when available

Use only source material and explicit user instructions as facts. Reasonable missing elements may be recorded as assumptions or clarification points, but must not be presented as confirmed scope.

## When To Use

Use this skill by default for standard proposal/business-case deck planning, because the reference storyline expects a WBS view in the TO BE / planning flow.

Also use it when:

- the user explicitly asks for a WBS;
- a slide plan includes a `WBS`, `Work Breakdown Structure`, `deliverable breakdown`, `scope breakdown`, `work package`, or `operational plan` slide;
- a deck needs to explain project scope at a level more detailed than a roadmap or macro implementation plan;
- source documentation must be converted into a planning structure for estimation, responsibilities, milestones, or Gantt construction.

For very small or early-stage decks, keep the WBS slide at executive level: macro-areas, key deliverables, and validation points. Do not over-engineer it into a task tree unless the user asks for an operational WBS.

## Core Principles

1. Follow the **100% rule**: the WBS must represent the full project scope described by the sources, neither more nor less.
2. Build around **deliverables and outcomes**, not activity verbs.
3. Use a clear hierarchy and stable numbering: `1`, `1.1`, `1.1.1`, `1.1.1.1`.
4. Each WBS element must appear in one place only. Avoid duplicated work packages.
5. Final work packages must be small enough to be estimated, assigned, and tracked.
6. Keep granularity consistent. Do not mix a whole delivery stream with a two-hour task at the same level.
7. Separate confirmed scope, inferred scope, assumptions, exclusions, and open questions.
8. Preserve the distinction between:
   - WBS: what must be produced;
   - roadmap: how the product/capability evolves;
   - macro plan/Gantt: when work happens;
   - backlog: implementation tasks or user stories.
9. Use C-level language when creating slides: business-readable, concise, and concrete.
10. Do not inflate the scope to look complete. Missing scope must be flagged, not invented. La fuffa resta fuori dalla porta.

## Recommended 4-Level Structure

Prefer a four-level structure when the source material supports it:

- **Level 1 — Macro-area / phase / stream**
- **Level 2 — Deliverable**
- **Level 3 — Component / sub-deliverable**
- **Level 4 — Work package**

Typical Level 1 areas for software and data projects:

- Governance and project setup
- Business analysis and requirements
- Functional scope and process design
- Architecture and technical design
- Data and migration
- Application/backend/frontend implementation
- Integrations
- Security, privacy, and compliance
- Testing, QA, and UAT
- Deployment, release, and hypercare
- Documentation, training, and handover
- Monitoring, operations, and run model

Adapt the areas to the actual project. Do not force every area if the documentation does not support it.

## Naming Rules

Prefer deliverable-oriented names:

- `Documento di analisi approvato`
- `Blueprint architetturale`
- `Data contract definiti`
- `Pipeline di ingestion implementata`
- `Modelli dbt validati`
- `Ambiente di deploy configurato`
- `Piano di collaudo completato`
- `Runbook operativo consegnato`

Avoid raw activity wording:

- `fare analisi`
- `fare meeting`
- `sviluppare backend`
- `testare`
- `parlare con cliente`

If an activity is necessary, rephrase it as the artifact or decision it produces.

## Extraction Workflow

1. Inventory source materials and identify the project perimeter.
2. Extract confirmed deliverables, components, systems, processes, data objects, integrations, roles, constraints, and non-functional requirements.
3. Identify implicit but necessary delivery work, then label it as inferred or assumption unless clearly supported.
4. Group deliverables into Level 1 macro-areas.
5. Decompose each macro-area into deliverables, components, and work packages.
6. Check for missing areas, duplication, inconsistent granularity, and unsupported scope.
7. Validate the WBS against downstream uses: effort, responsibility matrix, roadmap, Gantt, milestones, testing, and economics.
8. When creating a slide, compress the WBS into a readable executive view without losing the logic.
9. Link the macro plan, releases, or milestones back to WBS items when the deck includes a `Piano di lavoro`.

## Output For Planning Artifact

When producing a WBS artifact, use:

````markdown
# WBS del progetto

## 1. Sintesi del perimetro
Brief source-grounded description of the project.

## 2. Assunzioni
- ...

## 3. WBS principale
| Codice WBS | Livello | Nome elemento | Descrizione | Deliverable atteso | Fonte / evidenza | Note |
|---|---:|---|---|---|---|---|

## 4. Vista gerarchica
```text
1. Macro-area
   1.1 Deliverable
      1.1.1 Componente
         1.1.1.1 Work package
```

## 5. Esclusioni
- ...

## 6. Aree mancanti o ambigue
- ...

## 7. Rischi e attenzioni PM/BA
| Rischio / attenzione | Impatto | Evidenza | Mitigazione / chiarimento richiesto |
|---|---|---|---|

## 8. Uso consigliato della WBS
Explain how to use it for effort estimation, responsibility matrix, roadmap, Gantt, milestones, testing, and economics.
````

## Output For WBS Slide Brief

For standard decks, produce a WBS slide brief. Use a compact version when the project is small or when the WBS is still pre-analysis.

```markdown
## Slide: WBS del progetto — dal perimetro ai work package stimabili

### Slide Brief
- Message: show how the project scope is decomposed into controllable deliverables and work packages.
- Audience: executive / PMO / delivery stakeholders.
- Source grounding: list source files or sections used.
- Must include: 4-6 macro-areas, key deliverables, visible distinction between deliverables and work packages, assumptions/open points if relevant.
- Must not claim: unconfirmed dates, costs, owners, scope items, or commitments.

### Recommended Visual Pattern
Use one of these patterns depending on density:
- hierarchical tree for compact WBS;
- nested cards grouped by macro-area;
- matrix with macro-area, deliverable, work package, output;
- swimlane-style decomposition when streams are parallel.

### Slide Content
| Macro-area | Deliverable | Work packages / components | Output |
|---|---|---|---|

### Speaker / Review Notes
- Clarify that this is not the timeline.
- Explain which parts are confirmed and which require validation.
- Point out scope areas that may affect effort or economics.
- Explain how releases/milestones in the work plan link back to the WBS when applicable.

### Creative Direction
- Keep it visual and structured: few text blocks, strong hierarchy, no wall of text.
- Prefer diagrams, grouped cards, and progressive decomposition over long tables.
- Use C-level language; technical labels are allowed only when they identify real components.
- Creative freedom: Medium, unless a specific visual reference is requested.
```

## Quality Checklist

Before finalizing, verify:

- [ ] The WBS covers the full documented scope.
- [ ] Every element is grounded in sources, user instructions, or explicit assumptions.
- [ ] The hierarchy is numbered and consistent.
- [ ] Names describe deliverables, not vague activities.
- [ ] There are no duplicate work packages.
- [ ] Final work packages are estimable and assignable.
- [ ] Roadmap, Gantt, backlog, and WBS are not confused.
- [ ] Missing information is visible as assumptions, exclusions, or open questions.
- [ ] The slide version is readable by non-technical stakeholders.
- [ ] The output can feed effort estimation and responsibility mapping.
- [ ] Work-plan releases or milestones can be traced back to WBS items when applicable.

## Stop Conditions

Ask for clarification before producing a customer-facing WBS when:

- the project boundary is unclear;
- source materials conflict on scope;
- deliverables cannot be separated from optional future work;
- the WBS would imply costs, dates, responsibilities, or contractual commitments not approved by the user;
- a detailed operational WBS is requested but the source documentation only supports a macro plan.

If the deck must proceed despite incomplete source material, include a WBS slide with explicit `assunzioni da validare` and `punti aperti`, rather than omitting the WBS.

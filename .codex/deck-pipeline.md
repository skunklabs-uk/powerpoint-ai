# Quality-First Deck Pipeline

Status: Active
Authority Class: Repository Policy
Owner: Repository Owner
Scope: Pipeline for commercial proposals and business cases for software-development projects
Created: 2026-06-05
Last Reviewed: 2026-06-05
Review Cadence: Quarterly
Supersedes: None
Superseded By: None
Related Artifacts: AGENTS.md, .codex/routing.md, .codex/skills/*
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

When the input is a software repository, use `.codex/skills/repo-to-deck-brief/SKILL.md` before deck planning.

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

Slide titles must state the message of the slide, not only the section label.

Use `.codex/skills/executive-slide-writing/SKILL.md` when drafting or compressing slide language.

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

Use `.codex/skills/pptx-template-extraction/SKILL.md` when a reusable visual-system brief is needed.

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
- section coverage;
- source mapping;
- assumptions;
- open questions;
- creative direction and freedom level;
- validation criteria.

Ask for approval when the plan changes commercial positioning, economics, or scope.

Before moving from Markdown planning artifacts to PPTX generation, ask the user any remaining questions that affect audience, positioning, economics, baseline metrics, output fidelity, or customer-facing claims. Do not generate the PPTX while those questions are only listed inside an artifact.

For software-development estimates, use `.codex/skills/software-delivery-estimation/SKILL.md` to produce delivery phases, effort ranges, role mix, dependencies, risks, and estimate assumptions. These estimates are delivery inputs, not binding pricing.

When the slide plan requires a WBS, Work Breakdown Structure, deliverable breakdown, work-package view, or operational scope decomposition, use `.codex/skills/wbs-generation/SKILL.md`. The WBS must be source-grounded, deliverable-oriented, and distinct from roadmap, macro Gantt, backlog, and implementation task list.

For executive proposal decks, distinguish the strategic evolution roadmap from the implementation macro plan. The roadmap explains how the product, service, or capability evolves over releases and business cases. The macro plan explains feasible delivery phases, indicative ranges, milestones, releases, replanning points, and run/maintenance where relevant. When `docs/gantt.pdf` is available, use it as the planning reference for the macro plan. Do not turn the macro-plan slide into a detailed WBS or a list of individual implementation tasks unless the user explicitly asks for an operational plan.

## 6. Build

Create or update the `.pptx`:

- keep it editable in PowerPoint;
- use real text boxes, shapes, tables, connectors, and PowerPoint-native objects;
- use images only for visual assets;
- use `.codex/skills/powerpoint-manipulation/SKILL.md` for package inspection, editing, validation, repair, and export;
- prefer `pptxgenjs` for generated decks only when a generation script/dependency is intentionally added for the task;
- keep scripts under `scripts/`;
- save final deliverables in the relevant presentation folder.

Do not overwrite existing files without confirmation.

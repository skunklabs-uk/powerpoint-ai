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

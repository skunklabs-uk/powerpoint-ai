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

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

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

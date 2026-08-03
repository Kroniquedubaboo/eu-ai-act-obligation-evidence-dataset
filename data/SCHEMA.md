# Data dictionary

The canonical file is [`graph.json`](graph.json). [`obligations.json`](obligations.json) is the `obligations` array from it; [`obligations-evidence.csv`](obligations-evidence.csv) is a flattened obligation × evidence view.

All entities use stable, human-readable string ids. Cross-references use `*_id` (single) or `*_ids` (array) fields that resolve to those ids.

## `graph.json` top level

| Key | Type | Notes |
|---|---|---|
| `generator` | string | "EU AI Regulation Decoded" |
| `domain` | string | Canonical platform URL |
| `license` | string | CC BY 4.0 with attribution |
| `note` | string | "Practitioner reference, not legal advice." |
| `obligations` | array | see below |
| `evidence_artifacts` | array | see below |
| `articles` | array | AI Act articles |
| `annexes` | array | AI Act annexes |
| `deadlines` | array | applicability dates (with `history[]` where moved) |
| `roles` | array | actor types |

## `obligation`

| Field | Type | Description |
|---|---|---|
| `id` | string | Stable id, e.g. `obl-art15-declare-accuracy-metrics` |
| `short_title` | string | Plain-language title |
| `statement` | string | What the duty requires |
| `derived_from_ids` | string[] | → `article` / `annex` ids |
| `applies_to_role_ids` | string[] | → `role` ids |
| `risk_category_ids` | string[] | risk tiers that scope the obligation |
| `deadline_id` | string | → `deadline` id |
| `evidence_ids` | string[] | → `evidence_artifact` ids |
| `red_flag_ids` | string[] | audit red flags (in `obligations.json`/graph via evidence source) |
| `mistake_ids` | string[] | common mistakes |
| `issue_ids` | string[] | newsletter issues explaining it |
| `source_ids` | string[] | → primary-source citations |
| `version` | int | record version |
| `last_reviewed` | date | ISO date of last review |
| `status` | string | `active` / `draft` / `superseded` |
| `needs_review` | bool | true = not yet verified against primary text |
| `confidence` | string | `high` / `medium` / `low` |

## `evidence_artifact`

| Field | Type | Description |
|---|---|---|
| `id` | string | Stable id, e.g. `ev-accuracy-declaration-record` |
| `name` | string | Human name of the document/record |
| `description` | string | What it is and what it must show |
| `satisfies_obligation_ids` | string[] | → `obligation` ids |
| `annex_iv_section` | string / null | Relevant Annex IV section (e.g. `anx-4-2`) |
| `contemporaneous` | bool | Must be created at decision time, not retrospectively |
| `format` | string | e.g. `record`, `dossier`, `matrix`, `declaration` |
| `source_ids` | string[] | → primary-source citations |

## `obligations-evidence.csv` columns

`obligation_id`, `obligation`, `article`, `roles`, `risk_categories`, `deadline`, `evidence_artifact`, `evidence_description`, `annex_iv_section`, `audit_red_flags`, `source_urls`.

One row per (obligation × evidence artifact) pair. Multi-valued cells use `; ` as the separator.

## `sources.json` — citation registry

`source_id` values throughout the dataset resolve here.

| Field | Type | Description |
|---|---|---|
| `id` | string | e.g. `src-art15` |
| `type` | string | `regulation` / `article` / `annex` / `guidance` / `official` |
| `title` | string | Human title of the source |
| `url` | string | Link to the primary source |
| `cite` | string | Short citation, e.g. `Art. 15 AIA` |


## `red-flags.json`

Resolves `red_flag_ids` and `mistake_ids` referenced by obligations.

- `audit_red_flags[]`: `{ id, statement, related_obligation_ids, related_evidence_ids, severity }` — what fails an audit.
- `common_mistakes[]`: `{ id, mistake, correction, related_obligation_ids }` — frequent practitioner errors and the fix.

## `risk-categories.json`

Resolves `risk_category_ids`. `risk_categories[]`: `{ id, name, definition, source_ids }` — the risk tiers that scope obligations (`risk-prohibited`, `risk-high-annex3`, `risk-high-annex1`, `risk-gpai`, `risk-gpai-systemic`, `risk-transparency`, plus limited/minimal where relevant).

## External references

- `issue_ids` on obligations point to the newsletter issues that explain them on the live platform (<https://euaird.vercel.app>). They are not published as a collection here.

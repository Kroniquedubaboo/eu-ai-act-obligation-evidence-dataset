# EU AI Act — Obligation-to-Evidence Dataset

A free, open, machine-readable dataset that maps **EU AI Act obligations** to the **specific evidence an auditor expects**, together with the applicable roles, risk tiers, deadlines, and common audit red flags.

Most EU AI Act resources explain *what the law says*. This dataset encodes the harder, practitioner-facing question: **which document or record must exist, for which role, by when — and what fails an audit.**

- **Live reference & interactive tool:** <https://euaird.vercel.app>
- **Interactive Audit-Readiness Checklist:** <https://euaird.vercel.app/audit-readiness.html>
- **Dataset landing page:** <https://euaird.vercel.app/data.html>
- **Licence:** [CC BY 4.0](LICENSE) — free to use, share and adapt with attribution.
- **Status:** early release. Some legal facts are flagged `needs_review` (see [Known limitations](#known-limitations--review-status)).

> **This is not legal advice.** It is a practitioner reference for audit preparation. Verify every fact against the cited primary sources and take qualified legal advice before relying on it for a compliance decision.

---

## Contents

- [1. What the dataset contains](#1-what-the-dataset-contains)
- [2. Who it is for](#2-who-it-is-for)
- [3. The obligation → evidence → red-flag structure](#3-the-obligation--evidence--red-flag-structure)
- [4. Data formats](#4-data-formats)
- [5. Example records](#5-example-records)
- [6. How to cite it](#6-how-to-cite-it)
- [7. How to reuse it](#7-how-to-reuse-it)
- [8. Update methodology](#8-update-methodology)
- [9. Source & legal-accuracy methodology](#9-source--legal-accuracy-methodology)
- [10. Known limitations & review status](#10-known-limitations--review-status)
- [11–13. Links & disclaimer](#links--disclaimer)

---

## 1. What the dataset contains

As of this release the dataset covers:

| Entity | Count | Description |
|---|---:|---|
| Obligations | 14 | Atomic duties under the EU AI Act (Regulation (EU) 2024/1689) |
| Evidence artifacts | 17 | The document/record an auditor expects for an obligation |
| Articles | 11 | AI Act articles referengwed (e.g. 5, 6, 9, 10, 11, 15, 26, 43, 49, 50, 53) |
| Annexes | 2 | Annex III (high-risk use cases) and Annex IV (technical documentation) |
| Deadlines | 5 | Applicability dates, with change history where a date moved |
| Roles | 6 | Provider, deployer, GPAI provider, importer, distributor, authorised representative |

It is **not** a complete encoding of the entire Regulation. It is a growing, cited subset focused on the obligation → evidence mapping. See [Known limitations](#10-known-limitations--review-status).

## 2. Who it is for

- **Compliance officers & legal teams** preparing high-risk AI systems or GPAI models for audit.
- **ML / product engineers** who need to know which records and tests must exist for their system.
- **Auditors** who want a structured "what evidence, what red flags" reference.
- **Tool builders & researchers** who want structured, cited EU AI Act data to build on rather than re-derive from prose.

## 3. The obligation → evidence → red-flag structure

The core relationship is:

```
role  ─┐
       ├─►  obligation  ─►  evidence artifact(s)  ─►  audit red flag(s)
risk  ─┘        │
                └─►  deadline   └─►  source citation(s)   └─►  common mistakes
```

Each **obligation** records: a stable id, a plain-language statement, the article/annex it derives from, the roles it applies to, the risk categories that scope it, a deadline reference, the evidence artifacts that satisfy it, associated audit red flags and common mistakes, primary-source citations, a `version`, a `last_reviewed` date, and a `needs_review` flag.

Each **evidence artifact** records: a stable id, name, description, which obligations it satisfies, the relevant Annex IV section (where applicable), whether it must be a *contemporaneous* record, a format, and source citations.

## 4. Data formats

| File | Format | Best for |
|---|---|---|
| [`data/graph.json`](data/graph.json) | JSON | Full knowledge graph — obligations, evidence, articles, annexes, deadlines, roles, with cross-referencing ids |
| [`data/obligations.json`](data/obligations.json) | JSON | Obligations only, with their cross-references |
| [`data/obligations-evidence.csv`](data/obligations-evidence.csv) | CSV | Flattened obligation × evidence table for spreadsheets / analysis |
| [`data/red-flags.json`](data/red-flags.json) | JSON | Audit red flags and common mistakes (what fails an audit) — resolves `red_flag_ids` / `mistake_ids` |
| [`data/sources.json`](data/sources.json) | JSON | Citation registry — `source_id` → primary-source title, type and URL |
| [`data/risk-categories.json`](data/risk-categories.json) | JSON | Risk tiers (Annex III high-risk, Annex I high-risk, GPAI, GPAI-systemic, transparency) — resolves `risk_category_ids` |
| [`data/SCHEMA.md`](data/SCHEMA.md) | Markdown | Field-by-field data dictionary |

> Note: obligation records also carry `issue_ids` — these point to the newsletter issues on the [live platform](https://euaird.vercel.app) that explain the obligation, and are **external references**, not a collection published in this dataset.
| [`version.json`](version.json) | JSON | Machine-readable dataset version metadata |

All identifiers are stable, human-readable slugs (e.g. `obl-art15-declare-accuracy-metrics`, `ev-accuracy-declaration-record`, `art-15`). Cross-references use `*_id` / `*_ids` fields resolving to those ids.

## 5. Example records

**Obligation** (from `graph.json` / `obligations.json`):

```json
{
  "id": "obl-art15-declare-accuracy-metrics",
  "short_title": "Declare accuracy metrics in instructions for use",
  "statement": "Choose appropriate accuracy metrics for the high-risk system and declare the levels and the metrics in the accompanying instructions for use; substantiate them in the technical documentation.",
  "derived_from_ids": ["art-15", "art-11"],
  "applies_to_role_ids": ["role-provider"],
  "risk_category_ids": ["risk-high-annex3", "risk-high-annex1"],
  "deadline_id": "dl-2027-12-02-highrisk-annex3",
  "evidence_ids": ["ev-accuracy-declaration-record", "ev-instructions-for-use", "ev-technical-file-annexiv"],
  "red_flag_ids": ["rf-no-accuracy-metric-declared", "rf-retroactive-documentation"],
  "source_ids": ["src-art15"],
  "version": 1,
  "last_reviewed": "2026-07-30",
  "needs_review": false
}
```

**Flattened CSV** (obligation × evidence):

```
obligation_id,obligation,article,roles,risk_categories,deadline,evidence_artifact,evidence_description,annex_iv_section,audit_red_flags,source_urls
obl-art15-declare-accuracy-metrics,Declare accuracy metrics in instructions for use,Proving your system is accurate robust and secure; The technical file you must keep current,Provider,High-risk (Annex III use case); High-risk (Annex I regulated product),2027-12-02,Accuracy Declaration Record,Dated record stating the chosen accuracy metric(s)...,anx-4-2,...,https://artificialintelligenceact.eu/article/15/
```

## 6. How to cite it

See [`CITATION.cff`](CITATION.cff). Suggested citation:

> EU AI Regulation Decoded (2026). *EU AI Act — Obligation-to-Evidence Dataset* (v1.0.0). CC BY 4.0. https://github.com/Kroniquedubaboo/eu-ai-act-obligation-evidence-dataset

## 7. How to reuse it

Under **CC BY 4.0** you may use, share and adapt the dataset, including commercially, **with attribution** to *EU AI Regulation Decoded* and a link back to this repository or <https://euaird.vercel.app>.

Quick start (Python):

```python
import json
g = json.load(open("data/graph.json"))
for o in g["obligations"]:
    ev = [e["name"] for e in g["evidence_artifacts"] if e["id"] in o["evidence_ids"]]
    print(o["short_title"], "→", ev)
```

Run the integrity check:

```bash
python3 validate.py
```

## 8. Update methodology

The dataset is maintained alongside the [EU AI Regulation Decoded](https://euaird.vercel.app) newsletter, which acts as the update engine: when Commission guidance, a delegated act, a standard, or an enforcement action changes a fact, the affected record is updated — its `version` is bumped, `last_reviewed` is set, and the change is recorded in [`CHANGELOG.md`](CHANGELOG.md), citing the source. Deadlines keep their full change history inside the data (for example, the stand-alone high-risk obligations deferred by the 7 May 2026 political agreement). Corrections and additions are welcome via [Issues](../../issues) and Pull Requests — see [`CONTRIBUTING.md`](CONTRIBUTING.md).

## 9. Source & legal-accuracy methodology

Every factual record cites at least one **primary source** — the Regulation article/annex or official European Commission guidance (URLs are in `source_urls` / the `sources` references). Evidence guidance reflects the *contemporaneous documentation* standard that national competent authorities apply. Facts still being verified against the primary text are marked `needs_review: true` rather than presented as settled.

## 10. Known limitations & review status

- **Coverage is partial.** 14 obligations is a growing subset, not the full Regulation. Missing areas include, among others, parts of Articles 13/14/17/72 and the eight Annex III domains as individual records.
- **Some facts need verification.** 7 of 14 obligations are flagged `needs_review` (chiefly items touching the post–7 May 2026 timeline changes and GPAI/registration scope). Treat flagged records as directional.
- **Not legal advice, not official.** This is an independent practitioner dataset. It is not produced or endorsed by the European Commission or any authority, and does not replace the primary legal text or qualified legal counsel.
- **The law is moving.** Deadlines and obligations are subject to change; always check the cited primary sources for the current position.

## Links & disclaimer

- **Live platform:** <https://euaird.vercel.app>
- **Interactive Audit-Readiness Checklist:** <https://euaird.vercel.app/audit-readiness.html>
- **Dataset landing page:** <https://euaird.vercel.app/data.html>

**Disclaimer:** This dataset is a practitioner reference, **not legal advice**, and does not create a client relationship. Verify against the cited primary sources and take qualified legal advice before relying on it for any compliance decision.

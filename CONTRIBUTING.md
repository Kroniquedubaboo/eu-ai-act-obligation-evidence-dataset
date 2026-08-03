# Contributing

Thanks for helping keep this dataset accurate and useful. Corrections and additions are welcome.

## Factual corrections

If a fact is wrong, out of date, or missing a source:

1. Open an [Issue](../../issues/new/choose) using the **Factual correction** template, **or**
2. Open a Pull Request editing the relevant record.

Please include the **primary source** (Regulation article/annex or official Commission guidance) that supports the change. Legal facts are not changed without a citation.

## Data rules

- Every factual record must cite at least one primary source (`source_ids` / `source_urls`).
- Keep identifiers stable. Do not rename an existing id; add a new record instead and mark the old one `superseded_by` if needed.
- Prefer the *contemporaneous documentation* standard for evidence guidance.
- If a fact is not yet verified against the primary text, mark it `needs_review: true` rather than presenting it as settled.
- When you change a fact, bump the record's `version`, set `last_reviewed`, and add a line to `CHANGELOG.md` citing the source.

## Keep the three files in sync

`data/graph.json`, `data/obligations.json`, and `data/obligations-evidence.csv` are generated from the same canonical model. If you edit one, update the others so they agree, and run:

```bash
python3 validate.py
```

which checks JSON validity, CSV structure, and referential integrity.

## Scope

This is a practitioner reference for the EU AI Act obligation → evidence mapping. Please keep contributions within that scope. It is **not legal advice**.

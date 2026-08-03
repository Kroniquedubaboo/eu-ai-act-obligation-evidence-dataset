# Changelog

All notable changes to this dataset are recorded here. Versioning is semantic at the dataset level (`MAJOR.MINOR.PATCH`): MAJOR for breaking schema changes, MINOR for added records/fields, PATCH for corrections to existing facts.

## [1.0.0] — 2026-07-31

Initial public release.

- 14 obligations, 17 evidence artifacts, 11 articles, 2 annexes (III, IV), 5 deadlines, 6 roles.
- Each record cited to primary sources (Regulation (EU) 2024/1689 articles/annexes and official Commission guidance).
- Deadlines include change history where a date moved (e.g. stand-alone high-risk Annex III obligations deferred to 2 December 2027 by the 7 May 2026 political agreement).
- 7 of 14 obligations flagged `needs_review` pending verification against primary text (chiefly post-7-May-2026 timeline items and GPAI/registration scope).
- Formats: `data/graph.json`, `data/obligations.json`, `data/obligations-evidence.csv`; data dictionary in `data/SCHEMA.md`; integrity checker in `validate.py`.

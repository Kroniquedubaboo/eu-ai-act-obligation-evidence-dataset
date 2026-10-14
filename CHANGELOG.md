# Changelog

All notable changes to this dataset are recorded here. Versioning is semantic at the dataset level (`MAJOR.MINOR.PATCH`): MAJOR for breaking schema changes, MINOR for added records/fields, PATCH for corrections to existing facts.

## [1.1.0] — 2026-10-14

Synchronised with the live platform data (euaird.vercel.app/api, build of 2026-10-08).

**Corrections**
- `obl-art50-synthetic-content-marking`: removed `role-gpai-provider` as a duty-holder. Article 50 does not explicitly apply to GPAI models; the Art 50(2) marking and detection duties rest with the provider of the AI system, which may rely on upstream marking only to the extent it complies with Art 50(2) and remains responsible for demonstrating compliance (Commission Article 50 Guidelines, 20 July 2026, paras 27 and 74).
- `obl-art6-classify-high-risk`: added the Article 6(1a)–(1c) safety-component clarifications introduced by Regulation (EU) 2026/1744 (Digital Omnibus).

**Added**
- 2 deadlines: `dl-2026-12-02-art50-2-grace` (Art 111(4) as inserted by Regulation (EU) 2026/1744: systems placed on the market before 2 August 2026 must comply with Art 50(2) by 2 December 2026) and `dl-2026-12-02-art5-new-prohibitions` (Art 5(1)(ba)/(bb), applicable from 2 December 2026).
- 4 sources: Commission Article 50 Guidelines (July 2026), Article 50 FAQ, Transparency Code of Practice (June 2026) and the Commission opinion and AI Board adequacy assessment of that Code (July 2026).

Counts: deadlines 5 → 7, sources 18 → 22; all other counts unchanged. `validate.py` passes.

## [1.0.0] — 2026-07-31

Initial public release.

- 14 obligations, 17 evidence artifacts, 11 articles, 2 annexes (III, IV), 5 deadlines, 6 roles.
- Each record cited to primary sources (Regulation (EU) 2024/1689 articles/annexes and official Commission guidance).
- Deadlines include change history where a date moved (e.g. stand-alone high-risk Annex III obligations deferred to 2 December 2027 by the 7 May 2026 political agreement).
- 7 of 14 obligations flagged `needs_review` pending verification against primary text (chiefly post-7-May-2026 timeline items and GPAI/registration scope).
- Formats: `data/graph.json`, `data/obligations.json`, `data/obligations-evidence.csv`; data dictionary in `data/SCHEMA.md`; integrity checker in `validate.py`.

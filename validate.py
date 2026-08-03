#!/usr/bin/env python3
"""Integrity checks for the EU AI Act obligation-to-evidence dataset.

Verifies:
  - JSON files parse
  - CSV parses with a stable header
  - graph.json and obligations.json agree
  - referential integrity (every *_id / *_ids resolves to a known entity id)

Usage:  python3 validate.py
Exit code 0 = all checks pass, 1 = failure.
"""
import json, csv, sys, os

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "data")

def load(name):
    with open(os.path.join(DATA, name), encoding="utf-8") as f:
        return json.load(f)

def main():
    errors = []

    graph = load("graph.json")
    obligations_only = load("obligations.json")
    sources = load("sources.json")
    redflags = load("red-flags.json")
    riskcats = load("risk-categories.json")

    # `issue_ids` reference newsletter issues on the live platform, not published as a
    # collection in this dataset; they are documented external references (see SCHEMA.md).
    EXTERNAL_REF_FIELDS = {"issue_ids"}

    # collect every entity id in the graph + the source registry (source_ids resolve to sources.json)
    ids = set()
    def collect(obj):
        if isinstance(obj, dict):
            if isinstance(obj.get("id"), str):
                ids.add(obj["id"])
            for v in obj.values():
                collect(v)
        elif isinstance(obj, list):
            for v in obj:
                collect(v)
    collect(graph)
    collect(sources)
    collect(redflags)
    collect(riskcats)

    # graph vs obligations.json agreement
    g_obl = {o["id"]: o for o in graph["obligations"]}
    o_obl = {o["id"]: o for o in obligations_only}
    if set(g_obl) != set(o_obl):
        errors.append("obligations.json and graph.json have different obligation ids")

    # referential integrity: every *_id/*_ids resolves (except wildcards and known external source urls)
    missing = []
    def check(obj, path=""):
        if isinstance(obj, dict):
            for k, v in obj.items():
                if k in EXTERNAL_REF_FIELDS:
                    continue
                if k.endswith("_ids") and isinstance(v, list):
                    for r in v:
                        if isinstance(r, str) and r not in ids:
                            missing.append(f"{path}.{k} -> {r}")
                elif k.endswith("_id") and isinstance(v, str):
                    if v not in ids:
                        missing.append(f"{path}.{k} -> {v}")
                else:
                    check(v, f"{path}.{k}")
        elif isinstance(obj, list):
            for i, v in enumerate(obj):
                check(v, path)
    check(graph, "graph")
    if missing:
        errors.append("dangling references: " + "; ".join(sorted(set(missing))[:10]))

    # CSV structure
    with open(os.path.join(DATA, "obligations-evidence.csv"), encoding="utf-8") as f:
        rows = list(csv.reader(f))
    expected = ["obligation_id","obligation","article","roles","risk_categories","deadline",
                "evidence_artifact","evidence_description","annex_iv_section","audit_red_flags","source_urls"]
    if not rows or rows[0] != expected:
        errors.append("CSV header does not match the expected columns")
    for i, r in enumerate(rows[1:], start=2):
        if len(r) != len(expected):
            errors.append(f"CSV row {i} has {len(r)} columns, expected {len(expected)}")
            break

    # report
    print(f"entities: {len(ids)}")
    print(f"obligations: {len(g_obl)} | evidence: {len(graph['evidence_artifacts'])} | csv rows: {len(rows)-1}")
    if errors:
        print("\nFAIL:")
        for e in errors:
            print("  -", e)
        sys.exit(1)
    print("\nPASS — JSON valid, CSV valid, files agree, referential integrity clean.")

if __name__ == "__main__":
    main()

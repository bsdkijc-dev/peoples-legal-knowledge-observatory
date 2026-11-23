# Kaggle Release Candidate (SAFE MODE — `REQUIRES HUMAN APPROVAL`)

**Target Kaggle Slug:** `judicialcollege/peoples-legal-knowledge-observatory`  
**Status:** `REQUIRES HUMAN APPROVAL` before running `kaggle datasets create` (Human Approval Gate P7).

## Included Files (Safe for Public Release After Sign-Off)
- `dataset_01_legal_sources.json` — Verified metadata and official URLs (`peraturan.bpk.go.id`) for 14 Indonesian primary legal sources.
- `source-register.csv` — Tabular version of Dataset 01 with amendment/repeal status and retrieval dates (`2026-11-23`).
- `synthetic/` — Synthetic test fixtures (`SYNTHETIC_TEST`) for all 12 schemas (strictly for pipeline reproducibility, not empirical legal evidence).

## Excluded Until Human Legal Review
- `data/interim/dataset_02_legal_provisions.json` through `dataset_07_terminology.json` (`PENDING_HUMAN_REVIEW`).
- `content/plain-language/*.md` (`PENDING_HUMAN_REVIEW`).

## Upload Command (After Human Approval)
```bash
kaggle datasets create -p kaggle-release-candidate -r zip
```

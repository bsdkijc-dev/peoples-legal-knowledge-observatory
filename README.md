# People's Legal Knowledge Observatory (PLKO)

**Tagline:** Legal Knowledge for Everyone. Justice Without Barriers.  
**Parent Initiative:** MA Open Justice & Public Prosperity Initiative 2027–2030  
**Status:** Independent research and public-interest knowledge project (SAFE MODE — Pilot Phase).

> **Important Notice:** PLKO is an independent research and public-interest knowledge project. It does **not** claim official endorsement, authorization, or institutional representation by Mahkamah Agung RI or any government institution. All legal content produced by this system is strictly for public legal literacy and educational purposes, not individualized legal advice, and requires human legal review before public release.

## Research Question

*Can every Indonesian citizen access, understand, and use reliable legal information to protect their rights?*

## Mission & Architecture

PLKO connects verified primary Indonesian legal sources to accessible, plain-language public knowledge through a governed, traceable pipeline:

```
OFFICIAL LEGAL SOURCES -> SOURCE VERIFICATION -> LEGAL KNOWLEDGE EXTRACTION -> PLAIN-LANGUAGE TRANSFORMATION -> HUMAN LEGAL REVIEW -> PUBLIC LEGAL KNOWLEDGE -> LEGAL LITERACY EVALUATION
```

### Legal Knowledge Domains (LK01–LK12)
- **LK01**: Court access and judicial procedures (`knowledge/peradilan/`)
- **LK02**: Civil law and contracts (`knowledge/perdata/`)
- **LK03**: Criminal justice and procedural rights (`knowledge/pidana/`)
- **LK04**: Family and religious court matters (`knowledge/keluarga/`)
- **LK05**: Labour and industrial relations (`knowledge/ketenagakerjaan/`)
- **LK06**: UMKM and commercial law (`knowledge/umkm/`)
- **LK07**: Land and agrarian law (`knowledge/pertanahan/`)
- **LK08**: Administrative and public service law (`knowledge/administrasi/`)
- **LK09**: Consumer protection (`knowledge/konsumen/`)
- **LK10**: Legal aid and access to justice (`knowledge/bantuan-hukum/`)
- **LK11**: Digital rights and electronic transactions (`knowledge/digital-rights/`)
- **LK12**: Environmental and community rights (`knowledge/lingkungan/`)

## Repository Layout

- `governance/` — Charter, legal accuracy, source verification, privacy, publication, AI governance, and review protocols.
- `research/` — Research questions, conceptual framework, methodology, legal literacy framework, and evaluation protocol.
- `schemas/` — 12 JSON Schema Draft 2020-12 definitions for Datasets 01–12.
- `sources/` — Authoritative source register (`source-register.csv`) and source verification assessment (`source-verification.md`).
- `data/` — Raw, interim, processed, synthetic (`data/synthetic/`), and approved-public datasets.
- `content/` — Plain-language drafts, FAQs, procedure guides, audio scripts, visual guides, and offline materials (all flagged `REQUIRES HUMAN APPROVAL` until reviewed).
- `src/` — Pipeline modules (`acquisition/`, `extraction/`, `verification/`, `transformation/`, `validation/`, `evaluation/`, `publishing/`).
- `tests/` — Automated schema and source-traceability validation tests.
- `reports/` — Baseline, legal literacy, thematic, and policy brief reports.

## Setup & Validation

### Prerequisites
- Python 3.11+ (uses standard library `unittest`, `json`, `csv`; optional: `jsonschema`, `pandas`, `duckdb`).

### Run Traceability & Schema Validation
```bash
cd peoples-legal-knowledge-observatory
python3 -m src.validation.traceability_validator --data-dir data/synthetic --schemas-dir schemas
```

### Run Automated Tests
```bash
cd peoples-legal-knowledge-observatory
python3 -m unittest discover -s tests -v
```

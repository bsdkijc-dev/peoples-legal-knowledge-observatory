# Research & Pipeline Methodology

## 1. Controlled Domain Taxonomy (LK01–LK12)
Every knowledge item is classified under one primary domain (`LK01`–`LK12`), mapped to target audience(s) (`C1`–`C10`), and linked to `source_id` and `provision_id` keys.

## 2. 10-Step Knowledge Production Pipeline
1. **Source Identification**: Locate primary legal materials on official portals.
2. **Source Verification**: Verify status (`BERLAKU`, `DIUBAH`, `DICABUT`, `UJI_MATERI`), effective dates, and transitional rules.
3. **Legal Extraction**: Extract relevant articles/paragraphs into `Dataset 02`.
4. **Knowledge Structuring**: Populate structured JSON/CSV records conforming to `schemas/`.
5. **Plain-Language Transformation**: Draft accessible Indonesian explanations with hypothetical examples.
6. **Traceability Validation**: Run automated schema and referential-integrity checks (`src/validation/traceability_validator.py`).
7. **Legal Review**: Human legal expert verifies substantive accuracy.
8. **Accessibility Review**: Human reviewer verifies readability and format suitability.
9. **Publication Approval**: Explicit human sign-off (`Dataset 12`).
10. **Maintenance**: Monitor legal updates (`Dataset 11`) and trigger re-verification on amendments or MKRI/MA rulings.

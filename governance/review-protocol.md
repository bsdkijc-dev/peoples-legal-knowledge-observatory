# Human Legal & Accessibility Review Protocol

## 1. Two-Stage Review Gate
Every knowledge item (`Dataset 03`–`08`) must pass two independent human reviews before `approval_status` can transition to `APPROVED`:

### Stage A: Substantive Legal Review
- Verified by a qualified Indonesian legal reviewer.
- Checks: accuracy against `source_ids` and `provision_id`, current `legal_status` (amendments/MKRI rulings), absence of fabricated deadlines/fees, clear distinction between binding law and commentary, and explicit `limitations`.

### Stage B: Plain-Language & Accessibility Review
- Checks: clear Bahasa Indonesia, short sentences, explanation of technical legal terms, hypothetical labeling of examples, screen-reader friendliness, and low-bandwidth suitability.

## 2. Review Status Taxonomy
- `PENDING_HUMAN_REVIEW`
- `IN_LEGAL_REVIEW`
- `REVISION_REQUIRED`
- `LEGAL_APPROVED_PENDING_ACCESSIBILITY`
- `APPROVED`
- `REJECTED` / `ARCHIVED`

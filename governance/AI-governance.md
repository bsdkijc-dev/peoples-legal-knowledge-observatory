# AI Governance Policy

## 1. Role of AI Agents
PLKO uses 12 logical agents (Orchestrator, Official Source, Legal Status Verification, Extraction, Taxonomy, Plain Language, Q&A, Procedure Guide, Legal Literacy Research, Accessibility, Legal Update Monitoring, and Data Governance/Publication).

## 2. Fundamental Constraint
**AI may assist with all steps, but AI CANNOT independently certify legal validity or approve public release.**

## 3. Mandatory Agent Logging
Every agent execution must record in Dataset 12 (`Provenance and Publication Register`):
- `task_id` / `record_id`
- `source_id`
- `transformation_method`
- `AI_assistance_status`
- `human_reviewer`
- `quality_status`
- `publication_classification`
- `approval_status`
- `publication_date`

## 4. Separation of Duties
- The **Legal Status Verification Agent** must never approve its own legal interpretation.
- The **Plain Language Agent** must preserve legal meaning and retain `source_ids`.
- The **Publication Agent** is technically blocked from publishing any record lacking `approval_status == "APPROVED"`.

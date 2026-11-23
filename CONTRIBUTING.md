# Contributing to People's Legal Knowledge Observatory (PLKO)

Thank you for contributing to PLKO. Because legal misinformation can harm citizens' rights, all contributions must adhere strictly to our governance, verification, and plain-language standards.

## Mandatory Contribution Rules
1. **No Unverified Legal Claims**: Every substantive legal statement must cite an official primary Indonesian legal source (`source_id` in `sources/source-register.csv`) with a verified URL and effective date.
2. **No Official Endorsement Claims**: Never imply official endorsement by Mahkamah Agung RI or any government agency.
3. **Human Approval Gate**: All new plain-language articles, FAQs, procedure guides, and Q&A pairs must enter with `review_status: "PENDING_HUMAN_REVIEW"` and `approval_status: "DRAFT"`.
4. **Zero PII**: Never include personal data of litigants, judges, witnesses, or survey respondents.
5. **Run Validation Before PR**: Always run `python3 -m unittest discover -s tests -v` and `python3 -m src.validation.traceability_validator` before submitting changes.

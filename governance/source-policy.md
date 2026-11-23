# Authoritative Source Policy

## 1. Source Hierarchy
PLKO prioritizes official Indonesian primary legal repositories:
1. **Database Peraturan BPK (JDIH BPK)** (`https://peraturan.bpk.go.id`) — Consolidated statutory metadata, status, and judicial review notes.
2. **JDIHN (Badan Pembinaan Hukum Nasional)** (`https://jdihn.go.id`) — National Legal Documentation and Information Network.
3. **Mahkamah Agung RI & JDIH MA / e-Court** (`https://www.mahkamahagung.go.id`, `https://ecourt.mahkamahagung.go.id`) — Perma, SEMA, and judicial service procedures.
4. **Direktori Putusan Mahkamah Agung RI** (`https://putusan3.mahkamahagung.go.id`) — Official court decisions.
5. **Mahkamah Konstitusi RI** (`https://www.mkri.id`) — Constitutional Court decisions (Uji Materi UU terhadap UUD 1945).
6. **BPHN & SIDBANKUM** (`https://bphn.go.id`, `https://sidbankum.kemenkum.go.id`) — Legal aid (OBH) accreditation and national legal counseling.
7. **Official Ministries & Agencies** — Ministerial regulations and official public service portals.

## 2. Mandatory Source Metadata
Every registered source in `sources/source-register.csv` must record:
`source_id`, `document_title`, `issuing_authority`, `regulation_or_decision_number`, `publication_date`, `promulgation_date`, `effective_date`, `amendment_status`, `repeal_status`, `official_source_url`, `retrieval_date`, `legal_verification_status`.

## 3. Temporal & Status Verification
Online availability does not imply a regulation is in force. Researchers must check:
- Subsequent amendments (`perubahan`) or repeals (`pencabutan`),
- Constitutional Court (`MKRI`) or Supreme Court (`MA`) judicial review rulings,
- Transitional provisions (`ketentuan peralihan`), e.g., UU No. 1 Tahun 2023 (KUHP) effective 2 January 2026.

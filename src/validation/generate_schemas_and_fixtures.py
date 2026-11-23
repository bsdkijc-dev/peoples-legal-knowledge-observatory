import json
from pathlib import Path

BASE = Path("/working_dir/c_63d12d3880bbb2c8/peoples-legal-knowledge-observatory")
SCHEMAS_DIR = BASE / "schemas"
SYNTH_DIR = BASE / "data" / "synthetic"

DOMAINS = [f"LK{i:02d}" for i in range(1, 13)]

def make_schema(title, required, properties):
    return {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "title": title,
        "type": "array",
        "items": {
            "type": "object",
            "required": required,
            "properties": properties,
            "additionalProperties": False,
        },
    }

schemas = {
    "legal-sources.schema.json": make_schema(
        "Dataset 01: Official Legal Sources",
        ["source_id", "title", "document_type", "issuing_authority", "document_number", "publication_date", "effective_date", "legal_status", "official_url", "verification_status"],
        {
            "source_id": {"type": "string", "pattern": "^SRC-[A-Z0-9-]+$"},
            "title": {"type": "string", "minLength": 3},
            "document_type": {"type": "string"},
            "issuing_authority": {"type": "string"},
            "document_number": {"type": "string"},
            "publication_date": {"type": "string", "format": "date"},
            "effective_date": {"type": "string", "format": "date"},
            "legal_status": {"type": "string", "enum": ["BERLAKU", "DIUBAH", "DICABUT", "UJI_MATERI", "SYNTHETIC_TEST"]},
            "official_url": {"type": "string", "format": "uri"},
            "verification_status": {"type": "string", "enum": ["VERIFIED", "UNVERIFIED", "CONFLICT_FLAGGED", "SYNTHETIC_TEST"]},
        },
    ),
    "legal-provisions.schema.json": make_schema(
        "Dataset 02: Legal Provisions",
        ["provision_id", "source_id", "article_number", "paragraph_number", "original_text_reference", "legal_topic", "effective_period", "verification_status"],
        {
            "provision_id": {"type": "string", "pattern": "^PRV-[A-Z0-9-]+$"},
            "source_id": {"type": "string", "pattern": "^SRC-[A-Z0-9-]+$"},
            "article_number": {"type": "string"},
            "paragraph_number": {"type": "string"},
            "original_text_reference": {"type": "string"},
            "legal_topic": {"type": "string"},
            "effective_period": {"type": "string"},
            "verification_status": {"type": "string", "enum": ["VERIFIED", "UNVERIFIED", "CONFLICT_FLAGGED", "SYNTHETIC_TEST"]},
        },
    ),
    "knowledge-articles.schema.json": make_schema(
        "Dataset 03: Legal Knowledge Articles",
        ["knowledge_id", "title", "legal_domain", "audience", "plain_language_summary", "source_ids", "review_status", "last_verified_date"],
        {
            "knowledge_id": {"type": "string", "pattern": "^KNW-[A-Z0-9-]+$"},
            "title": {"type": "string"},
            "legal_domain": {"type": "string", "enum": DOMAINS},
            "audience": {"type": "array", "items": {"type": "string"}, "minItems": 1},
            "plain_language_summary": {"type": "string"},
            "source_ids": {"type": "array", "items": {"type": "string", "pattern": "^SRC-[A-Z0-9-]+$"}, "minItems": 1},
            "review_status": {"type": "string", "enum": ["PENDING_HUMAN_REVIEW", "IN_LEGAL_REVIEW", "APPROVED", "REJECTED", "SYNTHETIC_TEST"]},
            "last_verified_date": {"type": "string", "format": "date"},
        },
    ),
    "questions.schema.json": make_schema(
        "Dataset 04: Public Legal Questions",
        ["question_id", "question_text", "audience_category", "legal_domain", "source_ids", "response_status", "review_status"],
        {
            "question_id": {"type": "string", "pattern": "^QST-[A-Z0-9-]+$"},
            "question_text": {"type": "string"},
            "audience_category": {"type": "string"},
            "legal_domain": {"type": "string", "enum": DOMAINS},
            "source_ids": {"type": "array", "items": {"type": "string", "pattern": "^SRC-[A-Z0-9-]+$"}, "minItems": 1},
            "response_status": {"type": "string", "enum": ["DRAFTED", "ANSWERED", "ESCALATED", "SYNTHETIC_TEST"]},
            "review_status": {"type": "string", "enum": ["PENDING_HUMAN_REVIEW", "APPROVED", "REJECTED", "SYNTHETIC_TEST"]},
        },
    ),
    "answers.schema.json": make_schema(
        "Dataset 05: Verified Legal Answers",
        ["answer_id", "question_id", "answer_text", "source_provisions", "limitations", "reviewer_status", "verification_date"],
        {
            "answer_id": {"type": "string", "pattern": "^ANS-[A-Z0-9-]+$"},
            "question_id": {"type": "string", "pattern": "^QST-[A-Z0-9-]+$"},
            "answer_text": {"type": "string"},
            "source_provisions": {"type": "array", "items": {"type": "string", "pattern": "^PRV-[A-Z0-9-]+$"}, "minItems": 1},
            "limitations": {"type": "string"},
            "reviewer_status": {"type": "string", "enum": ["PENDING_HUMAN_REVIEW", "APPROVED", "REJECTED", "SYNTHETIC_TEST"]},
            "verification_date": {"type": "string", "format": "date"},
        },
    ),
    "procedure-guides.schema.json": make_schema(
        "Dataset 06: Legal Procedure Guides",
        ["guide_id", "procedure_name", "jurisdiction", "eligibility", "required_documents", "process_steps", "official_fee_reference", "official_service_url", "verification_date"],
        {
            "guide_id": {"type": "string", "pattern": "^GDE-[A-Z0-9-]+$"},
            "procedure_name": {"type": "string"},
            "jurisdiction": {"type": "string"},
            "eligibility": {"type": "string"},
            "required_documents": {"type": "array", "items": {"type": "string"}, "minItems": 1},
            "process_steps": {"type": "array", "items": {"type": "string"}, "minItems": 1},
            "official_fee_reference": {"type": "string"},
            "official_service_url": {"type": "string", "format": "uri"},
            "verification_date": {"type": "string", "format": "date"},
        },
    ),
    "terminology.schema.json": make_schema(
        "Dataset 07: Legal Terminology Dictionary",
        ["term_id", "legal_term", "plain_language_definition", "example", "domain", "source_reference", "review_status"],
        {
            "term_id": {"type": "string", "pattern": "^TRM-[A-Z0-9-]+$"},
            "legal_term": {"type": "string"},
            "plain_language_definition": {"type": "string"},
            "example": {"type": "string"},
            "domain": {"type": "string", "enum": DOMAINS},
            "source_reference": {"type": "string", "pattern": "^SRC-[A-Z0-9-]+$"},
            "review_status": {"type": "string", "enum": ["PENDING_HUMAN_REVIEW", "APPROVED", "REJECTED", "SYNTHETIC_TEST"]},
        },
    ),
    "audio-visual.schema.json": make_schema(
        "Dataset 08: Legal Audio and Visual Content",
        ["content_id", "format", "title", "script", "source_references", "target_audience", "accessibility_status", "approval_status"],
        {
            "content_id": {"type": "string", "pattern": "^AVC-[A-Z0-9-]+$"},
            "format": {"type": "string", "enum": ["AUDIO_SCRIPT", "INFOGRAPHIC", "LOW_BANDWIDTH_TEXT", "PRINTABLE_GUIDE"]},
            "title": {"type": "string"},
            "script": {"type": "string"},
            "source_references": {"type": "array", "items": {"type": "string", "pattern": "^SRC-[A-Z0-9-]+$"}, "minItems": 1},
            "target_audience": {"type": "string"},
            "accessibility_status": {"type": "string", "enum": ["PENDING_ACCESSIBILITY_REVIEW", "ACCESSIBLE_VERIFIED", "SYNTHETIC_TEST"]},
            "approval_status": {"type": "string", "enum": ["DRAFT", "PENDING_HUMAN_REVIEW", "APPROVED", "SYNTHETIC_TEST"]},
        },
    ),
    "literacy-assessment.schema.json": make_schema(
        "Dataset 09: Legal Literacy Assessment",
        ["assessment_id", "topic", "question", "correct_answer_reference", "difficulty", "learning_objective", "reviewer_status"],
        {
            "assessment_id": {"type": "string", "pattern": "^ASM-[A-Z0-9-]+$"},
            "topic": {"type": "string"},
            "question": {"type": "string"},
            "correct_answer_reference": {"type": "string", "pattern": "^PRV-[A-Z0-9-]+$"},
            "difficulty": {"type": "string", "enum": ["BASIC", "INTERMEDIATE", "ADVANCED"]},
            "learning_objective": {"type": "string"},
            "reviewer_status": {"type": "string", "enum": ["PENDING_HUMAN_REVIEW", "APPROVED", "SYNTHETIC_TEST"]},
        },
    ),
    "feedback.schema.json": make_schema(
        "Dataset 10: Legal Knowledge Feedback",
        ["feedback_id", "anonymous_user_category", "content_id", "comprehension_rating", "usefulness_rating", "feedback_category", "consent_status"],
        {
            "feedback_id": {"type": "string", "pattern": "^FBK-[A-Z0-9-]+$"},
            "anonymous_user_category": {"type": "string"},
            "content_id": {"type": "string"},
            "comprehension_rating": {"type": "integer", "minimum": 1, "maximum": 5},
            "usefulness_rating": {"type": "integer", "minimum": 1, "maximum": 5},
            "feedback_category": {"type": "string"},
            "consent_status": {"type": "string", "enum": ["CONSENT_GIVEN", "WITHDRAWN", "SYNTHETIC_TEST"]},
        },
    ),
    "legal-updates.schema.json": make_schema(
        "Dataset 11: Legal Update Register",
        ["update_id", "source_id", "change_type", "affected_provisions", "affected_content_ids", "impact_assessment", "review_status", "update_date"],
        {
            "update_id": {"type": "string", "pattern": "^UPD-[A-Z0-9-]+$"},
            "source_id": {"type": "string", "pattern": "^SRC-[A-Z0-9-]+$"},
            "change_type": {"type": "string", "enum": ["AMENDMENT", "REPEAL", "JUDICIAL_REVIEW", "IMPLEMENTING_REGULATION"]},
            "affected_provisions": {"type": "array", "items": {"type": "string"}},
            "affected_content_ids": {"type": "array", "items": {"type": "string"}},
            "impact_assessment": {"type": "string"},
            "review_status": {"type": "string", "enum": ["PENDING_HUMAN_REVIEW", "IN_REVIEW", "COMPLETED", "SYNTHETIC_TEST"]},
            "update_date": {"type": "string", "format": "date"},
        },
    ),
    "provenance.schema.json": make_schema(
        "Dataset 12: Provenance and Publication Register",
        ["record_id", "source_id", "transformation_method", "AI_assistance_status", "human_reviewer", "quality_status", "publication_classification", "approval_status", "publication_date"],
        {
            "record_id": {"type": "string", "pattern": "^PRVNC-[A-Z0-9-]+$"},
            "source_id": {"type": "string", "pattern": "^SRC-[A-Z0-9-]+$"},
            "transformation_method": {"type": "string"},
            "AI_assistance_status": {"type": "string", "enum": ["AI_ASSISTED", "HUMAN_ONLY"]},
            "human_reviewer": {"type": "string"},
            "quality_status": {"type": "string", "enum": ["PASSED_VALIDATION", "PENDING_REVIEW", "SYNTHETIC_TEST"]},
            "publication_classification": {"type": "string", "enum": ["INTERNAL_DRAFT", "SYNTHETIC_TEST", "APPROVED_PUBLIC"]},
            "approval_status": {"type": "string", "enum": ["DRAFT", "PENDING_HUMAN_REVIEW", "APPROVED", "SYNTHETIC_TEST"]},
            "publication_date": {"type": "string", "format": "date"},
        },
    ),
}

for fname, schema in schemas.items():
    (SCHEMAS_DIR / fname).write_text(json.dumps(schema, indent=2), encoding="utf-8")

synthetic_datasets = {
    "dataset_01_legal_sources.json": [
        {
            "source_id": "SRC-SYNTH-001",
            "title": "[SYNTHETIC TEST] Peraturan Contoh Tentang Akses Keadilan",
            "document_type": "Undang-Undang (Synthetic)",
            "issuing_authority": "Lembaga Legislatif (Synthetic)",
            "document_number": "UU No. 999 Tahun 2099 (Synthetic)",
            "publication_date": "2026-01-15",
            "effective_date": "2026-01-15",
            "legal_status": "SYNTHETIC_TEST",
            "official_url": "https://example.go.id/synthetic/uu-999-2099",
            "verification_status": "SYNTHETIC_TEST",
        }
    ],
    "dataset_02_legal_provisions.json": [
        {
            "provision_id": "PRV-SYNTH-001",
            "source_id": "SRC-SYNTH-001",
            "article_number": "Pasal 1 (Synthetic)",
            "paragraph_number": "Ayat (1)",
            "original_text_reference": "[SYNTHETIC TEST] Contoh teks ketentuan hukum untuk pengujian skema.",
            "legal_topic": "Akses Bantuan Hukum (Synthetic)",
            "effective_period": "2026-01-15 s.d. berlaku",
            "verification_status": "SYNTHETIC_TEST",
        }
    ],
    "dataset_03_knowledge_articles.json": [
        {
            "knowledge_id": "KNW-SYNTH-001",
            "title": "[SYNTHETIC TEST] Panduan Contoh Bantuan Hukum",
            "legal_domain": "LK10",
            "audience": ["General public", "Rural communities"],
            "plain_language_summary": "[SYNTHETIC TEST] Ringkasan bahasa sederhana untuk pengujian validasi.",
            "source_ids": ["SRC-SYNTH-001"],
            "review_status": "SYNTHETIC_TEST",
            "last_verified_date": "2026-11-23",
        }
    ],
    "dataset_04_questions.json": [
        {
            "question_id": "QST-SYNTH-001",
            "question_text": "[SYNTHETIC TEST] Bagaimana cara mengajukan bantuan hukum contoh?",
            "audience_category": "Rural communities",
            "legal_domain": "LK10",
            "source_ids": ["SRC-SYNTH-001"],
            "response_status": "SYNTHETIC_TEST",
            "review_status": "SYNTHETIC_TEST",
        }
    ],
    "dataset_05_answers.json": [
        {
            "answer_id": "ANS-SYNTH-001",
            "question_id": "QST-SYNTH-001",
            "answer_text": "[SYNTHETIC TEST] Jawaban contoh berbasis ketentuan sintetis.",
            "source_provisions": ["PRV-SYNTH-001"],
            "limitations": "Data sintetis untuk pengujian sistem, bukan informasi hukum nyata.",
            "reviewer_status": "SYNTHETIC_TEST",
            "verification_date": "2026-11-23",
        }
    ],
    "dataset_06_procedure_guides.json": [
        {
            "guide_id": "GDE-SYNTH-001",
            "procedure_name": "[SYNTHETIC TEST] Prosedur Contoh Permohonan Layanan",
            "jurisdiction": "Nasional (Synthetic)",
            "eligibility": "Warga negara memenuhi syarat contoh",
            "required_documents": ["KTP (Synthetic)", "Formulir Permohonan (Synthetic)"],
            "process_steps": ["Langkah 1: Siapkan dokumen contoh", "Langkah 2: Ajukan ke loket resmi contoh"],
            "official_fee_reference": "Gratis (Synthetic Test)",
            "official_service_url": "https://example.go.id/synthetic/layanan",
            "verification_date": "2026-11-23",
        }
    ],
    "dataset_07_terminology.json": [
        {
            "term_id": "TRM-SYNTH-001",
            "legal_term": "Gugatan Sederhana (Synthetic)",
            "plain_language_definition": "[SYNTHETIC TEST] Penjelasan istilah hukum dalam bahasa sehari-hari.",
            "example": "Contoh Hipotetis: Sengketa jual beli kecil.",
            "domain": "LK01",
            "source_reference": "SRC-SYNTH-001",
            "review_status": "SYNTHETIC_TEST",
        }
    ],
    "dataset_08_audio_visual.json": [
        {
            "content_id": "AVC-SYNTH-001",
            "format": "AUDIO_SCRIPT",
            "title": "[SYNTHETIC TEST] Naskah Audio Contoh 60 Detik",
            "script": "[SYNTHETIC TEST] Halo warga, ini adalah naskah audio contoh untuk pengujian aksesibilitas.",
            "source_references": ["SRC-SYNTH-001"],
            "target_audience": "Persons with disabilities",
            "accessibility_status": "SYNTHETIC_TEST",
            "approval_status": "SYNTHETIC_TEST",
        }
    ],
    "dataset_09_literacy_assessment.json": [
        {
            "assessment_id": "ASM-SYNTH-001",
            "topic": "Akses Bantuan Hukum (Synthetic)",
            "question": "[SYNTHETIC TEST] Manakah kanal resmi untuk mencari OBH terakreditasi?",
            "correct_answer_reference": "PRV-SYNTH-001",
            "difficulty": "BASIC",
            "learning_objective": "Mengidentifikasi layanan resmi bantuan hukum",
            "reviewer_status": "SYNTHETIC_TEST",
        }
    ],
    "dataset_10_feedback.json": [
        {
            "feedback_id": "FBK-SYNTH-001",
            "anonymous_user_category": "Workers and informal workers",
            "content_id": "KNW-SYNTH-001",
            "comprehension_rating": 5,
            "usefulness_rating": 5,
            "feedback_category": "CLARITY",
            "consent_status": "SYNTHETIC_TEST",
        }
    ],
    "dataset_11_legal_updates.json": [
        {
            "update_id": "UPD-SYNTH-001",
            "source_id": "SRC-SYNTH-001",
            "change_type": "AMENDMENT",
            "affected_provisions": ["PRV-SYNTH-001"],
            "affected_content_ids": ["KNW-SYNTH-001"],
            "impact_assessment": "[SYNTHETIC TEST] Simulasi deteksi perubahan regulasi.",
            "review_status": "SYNTHETIC_TEST",
            "update_date": "2026-11-23",
        }
    ],
    "dataset_12_provenance.json": [
        {
            "record_id": "PRVNC-SYNTH-001",
            "source_id": "SRC-SYNTH-001",
            "transformation_method": "SYNTHETIC_FIXTURE_GENERATION",
            "AI_assistance_status": "AI_ASSISTED",
            "human_reviewer": "UNASSIGNED_SYNTHETIC",
            "quality_status": "SYNTHETIC_TEST",
            "publication_classification": "SYNTHETIC_TEST",
            "approval_status": "SYNTHETIC_TEST",
            "publication_date": "2026-11-23",
        }
    ],
}

for fname, data in synthetic_datasets.items():
    (SYNTH_DIR / fname).write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")

print(f"Generated {len(schemas)} schemas and {len(synthetic_datasets)} synthetic datasets.")

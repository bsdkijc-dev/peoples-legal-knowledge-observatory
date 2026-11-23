import argparse
import json
import re
from pathlib import Path
from typing import Dict, List, Tuple

import jsonschema

SCHEMA_MAP = {
    "dataset_01_legal_sources.json": "legal-sources.schema.json",
    "dataset_02_legal_provisions.json": "legal-provisions.schema.json",
    "dataset_03_knowledge_articles.json": "knowledge-articles.schema.json",
    "dataset_04_questions.json": "questions.schema.json",
    "dataset_05_answers.json": "answers.schema.json",
    "dataset_06_procedure_guides.json": "procedure-guides.schema.json",
    "dataset_07_terminology.json": "terminology.schema.json",
    "dataset_08_audio_visual.json": "audio-visual.schema.json",
    "dataset_09_literacy_assessment.json": "literacy-assessment.schema.json",
    "dataset_10_feedback.json": "feedback.schema.json",
    "dataset_11_legal_updates.json": "legal-updates.schema.json",
    "dataset_12_provenance.json": "provenance.schema.json",
}

NIK_PATTERN = re.compile(r"\b\d{16}\b")


def validate_directory(data_dir: Path, schemas_dir: Path) -> Tuple[bool, List[str]]:
    errors: List[str] = []
    loaded: Dict[str, list] = {}

    for data_file, schema_file in SCHEMA_MAP.items():
        d_path = data_dir / data_file
        s_path = schemas_dir / schema_file
        if not d_path.exists():
            errors.append(f"Missing dataset file: {d_path}")
            continue
        if not s_path.exists():
            errors.append(f"Missing schema file: {s_path}")
            continue

        data = json.loads(d_path.read_text(encoding="utf-8"))
        schema = json.loads(s_path.read_text(encoding="utf-8"))
        try:
            jsonschema.validate(instance=data, schema=schema)
        except jsonschema.ValidationError as exc:
            errors.append(f"Schema validation failed for {data_file}: {exc.message}")
        loaded[data_file] = data

    if errors:
        return False, errors

    source_ids = {row["source_id"] for row in loaded["dataset_01_legal_sources.json"]}
    provision_ids = {row["provision_id"] for row in loaded["dataset_02_legal_provisions.json"]}
    question_ids = {row["question_id"] for row in loaded["dataset_04_questions.json"]}

    for row in loaded["dataset_02_legal_provisions.json"]:
        if row["source_id"] not in source_ids:
            errors.append(f"Orphan provision {row['provision_id']}: unknown source_id {row['source_id']}")

    for row in loaded["dataset_03_knowledge_articles.json"]:
        for sid in row["source_ids"]:
            if sid not in source_ids:
                errors.append(f"Orphan article {row['knowledge_id']}: unknown source_id {sid}")

    for row in loaded["dataset_04_questions.json"]:
        for sid in row["source_ids"]:
            if sid not in source_ids:
                errors.append(f"Orphan question {row['question_id']}: unknown source_id {sid}")

    for row in loaded["dataset_05_answers.json"]:
        if row["question_id"] not in question_ids:
            errors.append(f"Orphan answer {row['answer_id']}: unknown question_id {row['question_id']}")
        for pid in row["source_provisions"]:
            if pid not in provision_ids:
                errors.append(f"Orphan answer {row['answer_id']}: unknown provision_id {pid}")

    for row in loaded["dataset_07_terminology.json"]:
        if row["source_reference"] not in source_ids:
            errors.append(f"Orphan term {row['term_id']}: unknown source_reference {row['source_reference']}")

    for row in loaded["dataset_08_audio_visual.json"]:
        for sid in row["source_references"]:
            if sid not in source_ids:
                errors.append(f"Orphan AV content {row['content_id']}: unknown source_id {sid}")

    for row in loaded["dataset_09_literacy_assessment.json"]:
        if row["correct_answer_reference"] not in provision_ids:
            errors.append(f"Orphan assessment {row['assessment_id']}: unknown provision_id {row['correct_answer_reference']}")

    for row in loaded["dataset_11_legal_updates.json"]:
        if row["source_id"] not in source_ids:
            errors.append(f"Orphan update {row['update_id']}: unknown source_id {row['source_id']}")

    for row in loaded["dataset_12_provenance.json"]:
        if row["source_id"] not in source_ids:
            errors.append(f"Orphan provenance {row['record_id']}: unknown source_id {row['source_id']}")
        if row["approval_status"] == "APPROVED" and not row["human_reviewer"].strip():
            errors.append(f"Governance violation {row['record_id']}: APPROVED without human_reviewer")

    # PII check (16-digit Indonesian NIK)
    for fname, rows in loaded.items():
        text_blob = json.dumps(rows)
        if NIK_PATTERN.search(text_blob):
            errors.append(f"Potential PII (16-digit NIK) detected in {fname}")

    return len(errors) == 0, errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate PLKO datasets against schemas and source traceability rules.")
    parser.add_argument("--data-dir", type=Path, default=Path("data/synthetic"))
    parser.add_argument("--schemas-dir", type=Path, default=Path("schemas"))
    args = parser.parse_args()

    ok, errors = validate_directory(args.data_dir, args.schemas_dir)
    if ok:
        print(f"VALIDATION PASSED: All 12 datasets in {args.data_dir} passed schema and traceability checks.")
        return 0
    for err in errors:
        print(f"ERROR: {err}")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())

import json
import re
import shutil
import tempfile
import unittest
from pathlib import Path

import jsonschema

from src.validation.traceability_validator import SCHEMA_MAP, validate_directory

REPO_ROOT = Path(__file__).resolve().parents[1]
SCHEMAS_DIR = REPO_ROOT / "schemas"
SYNTH_DIR = REPO_ROOT / "data" / "synthetic"
INTERIM_DIR = REPO_ROOT / "data" / "interim"
NIK_PATTERN = re.compile(r"\b\d{16}\b")


class TestPLKOValidation(unittest.TestCase):
    def test_all_twelve_schemas_exist(self):
        self.assertEqual(len(SCHEMA_MAP), 12)
        for schema_name in SCHEMA_MAP.values():
            self.assertTrue((SCHEMAS_DIR / schema_name).exists(), f"Missing {schema_name}")

    def test_synthetic_datasets_pass_traceability(self):
        ok, errors = validate_directory(SYNTH_DIR, SCHEMAS_DIR)
        self.assertTrue(ok, f"Unexpected errors: {errors}")

    def test_interim_datasets_01_to_07_pass_schema_and_traceability(self):
        interim_files = [
            ("dataset_01_legal_sources.json", "legal-sources.schema.json"),
            ("dataset_02_legal_provisions.json", "legal-provisions.schema.json"),
            ("dataset_03_knowledge_articles.json", "knowledge-articles.schema.json"),
            ("dataset_04_questions.json", "questions.schema.json"),
            ("dataset_05_answers.json", "answers.schema.json"),
            ("dataset_06_procedure_guides.json", "procedure-guides.schema.json"),
            ("dataset_07_terminology.json", "terminology.schema.json"),
        ]
        loaded = {}
        for d_name, s_name in interim_files:
            d_path = INTERIM_DIR / d_name
            self.assertTrue(d_path.exists(), f"Missing {d_name}")
            data = json.loads(d_path.read_text(encoding="utf-8"))
            schema = json.loads((SCHEMAS_DIR / s_name).read_text(encoding="utf-8"))
            jsonschema.validate(instance=data, schema=schema)
            self.assertFalse(NIK_PATTERN.search(json.dumps(data)), f"Potential PII in {d_name}")
            loaded[d_name] = data

        source_ids = {r["source_id"] for r in loaded["dataset_01_legal_sources.json"]}
        provision_ids = {r["provision_id"] for r in loaded["dataset_02_legal_provisions.json"]}
        question_ids = {r["question_id"] for r in loaded["dataset_04_questions.json"]}

        for r in loaded["dataset_02_legal_provisions.json"]:
            self.assertIn(r["source_id"], source_ids)
        for r in loaded["dataset_03_knowledge_articles.json"]:
            for sid in r["source_ids"]:
                self.assertIn(sid, source_ids)
        for r in loaded["dataset_04_questions.json"]:
            for sid in r["source_ids"]:
                self.assertIn(sid, source_ids)
        for r in loaded["dataset_05_answers.json"]:
            self.assertIn(r["question_id"], question_ids)
            for pid in r["source_provisions"]:
                self.assertIn(pid, provision_ids)
        for r in loaded["dataset_07_terminology.json"]:
            self.assertIn(r["source_reference"], source_ids)

    def test_orphan_source_id_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            tmp_data = Path(tmp)
            for fname in SCHEMA_MAP:
                shutil.copy(SYNTH_DIR / fname, tmp_data / fname)

            articles_path = tmp_data / "dataset_03_knowledge_articles.json"
            articles = json.loads(articles_path.read_text(encoding="utf-8"))
            articles[0]["source_ids"] = ["SRC-NONEXISTENT-999"]
            articles_path.write_text(json.dumps(articles), encoding="utf-8")

            ok, errors = validate_directory(tmp_data, SCHEMAS_DIR)
            self.assertFalse(ok)
            self.assertTrue(any("unknown source_id SRC-NONEXISTENT-999" in e for e in errors))

    def test_approved_without_human_reviewer_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            tmp_data = Path(tmp)
            for fname in SCHEMA_MAP:
                shutil.copy(SYNTH_DIR / fname, tmp_data / fname)

            prov_path = tmp_data / "dataset_12_provenance.json"
            prov = json.loads(prov_path.read_text(encoding="utf-8"))
            prov[0]["approval_status"] = "APPROVED"
            prov[0]["human_reviewer"] = ""
            prov_path.write_text(json.dumps(prov), encoding="utf-8")

            ok, errors = validate_directory(tmp_data, SCHEMAS_DIR)
            self.assertFalse(ok)
            self.assertTrue(any("APPROVED without human_reviewer" in e for e in errors))


if __name__ == "__main__":
    unittest.main()

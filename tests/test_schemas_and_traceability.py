import json
import shutil
import tempfile
import unittest
from pathlib import Path

from src.validation.traceability_validator import SCHEMA_MAP, validate_directory

REPO_ROOT = Path(__file__).resolve().parents[1]
SCHEMAS_DIR = REPO_ROOT / "schemas"
SYNTH_DIR = REPO_ROOT / "data" / "synthetic"
INTERIM_DIR = REPO_ROOT / "data" / "interim"
NOTEBOOKS_DIR = REPO_ROOT / "notebooks"
WEBSITE_DIR = REPO_ROOT / "website"


class TestPLKOValidation(unittest.TestCase):
    def test_all_twelve_schemas_exist(self):
        self.assertEqual(len(SCHEMA_MAP), 12)
        for schema_name in SCHEMA_MAP.values():
            self.assertTrue((SCHEMAS_DIR / schema_name).exists(), f"Missing {schema_name}")

    def test_synthetic_datasets_pass_traceability(self):
        ok, errors = validate_directory(SYNTH_DIR, SCHEMAS_DIR)
        self.assertTrue(ok, f"Unexpected errors: {errors}")

    def test_all_twelve_interim_datasets_pass_traceability(self):
        ok, errors = validate_directory(INTERIM_DIR, SCHEMAS_DIR)
        self.assertTrue(ok, f"Unexpected interim errors: {errors}")

    def test_eight_notebooks_and_website_exist(self):
        nb_files = sorted(NOTEBOOKS_DIR.glob("0[1-8]_*.ipynb"))
        self.assertEqual(len(nb_files), 8, f"Expected 8 notebooks, found {len(nb_files)}")
        for nb in nb_files:
            parsed = json.loads(nb.read_text(encoding="utf-8"))
            self.assertEqual(parsed["nbformat"], 4)
        self.assertTrue((WEBSITE_DIR / "index.html").exists())
        self.assertTrue((WEBSITE_DIR / "styles.css").exists())
        self.assertTrue((WEBSITE_DIR / "app.js").exists())

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

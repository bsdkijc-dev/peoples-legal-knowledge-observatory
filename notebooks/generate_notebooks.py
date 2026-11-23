import json
from pathlib import Path

NB_DIR = Path("/working_dir/c_63d12d3880bbb2c8/peoples-legal-knowledge-observatory/notebooks")

def make_nb(title: str, description: str, code: str) -> dict:
    return {
        "nbformat": 4,
        "nbformat_minor": 5,
        "metadata": {
            "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
            "language_info": {"name": "python", "version": "3.11"},
        },
        "cells": [
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [f"# {title}\n", "\n", f"{description}\n", "\n", "> **SAFE MODE:** Reads `data/interim/` and `sources/source-register.csv`. Unreviewed records remain `PENDING_HUMAN_REVIEW`."],
            },
            {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": [line + "\n" for line in code.strip().splitlines()],
            },
        ],
    }

notebooks = {
    "01_source_inventory.ipynb": make_nb(
        "01 — Official Legal Source Inventory",
        "Inspects `sources/source-register.csv` and `dataset_01_legal_sources.json` by issuing authority and verification status.",
        """import pandas as pd
from pathlib import Path
df = pd.read_csv(Path("../sources/source-register.csv"))
print(f"Total registered official sources: {len(df)}")
display(df[["source_id", "regulation_or_decision_number", "effective_date", "legal_verification_status"]])
print("\\nCounts by issuing authority:")
print(df["issuing_authority"].value_counts())"""
    ),
    "02_legal_status.ipynb": make_nb(
        "02 — Legal Status, Amendments & Judicial Review",
        "Tracks `BERLAKU`, `DIUBAH`, `UJI_MATERI`, and `Dataset 11` legal updates.",
        """import json
import pandas as pd
from pathlib import Path
ds01 = pd.read_json(Path("../data/interim/dataset_01_legal_sources.json"))
ds11 = pd.read_json(Path("../data/interim/dataset_11_legal_updates.json"))
print("Source Legal Status Distribution:")
print(ds01["legal_status"].value_counts())
print("\\nRegistered 2026 Legal Updates:")
display(ds11[["update_id", "source_id", "change_type", "update_date", "review_status"]])"""
    ),
    "03_legal_knowledge_coverage.ipynb": make_nb(
        "03 — Legal Knowledge Domain & Audience Coverage",
        "Analyzes domain coverage (`LK01`–`LK12`) and target audience distribution across `Dataset 03` and `Dataset 04`.",
        """import pandas as pd
from pathlib import Path
ds03 = pd.read_json(Path("../data/interim/dataset_03_knowledge_articles.json"))
ds04 = pd.read_json(Path("../data/interim/dataset_04_questions.json"))
print("Articles per Legal Domain:")
print(ds03["legal_domain"].value_counts().sort_index())
print("\\nQuestions per Audience Category:")
print(ds04["audience_category"].value_counts())"""
    ),
    "04_plain_language_quality.ipynb": make_nb(
        "04 — Plain-Language Readability & Sentence Length",
        "Evaluates summary length and average words per sentence in `Dataset 03` and `Dataset 07`.",
        """import re
import pandas as pd
from pathlib import Path
ds03 = pd.read_json(Path("../data/interim/dataset_03_knowledge_articles.json"))
def avg_words_per_sentence(text):
    sents = [s.strip() for s in re.split(r"[.!?]+", text) if s.strip()]
    return round(sum(len(s.split()) for s in sents) / max(len(sents), 1), 1)
ds03["avg_words_per_sentence"] = ds03["plain_language_summary"].apply(avg_words_per_sentence)
display(ds03[["knowledge_id", "legal_domain", "avg_words_per_sentence", "review_status"]])"""
    ),
    "05_source_traceability.ipynb": make_nb(
        "05 — Source Traceability & Schema Validation",
        "Runs the deterministic `traceability_validator` across `data/interim/` and `data/synthetic/`.",
        """import sys
from pathlib import Path
sys.path.insert(0, str(Path("..").resolve()))
from src.validation.traceability_validator import validate_directory
ok, errors = validate_directory(Path("../data/interim"), Path("../schemas"))
print("Interim Validation Passed:", ok)
if errors:
    for e in errors:
        print(" -", e)"""
    ),
    "06_legal_literacy_assessment.ipynb": make_nb(
        "06 — Legal Literacy Assessment Blueprint",
        "Audits `Dataset 09` assessment items by difficulty, learning objective, and provision linkage.",
        """import pandas as pd
from pathlib import Path
ds09 = pd.read_json(Path("../data/interim/dataset_09_literacy_assessment.json"))
print(f"Total assessment items: {len(ds09)}")
print(ds09["difficulty"].value_counts())
display(ds09[["assessment_id", "topic", "difficulty", "correct_answer_reference", "reviewer_status"]])"""
    ),
    "07_content_freshness.ipynb": make_nb(
        "07 — Content Freshness & Review Backlog",
        "Monitors `last_verified_date` and `PENDING_HUMAN_REVIEW` backlog across `Dataset 03` and `Dataset 12`.",
        """import pandas as pd
from pathlib import Path
ds03 = pd.read_json(Path("../data/interim/dataset_03_knowledge_articles.json"))
ds12 = pd.read_json(Path("../data/interim/dataset_12_provenance.json"))
print("Article Review Status:")
print(ds03["review_status"].value_counts())
print("\\nProvenance Approval Status:")
print(ds12["approval_status"].value_counts())"""
    ),
    "08_public_accessibility.ipynb": make_nb(
        "08 — Public Accessibility & Multi-Format Readiness",
        "Reviews `Dataset 08` audio scripts, low-bandwidth text, and printable guides by target audience.",
        """import pandas as pd
from pathlib import Path
ds08 = pd.read_json(Path("../data/interim/dataset_08_audio_visual.json"))
print("Formats in Dataset 08:")
print(ds08["format"].value_counts())
display(ds08[["content_id", "format", "target_audience", "accessibility_status", "approval_status"]])"""
    ),
}

for name, nb in notebooks.items():
    (NB_DIR / name).write_text(json.dumps(nb, indent=2, ensure_ascii=False), encoding="utf-8")

print(f"Generated {len(notebooks)} notebooks.")

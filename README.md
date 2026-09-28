# AI-Assisted QA: CSV Data Validation & API Testing

A project demonstrating practical experience with **CSV files, spreadsheets, data validation, dataset inconsistency detection, API validation, and thoughtful use of ChatGPT/Claude**.

## What this project demonstrates

### Data / QA

- CSV test-data creation and validation
- Required-field and format validation
- Duplicate, missing-value, invalid-status and date-format detection
- Spreadsheet-based test-case management
- Data-findings tracking
- API payload/schema validation
- Automated regression tests with pytest

### AI-assisted workflow

AI is used as a **drafting and analysis assistant**, not as an authority.

Workflow:

Requirement → ChatGPT/Claude → Draft scenarios → Human review → Spreadsheet test cases → CSV test data → Automated validation → Findings


## Project structure

```text
ai-assisted-qa-data-validation/
├── .github/workflows/ci.yml
├── ai_prompts/
│   ├── test_case_generation.md
│   ├── edge_case_review.md
│   └── ai_output_review_checklist.md
├── data/
│   ├── valid_test_data.csv
│   └── inconsistent_test_data.csv
├── docs/
│   ├── qa_test_cases_and_data_findings.xlsx
│   └── ai_review_log.csv
├── src/
│   ├── api_validator.py
│   └── csv_validator.py
├── tests/
│   ├── test_api_validator.py
│   └── test_csv_validator.py
├── requirements.txt
└── README.md
```

## Run locally

```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

pip install -r requirements.txt
pytest -q
```

## Validate a CSV manually

```python
from src.csv_validator import validate_csv

issues = validate_csv("data/inconsistent_test_data.csv")

for issue in issues:
    print(issue)
```

## Example findings

The intentionally inconsistent dataset contains examples of:

- duplicate IDs
- missing required values
- unsupported status values
- invalid date formatting
- malformed/incorrect data combinations

These are deliberately seeded so the project demonstrates the ability to **find inconsistencies**, rather than merely describing data validation as a skill.

## Spreadsheet evidence

`docs/qa_test_cases_and_data_findings.xlsx` contains:

- test cases
- validation criteria
- expected results
- AI-assisted indicator
- human-review indicator
- documented data findings

## AI usage principles

The project demonstrates responsible AI-assisted QA:

1. Use ChatGPT/Claude to generate or critique an initial draft.
2. Check generated scenarios against requirements.
3. Reject unsupported assumptions.
4. Validate generated code and data independently.
5. Keep sensitive information out of prompts.
6. Record how AI output influenced the final test artifacts.

from pathlib import Path
from src.csv_validator import validate_csv

ROOT = Path(__file__).parents[1]

def test_valid_dataset_has_no_validation_errors():
    issues = validate_csv(ROOT / "data" / "valid_test_data.csv")
    assert issues == []

def test_inconsistent_dataset_detects_multiple_issue_types():
    issues = validate_csv(ROOT / "data" / "inconsistent_test_data.csv")
    messages = [i.message for i in issues]
    fields = [i.field for i in issues]

    assert any("Duplicate" in m for m in messages)
    assert "name" in fields
    assert "status" in fields
    assert "created_date" in fields

import csv
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import List
import re

EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")
ALLOWED_STATUS = {"active", "inactive"}

@dataclass
class Issue:
    row: int
    field: str
    value: str
    message: str

def validate_csv(path: str | Path) -> List[Issue]:
    issues: List[Issue] = []
    seen_ids = set()
    path = Path(path)

    with path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        required = {"test_id", "name", "email", "status", "created_date"}
        if set(reader.fieldnames or []) != required:
            missing = required - set(reader.fieldnames or [])
            extra = set(reader.fieldnames or []) - required
            if missing:
                issues.append(Issue(1, "headers", "", f"Missing columns: {sorted(missing)}"))
            if extra:
                issues.append(Issue(1, "headers", "", f"Unexpected columns: {sorted(extra)}"))

        for row_number, row in enumerate(reader, start=2):
            test_id = (row.get("test_id") or "").strip()
            name = (row.get("name") or "").strip()
            email = (row.get("email") or "").strip()
            status = (row.get("status") or "").strip().lower()
            created_date = (row.get("created_date") or "").strip()

            if not test_id:
                issues.append(Issue(row_number, "test_id", test_id, "Required value is missing"))
            elif test_id in seen_ids:
                issues.append(Issue(row_number, "test_id", test_id, "Duplicate test_id"))
            seen_ids.add(test_id)

            if not name:
                issues.append(Issue(row_number, "name", name, "Required value is missing"))

            if not EMAIL_RE.match(email):
                issues.append(Issue(row_number, "email", email, "Invalid email format"))

            if status not in ALLOWED_STATUS:
                issues.append(Issue(row_number, "status", status, f"Unexpected status; expected one of {sorted(ALLOWED_STATUS)}"))

            try:
                datetime.strptime(created_date, "%Y-%m-%d")
            except ValueError:
                issues.append(Issue(row_number, "created_date", created_date, "Expected YYYY-MM-DD"))

    return issues

def write_issue_report(issues: List[Issue], output: str | Path) -> None:
    output = Path(output)
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["row", "field", "value", "message"])
        for issue in issues:
            writer.writerow([issue.row, issue.field, issue.value, issue.message])

from dataclasses import dataclass
from typing import Any

@dataclass
class ApiValidationResult:
    passed: bool
    message: str

def validate_user_payload(payload: dict[str, Any]) -> list[ApiValidationResult]:
    results = []
    required = {"id", "name", "username", "email"}
    missing = required - payload.keys()
    results.append(ApiValidationResult(
        not missing,
        "All required API fields are present" if not missing else f"Missing fields: {sorted(missing)}"
    ))

    email = str(payload.get("email", ""))
    results.append(ApiValidationResult(
        "@" in email,
        "API email field has a plausible email format" if "@" in email else "API email field is invalid"
    ))
    return results

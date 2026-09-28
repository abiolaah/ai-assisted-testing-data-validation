from src.api_validator import validate_user_payload

def test_api_payload_passes_schema_checks():
    payload = {
        "id": 1,
        "name": "Leanne Graham",
        "username": "Bret",
        "email": "Sincere@april.biz",
    }
    results = validate_user_payload(payload)
    assert all(r.passed for r in results)

def test_api_payload_missing_required_field_fails():
    payload = {"id": 1, "name": "Leanne Graham", "username": "Bret"}
    results = validate_user_payload(payload)
    assert not all(r.passed for r in results)

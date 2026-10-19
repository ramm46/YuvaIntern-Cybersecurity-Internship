
import pytest

from backend.app.log_parser import parse_security_logs


VALID_CSV = """event_id,timestamp,event_type,source,actor,source_ip,action,outcome,details
EVT-001,2026-10-18T09:00:00Z,authentication,auth-service,alice,192.0.2.10,login,failure,Invalid password
"""


def test_valid_csv_is_parsed():
    result = parse_security_logs(VALID_CSV)

    assert result["valid_count"] == 1
    assert result["invalid_count"] == 0
    assert result["valid_rows"][0]["actor"] == "alice"


def test_empty_csv_is_rejected():
    with pytest.raises(ValueError, match="empty"):
        parse_security_logs("")


def test_missing_required_column_is_rejected():
    csv_content = "event_id,timestamp,actor\nEVT-001,2026-10-18T09:00:00Z,alice"

    with pytest.raises(ValueError, match="Missing required columns"):
        parse_security_logs(csv_content)


def test_invalid_row_is_reported():
    csv_content = (
        "event_id,timestamp,event_type,source,actor,source_ip,action,outcome,details\n"
        "EVT-001,2026-10-18T09:00:00Z,authentication,auth-service,alice,192.0.2.10,login,failure,Invalid password\n"
        ",2026-10-18T09:01:00Z,authentication,auth-service,bob,192.0.2.11,login,failure,Missing ID\n"
    )

    result = parse_security_logs(csv_content)

    assert result["valid_count"] == 1
    assert result["invalid_count"] == 1
    assert result["invalid_rows"][0]["row_number"] == 3


def test_oversized_csv_field_is_rejected():
    from backend.app.log_parser import MAX_CSV_FIELD_SIZE

    oversized_value = "x" * (MAX_CSV_FIELD_SIZE + 1)

    csv_content = (
        "event_id,timestamp,event_type,source,actor,"
        "action,outcome,details\n"
        f"EVT-001,2026-10-18T09:00:00Z,authentication,"
        f"auth-service,alice,login,failure,{oversized_value}\n"
    )

    with pytest.raises(ValueError, match="maximum allowed size"):
        parse_security_logs(csv_content)

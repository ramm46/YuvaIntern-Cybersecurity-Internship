
from fastapi.testclient import TestClient

from backend.app.main import app
from backend.app.detection_engine import detect_security_alerts
from backend.app.log_parser import parse_security_logs


client = TestClient(app)

HEADERS = (
    "event_id,timestamp,event_type,source,actor,action,outcome"
)


def make_event(event_id, timestamp, actor, action, outcome):
    return {
        "event_id": event_id,
        "timestamp": timestamp,
        "event_type": "authentication",
        "source": "test-system",
        "actor": actor,
        "action": action,
        "outcome": outcome,
    }


def test_duplicate_csv_headers_are_rejected():
    csv_data = (
        "event_id,timestamp,event_type,source,actor,actor,action,outcome\n"
        "1,2026-10-01T10:00:00Z,authentication,server,user,user,login,failure"
    )

    try:
        parse_security_logs(csv_data)
        assert False, "Duplicate headers should be rejected"
    except ValueError as exc:
        assert "duplicate" in str(exc).lower()


def test_unexpected_csv_column_is_rejected():
    csv_data = (
        HEADERS + ",unexpected_column\n"
        "1,2026-10-01T10:00:00Z,authentication,server,user,login,failure,extra"
    )

    try:
        parse_security_logs(csv_data)
        assert False, "Unexpected columns should be rejected"
    except ValueError as exc:
        assert "unexpected" in str(exc).lower()


def test_optional_columns_can_be_omitted():
    csv_data = (
        HEADERS + "\n"
        "1,2026-10-01T10:00:00Z,authentication,server,user,login,failure"
    )

    result = parse_security_logs(csv_data)

    assert result["valid_count"] == 1
    assert result["invalid_count"] == 0


def test_missing_row_values_are_reported():
    csv_data = (
        HEADERS + "\n"
        "1,2026-10-01T10:00:00Z,authentication,server,user,login"
    )

    result = parse_security_logs(csv_data)

    assert result["valid_count"] == 0
    assert result["invalid_count"] == 1


def test_invalid_timestamp_returns_http_400():
    csv_data = (
        HEADERS + "\n"
        "1,not-a-timestamp,authentication,server,user,login,failure"
    )

    response = client.post(
        "/api/analyze",
        files={"file": ("invalid_timestamp.csv", csv_data, "text/csv")},
    )

    assert response.status_code == 400


def test_security_admin_is_allowlisted():
    logs = [{
        "event_id": "P001",
        "timestamp": "2026-10-01T10:00:00Z",
        "event_type": "privilege_change",
        "source": "test-system",
        "actor": "security_admin",
        "action": "privilege_change",
        "outcome": "success",
    }]

    alerts = detect_security_alerts(logs)

    assert not any(alert["rule_id"] == "DET-03" for alert in alerts)


def test_login_failures_from_different_users_are_not_combined():
    logs = []

    for i in range(4):
        logs.append(
            make_event(
                f"A{i}",
                f"2026-10-01T10:0{i}:00Z",
                "alice",
                "login",
                "failure",
            )
        )

    logs.append(
        make_event(
            "B1",
            "2026-10-01T10:05:00Z",
            "bob",
            "login",
            "failure",
        )
    )

    alerts = detect_security_alerts(logs)

    assert not any(alert["rule_id"] == "DET-01" for alert in alerts)


def test_det01_detects_five_failures_at_ten_minute_boundary():
    logs = [
        make_event("E1", "2026-10-01T10:00:00Z", "alice", "login", "failure"),
        make_event("E2", "2026-10-01T10:02:00Z", "alice", "login", "failure"),
        make_event("E3", "2026-10-01T10:04:00Z", "alice", "login", "failure"),
        make_event("E4", "2026-10-01T10:06:00Z", "alice", "login", "failure"),
        make_event("E5", "2026-10-01T10:10:00Z", "alice", "login", "failure"),
    ]

    alerts = detect_security_alerts(logs)

    det01 = [a for a in alerts if a["rule_id"] == "DET-01"]

    assert len(det01) == 1
    assert set(det01[0]["event_ids"]) == {"E1", "E2", "E3", "E4", "E5"}

def test_det01_excludes_failure_outside_ten_minute_window():
    logs = [
        make_event("E1", "2026-10-01T10:00:00Z", "alice", "login", "failure"),
        make_event("E2", "2026-10-01T10:01:00Z", "alice", "login", "failure"),
        make_event("E3", "2026-10-01T10:02:00Z", "alice", "login", "failure"),
        make_event("E4", "2026-10-01T10:03:00Z", "alice", "login", "failure"),
        make_event("E5", "2026-10-01T10:10:01Z", "alice", "login", "failure"),
    ]

    alerts = detect_security_alerts(logs)

    assert not any(a["rule_id"] == "DET-01" for a in alerts)
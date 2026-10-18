
from io import BytesIO

from fastapi.testclient import TestClient

from backend.app.main import app


client = TestClient(app)


VALID_CSV = b"""event_id,timestamp,event_type,source,actor,source_ip,action,outcome,details
EVT-001,2026-10-18T09:00:00Z,authentication,auth-service,alice,192.0.2.10,login,failure,Invalid password
EVT-002,2026-10-18T09:01:00Z,authentication,auth-service,alice,192.0.2.10,login,failure,Invalid password
EVT-003,2026-10-18T09:02:00Z,authentication,auth-service,alice,192.0.2.10,login,failure,Invalid password
EVT-004,2026-10-18T09:03:00Z,authentication,auth-service,alice,192.0.2.10,login,failure,Invalid password
EVT-005,2026-10-18T09:04:00Z,authentication,auth-service,alice,192.0.2.10,login,failure,Invalid password
EVT-006,2026-10-18T09:05:00Z,authentication,auth-service,alice,192.0.2.10,login,success,Login successful
"""


def test_health_check():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["status"] == "running"


def test_csv_upload_detects_security_alerts():
    response = client.post(
        "/api/analyze",
        files={
            "file": (
                "test_logs.csv",
                BytesIO(VALID_CSV),
                "text/csv",
            )
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert data["summary"]["total_rows"] == 6
    assert data["summary"]["valid_rows"] == 6
    assert data["summary"]["invalid_rows"] == 0
    assert data["summary"]["alerts_detected"] == 2

    rule_ids = {alert["rule_id"] for alert in data["alerts"]}

    assert "DET-01" in rule_ids
    assert "DET-02" in rule_ids


def test_non_csv_file_is_rejected():
    response = client.post(
        "/api/analyze",
        files={
            "file": (
                "notes.txt",
                BytesIO(b"not a CSV"),
                "text/plain",
            )
        },
    )

    assert response.status_code == 400
    assert response.json()["detail"] == "Please upload a CSV file."


def test_empty_csv_file_is_rejected():
    response = client.post(
        "/api/analyze",
        files={
            "file": (
                "empty.csv",
                BytesIO(b""),
                "text/csv",
            )
        },
    )

    assert response.status_code == 400
    assert response.json()["detail"] == "Uploaded file is empty."


def test_csv_with_missing_columns_is_rejected():
    csv_content = b"event_id,timestamp,actor\nEVT-001,2026-10-18T09:00:00Z,alice"

    response = client.post(
        "/api/analyze",
        files={
            "file": (
                "invalid.csv",
                BytesIO(csv_content),
                "text/csv",
            )
        },
    )

    assert response.status_code == 400
    assert "Missing required columns" in response.json()["detail"]

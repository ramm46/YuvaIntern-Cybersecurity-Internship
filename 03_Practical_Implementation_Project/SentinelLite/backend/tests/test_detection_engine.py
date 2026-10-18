
from backend.app.detection_engine import detect_security_alerts


def make_log(event_id, timestamp, actor="alice",
             event_type="authentication", action="login",
             outcome="failure"):
    return {
        "event_id": event_id,
        "timestamp": timestamp,
        "event_type": event_type,
        "source": "auth-service",
        "actor": actor,
        "source_ip": "192.0.2.10",
        "action": action,
        "outcome": outcome,
        "details": "Test security event",
    }


def test_det01_detects_five_login_failures():
    logs = [
        make_log(f"EVT-{i}", f"2026-10-18T09:0{i}:00Z")
        for i in range(5)
    ]

    alerts = detect_security_alerts(logs)

    assert any(alert["rule_id"] == "DET-01" for alert in alerts)


def test_det02_detects_success_after_five_failures():
    logs = [
        make_log(f"EVT-{i}", f"2026-10-18T09:0{i}:00Z")
        for i in range(5)
    ]
    logs.append(
        make_log(
            "EVT-006",
            "2026-10-18T09:06:00Z",
            outcome="success",
        )
    )

    alerts = detect_security_alerts(logs)

    assert any(
        alert["rule_id"] == "DET-02"
        and alert["severity"] == "High"
        for alert in alerts
    )


def test_det03_detects_unapproved_privilege_change():
    logs = [
        make_log(
            "EVT-100",
            "2026-10-18T10:00:00Z",
            actor="alice",
            event_type="authorization",
            action="privilege_change",
            outcome="success",
        )
    ]

    alerts = detect_security_alerts(logs)

    assert any(
        alert["rule_id"] == "DET-03"
        and alert["severity"] == "Medium"
        for alert in alerts
    )


def test_no_alert_for_fewer_than_five_failures():
    logs = [
        make_log(f"EVT-{i}", f"2026-10-18T09:0{i}:00Z")
        for i in range(4)
    ]

    alerts = detect_security_alerts(logs)

    assert not any(
        alert["rule_id"] in {"DET-01", "DET-02"}
        for alert in alerts
    )


def test_approved_admin_does_not_trigger_det03():
    logs = [
        make_log(
            "EVT-200",
            "2026-10-18T10:00:00Z",
            actor="admin",
            event_type="authorization",
            action="privilege_change",
            outcome="success",
        )
    ]

    alerts = detect_security_alerts(logs)

    assert not any(alert["rule_id"] == "DET-03" for alert in alerts)

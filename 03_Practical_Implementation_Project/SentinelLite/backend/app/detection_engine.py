
from datetime import datetime, timedelta, timezone


FAILURE_THRESHOLD = 5
TIME_WINDOW_MINUTES = 10

# Synthetic allowlist for the MVP.
# Replace these sample values with your approved test actors.
PRIVILEGED_ACTORS_ALLOWLIST = {"admin", "security_admin"}


def parse_timestamp(value: str) -> datetime:
    """Parse an ISO 8601 timestamp and normalize it to UTC."""
    timestamp = datetime.fromisoformat(value.replace("Z", "+00:00"))

    if timestamp.tzinfo is None:
        timestamp = timestamp.replace(tzinfo=timezone.utc)

    return timestamp.astimezone(timezone.utc)


def detect_security_alerts(logs: list[dict]) -> list[dict]:
    """Detect brute-force attempts, suspicious successful logins,
    and privilege changes by actors outside the allowlist.
    """
    alerts = []
    failed_logins = {}

    # Sort logs chronologically before analyzing them.
    sorted_logs = sorted(
        logs,
        key=lambda log: parse_timestamp(log["timestamp"])
    )

    for log in sorted_logs:
        actor = log["actor"]
        event_type = log["event_type"].strip().lower()
        action = log["action"].strip().lower()
        outcome = log["outcome"].strip().lower()
        timestamp = parse_timestamp(log["timestamp"])

        # DET-01 and DET-02: Authentication failure tracking.
        is_login = (
            event_type == "authentication"
            or action in {"login", "log in", "sign_in", "signin"}
        )

        if is_login and outcome == "failure":
            actor_failures = failed_logins.setdefault(actor, [])

            # Keep only failures within the preceding 10 minutes.
            actor_failures[:] = [
                failed_time
                for failed_time in actor_failures
                if timedelta(0) <= timestamp - failed_time
                <= timedelta(minutes=TIME_WINDOW_MINUTES)
            ]

            actor_failures.append(timestamp)

            if len(actor_failures) == FAILURE_THRESHOLD:
                alerts.append({
                    "rule_id": "DET-01",
                    "severity": "Medium",
                    "actor": actor,
                    "timestamp": log["timestamp"],
                    "description": (
                        f"{actor} had at least {FAILURE_THRESHOLD} "
                        "login failures within 10 minutes."
                    ),
                    "event_ids": [
                        item["event_id"]
                        for item in sorted_logs
                        if item["actor"] == actor
                        and (
                            item["event_type"].strip().lower()
                            == "authentication"
                            or item["action"].strip().lower()
                            in {"login", "log in", "sign_in", "signin"}
                        )
                        and item["outcome"].strip().lower() == "failure"
                        and timedelta(0)
                        <= timestamp - parse_timestamp(item["timestamp"])
                        <= timedelta(minutes=TIME_WINDOW_MINUTES)
                    ],
                })

        # DET-02: A successful login following at least 5 failures.
        elif is_login and outcome == "success":
            recent_failures = [
                failed_time
                for failed_time in failed_logins.get(actor, [])
                if timedelta(0) <= timestamp - failed_time
                <= timedelta(minutes=TIME_WINDOW_MINUTES)
            ]

            if len(recent_failures) >= FAILURE_THRESHOLD:
                alerts.append({
                    "rule_id": "DET-02",
                    "severity": "High",
                    "actor": actor,
                    "timestamp": log["timestamp"],
                    "description": (
                        f"{actor} successfully logged in within 10 minutes "
                        "after at least 5 login failures."
                    ),
                    "event_ids": [log["event_id"]],
                })

        # DET-03: Privilege changes by actors outside the allowlist.
        if action == "privilege_change":
            if actor not in PRIVILEGED_ACTORS_ALLOWLIST:
                alerts.append({
                    "rule_id": "DET-03",
                    "severity": "Medium",
                    "actor": actor,
                    "timestamp": log["timestamp"],
                    "description": (
                        f"{actor} performed a privilege change "
                        "but is not in the approved actor allowlist."
                    ),
                    "event_ids": [log["event_id"]],
                })

    return alerts

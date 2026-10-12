
# Incident Response Simulator
# Safe educational simulation: no files are modified or isolated.

print("=== Incident Response Simulator ===")

incident_type = input(
    "Enter alert type (ransomware/phishing/unknown): "
).strip().lower()

severity = input(
    "Enter severity (low/medium/high): "
).strip().lower()

valid_types = ["ransomware", "phishing", "unknown"]
valid_severities = ["low", "medium", "high"]

if incident_type not in valid_types:
    print("Invalid alert type. Please record the alert for review.")

elif severity not in valid_severities:
    print("Invalid severity. Please reassess the alert.")

else:
    print("\n--- Incident Assessment ---")
    print("Alert type:", incident_type)
    print("Severity:", severity)

    if incident_type == "ransomware":
        print("Detection: Possible ransomware activity.")
        print("Containment: Escalate and isolate affected device")
        print("only through an approved response procedure.")

    elif incident_type == "phishing":
        print("Detection: Possible phishing activity.")
        print("Containment: Report the message and block indicators")
        print("through approved security procedures.")

    else:
        print("Detection: Alert needs further investigation.")
        print("Containment: Follow the incident response policy.")

    if severity == "high":
        print("Priority: Urgent security team escalation.")
    elif severity == "medium":
        print("Priority: Prompt investigation required.")
    else:
        print("Priority: Review and monitor according to policy.")

    print("Recovery: Verify system safety before restoration.")
    print("Documentation: Record evidence, actions, and timestamps.")

print("\nSimulation complete. No real system actions were performed.")

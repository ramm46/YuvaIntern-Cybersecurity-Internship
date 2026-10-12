
## Practical: Incident Response Simulator

### Objective

To simulate incident classification and response recommendations for ransomware, phishing, and unknown alerts using Python.

### Implementation

File: `incident_response_simulator.py`

The program accepts an alert type and severity, validates both inputs, and displays response guidance.

### Test Summary

- Total test cases: 11
- Valid alert/severity combinations: 9
- Invalid-input tests: 2
- Invalid alert type test: Pass
- Invalid severity test: Pass

### Test Results

| Test | Input              | Expected Behavior                             | Observed Result           | Status|
|------|--------------------|-----------------------------------------------|---------------------------|-------|
| 1    | ransomware, low    | Ransomware response; review and monitor       | Matched                   | Pass  |
| 2    | ransomware, medium | Ransomware response; prompt investigation     | Matched                   | Pass  |
| 3    | ransomware, high   | Ransomware response; urgent escalation        | Matched                   | Pass  |
| 4    | phishing, low      | Phishing response; review and monitor         | Matched                   | Pass  |
| 5    | phishing, medium   | Phishing response; prompt investigation       | Matched                   | Pass  |
| 6    | phishing, high     | Phishing response; urgent escalation          | Matched                   | Pass  |
| 7    | unknown, low       | Further investigation; review and monitor     | Matched                   | Pass  |
| 8    | unknown, medium    | Further investigation; prompt investigation   | Matched                   | Pass  |
| 9    | unknown, high      | Further investigation; urgent escalation      | Matched                   | Pass  |
| 10   | malware, high      | Reject invalid alert type                     | Invalid alert type message| Pass  |
| 11   | ransomware, urgent | Reject invalid severity                       | Invalid severity message  | Pass  |

### Incident Response Workflow

1. Detection: Identify and record a potential security alert.
2. Analysis: Classify the alert and assess its severity.
3. Containment: Follow approved procedures to limit the incident's impact.
4. Eradication and recovery: Remove the threat, verify system safety, and restore services through authorized procedures.
5. Lessons learned: Document the timeline, evidence, decisions, and improvements.

### Learning Outcome

I implemented a Python incident response simulation and tested three alert categories across three severity levels. I also tested invalid alert types and invalid severity values.

### Limitations

This program is an educational simulation. It does not detect real malware, isolate devices, investigate logs, or perform recovery actions. Its output is guidance only; actual incident handling must follow the organization's response plan and authorization requirements.

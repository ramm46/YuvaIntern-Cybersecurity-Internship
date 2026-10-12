
## Practical: Security Checklist Validator

### Objective

To create a Python program that records responses to five security controls and calculates pass count, fail count, and completion percentage.

### Implementation

File: `security_checklist_validator.py`

Controls assessed:
1. Firewall enabled
2. Operating system updated
3. Multi-factor authentication enabled
4. Important data backups available
5. Least-privilege access configured

### Test Results

| Test | Inputs                     | Expected Result            | Observed Result                        | Status |
|------|----------------------------|----------------------------|----------------------------------------|--------|
| 1    | All five answers are `yes` | 5 passed, 0 failed, 100%   | 5 passed, 0 failed, 100.0%             | Pass   |
| 2    | Three `yes`, two `no`      | 3 passed, 2 failed, 60%    | 3 passed, 2 failed, 60.0%              | Pass   |
| 3    | Invalid answer `yrs`       | Reject input and ask again | Invalid input message; prompt repeated | Pass   |

### Results Summary

- Security controls assessed per run: 5
- Test runs: 2 complete checklist assessments
- Additional input-validation test: 1
- All-yes completion: 100%
- Partial-compliance completion: 60%

### Limitations

The program relies on user-provided answers. It does not independently inspect firewall settings, software updates, MFA configuration, backups, or access permissions. The completion percentage is a checklist score, not a formal security certification or risk rating.

### Learning Outcome

I implemented a Python checklist validator with input validation, pass/fail counting, and percentage calculation. I tested full compliance, partial compliance, and invalid input handling.

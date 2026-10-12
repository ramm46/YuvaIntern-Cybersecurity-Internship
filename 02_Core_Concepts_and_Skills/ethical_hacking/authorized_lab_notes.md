
## Practical: Authorization and Scope Checker

### Objective

To create a Python program that checks whether explicit written permission and an approved testing scope have been confirmed before authorized security testing.

### Implementation

File: `authorization_checker.py`

Language: Python

Inputs:
- Written authorization: yes/no
- Target within approved scope: yes/no

### Test Results

| Test | Permission | In Scope | Expected Result              | Actual Result                                    | Status |
|------|------------|----------|------------------------------|--------------------------------------------------|--------|
| 1    | yes        | yes      | Check passed                 | Check passed                                     | Pass   |
| 2    | yes        | no       | Stop: target out of scope    | Stop: target is not confirmed to be in scope     | Pass   |
| 3    | no         | no       | Stop: authorization required | Stop: explicit written authorization is required | Pass   |
| 4    | no         | yes      | Stop: authorization required | Stop: explicit written authorization is required | Pass   |

### Summary

- Total test cases: 4
- Passed: 4
- Failed: 0
- Pass rate: 100%

### Learning Outcome

I learned that ethical security testing requires both explicit authorization and an approved scope. I implemented and tested a Python checker for these conditions.

### Limitation

This program only evaluates the user's input. It does not verify actual written permission or independently confirm the target's scope. Security testing must remain within the documented authorization and agreed limits.

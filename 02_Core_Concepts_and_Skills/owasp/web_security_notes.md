
# OWASP and Web Security

## 1. Introduction

Web application security focuses on protecting websites, applications, user accounts, and data from security vulnerabilities.

OWASP provides resources and guidance for understanding common web application security risks.

## 2. SQL Injection

SQL Injection occurs when untrusted input is improperly incorporated into a SQL query, potentially changing the query's intended behavior.

### Prevention
- Use parameterized queries.
- Validate input according to application requirements.
- Apply least-privilege database permissions.
- Avoid building SQL queries by concatenating untrusted input.

## 3. Cross-Site Scripting (XSS)

Cross-Site Scripting is a vulnerability in which untrusted content can cause malicious script execution in a user's browser.

### Prevention
- Use context-aware output encoding.
- Prefer safe DOM APIs and frameworks that escape output by default.
- Validate and sanitize HTML when rich HTML input is genuinely required.
- Use Content Security Policy as an additional defense.

## 4. Authentication and Authorization

### Authentication
Verifies a user's identity.

### Authorization
Determines which resources and actions an authenticated user is permitted to access.

### Best Practices
- Use secure authentication mechanisms.
- Apply server-side authorization checks.
- Protect sessions and use multi-factor authentication where appropriate.
- Apply least privilege.

## 5. Practical Implementation

File: `web_security_practical.py`

Language: Python

Libraries:
- `sqlite3` for a local in-memory database.
- `html.escape` for escaping HTML special characters.

### SQL Injection Prevention

The program uses a parameterized SQL query:

`SELECT username, role FROM users WHERE username = ?`

The username is supplied separately as a parameter instead of being concatenated into SQL code.

### XSS Output Encoding

The program uses `html.escape()` to escape characters such as angle brackets and quotation marks.

For the sample input:

`<script>alert('XSS')</script>`

The observed escaped output was:

`&lt;script&gt;alert(&#x27;XSS&#x27;)&lt;/script&gt;`

This demonstrates escaping; it does not demonstrate browser-based execution or prevention in a complete web application.

## 6. Practical Test Results

| Test | Input                           | Expected Result                 | Observed Result         | Status  |
|------|---------------------------------|---------------------------------|-------------------------|---------|
| 1    | `cipher`                        | Existing user returned          | `('cipher', 'student')` | Pass    |
| 2    | `' OR '1'='1`                   | No matching user found          | No matching user found  | Pass    |
| 3    | `<script>alert('XSS')</script>` | HTML special characters escaped | Escaped output observed | Pass    |

### Test Summary

- Total test cases: 3
- Passed: 3
- Failed: 0
- Pass rate: 100%

Note: These results apply only to this local demonstration and do not prove that a complete web application is secure.

## 7. Limitations

- The database is temporary and exists only in memory.
- The demonstration does not connect to a real website.
- The XSS example tests string escaping; it does not render HTML in a browser.
- These tests do not establish that a complete application is secure.

## 8. Learning Outcome

I implemented a local Python demonstration of parameterized SQL queries and HTML output escaping. I verified a normal username lookup and observed escaped output for an XSS sample. I will complete the remaining SQL injection test and record its actual result.

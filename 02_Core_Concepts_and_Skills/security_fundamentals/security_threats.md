# Common Cybersecurity Threats

## Introduction

Cybersecurity threats are potential dangers that can affect the
confidentiality, integrity, or availability of systems and information.

Understanding common threats helps security professionals identify risks,
analyze incidents, and select appropriate security controls.

---

## 1. Malware

Malware means malicious software. It is software intentionally created to
damage systems, steal information, disrupt operations, or gain
unauthorized access.

### Common Types

- Virus - Malicious code that can attach to files or programs.
- Worm - Malware that can spread across networks.
- Trojan - Malicious software disguised as legitimate software.
- Spyware - Software that secretly collects information.
- Ransomware - Malware that encrypts or blocks access to data.

### Example

A user downloads a fake application. After running it, the application
installs malicious software on the computer.

---

## 2. Phishing

Phishing is a social-engineering technique in which an attacker
pretends to be a trusted person or organization to trick a victim into
revealing information or performing an unsafe action.

### Common Targets

- Passwords
- Login credentials
- OTPs
- Banking information
- Personal information

### Example

An attacker sends an email claiming that a college account will be
disabled unless the student clicks a link and verifies the password.
The link leads to a fake login page.

---

## 3. Ransomware

Ransomware is a type of malware that typically encrypts or blocks access
to data and demands payment from the victim.

### Example

A company's files are encrypted by ransomware and the attacker demands
payment to provide recovery instructions or a decryption mechanism.

### Security Measures

- Regular backups
- Endpoint protection
- Security awareness
- Software updates
- Access controls

---

## 4. Distributed Denial-of-Service (DDoS)

DDoS stands for Distributed Denial-of-Service.

In a DDoS attack, many systems or sources send a large number of requests
or traffic toward a target service, potentially making it unavailable
to legitimate users.

### Example

Thousands of compromised devices send requests to a company's website,
causing the website to become unavailable.

### Primary Impact

DDoS attacks primarily affect **Availability**.

---

## 5. Social Engineering

Social engineering involves manipulating people into revealing
information or performing actions that may compromise security.

### Common Techniques

- Impersonation
- Creating urgency
- Fake technical support
- Baiting
- Pretexting

### Example

An attacker pretends to be an IT administrator and asks an employee
for their password over the phone.

### Important Note

Phishing is one type of social-engineering technique.

---

## 6. Credential Attacks

Credential attacks attempt to obtain or use usernames and passwords
without authorization.

### Common Types

- Brute-force attacks
- Password spraying
- Credential stuffing
- Dictionary attacks

### Example

An attacker repeatedly tries different passwords against an employee's
account to gain unauthorized access.

---

## 7. Man-in-the-Middle (MITM)

A Man-in-the-Middle attack occurs when an attacker gets between two
communicating parties and attempts to intercept or manipulate their
communication.

### Basic Concept

User <--> Attacker <--> Server

Instead of:

User <----------------> Server

### Example

An attacker on an insecure network attempts to intercept communication
between a user and a server.

---

## 8. Insider Threat

An insider threat occurs when a person with legitimate access misuses
that access or accidentally causes a security incident.

### Types

- Malicious insider
- Negligent insider
- Accidental insider

### Example

An employee intentionally copies confidential customer information and
sends it to an unauthorized third party.

---

# Threat Analysis Practical

## Scenario 1: Phishing

### Scenario

An employee receives an email saying:

"Your Microsoft account will be disabled today. Verify your password
using this link."

The link opens a fake login page.

### Threat

Phishing

### Reason

The attacker uses a fake message and website to trick the victim into
revealing credentials.

---

## Scenario 2: Ransomware

### Scenario

A company discovers that its files have been encrypted and a message
demands cryptocurrency for recovery.

### Threat

Ransomware

### Reason

The malicious software has encrypted the company's data and the attacker
is demanding payment.

---

## Scenario 3: Insider Threat

### Scenario

An employee deliberately downloads confidential customer information
and sends it to an unauthorized third party.

### Threat

Insider Threat

### Reason

A person with legitimate access intentionally misuses confidential
company information.

---

## Scenario 4: Credential Attack

### Scenario

An attacker repeatedly attempts thousands of passwords against an
employee's account.

### Threat

Credential Attack

### Reason

The attacker is attempting to gain unauthorized access by guessing or
trying different credentials.

---

## Scenario 5: DDoS

### Scenario

A website receives enormous volumes of requests from a distributed
network of compromised machines and becomes unavailable.

### Threat

Distributed Denial-of-Service (DDoS)

### Reason

The large volume of traffic overwhelms the service and affects its
availability.

---

# Threat Classification Summary

| Scenario                         | Threat            |
|----------------------------------|-------------------|
| Fake login email                 | Phishing          |
| Files encrypted for payment      | Ransomware        |
| Employee leaks confidential data | Insider Threat    |
| Repeated password attempts       | Credential Attack |
| Website overwhelmed by traffic   | DDoS              |

---

# Learning Outcome

Through this exercise, I learned to identify common cybersecurity
threats and distinguish between phishing, ransomware, DDoS, social
engineering, credential attacks, MITM attacks, malware, and insider
threats.

I also practised classifying realistic security incidents according to
the threat involved and understanding their potential impact on
information and systems.
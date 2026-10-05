# CIA Triad

## Introduction

The CIA Triad is a fundamental information security model consisting of
Confidentiality, Integrity, and Availability.

These three principles help organizations protect information and
maintain secure and reliable systems.

## 1. Confidentiality

Confidentiality means that information should only be accessible to
authorized users.

### Examples
- Password protection
- Access control
- Encryption
- Multi-factor authentication

### Example Scenario

If an attacker steals a customer database and reads personal information,
confidentiality has been compromised.

## 2. Integrity

Integrity means that information should remain accurate, complete, and
protected from unauthorized modification.

### Examples
- Hashing
- Digital signatures
- Access controls
- Audit logs

### Example Scenario

If an attacker modifies financial records without authorization,
integrity has been compromised.

## 3. Availability

Availability means that authorized users should be able to access
systems and information when required.

### Examples
- Backups
- Redundant systems
- Disaster recovery
- Monitoring
- DDoS protection

### Example Scenario

If a DDoS attack makes an organization's website unavailable,
availability has been compromised.

## CIA Triad Summary

| Principle             | Main Question                               |
|-----------------------|---------------------------------------------|
| Confidentiality       | Who can access the information?             |
| Integrity             | Has the information been changed?           |
| Availability          | Can authorized users access it when needed? |

## Practical Classification

| Scenario                                       |  CIA Principle       |
|------------------------------------------------|----------------------|
| Customer information is stolen and viewed      | Confidentiality      |
| Financial records are modified                 | Integrity            |
| Ransomware makes files inaccessible            | Availability         |
| Unauthorized employee views salary information | Confidentiality      |
| DDoS attack takes a website offline            | Availability         |

## Learning Outcome

Through this exercise, I learned how the CIA Triad is used to identify
the primary security objective affected by different cybersecurity
incidents.

## Practical Incident Analysis

### Incident 1: Ransomware

**Scenario:** A company's employee database is encrypted by ransomware,
making the records inaccessible to employees.

**CIA Principle:** Availability

**Reason:** Authorized employees cannot access the data when they need it,
so availability is compromised.

### Incident 2: Unauthorized Transaction Modification

**Scenario:** An attacker changes a customer's transaction from ₹5,000
to ₹50,000.

**CIA Principle:** Integrity

**Reason:** The attacker unauthorizedly modifies the transaction data,
making the information inaccurate.

### Incident 3: Unauthorized Salary File Access

**Scenario:** An unauthorized person obtains and reads a confidential
employee salary file.

**CIA Principle:** Confidentiality

**Reason:** Confidential information has been accessed by an
unauthorized person.

# Cryptography and Hashing

## 1. Introduction

Cryptography is the practice of protecting information using techniques that help maintain confidentiality, integrity, and authenticity.

## 2. Encryption vs Hashing

### Encryption
- Converts readable data (plaintext) into unreadable data (ciphertext).
- Uses a key to encrypt and decrypt data.
- Encryption is reversible when the correct decryption key and method are available.
- Example: AES.

### Hashing
- Converts input data into a fixed-length hash value.
- Designed as a one-way operation.
- The original input is not normally recovered from the hash.
- Example: SHA-256.

## 3. Types of Cryptography

### Symmetric Encryption
- Uses the same secret key for encryption and decryption.
- Example: AES.

### Asymmetric Cryptography
- Uses a public key and a private key.
- Used in applications such as secure key exchange and digital signatures.
- Examples: RSA and ECC.

## 4. SHA-256 Hashing

SHA-256 is a cryptographic hash function that produces a 256-bit hash value.

The hexadecimal representation contains 64 characters.

### Important Properties
- Same input produces the same hash.
- A small input change produces a substantially different hash.
- Hashing is designed to be one-way.
- Hashes can help verify data integrity.

## 5. Practical Implementation

File: `hashing_demo.py`

Python library used: `hashlib`

Function used: `hashlib.sha256()`

Method used: `hexdigest()`

### Test Results

| Input              | Result                                                             |
|--------------------|--------------------------------------------------------------------|
| `hello`            | `2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824` |
| `hello` (repeated) | Same hash                                                          |
| `Hello`            | `185f8db32271fe25f561a6fc938b2e264306ec304eda518007d1764826381969` |

Observation: Changing the capitalization from `hello` to `Hello` produces a different SHA-256 hash.

## 6. Salt and Password Storage

A salt is a random value added to a password before hashing. It helps prevent attackers from using precomputed hash tables to identify passwords.

For real password storage, use dedicated password-hashing algorithms such as Argon2id, bcrypt, scrypt, or PBKDF2. Do not store passwords using plain SHA-256 alone.

## 7. Digital Signatures

Digital signatures help verify the authenticity and integrity of a message. They use public-key cryptography to allow a recipient to verify a signature.

## 8. Cybersecurity Applications

- Verifying file integrity.
- Detecting unexpected changes in data.
- Supporting secure communication.
- Protecting stored passwords when appropriate password-hashing algorithms are used.
- Verifying digital signatures.

## 9. Learning Outcome

I learned the difference between encryption and hashing, explored symmetric and asymmetric cryptography, and implemented SHA-256 hashing in Python using `hashlib`. I verified that identical inputs produce identical hashes and that changing the input changes the hash.

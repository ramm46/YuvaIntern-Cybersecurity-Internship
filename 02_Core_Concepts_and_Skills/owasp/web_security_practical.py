
import sqlite3
from html import escape

print("=== OWASP Web Security Practical ===")

# PRACTICAL 1: SQL Injection Prevention

connection = sqlite3.connect(":memory:")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE users (
    username TEXT,
    role TEXT
)
""")

cursor.executemany(
    "INSERT INTO users (username, role) VALUES (?, ?)",
    [
        ("cipher", "student"),
        ("admin", "administrator")
    ]
)

print("\n1. SQL Injection Prevention")
username = input("Enter username to search: ")

# Parameterized query: user input is treated as data
cursor.execute(
    "SELECT username, role FROM users WHERE username = ?",
    (username,)
)

results = cursor.fetchall()

if results:
    for user in results:
        print("User found:", user)
else:
    print("No matching user found.")

print("SQL query executed safely using a parameterized query.")

# PRACTICAL 2: XSS Prevention

print("\n2. XSS Output Encoding")
user_text = input("Enter sample text for HTML output: ")

safe_text = escape(user_text)

print("Original text:", user_text)
print("Escaped HTML text:", safe_text)

connection.close()

print("\nPractical completed.")

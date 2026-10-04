
password = input("Enter a password: ")

if len(password) < 8:
    print("Result: Weak")
    print("Reason: Password must contain at least 8 characters.")
elif len(password) < 12:
    print("Result: Moderate")
    print("Tip: Use a longer password.")
else:
    print("Result: Length requirement passed")
    print("Note: Length alone does not guarantee password security.")

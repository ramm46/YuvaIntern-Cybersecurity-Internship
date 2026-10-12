
print("=== Ethical Hacking Authorization Checker ===")

authorization = input("Do you have explicit written permission? (yes/no): ").strip().lower()
scope = input("Is the target included in the approved scope? (yes/no): ").strip().lower()

if authorization == "yes":
    if scope == "yes":
        print("CHECK PASSED: Both authorization and scope are confirmed.")
        print("Proceed only within the approved rules and limits.")
    else:
        print("STOP: The target is not confirmed to be in scope.")
else:
    print("STOP: Explicit written authorization is required.")

print("Reminder: This program records your answers; it does not verify permission.")

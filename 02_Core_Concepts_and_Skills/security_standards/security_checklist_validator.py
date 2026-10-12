
# Security Checklist Validator
# Educational assessment only; does not scan or modify a real system.

checks = [
    "Firewall enabled",
    "Operating system updated",
    "Multi-factor authentication enabled",
    "Important data backups available",
    "Least-privilege access configured"
]

print("=== Security Checklist Validator ===")
print("Enter yes or no for each control.\n")

passed = 0
failed = 0

for check in checks:
    while True:
        answer = input(check + "? (yes/no): ").strip().lower()

        if answer == "yes":
            passed += 1
            break
        elif answer == "no":
            failed += 1
            break
        else:
            print("Invalid input. Please enter yes or no.")

total = len(checks)
percentage = (passed / total) * 100

print("\n--- Assessment Results ---")
print("Total controls:", total)
print("Passed:", passed)
print("Failed:", failed)
print(f"Completion: {percentage:.1f}%")

if failed == 0:
    print("Result: All checklist controls marked as passed.")
else:
    print("Result: Review controls marked as failed.")

print("\nNote: Results depend on your answers; controls are not independently verified.")


import hashlib

# Get input from the user
message = input("Enter a message to hash: ")

# Generate SHA-256 hash
hash_object = hashlib.sha256(message.encode())

# Convert hash into hexadecimal format
hash_value = hash_object.hexdigest()

# Display the results
print("\n--- SHA-256 Hashing Demo ---")
print("Original Message:", message)
print("SHA-256 Hash:", hash_value)
print("Hash Length:", len(hash_value), "characters")

from encryption import *


password = "12345"

encrypted = encrypt_password(password)

print("Original:", password)

print("Encrypted:", encrypted)


decrypted = decrypt_password(encrypted)

print("Decrypted:", decrypted)


if password == decrypted:
    print("Encryption Test Passed")
else:
    print("Test Failed")
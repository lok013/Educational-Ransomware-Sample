# Educational-Ransomware-Sample

# Python Ransomware Project (Educational Purposes Only)

## Description

This project demonstrates a basic ransomware encryption and decryption system built using Python. The ransomware consists of two scripts:

- **`ransomware.py`**: Encrypts files in the current directory.
- **`decrypt.py`**: Decrypts the files when the correct password is provided.

**Disclaimer:** This project is strictly for educational purposes. It is intended to showcase how encryption can be implemented using Python. Any malicious use of this code is strictly prohibited. The author takes no responsibility for any misuse of the project or its consequences.

## Features

- Encrypts all files in the directory except for the script itself and a few key files.
- Generates a random encryption key saved as `thekey.key`.
- Allows decryption of files only upon entering the correct password.

## How It Works

1. **`ransomware.py`** scans the current directory for files, excluding itself, the key file (`thekey.key`), and `decrypt.py`.
2. It generates a random key using the `cryptography` module, saves it to `thekey.key`, and encrypts all other files in the directory.
3. **`decrypt.py`** requires the user to enter a password to decrypt the files. If the correct password is entered, it decrypts the files using the key stored in `thekey.key`.

## Usage Instructions

### Encrypting Files

- Run the `ransomware.py` script in the directory where the files are located.
- The script will generate a key and encrypt all files except for `ransomware.py`, `thekey.key`, and `decrypt.py`.

### Decrypting Files

- Run the `decrypt.py` script.
- Enter the correct decryption password (default: **SecureP@ssw0rd123!**).
- If the password is correct, the files will be decrypted using the stored key.

## Important Notes

- **Password:** The default password for decryption is **SecureP@ssw0rd123!**. You can change this in the code if needed.
- Ensure the `thekey.key` file is in the same directory when running `decrypt.py`. Without the key, decryption will not work.
- This project is for **educational purposes only**. Do not use this code for malicious activities or to harm others.

## Educational Purpose

This project serves as a basic introduction to:

- How ransomware can be written in Python using file encryption.
- Basic concepts of encryption using the `cryptography` library.
- Understanding how file encryption and decryption processes work in real-world scenarios.

# aes_key.py

from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
import os
import base64

def generate_key(password):
    salt = os.urandom(16)  # Generate a random salt
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,  # AES-256 requires a 32-byte key
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    key = kdf.derive(password.encode())
    return key, salt

def save_key(key, salt, password):
    with open("key.key", "wb") as key_file:
        key_file.write(base64.urlsafe_b64encode(key) + b'\n' + base64.urlsafe_b64encode(salt) + b'\n' + password.encode())

def main():
    password = input("\nEnter a password to generate the key: ")
    key, salt = generate_key(password)
    save_key(key, salt, password)
    print(f"\nKey generated: {base64.urlsafe_b64encode(key).decode()}")  # Display the key

if __name__ == "__main__":
    main()

# aes_encrypt.py
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import base64
import os

def load_key():
    with open("key.key", "rb") as key_file:
        saved_key, salt, _ = key_file.read().split(b'\n')
    saved_key = base64.urlsafe_b64decode(saved_key)
    salt = base64.urlsafe_b64decode(salt)
    return saved_key, salt

def encrypt_file(filename, key):
    # Generate a random IV (Initialization Vector)
    iv = os.urandom(16)
    # Create a Cipher object for encryption
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv))
    encryptor = cipher.encryptor()

    # Read the file contents
    with open(filename, "rb") as f:
        data = f.read()

    # Encrypt the data
    encrypted_data = encryptor.update(data) + encryptor.finalize()

    # Save the encrypted data with the IV prepended
    with open("encrypted_dataset.bin", "wb") as f:
        f.write(iv + encrypted_data)
    print(f"\nFile {filename} encrypted and saved as encrypted_dataset.bin\n")

def main():
    # Load the key and salt from the file
    key, _ = load_key()

    # Specify the file to be encrypted
    filename = "D:\mitedpaes256b\src\dataset.csv"  # Replace with your dataset file

    # Encrypt the file
    encrypt_file(filename, key)

if __name__ == "__main__":
    main()

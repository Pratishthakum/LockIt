# aes_decrypt.py

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import base64

def load_key_and_password():
    with open("key.key", "rb") as key_file:
        saved_key, salt, saved_password = key_file.read().split(b'\n')
    saved_key = base64.urlsafe_b64decode(saved_key)
    saved_password = saved_password.decode()
    return saved_key, saved_password

def decrypt_file(encrypted_filename, key):
    # Read the encrypted file
    with open(encrypted_filename, "rb") as f:
        iv = f.read(16)  # The first 16 bytes are the IV
        encrypted_data = f.read()

    # Create a Cipher object for decryption
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv))
    decryptor = cipher.decryptor()

    # Decrypt the data
    decrypted_data = decryptor.update(encrypted_data) + decryptor.finalize()

    # Save the decrypted data to a new file
    with open("decrypted_dataset.csv", "wb") as f:
        f.write(decrypted_data)

    print(f"\nFile {encrypted_filename} decrypted and saved as decrypted_dataset.csv")

def main():
    # Load the saved key and password
    saved_key, saved_password = load_key_and_password()

    # Verify the user's password
    password_input = input("\nEnter the password for verification: ")
    if password_input != saved_password:
        print("\nIncorrect password! Decryption failed.")
        return

    # Take the key input from the user
    key_input = input("\nEnter the key for decryption: ")
    key_input = base64.urlsafe_b64decode(key_input)

    # Compare the entered key with the saved key
    if key_input != saved_key:
        print("\nIncorrect key! Decryption failed.")
        return

    # Specify the encrypted file to be decrypted
    encrypted_filename = "enc_dataset.bin"

    # Decrypt the file
    decrypt_file(encrypted_filename, key_input)

if __name__ == "__main__":
    main()

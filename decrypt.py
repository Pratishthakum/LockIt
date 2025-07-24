# decrypt.py
from cryptography.fernet import Fernet

def load_key(filename):
    with open(filename, 'rb') as key_file:
        return key_file.read()

def decrypt_file(input_file, output_file, key):
    cipher = Fernet(key)
    with open(input_file, 'rb') as file:
        encrypted_data = file.read()
    decrypted_data = cipher.decrypt(encrypted_data)
    with open(output_file, 'wb') as file:
        file.write(decrypted_data)

def main():
    original_key = load_key('secret.key')

    user_key = input("\nDecrypting the encrypted file by Fernet...\n").encode()
    if user_key == original_key:
        print("\nKey is correct.\nDecrypting the file...\n")
        # Decrypt the dataset
        decrypt_file('dataset.enc', 'enc_dataset.bin', user_key)
        print("\nDecryption successful. \nDecrypted file saved as 'enc_dataset.bin'.")
    else:
        print("Error: The entered key is incorrect. Decryption aborted.")
    #decrypt_file('dataset.enc', 'decrypted_dataset.csv', key)

if __name__ == '__main__':
    main()

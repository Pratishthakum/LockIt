# encrypt.py
from cryptography.fernet import Fernet

def generate_key():
    return Fernet.generate_key()

def save_key(key, filename):
    with open(filename, 'wb') as key_file:
        key_file.write(key)

def encrypt_file(input_file, output_file, key):
    cipher = Fernet(key)
    with open(input_file, 'rb') as file:
        data = file.read()
    encrypted_data = cipher.encrypt(data)
    with open(output_file, 'wb') as file:
        file.write(encrypted_data)

def main():
    
    key = generate_key()
    print(f"Generated Key by Fernet: {key.decode()}")

    save_key(key, 'secret.key')

    encrypt_file('encrypted_dataset.bin', 'dataset.enc', key)

if __name__ == '__main__':
    main()

import aes_key # type: ignore
import aes_encrypt # type: ignore
import aes_decrypt # type: ignore
import data_mining
import main

def main1():
    # Generate and save the AES-256 key
    aes_key.main()

    # Encrypt a CSV filed
    aes_encrypt.main()
    main.main()
    # Decrypt the CSV file
    aes_decrypt.main()
    data_mining.main()
    

if __name__ == "__main__":
    main1()

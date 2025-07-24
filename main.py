# main.py
import subprocess

def run_command(command):
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    if process.returncode != 0:
        print(f"Error: {stderr.decode()}")
    else:
        print(stdout.decode())


def main():

    print("Encrypting the dataset...")
    run_command('python encrypt.py')

    print("For Decryption: ")
    print("Enter the decryption key: ")
    run_command('python decrypt.py')

"""    print("Performing data mining...")
    run_command('python data_mining.py')"""

if __name__ == '__main__':
    main()

"""
Creates all the necessary functions to encrypt a file
"""

from cryptography.fernet import Fernet


def generate_key():
    """
    This function generates an encryption key and writes it to a new file
    """
    with open("./key.key", "wb") as file:
        file.write(Fernet.generate_key())


def read_file(file):
    """
    This function opens a fie for reading purposes

    Parameters:
        file: a file containing text

    Returns:
        file.read(): opens the file in readable mode
    """
    with open(file, "rb") as file:
        return file.read()

def encryption(data):
    """
    This encrypts data and writes the encrypted code in a new file

    Parameters:
        data: data to be encrypted

    Returns:
        file.write(): writes the encrypted code to a file
    """
    # Generate an encryption key and initialize the Fernet class
    fernet = Fernet(read_file("key.key"))

    # Create a new file called "encrypted_file.txt"
    with open("./encrypted_file.txt", "wb") as file:
        # Encrypt the data and write it to the file
        file.write(fernet.encrypt(read_file(data)))

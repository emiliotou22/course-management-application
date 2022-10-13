"""
Creates a Server to accept connections, decrypt messages,
and prints them on the screen or store the message to a file. 
"""
import socket
from encrypt import *
from cryptography.fernet import Fernet

socket_address = ("127.0.0.1", 5050) # Initiates server's IP address and socket port

def main(encrypted_file: bool, write_output: bool, print_required: bool):
    """
    This function creates a server to listen and accept client connections and decrypt messages from clients.
    
    Parameters:
        encrypted_file (bool): boolean variable that defines if the file will be encrypted or not 
        write_output (bool): boolean variable that defines if the output will be written in a file
        print_required (bool):  boolean variable that defines if the output will be printed on the screen    
    """
    data = ""  # Empty string to hold the received data

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.bind(socket_address) # Bind host address and port together
        server.listen() # Listens for connections
        connection, address = server.accept() # If there is a new connection, it accepts it

        with connection:
            while True:
                bytes_received = connection.recv(1024)
                # The data is converted into UTF-8 to be store in a string
                data += bytes_received.decode("utf-8")

                if not bytes_received:
                    break

    if encrypted_file:
        # Decrypting any encrypted data
        print("The decrypted message is: ")
        fernet = Fernet(read_file("./key.key").decode("utf-8"))
        # The data is converted back into bytes for Fernet to decrypt
        data = fernet.decrypt(data.encode("utf-8"))

    if print_required:
        print(data)
    if write_output:
        with open("./output.txt", "w") as file:
            file.write(data)

if __name__ == "__main__":
    # Set the encrypted_required argument to False if sending a dictionary
    main(encrypted_file=True, write_output=False, print_required=True)

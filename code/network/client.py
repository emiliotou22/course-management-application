"""
Creates a Client and sends a message to the Server 
"""

import socket
from encrypt import *
from pickling import *

# Variables
socket_address = ("127.0.0.1", 5050)  # Localhost on port 5050

# Sample dictionary
cars = {
    "Mazda RX4": {"mpg": 21, "cyl": 6, "disp": 160, "hp": 110},
    "Mazda RX4 Wag": {"mpg": 21, "cyl": 6, "disp": 160, "hp": 110},
    "Datsun 710": {"mpg": 22.8, "cyl": 4, "disp": 108, "hp": 93},
    "Hornet 4 Drive": {"mpg": 21.4, "cyl": 6, "disp": 258, "hp": 110}
}

encryption_required = True # Only for files
# Code begins
def main():
    """
    Main function that connectes the client to the server and sends either a file or
    a dictionary message to the server.
    """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.connect(socket_address)

        # Encrypts and sends a file
        if encryption_required:
            encryption("./data.txt")
            server.sendall(read_file("./encrypted_file.txt")) # Send file to the server
        else:
            server.sendall(read_file("./data.txt"))
        
        # Uncommend to send a dictionary through pickling and comment lines 27-31
        # server.sendall(to_json(cars))

if __name__ == "__main__":
    main()

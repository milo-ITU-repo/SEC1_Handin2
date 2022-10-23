# Socket code is partially from https://www.youtube.com/watch?v=3QiPPX-KeSc

import random
import socket
from sqlite3 import connect
import ssl
import threading
import commitment as c
import primes as p

HEADER = 64
PORT = 6969
#SERVER = "192.168.50.191"
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER,PORT)
FORMAT = 'utf-8'
DISCONNEC_MESSAGE = "DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # we stream data through the socket 
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server = ssl.wrap_socket(
    server, server_side=True, keyfile="./CA/server.key", certfile="./CA/server.crt"
)

server.bind(ADDR)








def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)

            if msg == DISCONNEC_MESSAGE :
                connected = False

            print(f"[{addr}]: {msg}")
            conn.send("MSG recieved".encode(FORMAT))
    
    conn.close()


def start():
    server.listen()

    print(f"[LISTENING] Server is listening on {SERVER}") 

    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")

    





if __name__== "__main__":
    print("Starting server...")
    start()
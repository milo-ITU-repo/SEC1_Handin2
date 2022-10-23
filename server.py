# Socket code is partially from https://www.youtube.com/watch?v=3QiPPX-KeSc

import random
import socket
import ssl
import threading
import commitment as c

HEADER = 64
PORT = 6969
#SERVER = "192.168.50.191"
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER,PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # we stream data through the socket 
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server = ssl.wrap_socket(
    server, server_side=True, keyfile="./CA/server.key", certfile="./CA/server.crt"
)

server.bind(ADDR)

def recieve(conn, addr):
    msg = conn.recv(HEADER).decode(FORMAT)
    print(f"[{addr}]: {msg}")
    return msg

def send(conn, addr, msg):
    conn.send(msg.encode(FORMAT))
    print(f"msg sent to [{addr}] :", msg)

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected and wants to play dice.")

    connected = True
    while connected:
        acom = recieve(conn, addr)

        roll = str(random.randint(1,6))
        print("you rolled:", roll)

        send(conn, addr, roll)

        a_msg = recieve(conn, addr)
        a_r = recieve(conn, addr)

        a_verify = c.verify(a_msg,a_r,acom)

        if a_verify:
            send(conn, addr, f"You told the truth. You rolled {a_msg}")
        else:
            send(conn, addr, f"You lied. You didn't originally roll {a_msg}")

        disc = recieve(conn, addr)

        # TODO
        if disc == DISCONNECT_MESSAGE :
            connected = False
            break
    
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
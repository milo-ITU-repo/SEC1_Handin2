# Socket code is partially from https://www.youtube.com/watch?v=3QiPPX-KeSc

import random
import socket
import ssl
from time import sleep
import commitment as c

HEADER = 64
PORT = 6969
#SERVER = "192.168.50.191"
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER,PORT)
FORMAT = 'utf-8'
DISCONNEC_MESSAGE = "DISCONNECT"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# setting a TLS wrapper socket using the ssl library
client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
client = ssl.wrap_socket(client, keyfile="./CA/client.key", certfile="./CA/client.crt")

client.connect(ADDR)


def send(msg):
    message = msg.encode(FORMAT)
    client.send(message)
    print("You sent:", msg)

def recieve():
    msg = client.recv(HEADER).decode(FORMAT)
    print("You recieved:", msg)
    return msg

if __name__== "__main__":
    print("Welcome to Bobs illegal dice ring \n")

    roll = str(random.randint(1,6))
    print("Your roll       :", roll)

    com , r = c.commit(roll)
    print("Your commitment :", com)
    print("Your randomness :", r, "\n")

    send(com)

    print()

    #sleep(1)
    b_roll = recieve()
    print("The other party rolled:", b_roll)

    send(roll)
    send(r)

    print()

    result = recieve()

    send("DISCONNECT")
    print("We hope you enjoyed your time at bobs illegal dice ring.")


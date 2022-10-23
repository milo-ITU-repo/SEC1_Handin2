import random
import socket
import ssl
import commitment as c
import primes as p

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
    msg_length = len(message)
    send_lenght = str(msg_length).encode(FORMAT)
    send_lenght += b' ' * (HEADER - len(send_lenght)) # padding the message to be the correct lenght
    client.send(send_lenght)
    client.send(message)
    print("You :", msg)


if __name__== "__main__":

    send("hello")
    send("hello again")
    send("DISCONNECT")

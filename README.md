# SEC1_Handin2

Mille Mei Zhen Loo *milo@itu.dk*

The following is a report on the second mandatory exercise in the course Security 1 at the IT-University in copenhagen.

# Code

## Requirements for running the code
`python 3.10` or later

## Running the code
To run the program you should run the server scribt first, and then the client scribt. This is done by writing the following in the terminal:
```
python .\server.py 
``` 

followed by the following in another terminal
```
python .\client.py
```

# Walk though of the protocol

In this scenario we can imagine that Bob is the best dice player in the world, being able to play multiple games at the time. By this logic Bob is the `server.py` program, and there can be multiple players (`client.py`) who can play against him.

all of these correspondances are encrypted

1. The server starts
2. The client starts and connects to the server
3. client rolls dice
4. client creates commitment to the dice roll
5. client sends commitment
6. server recieves commitment
7. server sends uncommited dice roll
8. client sends raw message and the random string used when commiting
9. server verifies the data send
10. server will send a message telling client that they know whether they were thruthfull or not.
 
# Concepts

## Secure communication
For communication over an instecure network to be secure we want to ensure the following:
- **Confidentiality**
- **Authenticity**
- **Integrity**

To ensure this I have used the tls protocol that the `TLS` protocol that the `ssl`library provides.

## Commitment scheme
Furthermore, since this is a dice rolling application, we want to ensure that one party cannot change the outcome of their roll based information recieved at a later state, and we want to ensure that another party cannot change their roll based on what they recieve. In order for this to be ensured we will use the commitment encryption scheme as well, as it ensures a **binding** and **hiding** property.

I have made my own commitment library in the `commitment.py`file. In that library there are the methods needed to make a commitment such as: `commit` and `verify`. The methods are implemented with the `sha256`hash funcion by using the `hashlib` library.

# Other comments
To generate your own certificate authority you need to have `openssl` installed. This shouldn't be needed as all certificates are saved in the `CA` folder.

It is worth noting that the library `random` only generates psudo random numbers and according to the documentation as of october 2022 the library isn't suitable for industrial use.

I have made a `primes` library that can be used in a manual implementation of a hash function. (The Sieves of Atkin could be optimised by using multithreading.)
# This is a commitment library that handles all the math behind creating and reading commitments

# https://github.com/raphaelrrcoelho/commitment-scheme/blob/master/commitment.py

from hashlib import sha256
from random import getrandbits

def commit(msg):
    r = "{0:0{1}x}".format(getrandbits(256), 64) 
    com = hashing(msg + r)
    return (com, r)

def hashing(msg):
    encoded_msg = msg.encode()
    return sha256(encoded_msg).hexdigest()

def verify(msg, r, com):
    return (com == hashing(msg + r))

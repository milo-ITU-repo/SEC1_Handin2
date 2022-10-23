# SEC1_Handin2

Mille Mei Zhen Loo *milo@itu.dk*

The following is a report on the second mandatory exercise in the course Security 1 at the IT-University in copenhagen.

# Code

## Requirements for running the code
python 3.10 or later

## Running the code


# Concepts

## Secure communication
For communication to be secure we want to ensure 3 things:
- Confidentiality
- Integrity
- Availability


## Commitment scheme
Furthermore, since this is a dice rolling application, we want to ensure that one party cannot change the outcome of their roll based information recieved at a later state, and we want to ensure that another party cannot change their roll based on what they recieve. In order for this to be ensured we will use the commitment encryption scheme as well.

binding property, and hiding property


## comments on the code
To generate your own certificate authority you need to have `openssl` installed.

It is worth noting that the library `random` only generates psudo random numbers and according to the documentation as of october 2022 the library isn't suitable for 

For better performance and security, one should probably refactor the `sieve_of_atkin` method to use multi threading

fermats and sieve of atkins


# sieve of atkin code from (has been modified): https://www.geeksforgeeks.org/sieve-of-atkin/
# other prime generation code from: https://github.com/bopace/generate-primes/blob/master/prime.py

# This library handles prime numbers

import random

def is_prime(num, test_count):
    """
    Based on Fermat's primality test
    """
    if num == 1:
        return False
    if test_count >= num:
        test_count = num - 1
    for x in range(test_count):
        val = random.randint(1, num - 1)
        if pow(val, num-1, num) != 1:
            return False
    return True

def generate_prime_fpt(n):
    """
    Based on Fermat's primality test
    """
    found_prime = False
    while not found_prime:
        p = random.randint(2**(n-1), 2**n)
        if is_prime(p, 1000):
            return p

def generate_prime_soa(limit=3000000):
    """
    Based on the Sieve of Atkin algorithm
    ::
    :return: A prime integer 
    """ 
    primes = sieve_of_atkin(limit)

    return random.choice(primes)



# Python 3 program for
# implementation of
# Sieve of Atkin
def sieve_of_atkin(limit):
    """
    :param limit: The limit for which primes will be generated. 
    :return: A list of primes less than the number given using the Sieve of Atkin algorithm
    """
    # 2 and 3 are known
    # to be prime
    primes = []
    if limit > 2:
        primes.append(2)
        #print(2, end=" ")
    if limit > 3:
        primes.append(3)
        #print(3, end=" ")
 
    # Initialise the sieve
    # array with False values
    sieve = [False] * (limit + 1)
    for i in range(0, limit + 1):
        sieve[i] = False
 
    # Mark sieve[n] is True if one of the following is True: a) n = (4*x*x)+(y*y) has odd number of solutions, i.e., there exist odd number of
    # distinct pairs (x, y) that satisfy the equation and n % 12 = 1 or n % 12 = 5. b) n = (3*x*x)+(y*y) has odd number of solutions and n % 12 = 7
    # c) n = (3*x*x)-(y*y) has odd number of solutions, x > y and n % 12 = 11
    x = 1
    while x * x <= limit:
        y = 1
        while y * y <= limit:
 
            # Main part of
            # Sieve of Atkin
            n = (4 * x * x) + (y * y)
            if (n <= limit and (n % 12 == 1 or
                                n % 12 == 5)):
                sieve[n] ^= True
 
            n = (3 * x * x) + (y * y)
            if n <= limit and n % 12 == 7:
                sieve[n] ^= True
 
            n = (3 * x * x) - (y * y)
            if (x > y and n <= limit and
                    n % 12 == 11):
                sieve[n] ^= True
            y += 1
        x += 1
 
    # Mark all multiples of
    # squares as non-prime
    r = 5
    while r * r <= limit:
        if sieve[r]:
            for i in range(r * r, limit+1, r * r):
                sieve[i] = False
 
        r += 1
 
        # Print primes
    # using sieve[]

    for a in range(5, limit+1):
        if sieve[a]:
            primes.append(a)
            #print(a, end=" ")
    
    return primes
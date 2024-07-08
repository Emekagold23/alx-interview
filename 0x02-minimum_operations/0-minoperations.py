#!/usr/bin/python3
"""
Minimum Operations
"""

import math

def factors(n):
    """Return the list of prime factors of n."""
    mylist = []
    # Handle the number of 2s that divide n
    while n % 2 == 0:
        mylist.append(2)
        n //= 2
    # n must be odd at this point so we can skip even numbers
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            mylist.append(i)
            n //= i
    # This condition is to handle the case when n is a prime number greater than 2
    if n > 2:
        mylist.append(n)
    return mylist

def minOperations(n):
    """Calculate the minimum operations to get exactly n 'H' characters."""
    if not isinstance(n, int) or n < 2:
        return 0
    else:
        return sum(factors(n))

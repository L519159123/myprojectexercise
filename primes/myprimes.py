# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 11:20:07 2018

@author: keerm
"""

import sys


def find_primes(n):
    myprimes = list(range(2, n+1))
    for i in myprimes:
        for num in myprimes:
            if num % i == 0 and num / i > 1:
                del(myprimes[myprimes.index(num)])
    return myprimes


if __name__ == "__main__":
    print(find_primes(int(sys.argv[1])))

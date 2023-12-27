import os
import gmpy2
from Crypto.Util.number import *
from random import randint
import sympy

def nbit_prime(l):
    bstr = os.urandom(l//8)# 2048-bit-random
    rnum = bytes_to_long(bstr)# convert the bytes to long
    return gmpy2.next_prime(rnum)# get the next prime

class CyclicGroup:# Cyclic group
    # test passed
    def __init__(self, p=None, g=None):
        self.p = p or nbit_prime() # get prime
        self.generator = g or self.find_generator()
    def mul(self, num1, num2):
        return (num1 * num2) % self.p
    def div(self,a,b):
        return self.mul(a,pow(b,self.p-2,self.p))
    def pow(self, base, exponent):
        return pow(base, exponent, self.p)
    def rand_int(self):
        return randint(1, self.p - 1)
    def find_generator(self):
        factors = sympy.primefactors(self.p-1)

        while True:
            candidate = self.rand_int()
            for factor in factors:
                if 1 == self.pow(candidate, (self.p -1) // factor):
                    break
            else:
                return candidate
import random
import gmpy2
import hashlib
import os
from random import randint
import socket
from Crypto.Util.number import *
import sympy
from cryptography.fernet import Fernet
from socket import *

def egcd(a, b):
    """
    return:  g: greastest common divisor
             x,y: ay + bx = gcd(a,b)
    """
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)


def mod_inverse(k, prime):
    """
     # 使用费马小定理计算乘法逆元
    :param k:
    :param prime:
    :return:
    """
    k = k % prime
    if k < 0:
        r = egcd(prime, -k)[2]
    else:
        r = egcd(prime, k)[2]
    return (prime + r) % prime

def is_prime(n, k=5):
    # 判断n是否为素数，使用Miller-Rabin算法进行k次检测
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False
    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s //= 2
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True
def generate_large_prime(bits):
    # 生成具有指定位数的大素数
    while True:
        n = random.getrandbits(bits)
        if is_prime(n):
            return n

def hash(t):
    h = hashlib.new('sha512_256')
    h.update(t)
    return h.hexdigest().encode('utf8')

def calculate_mersenne_primes():
    """ Returns all the mersenne primes with less than 500 digits.
        All primes:
        3, 7, 31, 127, 8191, 131071, 524287, 2147483647L, 2305843009213693951L,
        618970019642690137449562111L, 162259276829213363391578010288127L,
        170141183460469231731687303715884105727L,
        68647976601306097149...12574028291115057151L, (157 digits)
        53113799281676709868...70835393219031728127L, (183 digits)
        10407932194664399081...20710555703168729087L, (386 digits)
    """
    mersenne_prime_exponents = [
        2, 3, 5, 7, 13, 17, 19, 31, 61, 89, 107, 127, 521, 607, 1279
    ]
    primes = []
    for exp in mersenne_prime_exponents:
        prime = 1
        for i in range(exp):
            prime *= 2
        prime -= 1
        primes.append(prime)
    return primes

SMALLEST_257BIT_PRIME = (2**256 + 297)
SMALLEST_321BIT_PRIME = (2**320 + 27)
SMALLEST_385BIT_PRIME = (2**384 + 231)
STANDARD_PRIMES = calculate_mersenne_primes() + [
    SMALLEST_257BIT_PRIME, SMALLEST_321BIT_PRIME, SMALLEST_385BIT_PRIME
]
STANDARD_PRIMES.sort()

def get_large_enough_prime(batch):
    """ Returns a prime number that is greater all the numbers in the batch.
    """
    # build a list of primes
    primes = STANDARD_PRIMES
    # find a prime that is greater than all the numbers in the batch
    for prime in primes:
        numbers_greater_than_prime = [i for i in batch if i > prime]
        if len(numbers_greater_than_prime) == 0:
            return prime
    return None





if __name__ == "__main__":
    # print(mod_inverse(7,5))
    print(generate_large_prime(1024))

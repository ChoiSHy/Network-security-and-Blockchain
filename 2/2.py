import os
import random
import time
import struct
import math

def euclid(a, b):
    if b == 0:
        return a, 1, 0
    else:
        gcd, i, j = euclid(b, a % b)
        x = j
        y = i - (a//b) * j
        return gcd, x, y

def mod_inverse(a, b):
    gcd, x, y = euclid(a, b)
    if gcd == 1:
        return x % b
    else:
        return 0


def make_key(p):
    key_bytes = struct.pack('>d', random.random()) + struct.pack('>d', time.time()*1000) + os.urandom(16)
    private_key = int.from_bytes(key_bytes)
    while private_key >= p:
        private_key = int.from_bytes( struct.pack('>d', random.random()) + struct.pack('>d', time.time()*1000) + os.urandom(16))
    return private_key

def ellipticCurve_points(p):
    x = 0
    while x < p :
        w = (x**3+7) % p

        if int(w**0.5)== w**0.5:
            return (x,w**(0.5))
        x+=1




p = int(0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F)
key= make_key(p)

print(ellipticCurve_points(p))        
 
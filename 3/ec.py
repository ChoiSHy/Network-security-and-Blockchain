import os
import random
import time
import hashlib

p = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F
x = 0x79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798
y = 0x483ADA7726A3C4655DA4FBFC0E1108A8FD17B448A68554199C47D08FFB10D4B8

# 키 생성 함수
def generate_private_key():
    while (True):
        random_str = os.urandom(256 // 8) + str(random.random()).encode() + str(time.time()).encode()
        random_num = hashlib.sha256(random_str).digest()
        private_key = int.from_bytes(random_num, 'big')
        if private_key < p:
            break
    return private_key


def exEuclidian(n, b):
    r1 = n
    r2 = b
    t1 = 0
    t2 = 1

    while r2 > 0:
        q = r1 // r2

        r = r1 - q * r2
        r1 = r2
        r2 = r

        t = t1 - q * t2
        t1 = t2
        t2 = t

    return t1 if t1>0 else t1 + n

def add(p1:list, p2:list):
    if p1 == p2:
        r = (3*(p1[0]**2) * exEuclidian(p,(2*p1[1])%p))%p
    else:
        r = ((p2[1]-p1[1]) * exEuclidian(p, (p2[0] - p1[0])%p)) % p

    x = (r**2 - p1[0] - p2[0]) % p
    y = (r * (p1[0] - x) - p1[1]) % p

    return [x,y]

def double_and_add(k, G:list):
    bin_k = bin(k)
    res = G
    for i in range(3, len(bin_k)):
        if bin_k[i] == '1':
            res = add(add(res, res), G)
        else:
            res = add(res, res)

    return tuple(res)

def generate_public_key(key):
    
    G = [x,y]
    public_key= double_and_add(key, G)

    return public_key
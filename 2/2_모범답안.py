import os
import random
import time
import hashlib

p = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F
G = [0x79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798,
     0x483ADA7726A3C4655DA4FBFC0E1108A8FD17B448A68554199C47D08FFB10D4B8]
a = 0
b=7


def get_private_key():
    while (True):
        random_str = os.urandom(256 // 8) + str(random.random()).encode() + str(time.time()).encode()
        random_num = hashlib.sha256(random_str).digest()
        private_key = int.from_bytes(random_num, 'big')
        if private_key < p:
            break
    return private_key


def euclidian(b, n):
    r1 = n
    r2 = b if b > 0 else b+n
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
    if r1 == 1:
        return t1 if t1 > 0 else t1 + n
    else:
        return None

def euclidean_algorithm(a, b):
    if b == 0:
        return (a, 1, 0)
    else:
        gcd, x, y = euclidean_algorithm(b, a % b)
        return (gcd, y, x - (a // b) * y)

def find_inverse(a, p):
    gcd, x, y = euclidean_algorithm(a, p)
    if gcd == 1:
        return x % p
    else:
        return None

def add(point1: list, point2: list):
    if point1 == point2:
        w = (3 * point1[0] ** 2 + a) * euclidian((2 * point1[1]),p) % p
    else:
        w = (point2[1]- point1[1]) * euclidian( point2[0] - point1[0], p) % p
    if w < 0:
        w += p
    x3 = (w ** 2 - point1[0] - point2[0]) % p
    y3 = (w * (point1[0] - x3) - point1[1]) % p
    if x3 < 0:
        x3 += p
    if y3 < 0:
        y3 += p
    point3 = [x3, y3]
    return point3


def double_and_add(x, G: list):
    binary = bin(x)
    K = G
    for i in range(3, len(binary)):
        if binary[i] == '1':
            K = add(add(K, K), G)
        else:
            K = add(K, K)

    return tuple(K)

def printkeys(key):
    private_key =key
    hex_private_key = hex(private_key)
    K = double_and_add(private_key, G)
    hex_K = (hex(K[0]), hex(K[1]))
    print("개인키(16진수) = " + hex_private_key)
    print("개인키(10진수) = " + str(private_key))
    print("공개키(16진수) =" + str(hex_K))
    print("공개키(10진수) =" + str(K))


private_key = get_private_key()
test_key = int("fc9314daf42ea850f0aec302266095c346afbb7eecae5acfa86420ad2e47be65", 16)

printkeys(private_key)
print("아래는 테스트키")
printkeys(test_key)


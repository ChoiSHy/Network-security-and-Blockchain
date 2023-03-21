import os
import random
import time
import struct
import math

# 키 생성 함수
def make_key(p):
    key_bytes = struct.pack('>d', random.random()) + \
        struct.pack('>d', time.time()*1000) + os.urandom(16)
    private_key = int.from_bytes(key_bytes)
    while private_key >= p:
        private_key = int.from_bytes(struct.pack(
            '>d', random.random()) + struct.pack('>d', time.time()*1000) + os.urandom(16))
    return private_key

# 확장 유클리드드
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

    return t1%n

# 두 점 덧셈(= add)
def add(x1, y1, x2, y2, p):
    r = ((y2-y1) * exEuclidian(p, (x2 - x1)%p)) % p
    x = (r**2 - x1 - x2) % p
    y = (r * (x1 - x) - y1) % p

    return x, y

# 접점 덧셈(= double) 
def dadd(x1,y1,p):
    r = (3*(x1**2) * exEuclidian(p,(2*y1)%p))%p
    x = (r**2 - x1 - x1) % p
    y = (r * (x1-x) -y1)%p

    return x,y


p = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F
x = 0x79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798
y = 0x483ADA7726A3C4655DA4FBFC0E1108A8FD17B448A68554199C47D08FFB10D4B8
#k = 0x771ab89947b6e39e1aaa7610085e5657e1eef2da7ccdf7af7d35b0413e661d38
k = make_key(p)
print('k: ', hex(k))
k = format(k, 'b')

res_x = x
res_y = y
for i in range(1, len(k)):
    if k[i] == '1':
        res_x, res_y = dadd(res_x,res_y,p)
        res_x, res_y = add(res_x, res_y, x, y, p)
    else:
        res_x, res_y = dadd(res_x, res_y, p)
print('x: ', res_x)
print('y: ', res_y)


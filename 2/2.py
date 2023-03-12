import os
import random
import time
import struct

# 128바이트(= 1024비트)의 무작위 바이트 문자열을 생성
rand_bytes = os.urandom(128)

# 현재 시간의 밀리초 값을 반환
now_ms = int(time.time() * 1000)

# 64비트의 무작위 부동 소수점 수를 생성
rand_float = random.random()

# 무작위 바이트 문자열과 시간, 무작위 부동 소수점 수를 합쳐서 256비트의 무작위 키 생성
key_bytes = rand_bytes + struct.pack('>d', now_ms) + struct.pack('>d', rand_float)
key = int.from_bytes(key_bytes, byteorder='big')

# 256비트의 무작위 키를 16진수 형태의 문자열로 출력
print("{:064x}".format(key))



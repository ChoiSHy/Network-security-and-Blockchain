import os
import random
import time

# Generate a 128-bit random number using os.urandom()
rand_bytes = os.urandom(16)

# Convert the bytes to an integer
rand_int = int.from_bytes(rand_bytes, byteorder='big')

# Generate a random float between 0 and 1 using random.random()
rand_float = random.random()

# Get the current time in seconds using time.time()
current_time = time.time()

# Concatenate the random integer, random float, and current time
rand_str = f"{rand_int}{rand_float}{current_time}"

# Convert the string to bytes and hash it using SHA-256
import hashlib
rand_hash = hashlib.sha256(rand_str.encode()).digest()

# Convert the hash to an integer and truncate to 256 bits
rand_int = int.from_bytes(rand_hash, byteorder='big')
rand_int &= (1 << 256) - 1

# The result is a 256-bit random integer
print(hex(rand_int))
print(len(str(hex(rand_int))))

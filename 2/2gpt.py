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

# Convert the string to bytes and XOR it with a random key
key = os.urandom(32)
rand_bytes = rand_str.encode()
xored_bytes = bytes(b1 ^ b2 for b1, b2 in zip(rand_bytes, key))

# Convert the XORed bytes to an integer and truncate to 256 bits
rand_int = int.from_bytes(xored_bytes, byteorder='big')
rand_int &= (1 << 256) - 1

# The result is a 256-bit random integer
print(rand_int)
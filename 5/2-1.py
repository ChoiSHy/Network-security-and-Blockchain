import hashlib
import time

def sha256(data):
    return hashlib.sha256(data).digest()

def check_pow(message, target_bits, extra_nonce):
    target = int(target_bits, 16)
    max_nonce = 2 ** 32
    start_time = time.time()
    for nonce in range(max_nonce):
        hash_result = sha256(message.encode() + extra_nonce.to_bytes(4, byteorder='big') + nonce.to_bytes(4, byteorder='big'))
        hash_int = int.from_bytes(hash_result, byteorder='big')
        if hash_int < target:
            end_time = time.time()
            print(f"Target: {target_bits}")
            print(f"Message: {message}")
            print(f"Extra nonce: {extra_nonce}")
            print(f"Nonce: {nonce}")
            print(f"Execution time: {end_time - start_time} seconds")
            print(f"Hash result: 0x{hash_result.hex()}")
            return
    end_time = time.time()
    print(f"Proof of work not found after checking {max_nonce} nonces")
    print(f"Execution time: {end_time - start_time} seconds")

if __name__ == '__main__':
    message = '학번=123456'
    target_bits = '1e00ffff'
    extra_nonce = int(time.time())
    check_pow(message, target_bits, extra_nonce)

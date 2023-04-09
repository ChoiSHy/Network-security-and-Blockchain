import time
import hashlib
max_nonce = 2**32

def proof_of_work(header, target, extra_nonce):
    for nonce in range(max_nonce):
        h = hashlib.sha256()
        h.update((header+str(extra_nonce)+str(nonce)).encode())
        hash_result = h.hexdigest()

        if int(hash_result,16) <target:
            return (hash_result,nonce)

    return None, None

msg = input('메시지의 내용? ')
target_bit = input('Target bits? ')
#msg='학번=123456'
#target_bit='1e00ffff'

exponent = int(target_bit[:2], 16)-3
coefficient = int(target_bit[2:],16)

target = coefficient * 2 ** (8*exponent)

target_hex = '0x'+format(target,'x').zfill(64)
start_time=time.time()

extraNonce = int(start_time)
(hash_result, nonce) = proof_of_work(msg, target, extraNonce)

end_time=time.time()
elapsed_time = end_time-start_time
if hash_result is not None and nonce is not None:
    print('Target:', target_hex)
    print(f'메시지: {msg}, Extra nonce: {extraNonce}, nonce: {nonce}')
    print(f'실행 시간: {elapsed_time}초')
    print(f'Hash result: 0x{hash_result}')
else:
    print('실패')
      




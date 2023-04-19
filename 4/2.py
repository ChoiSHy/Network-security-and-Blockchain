import ec
import hashlib
from Crypto.Hash import RIPEMD160
import base58check

def generate_bitcoin_address(public_key):
    #take public key
    if public_key[1] % 2 == 0:
        public_key='02'+hex(public_key[0])[2:]
    else:
        public_key='03'+hex(public_key[0])[2:]
    # perform SHA-256 hashing on the public key
    if len(hex(int(public_key,16))) <67:
        return None
    sha256_hash = hashlib.sha256(bytes.fromhex(public_key)).hexdigest()

    # perform RIPEMD-160 hashing on the result of SHA-256
    h=RIPEMD160.new()
    h.update(bytes.fromhex(sha256_hash))
    ripemd_code = h.hexdigest()

    # add version byte in front of RIPEMD160
    ripemd_code = '00' + ripemd_code
    
    # perform sha-256 hash on the extended ripemd-160 result
    sha256_hash = hashlib.sha256(bytes.fromhex(ripemd_code)).hexdigest()

    # perform sha-256 hash on the result of the previous sha-256 hash
    sha256_hash = hashlib.sha256(bytes.fromhex(sha256_hash)).hexdigest()

    # Take the first 4 bytes of the second SHA-256 hash. This is the address checksum
    checksum = sha256_hash[:8]

    #Add the 4 checksum bytes from stage 7 at the end of extended RIPEMD-160 hash from stage 4. This is the 25-byte binary Bitcoin Address.
    address = ripemd_code+checksum

    # Convert the result from a byte string into a base58 string using Base58Check encoding.
    #This is the most commonly used Bitcoin Address format
    address=base58check.b58encode(bytes.fromhex(address))
    
    return ripemd_code, address, checksum

wanted = input('희망하는 주소의 문자열? ')

while(True):
    private_key= ec.generate_private_key()
    public_key=ec.generate_public_key(private_key)

    result = generate_bitcoin_address(public_key)
    if result is None:
        continue
    if result[1].decode()[1:len(wanted)+1] == wanted:
        print('개인 키 =', private_key)
        print('주소 =',result[1].decode())
        break
        
    







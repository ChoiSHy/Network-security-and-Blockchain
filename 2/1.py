from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import padding

from cryptography.fernet import Fernet


def encrypt(message):
    with open('public_key.pem', 'rb') as key_file:
        public_key = serialization.load_pem_public_key(
            key_file.read(),
            backend=default_backend()
        )

    encrypted = public_key.encrypt(
        message,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return encrypted

def decrypt(encrypted):
    with open('private_key.pem', 'rb') as key_file:
        private_key = serialization.load_pem_private_key(
        key_file.read(),
        password=None,
        backend=default_backend()
    )

    original_msg = private_key.decrypt(
        encrypted,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return original_msg

msg = bytes(input(), 'ms949')
print('평  문: ',msg)
aes_key1 = Fernet.generate_key()
f1 = Fernet(aes_key1)
enc_msg = f1.encrypt(msg)
rsa_key = encrypt(aes_key1)

print('암호화: ',enc_msg)

aes_key2 = decrypt(rsa_key)
f2=Fernet(aes_key2)
ori_msg = f2.decrypt(enc_msg)

print('복호화: ',ori_msg)
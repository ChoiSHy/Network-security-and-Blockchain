from string import ascii_lowercase
import random

# 대치 키 생성
def make_key(E, D):
    values=list(ascii_lowercase)
    random.shuffle(values)

    for k, v  in zip(range(97,123), values):
        E[chr(k)] = v
        D[v] = chr(k)

# 평문 암호화
def encrypt(plain, E):
    ret = []
    for c in plain:
        if(c==' '): ret+=' '
        else: ret+=E[c]

    return ''.join(ret)

# 암호문 복호화
def decrypt(encrp, D):
    ret = []
    for c in encrp:
        if(c==' '): ret+=' '
        else: ret+=D[c]
    return ''.join(ret)

E={}
D={}
make_key(E,D)

plain = input("평문 입력: ").lower()
encrp = encrypt(plain,E)
decrp = decrypt(encrp, D)

print('암호문: ',encrp)
print('복호문: ',decrp)




from cryptography.fernet import Fernet

# key 생성
key = Fernet.generate_key()
f= Fernet(key)

# data.txt 불러오기
with open('data.txt','r') as dataFile:
    data = dataFile.read()

# 평문 암호화
token = f.encrypt(bytes(data, 'utf-8'))
with open('encrypted.txt','w') as enFile:
    enFile.write(str(token,'utf-8'))

# 암호문 복호화
with open('encrypted.txt','r') as enFile:
    token = enFile.read()
d = f.decrypt(bytes(token,'utf-8'))
print(str(d, 'utf-8'))


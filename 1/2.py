# 입력
plain = input('평문 입력: ').upper().replace(' ','')
vigKey = input('Vigenere 암호? ').upper()

# Vigenere 암호화 
tlist = []
for i in range(0, len(plain), len(vigKey)):
    tlist += (''.join([chr((ord(p) + ord(v)) % 26 + 65)
                for p, v in zip(plain[i:i+len(vigKey)], vigKey)]))    # key길이만큼 plain문자열을 잘라내어 암호화    
vigEncrp = ''.join(tlist)
print('암호문: ', vigEncrp)

# Vigenere 복호화
tlist.clear()
for i in range(0, len(vigEncrp), len(vigKey)):
    tlist += (''.join([chr((ord(e) - ord(v)) % 26 + 65)
                for e, v in zip(vigEncrp[i:i+len(vigKey)], vigKey)]))
vigDecrp = ''.join(tlist)
print('복호문: ', vigDecrp) 

# 자동 키 암호화
autoKey = int(input('자동 키 암호? '))
keyStream = autoKey

tlist.clear()
for c in plain:
    tlist += chr( (ord(c) - 65 + keyStream) % 26 +65)
    keyStream = ord(c)-65

autoEncrp = ''.join(tlist)
print('암호문:', autoEncrp)

# 자동 키 복호화
keyStream = autoKey
tlist.clear()
for c in autoEncrp:
    tlist += chr((ord(c) - 65 - keyStream) % 26 + 65)
    keyStream = ord(c)-65-keyStream

autoDecrp = ''.join(tlist)
print('복호문:',autoDecrp)


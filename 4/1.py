import hashlib
import ec

goal1 = '0250863ad64a87ae8a2fe83c1af1a8403cb53f53e486d8511dad8a04887e5b2352'
goal2 = '0b7c28c9b7290c98d7438e70b3d3f7c848fbd7d1dc194ff83f4f7cc9b1378e98'
private_key = int('18e14a7b6a307f426a94f8114701e7c8e774e7f9a47e2c2035db29a206321725',16)

public_key = ec.generate_public_key(private_key)

if public_key[1] % 2 == 0:
    public_key='02'+hex(public_key[0])[2:]
else:
    public_key='03'+hex(public_key[0])[2:]
print('<1>')
print('goal:', goal1)
print('res :', public_key)

print('<2>')
h = hashlib.sha256(public_key.encode())
print('goal:',goal2)
print('res :',hashlib.sha256(public_key.encode()).hexdigest())

print(hashlib.sha256('03564213318d739994e4d9785bf40eac4edbfa21f0546040ce7e6859778dfce5d4'.encode()).hexdigest())
print('482c77b119e47024d00b38a256a3a83cbc716ebb4d684a0d30b8ea1af12d42d9')

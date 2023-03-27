from cryptography.hazmat.primitives import hashes
import ec
import random
import hashlib

p = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F
e1 = (
    0x79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798, 
    0x483ADA7726A3C4655DA4FBFC0E1108A8FD17B448A68554199C47D08FFB10D4B8)
q = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141
#r = 41003466362608940562794629182404967427451760136744234558038380002801394949900

def sign(msg, d):
    r = random.randint(1,q-1)
    
    P = ec.double_and_add(r, e1)
    S1 = P[0] % q
    h = hashlib.sha256()
    h.update(msg.encode())

    S2 = (int(h.hexdigest(),16)+d*S1)*ec.exEuclidian(q,r)%q

    return S1, S2
def verify(msg, S1, S2, e2):
    h = hashlib.sha256()
    h.update(msg.encode())
    A = int(h.hexdigest(), 16) * ec.exEuclidian(q, S2) % q
    B = S1 * ec.exEuclidian(q,S2) % q
    T = ec.add(ec.double_and_add(A,e1), ec.double_and_add(B, e2))

    print('\tA = ', hex(A))
    print('\tB = ', hex(B))
    if T[0] % q == S1 % q:
        return True
    else: return False

if __name__ == "__main__":
    d = ec.generate_private_key()  # 2주차 과제에서 작성한 함수
    e2 = ec.generate_public_key(d)  # 2주차 과제에서 작성한 함수

    M = input("메시지? ")
    S1, S2 = sign(M, d)
    print("1. Sign:")
    print("\tS1 =", hex(S1))
    print("\tS2 =", hex(S2))

    print("2. 정확한 서명을 입력할 경우:")
    if verify(M, S1, S2, e2) == True:
        print("검증 성공")
    else:
        print("검증 실패")

    print("3. 잘못된 서명을 입력할 경우:")
    if verify(M, S1-1, S2-1, e2) == True:
        print("검증 성공")
    else:
        print("검증 실패")

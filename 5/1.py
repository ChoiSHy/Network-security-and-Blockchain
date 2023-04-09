from bitmap import BitMap
import hashlib

class BloomFilter:
    def __init__(self,m,k) -> None:
        self.m=m
        self.k=k
        self.n=0
        self.bf = BitMap(m)
    
    def getPositions(self, item):
        plist=[]
        for i in range(1,self.k+1):
            shaHex = hashlib.sha256((item+str(i)).encode()).hexdigest()
            pos = int(shaHex,16) % self.m
            plist.append(pos)
            
        return plist
    
    def add(self, item):
        plist = self.getPositions(item)
        for i in plist:
            self.bf.set(i)
        self.n+=1

    
    def contains(self, item):
        ret = True
        plist = self.getPositions(item)
        for i in plist:
            ret = ret and self.bf.test(i)
        return ret

    def reset(self):
        for i in range(self.k):
            self.bf.reset(i)
        self.n=0

    def __repr__(self) -> str:
        ret = f'M = {self.m}, F = {self.k}\n'
        ret+= f'BitMap = {self.bf.tostring()}\n'
        ret+= f'항목의 수 = {self.n}, 1인 비트수 = {self.bf.count()}'
        return ret
if __name__ == "__main__":
    bf = BloomFilter(53, 3)
    for ch in "AEIOU":
        bf.add(ch)
    print(bf)
    for ch in "ABCDEFGHIJ":
        print(ch, bf.contains(ch))
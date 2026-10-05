class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for i in strs:
            a = len(i)
            s+=str(a)+":"+i
        return s
    def decode(self, s: str) -> List[str]:
        l = []
        
        i = 0
        while i < len(s):
            d = s.find(":",i)
            n = int(s[i:d])
            w = s[d+1:d+1+n]
            l.append(w)
            i = d+n+1
        return l


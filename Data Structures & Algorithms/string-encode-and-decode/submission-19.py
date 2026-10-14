class Solution:

    def encode(self, strs: List[str]) -> str:
        a = ""
        for i in strs:
            a+=str(len(i))+":"
            a +=i
        return a

    def decode(self, s: str) -> List[str]:
        l = []
        i = 0
        while i < len(s):
            if i < len(s) and s[i] in "1234567890":
                c = ""
                while i < len(s) and  s[i]!= ":":
                    c += (s[i])
                    i+=1
                i+=1
                n = len(c)
                d = int(c)
                l.append(s[i:i+d])
                i = i+d
        return (l)

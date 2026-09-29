class Solution:

    def encode(self, strs: List[str]) -> str:
        l = ""
        for i in strs:
            l += str(len(i)) + ":" + i
        return l

    def decode(self, s: str) -> List[str]:
        l = []
        i = 0
        while i < len(s):
            delim = s.find(":", i)
            length = int(s[i:delim])
            l.append(s[delim + 1 : delim + 1 + length])
            i = delim + 1 + length
        return l

from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        ns1 = Counter(s1)
        d = {}
        l = 0
        i = 0
        k = 0
        while i < len(s2):
            while i < len(s2) and k < len(s1):
                if s2[i] not in d:
                    d[s2[i]] = 0
                d[s2[i]] += 1
                i += 1
                k+=1
            print(d)
            if ns1 == d:
                return True
            else:
                d[s2[l]] -= 1
                if d[s2[l]] == 0:
                    del d[s2[l]]
                l += 1
                k -=1
        return False

from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = 0
        b = {}
        have = 0
        need = len(set(t))
        res,reslen = [-1,-1],float('inf')
        a = Counter(t)
        for r in range(len(s)):
            b[s[r]] = 1+b.get(s[r],0)
            if b[s[r]] == a[s[r]]:have +=1
            while have == need:
                if (r-l+1)<reslen:
                    res = [l,r]
                    reslen = r-l+1
                b[s[l]]-=1
                if s[l] in a and b[s[l]] < a[s[l]]:
                    have -=1
                l+=1
        n,m = res
        return s[n:m+1]



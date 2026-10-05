from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t=="":return""
        a = Counter(t)
        need = len(set(t))
        have = 0
        b = {}
        res = [-1,-1];reslen = float('inf')
        l = 0
        
        for i in range(len(s)):
            b[s[i]] = 1+b.get(s[i],0)
            if s[i] in a and a[s[i]] == b[s[i]]: have +=1
            while have == need:
                if (i-l+1)< reslen:
                    res = [l,i]
                    reslen = (i-l+1)
                b[s[l]]-=1
                if s[l] in a and b[s[l]] < a[s[l]]:
                    have -=1
                l+=1
        q,w= res
        return s[q:w+1]


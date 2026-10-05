class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d = {}
        l = 0; res = 0
        for i in range(len(s)):
            d[s[i]] = 1+ d.get(s[i],0)
            
            while (i-l+1) - max(d.values()) > k:
                d[s[l]]-=1
                l+=1
            res = max(res, i-l+1)
        return res
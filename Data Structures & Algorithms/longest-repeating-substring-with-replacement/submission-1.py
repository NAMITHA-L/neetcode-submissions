class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d = {}
        l = r = 0
        c = 0
        while r < len(s):
            d[s[r]] = 1+d.get(s[r],0)
            if r-l+1 - max(d.values()) <= k and r-l+1 > c:
                c = r-l+1
            else:
                d[s[l]]-=1
                l+=1
            r+=1
        return c
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        v = set()
        l = 0
        r = 0
        m = 0
        while r < len(s):
            if s[r] not in v:
                v.add(s[r])
            elif s[r] in v:
                m = max(m, len(v))
                while s[r]in v:
                    v.remove(s[l])
                    l+=1
                v.add(s[r])
            r+=1
        return max(m,len(v))

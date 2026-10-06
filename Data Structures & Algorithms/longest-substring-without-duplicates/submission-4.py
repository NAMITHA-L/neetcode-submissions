class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        saw = set()
        l = r = 0
        c = 0
        while r < len(s):
            while r < len(s) and s[r] not in saw:
                saw.add(s[r])
                r+=1
            c = max(c,len(saw))
            while r < len(s) and s[r] in saw:
                saw.remove(s[l])
                l+=1
            if r < len(s):saw.add(s[r])
            r+=1
        return max(c,len(saw))
            
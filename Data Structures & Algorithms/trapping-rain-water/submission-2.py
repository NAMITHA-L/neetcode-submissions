class Solution:
    def trap(self, h: List[int]) -> int:
        l = 0 
        r = len(h)-1
        ml = h[l]
        mr = h[r]
        c = 0
        while l < r:
            if ml < mr:
                l+=1
                ml = max(ml,h[l])
                c += ml - h[l]
            else:
                r -= 1
                mr = max(mr,h[r])
                c += mr - h[r]
        return c
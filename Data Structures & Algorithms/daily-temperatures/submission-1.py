class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        l1 = []
        r = [0]*len(temp)
        for i,t in enumerate(temp):
            while l1 and l1[-1][1] < t:
                pi,pv = l1.pop()
                r[pi] = i - pi
            l1.append((i,t))
        return r
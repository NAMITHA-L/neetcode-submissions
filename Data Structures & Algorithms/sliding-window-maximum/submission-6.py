from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res =[]
        q = deque()
        l = 0
        for i in range(len(nums)):
            while q and nums[i] > nums[q[-1]]:
                q.pop()
            q.append(i)
            if l > q[0]: q.popleft()
            if i+1 >= k:
                res.append(nums[q[0]])
                l+=1
        return res
from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = []
        l.append(1)
        for i in range(1,len(nums)):
            l.append(nums[i - 1] * l[i - 1])
        c = 1
        for i in range(len(nums) - 1, -1, -1):
            if i == len(nums) - 1:
                continue
            c *= nums[i + 1]
            l[i] *= c

        return l
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            if target - nums[i] in d:
                l =  [d[target-nums[i]],i]
                return l
            else:
                d[nums[i]] = i

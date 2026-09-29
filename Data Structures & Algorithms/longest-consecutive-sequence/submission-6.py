class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:return 0
        nums = sorted(list(set(nums)))
        if len(nums) == 1:return 1
        print(nums)
        l = 0
        r = 0
        mc = 1
        while r < len(nums)-1:
            if nums[r]+1 == nums[r+1]:
                print(nums[r])
                l = r
                while r < len(nums)-1 and nums[r]+1 == nums[r+1]:
                    r+=1
                print(r-l+1)
                mc = max(mc, r-l+1)
            else:
                r+=1

        return mc

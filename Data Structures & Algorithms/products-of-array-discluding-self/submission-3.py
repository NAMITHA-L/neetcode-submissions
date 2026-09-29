class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        postfix = []
        ans = []
        postfix.append(1)
        prefix.append(1)
        a = nums[:]
        nums.reverse()
        for i in range(1,len(nums)):
            prefix.append(prefix[i-1]*a[i-1])
            postfix.append(postfix[i-1]*nums[i-1])
        postfix.reverse()
        for i in range(len(nums)):
            ans.append(prefix[i]*postfix[i])
        return(ans)


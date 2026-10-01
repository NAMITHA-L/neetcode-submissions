class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        d = {}
        for i in range(1,len(numbers)+1):
            if target - numbers[i-1] in d:
                return [d[target-numbers[i-1]],i]
            else:
                d[numbers[i-1]] = i
        

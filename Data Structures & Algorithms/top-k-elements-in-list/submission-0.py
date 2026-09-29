from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c= Counter(nums)
        m = c.most_common(k)
        l= []
        for i in m:
            l.append(i[0])
        return (l)
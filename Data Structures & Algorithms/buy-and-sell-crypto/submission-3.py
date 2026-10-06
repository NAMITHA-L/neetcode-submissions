class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        c = 0
        mx = 0
        while r < len(prices) and l <len(prices):
            if prices[l] >= prices[r]:
                l+=1
                r = l+1
            elif prices[r] > prices[l]:
                while r< len(prices) and prices[r]>prices[l]:
                    c = prices[r]-prices[l]
                    mx = max(mx,c)
                    r+=1
        return max(mx,c)
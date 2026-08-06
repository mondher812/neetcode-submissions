class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prof = 0
        l = 0
        r = 1
        while r < len(prices):
            if prices[r] < prices[l]:
                l = r
                r += 1
            else:
                if prof < prices[r] - prices[l]:
                    prof = prices[r] - prices[l]
                    r+=1
                else:
                    r+=1
        print(l)
        return prof
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prof = 0
        l = 0
        r = 1
        while r<len(prices):
            prof = max(prof,prices[r]-prices[l])
            if prices[r]<prices[l]:
                l = r
                r = r+1
            else:
                r=r+1
        return prof
        


        
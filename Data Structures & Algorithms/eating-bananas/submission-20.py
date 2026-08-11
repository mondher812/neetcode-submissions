class Solution:
    def minEatingSpeed(self, piles: List[int], h: int)-> int:
        l = 1
        r = max(piles)
        out = float('inf')
        while l<=r:
            m = (l+r)//2
            t = 0
            for item in piles:
                t += -(item // -m)
            if t <=h:
                out = m
                r = m-1
            else:
                l = m+1
        return out
                

     


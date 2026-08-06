class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        cur_m = 0
        time_taken = 0
        l = 1
        r = max(piles)
        last_smallest_m = max(piles)
        
        while r >=l:
            cur_m = (r+l)//2
            time_taken = 0
            for pile in piles:
                time_taken += math.ceil((1.0*pile) / cur_m)
            if time_taken > h:
                l = cur_m +1
            elif time_taken <=h:
                last_smallest_m = cur_m
                r = cur_m - 1
        return last_smallest_m
            


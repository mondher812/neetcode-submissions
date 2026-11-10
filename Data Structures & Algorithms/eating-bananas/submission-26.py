class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        r = max(piles)
        l = 1
        t_taken = float("inf")
        saved_to = r
        while r>=l:
            mid = (l + r) // 2
            cur_t = 0
            for item in piles:
                cur_t+=math.ceil(item/mid)
            if cur_t > h:
                l = mid+1
            else:
                if t_taken> cur_t:
                    t_taken = cur_t
                    saved_to =  mid
                r = mid-1
        return l

            
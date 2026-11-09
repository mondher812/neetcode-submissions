class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0 
        r = len(heights)-1
        m = 0
        cur_m = 0
        while l<r:
            cur_m = (r-l) * (min(heights[l],heights[r]))
            m = max(m,cur_m)
            if heights[l] >= heights[r]:
                r-=1
            else:
                l+=1
        return m
            


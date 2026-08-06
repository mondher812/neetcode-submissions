class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights)-1
        m = 0
        while l<r:
            c_m = (r-l) * min(heights[r],heights[l])
            m = max(c_m,m)
            if heights[r]>= heights[l]:
                l+=1
            else:
                r-=1
        return m 

        
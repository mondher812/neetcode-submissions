class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights)-1
        maxa = 0
        while r>l:
            cur_a = (r-l)*(min(heights[r],heights[l]))
            if heights[r] < heights[l]:
                r-=1
            else:
                l+=1
            maxa = max(cur_a,maxa)
        return maxa

            

        
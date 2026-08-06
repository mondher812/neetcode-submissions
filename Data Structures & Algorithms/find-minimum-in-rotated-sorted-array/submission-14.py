class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        out = nums[0]
        r = len(nums)-1
        while l<= r:
            if nums[l] < nums[r]:
                out = min(out,nums[l])
                break
            m = (r+l)//2
            out = min(out,nums[m])
            if nums[m] >  nums[r]:
                l = m+1
            else:
                r = m -1
        return out
          


        
        

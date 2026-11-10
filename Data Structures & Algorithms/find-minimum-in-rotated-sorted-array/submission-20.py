class Solution:
    def findMin(self, nums: List[int]) -> int:
        # if right is sorted
        # check if r is greater then l
        # - answer on l 
        # else answer on r
        # if left is sorted
        # check if l is greater then r
        # answer is on r
        # else
        # answer on l 
        r = len(nums)-1
        l = 0
    
        while l<r:
            m = (r+l)//2
            print(m)
            if nums[m] < nums[r]:
                r = m 
            else:
                if nums[l] > nums[r]:
                    l = m+1
                else:
                    r = m
        return nums[l]
      


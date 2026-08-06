class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p = 1
        o = [1] * (len(nums))
        for i in range(len(nums)):
            o[i] = p
            p = p * nums[i]
        post = 1
        for i in range(len(nums)-1,-1,-1):
            
            o[i] = o[i] * post
            post = nums[i]* post
        return o
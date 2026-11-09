class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        before = [1] * len(nums)
        after = [1] * len(nums)
        for i in range(1,len(nums)):
            before[i] = before[i-1] * nums[i-1]
        for j in range(len(nums)-2,-1,-1):
            after[j] = after[j+1] * nums[j+1]
        return [after[x] * before[x] for x in range(len(nums))]
   
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        highest = len(nums)
        total_s = (highest *( highest + 1))//2
        for item in nums:
            total_s -= item
        return total_s
    

        
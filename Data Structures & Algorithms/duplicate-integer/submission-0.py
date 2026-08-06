class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        m = {}
        for i in range(len(nums)):
            if nums[i] not in m.values():
                m[i] = nums[i]
            else:
                return True
        return False
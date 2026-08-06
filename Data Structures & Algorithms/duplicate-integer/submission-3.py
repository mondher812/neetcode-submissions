class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        sol = set()
        for item in nums:
            if item in sol:
                return True
            else:
                sol.add(item)
        return False

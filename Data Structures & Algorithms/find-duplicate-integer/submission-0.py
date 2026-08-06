class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        h = {}
        for number in nums:
            if number in h:
                return number
            else:
                h[number] =1
    
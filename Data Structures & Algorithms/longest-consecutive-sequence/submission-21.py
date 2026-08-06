class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        
        num_s = set(nums)
        for item in num_s:
            if item-1 not in num_s:
                curr = 1
                while item +  curr in num_s:
                    curr+=1
                longest = max(longest,curr)
        return longest


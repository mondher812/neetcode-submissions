class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        first = False
        num = set(nums)
        ind = []
        seen =[]
    
        longest= 0 
        for item in num:
            if item-1 not in num:
                l = 1
                while item+l in num:
                    l+=1
                longest = max(l,longest)
        return longest
            

                

       
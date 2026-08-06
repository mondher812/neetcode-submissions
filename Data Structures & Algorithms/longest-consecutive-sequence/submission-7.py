class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        h = {}
        if len(nums) == 0:
            return 0
        for item in nums:
            h[item] = h.get(item,0) + 1
        maxout=[]
        for values in h.keys():
            count = 0
            if h.get(values-1,0) == 0:
                count += 1
                while h.get(values+1,0) != 0:
                    count+=1
                    values+=1
            maxout.append(count)
        return(max(maxout))




        
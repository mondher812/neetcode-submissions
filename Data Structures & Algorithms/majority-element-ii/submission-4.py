class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        limit = (n//3)
        nums.sort()
        curr_num = int
        out = set()
        i = 0
        while i < n:
            item = nums[i]
            if i+limit>=n:
                break
            if item == nums[i+limit]:
                if item not in out:
                    out.add(item)
                i+=limit
            i+=1
            
            
        return list(out)

        
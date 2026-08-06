class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        to_ret = [[]]

        nums.sort()
        for i in range(len(nums)):
            temp = []
            for sub in to_ret:
                ts = sub.copy()
                if i > 0 and nums[i] == nums[i-1] and sub == []:
                    continue
                ts.append(nums[i])
                if ts not in to_ret:
                    temp.append(ts)


            to_ret.extend(temp)
        return to_ret

        


        
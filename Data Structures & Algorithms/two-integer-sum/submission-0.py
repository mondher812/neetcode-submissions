class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            t_v = target - nums[i]
            if t_v in d.keys():
                return [d[t_v],i]
            d[nums[i]] = i
        return 
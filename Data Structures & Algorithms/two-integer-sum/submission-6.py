class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      seen = {}
      for i,item in enumerate(nums):
        if item in seen:
          return [seen[item][0],i]
        else:
          seen[target-item] = [i,item]


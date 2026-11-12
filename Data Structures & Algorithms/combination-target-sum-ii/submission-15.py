class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ins = set()
    
        sums = 0 
        out = []
        path = []
        def dfs(i,cursm):
            if cursm > target:
                return
            elif cursm == target:
                return out.append(path[:])
            else:
                if i<len(nums):
                    path.append(nums[i])
                    dfs(i+1,cursm+nums[i])
                    path.pop()
                    while i+1 < len(nums) and nums[i] == nums[i+1]:
                        i+=1                               
                    dfs(i+1,cursm)
            return
    
        dfs(0,0)
        return out

        
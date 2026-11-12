class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
    
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
                    dfs(i,cursm+nums[i])       
                    path.pop()                               
                    dfs(i+1,cursm)
            return
    
        dfs(0,0)
        return out

        
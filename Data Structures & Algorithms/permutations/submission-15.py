class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        l = len(nums)
        o = []
        sums = sum(nums)
        def dfs(i,path,taken):
            if i == len(nums) and sum(path) == sums:
                o.append(path[:])
                return
            if i == len(nums):
                return
            else:
                for ind in range(l):
                    if ind in taken:
                        continue
                    else:
                        taken.add(ind)
                        path[ind] = nums[i]
                        dfs(i+1,path,taken)
                        taken.remove(ind)
                        path[ind] = -11
                        dfs(i+1,path,taken)
        dfs(0,[-11]*l,set())
        return o
        



                


        
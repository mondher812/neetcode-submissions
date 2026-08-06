class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        cur_m = 0
        stack = []
        r = len(grid)
        c = len(grid[0])
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 1:
                    stack.append([i,j])
                    temp_m = 0
                    while len(stack)>0:
                        k ,l = stack.pop()
                        if min(k,l) >= 0 and k < r and l < c:
                            if grid[k][l] == 1:
                                temp_m +=1
                                grid[k][l] = 0
                                stack.append([k+1,l])
                                stack.append([k-1,l])
                                stack.append([k,l+1])
                                stack.append([k,l-1])
                    cur_m = max(cur_m,temp_m)
        return cur_m



        
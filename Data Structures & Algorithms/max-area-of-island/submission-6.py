class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:        
        island = 0
        def track(curx,cury):
            if grid[curx][cury] == 1:
                grid[curx][cury] = 0
                a, b, c, d = 0,0,0,0
                if curx+1 < len(grid):
                   a = track(curx+1,cury)
                if curx-1 >=0:
                   b= track(curx-1,cury)
                if cury+1<len(grid[0]):
                   c= track(curx,cury+1)
                if cury-1>=0:
                   d= track(curx,cury-1)
                return 1 + a + b +c +d
            

            else:
                return 0 
        maxx = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    maxx =max(maxx,track(i,j))
        return maxx


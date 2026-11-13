class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        island = 0
        def track(curx,cury):
            if grid[curx][cury] == "1":
                grid[curx][cury] = "0"
                if curx+1 < len(grid):
                    track(curx+1,cury)
                if curx-1 >=0:
                    track(curx-1,cury)
                if cury+1<len(grid[0]):
                    track(curx,cury+1)
                if cury-1>=0:
                    track(curx,cury-1)
            

            else:
                return
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    island+=1
                    track(i,j)
        return island


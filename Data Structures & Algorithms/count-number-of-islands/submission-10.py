class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:


        row = len(grid)
        col = len(grid[0])
        visited = set()
        count = 0

        def bfs(r,c,grid):
            visited.add((r,c))
            if r + 1 < row and (r+1,c) not in visited and grid[r+1][c] == "1":
                bfs(r+1,c,grid)
            if r - 1 >=0 and(r-1,c) not in visited and grid[r-1][c]=="1":
                bfs(r-1,c,grid)
            if c + 1 < col and (r,c+1) not in visited and grid[r][c+1] == "1":
                bfs(r,c+1,grid)
            if c - 1 >=0 and (r,c-1) not in visited and grid[r][c-1] == "1":
                bfs(r,c-1,grid)



            

        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1" and (i,j) not in visited:
                    count+=1
                    bfs(i,j,grid)
        return count

      


                        
        
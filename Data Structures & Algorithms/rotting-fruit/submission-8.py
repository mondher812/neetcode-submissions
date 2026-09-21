class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        t =0 
        q = collections.deque()
        normal = 0
        level =[]
        



        for i in range(row):
            for j in range(col):
                if grid[i][j] == 2:
                    q.append((i,j))
                if grid[i][j] == 1:
                    normal+=1
    

        while len(q)>0 and normal>0:
            l = len(q)
            for k in range(l):
                r,c = q.popleft()
                if r + 1 < row and grid[r+1][c] ==1:
                    grid[r+1][c] = 2
                    q.append((r+1,c))
                    normal -= 1
                if c + 1 < col and grid[r][c+1] ==1:
                    grid[r][c+1] = 2
                    q.append((r, c+1))
                    normal -= 1
                if r - 1 >=0 and grid[r-1][c] ==1:
                    grid[r-1][c] = 2
                    q.append((r-1,c))
                    normal -= 1
                if c - 1 >=0 and grid[r][c-1] ==1:
                    grid[r][c-1] = 2
                    q.append((r, c-1))
                    normal -= 1
            t+=1
        if normal == 0:
            return t
        return -1
                



class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        counter = 0
        stac = []
        r = len(grid)
        c = len(grid[0])
        for i in range(r):
            for j in range(c):
                if grid[i][j] == "1":
                    stac.append([i,j])
                    counter+=1
                    while len(stac) > 0:
                        ir, ic = stac.pop()
                        if min(ir,ic) < 0:
                            continue
                        if ir >= r or ic >= c:
                            continue

                        if grid[ir][ic] == "1":
                            grid[ir][ic] = "0"
                            stac.append([ir+1,ic])
                            stac.append([ir-1,ic])
                            stac.append([ir,ic+1])
                            stac.append([ir,ic-1])
        return counter




                        
        
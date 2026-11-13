class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rotten = set()
        fresh = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    fresh.add((i,j))
                elif grid[i][j] ==2:
                    rotten.add((i,j))
        t =0
        while len(fresh)>0:
            o = set()
            for item in rotten:
                rx,ry = item
                if (rx+1,ry) in fresh:
                    o.add((rx+1,ry))
                    fresh.remove((rx+1,ry))
                if (rx-1,ry) in fresh:
                    o.add((rx-1,ry))
                    fresh.remove((rx-1,ry))
                if (rx,ry+1) in fresh:
                    o.add((rx,ry+1))
                    fresh.remove((rx,ry+1))
                if (rx,ry-1) in fresh:
                    o.add((rx,ry-1))
                    fresh.remove((rx,ry-1))
            if len(o) == 0:
                return -1
            rotten.update(o)
            t+=1
        return t

        
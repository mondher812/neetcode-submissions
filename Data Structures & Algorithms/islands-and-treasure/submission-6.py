class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        r = len(grid)
        c = len(grid[0])
        q = deque()
        for i in range(r):
            for j in range(c):
                if grid[i][j] == INF:
                    visit = set()
                    q.append([i,j])
                    min_d = r*c
                    d = -1
                    while q:
                        qlen = len(q)
                        d+=1
                        for p in range(qlen):
                            pi,pj = q.popleft()
                            
                            if min(pi,pj) >= 0 and pi < r and pj < c:
                                visit.add((pi,pj))
                                if grid[pi][pj] == -1:
                                    continue
                                if grid[pi][pj] == 0:
                                    min_d = min(min_d,d)
                                else:
                                    if (pi+1,pj) not in visit:
                                        q.append([pi+1,pj])
                                    if (pi-1,pj) not in visit:

                                        q.append([pi-1,pj])
                                    if (pi,pj+1) not in visit:
                                        q.append([pi,pj+1])
                                    if (pi,pj-1) not in visit:

                                        q.append([pi,pj-1])
                    grid[i][j] = min_d
                    





        
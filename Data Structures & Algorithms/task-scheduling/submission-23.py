class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        t = 0
        h = []
        q = deque()
        m = defaultdict(int)
        i = 0
        for task in tasks:
            m[task]+=1
        for task in m.keys():
            heapq.heappush(h,(-m[task],task))
    
        while len(h)> 0 or len(q)>0:
            if len(h)>0:
                task = heapq.heappop(h)[1]
                if m[task] > 1:
                    q.append([t+n,task])
                m[task]-=1
            if len(q)>0:
                if q[0][0] <=t:
                    pop = q.popleft()
                    heapq.heappush(h,(-m[pop[1]],pop[1]))

            t+=1
        return t




          
             
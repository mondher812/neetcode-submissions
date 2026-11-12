class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance(x,y):
            return (x**2 + y**2)**(0.5)
        h = []
        hashed = defaultdict(list)
        for p in points:
            c = distance(p[0],p[1])
            hashed[c].append(p)
            if len(h) < k:
                heapq.heappush(h,(-c,p))
            else:
                if -c > h[0][0]:
                    heapq.heappop(h)
                    heapq.heappush(h,(-c,p))
        out = []
        for item in h:
            out.append(item[1])
        return out
        

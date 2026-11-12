class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        h = []
        h = [-stone for stone in stones]
        heapq.heapify(h)
        while len(h) >1:
            s1 = -heapq.heappop(h)
            s2 = -heapq.heappop(h)
            print(s1,s2,h)
            if s1< s2:
                heapq.heappush(h,-(s2-s1))
            elif s2 < s1:
                heapq.heappush(h,-(s1-s2))
        return -h[0] if h else 0
        
        
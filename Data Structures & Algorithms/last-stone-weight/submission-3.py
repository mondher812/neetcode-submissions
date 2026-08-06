class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i]*=-1

        heapq.heapify(stones)
        while len(stones)>=2:
            heavy1 = heapq.heappop(stones)
            heavy2 = heapq.heappop(stones)
            if heavy1 == heavy2:
                continue
            if heavy1 < heavy2:
                heapq.heappush(stones,heavy1 - heavy2)
        if len(stones) == 1:
            return -1*stones[0]
        return 0

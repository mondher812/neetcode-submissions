class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        out = {}
        h = []
        for item in nums:
            if item not in out:
                out[item] =1
            else:
                out[item]+=1
        for item in out:
            heapq.heappush(h,(out[item],item))
            if len(h) >k:
                heapq.heappop(h)
        res = []
        for i in range(k):
            res.append(heapq.heappop(h)[1])
        return res

            

        
        
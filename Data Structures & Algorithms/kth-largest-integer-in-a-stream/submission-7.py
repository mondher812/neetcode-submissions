class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.h= []
        self.k = k
        for i in nums:
            if len(self.h) < k:
                heapq.heappush(self.h,i)
            else:
                heapq.heappushpop(self.h,i)
        
    def add(self, val: int) -> int:
        if len(self.h) < self.k:
            heapq.heappush(self.h,val)
            return self.h[0]
        else:
            heapq.heappushpop(self.h,val)
            return self.h[0]
        
        

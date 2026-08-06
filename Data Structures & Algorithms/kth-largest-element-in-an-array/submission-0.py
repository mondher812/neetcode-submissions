class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        our_heap = []
        for i in range(len(nums)):
            if len(our_heap) < k:
                heapq.heappush(our_heap,nums[i])
            else:
                if nums[i] > our_heap[0]:
                    heapq.heappop(our_heap)
                    heapq.heappush(our_heap,nums[i])
        return our_heap[0]
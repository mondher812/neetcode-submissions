class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        import heapq
        max_h = []
        l = 0
        out = []

        for r in range(k):
            heapq.heappush(max_h,(-nums[r], r))
        out.append(-max_h[0][0])
        for r in range(k,len(nums)):
            l+=1
            heapq.heappush(max_h,(-nums[r],r))
            while l> max_h[0][1]:
                    heapq.heappop(max_h)
            out.append(-max_h[0][0])
        return out



           




        
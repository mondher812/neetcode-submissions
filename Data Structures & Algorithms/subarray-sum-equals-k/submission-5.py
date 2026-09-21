class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_s = {0:1}
        total = 0
        cur_sum = 0
        for item in nums:
            cur_sum +=item

            diff = cur_sum -k
            total+= prefix_s.get(diff,0) 
                
            prefix_s[cur_sum] = prefix_s.get(cur_sum,0) +1
        return total

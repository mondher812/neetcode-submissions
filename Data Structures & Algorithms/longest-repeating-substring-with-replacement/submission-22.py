class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0 
        prev_common = 0
        max_c = 0
        d =defaultdict(int)
        for r in range(len(s)):
            d[s[r]]+=1
            prev_common = max(prev_common,d[s[r]])
            while (r-l +1) - prev_common >k:
                d[s[l]]-=1
                l+=1
            max_c = max(max_c,r-l+1)  
        return max_c
    


                


        
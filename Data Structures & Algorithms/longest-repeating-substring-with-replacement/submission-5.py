class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d = {}
        l = 0
        m = 0
        max_c = ""
        max_v = 0
        for r in range(len(s)):
            d[s[r]] = d.get(s[r],0) + 1
            if d[s[r]] > max_v:
                max_c = s[r]
                max_v = d[s[r]]
            while r - l + 1 - max_v > k:
                d[s[l]] -= 1
                l+=1
            m = max(m, r-l + 1)
        return m


            
          
            



            
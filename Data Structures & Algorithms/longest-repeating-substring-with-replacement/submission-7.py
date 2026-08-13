class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        h = {}
        m = 0
        l = 0
        for r in range(len(s)):
            h[s[r]] = h.get(s[r],0)+1

            while ((r-l+1) -(max(h.values()))>k):
                h[s[l]] -=1
                l+=1
            m = max(m,r-l+1)
        return m 


        
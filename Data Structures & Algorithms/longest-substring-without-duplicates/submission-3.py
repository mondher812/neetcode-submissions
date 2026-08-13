class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        h = set()
        m = 0
        for i in range(len(s)):
            if s[i] not in h:
                h.add(s[i])
                m = max(m,len(h))
            else:
                while s[i] in h:
                    h.remove(s[l])
                    l+=1
                h.add(s[i])
                m = max(m,len(h))

        return m
            


        
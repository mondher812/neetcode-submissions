class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        c = {}
        for char in t:
            c[char] = c.get(char,0) +1
        l = 0
        o = {}
        need = len(c.keys())
        have = 0
        cur_s = []
        for r in range(len(s)):
            o[s[r]] = o.get(s[r],0) +1
            if s[r] in c and o[s[r]] == c[s[r]]:
                have +=1
                if have == need:
                    while s[l] not in c or o[s[l]] > c[s[l]]:
                        o[s[l]] -= 1
                        l+=1
                    cur_s.append([l,r])
                    o[s[l]] -= 1
                    l+=1
                
                    have -=1
        min_l = float("inf")
        min_ind = -1

        for i, pair in enumerate(cur_s):
            cur_len = pair[1] - pair[0] + 1

            if cur_len < min_l:
                min_l = cur_len
                min_ind = i
                print (cur_s[min_ind])
        if min_ind == -1:
            return ""
        start, end = cur_s[min_ind]
        return s[start:end + 1]
            

    

                    

                
            



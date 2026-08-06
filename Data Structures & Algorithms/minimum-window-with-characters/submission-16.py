class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        cur_l = len(s)
        out = [-1,-1]
        dt = {}
        ds = {}
        for char in t:
            dt[char] = dt.get(char,0) + 1
        have = 0
        need = len(dt)
        l = 0 
        for r in range(len(s)):
            ds[s[r]] = ds.get(s[r],0) + 1
            if s[r] in dt:
                if ds[s[r]] == dt[s[r]]:
                    have+=1
            while have == need:
                if r-l + 1<= cur_l:
                    cur_l = r-l+1
                    out[0] = l
                    out[1] =r
                if s[l] in dt:
                    ds[s[l]] -=1
                    if ds[s[l]] < dt[s[l]]:
                        have-=1
                else:
                    ds[s[l]] -=1
                l+=1
       
      
        return s[out[0]:out[1]+1]
                








        
        
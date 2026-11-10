class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        l = 0 
        need = defaultdict(int)
        for char in t:
            need[char]+=1
        cur_window = defaultdict(int)
        window_size = [0,0]
        changed = False
        window_len = 9999999999
        unique = len(set(t))
        have = 0
        for r in range(len(s)):
            cur_window[s[r]]+=1
            if cur_window[s[r]] == need[s[r]]:
                have+=1
                while have == unique:
                    if (r-l) + 1 < window_len:
                        changed = True
                        window_size[0] = l
                        window_size[1] = r
                        window_len = r - l + 1
                    if cur_window[s[l]] == need[s[l]]:
                        have-=1 
                    cur_window[s[l]] -=1
                    l+=1
        if not changed:
            return ""

        return s[window_size[0]:window_size[1]+1]
                




            
        
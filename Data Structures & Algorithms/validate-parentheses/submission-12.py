class Solution:
    def isValid(self, s: str) -> bool:
        st1 = []
        s_open = {}
        s_open["{"]="}"
        s_open["["]="]"
        s_open["("]=")"
        s_close = {}
        s_close["}"]="{"
        s_close["]"]="["
        s_close[")"]="("
    
    
        for char in s:
            if char in s_open.keys():
                st1.append(char)
            else:
                if len(st1) == 0 or st1[-1] != s_close[char]:
                    return False
                else:
                    st1.pop()
        return len(st1) == 0
            
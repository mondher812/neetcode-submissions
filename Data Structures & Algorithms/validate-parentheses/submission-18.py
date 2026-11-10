class Solution:
    def isValid(self, s: str) -> bool:
        opens  = set(["(","[","{"])
        close  = set([")","]","}"])
        d_p = {")":"(","}":"{","]":"["}
        from collections import deque
        stock = []
        for p in s:
            if p in opens:
                stock.append(p)
            if p in close:
                if len(stock) ==0:
                    return False
                else:
                    if stock[-1] == d_p[p]:
                        stock.pop()
                    else:
                        return False
        return len(stock) ==0        

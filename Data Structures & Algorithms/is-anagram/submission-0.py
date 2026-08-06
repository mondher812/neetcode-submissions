class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = {}
        for letter in s:
            if letter not in d.keys():
                d[letter] = 1
            else:
                d[letter]= d[letter]+1
        for letter in t:
            if letter in d.keys():
                if d[letter] ==0:
                    return False
                d[letter]= d[letter]- 1
                if d[letter] == 0:
                    del d[letter]
            else:
                return False
        return len(d) ==0
        
                
        

        

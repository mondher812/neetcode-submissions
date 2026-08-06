class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        ds_1 = {}
        ds_2 = {}
        for char in s1:
            ds_1[char] = ds_1.get(char,0)+ 1
        have = 0
        need = len(ds_1)
        r = 0
        if len(s2) < len(s1):
            return False
        while r < len(s1):
            ds_2[s2[r]] = ds_2.get(s2[r], 0) + 1
            if s2[r] in ds_1:
                if ds_2[s2[r]] == ds_1[s2[r]]:
                    have+=1
            if have == need:
                return True
            r+=1  
        print(ds_2)
            
        while r < len(s2):
            ds_2[s2[r]] = ds_2.get(s2[r], 0) + 1
            if s2[r] in ds_1:
                if ds_2[s2[r]] == ds_1[s2[r]]:
                    have+=1
            if s2[l] in ds_1:
                if ds_2[s2[l]] == ds_1[s2[l]]:
                    have-=1
            ds_2[s2[l]] = ds_2.get(s2[l], 0) - 1
            l+=1
            r+=1
            if have == need:
                return True
        return False

            
            
            

           
                
                

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        path= []
        def ispali(i,j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i+=1
                j-=1
            return True

            

        def rec(i):
            if i >= len(s):
                res.append(path.copy())
                return
            for j in range(i,len(s)):
                if ispali(i,j):
                    path.append(s[i:j+1])
                    rec(j+1)
                    path.pop()
        rec(0)
        return res
   
   
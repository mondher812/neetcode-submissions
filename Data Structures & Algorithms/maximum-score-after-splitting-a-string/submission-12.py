class Solution:
    def maxScore(self, s: str) -> int:
        ind = 0
        l = 0
        max_s = 0
        count= {}
        count["1"] = 0
        for item in s:
            if item not in count:
                count[item] =1
            else:
                count[item]+=1
        r = count["1"]
        while ind < len(s)-1:
            if s[ind] == "0":
                l +=1
            if s[ind] =="1":
                r -=1
        
            max_s = max(max_s,l+r)
        
            ind+=1
        return max_s

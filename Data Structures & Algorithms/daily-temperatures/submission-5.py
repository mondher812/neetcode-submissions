class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        s = []
        o = [0]*len(temperatures)
        for i in range(len(temperatures)):
            while len(s)>0 and temperatures[i]>s[-1][1]:
                k = s.pop()[0]
                o[k]= i-k
            s.append([i,temperatures[i]])
        return o 
           

        
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        popper = []
        c = 0
        hs = []
        
        for item in temperatures:
            hs.append(0)
        for i,item in enumerate(temperatures):
            while len(popper) > 0 and item > popper[-1][0]:
                popped = popper.pop()
                hs[popped[1]] = i - popped[1]
            popper.append([item,i])
        return hs


               
        
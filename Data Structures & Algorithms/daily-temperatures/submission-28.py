class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        out = [0] * len(temperatures)
        process = []
        for i,temp in enumerate(temperatures):
            if len(process) == 0:
                process.append([i,temp])
            else:
                while len(process) > 0 and process[-1][1] < temp:
                   popped = process.pop()
                   out[popped[0]] = i-popped[0]
                process.append([i,temp])
        return out




        
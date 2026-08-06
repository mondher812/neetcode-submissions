class Solution:
    def isValid(self, s: str) -> bool:
        s1 = []
        ke = {"]":"[",")":"(","}":"{"}
        for item in s:
            if item in ke.values():
                s1.append(item)
            if item in ke.keys():
                if len(s1) > 0 and (s1[-1] == ke[item]):
                    s1.pop()
                else:
                    return False
        return len(s1) == 0

        

        
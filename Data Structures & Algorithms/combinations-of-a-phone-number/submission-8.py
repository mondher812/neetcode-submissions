class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        number_map = {
            "1": [],
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]}
        out = []
        def dfs(c):
            if len(out) == 0:
                for ch in number_map[c]:
                    out.append(ch)
                return out
            else:
                temp = []
                for i in range(len(out)):
                    for ch in number_map[c]:
                        temp.append(out[i] + ch)
                return temp


        for char in digits:
            out = dfs(char)
        return out
        
            
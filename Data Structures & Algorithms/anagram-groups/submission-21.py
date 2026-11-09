class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for word in strs:
            made_of = [0] * 26
            for s in word:
                made_of[ord(s)- ord("a")] += 1
            k = tuple(made_of)
            if k not in d:
                d[k] = []

            d[k].append(word)
        return list(d.values())
                

                
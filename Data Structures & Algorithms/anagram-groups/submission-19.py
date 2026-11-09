class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for word in strs:
            made_of = [0] * 26
            for s in word:
                made_of[ord(s)- ord("a")] += 1
            if tuple(made_of) not in d:
                d[tuple(made_of)] = []

            d[tuple(made_of)].append(word)
        return list(d.values())
                

                
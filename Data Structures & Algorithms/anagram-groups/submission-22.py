from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)

        for word in strs:
            made_of = [0] * 26

            for s in word:
                made_of[ord(s) - 97] += 1

            d[tuple(made_of)].append(word)

        return list(d.values())
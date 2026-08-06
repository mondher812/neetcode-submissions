class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dct = defaultdict(list)
        for s in strs:
            x = [0]*26
            for i in s:
                val = ord(i) - ord("a")
                x[val]+=1
            dct[tuple(x)].append(s)
        return list(dct.values())

        
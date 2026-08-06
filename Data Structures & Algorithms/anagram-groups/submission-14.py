class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        maps = {}
        for i,item in enumerate(strs):
            base_tup = [0,]*26
            for letter in item:
                base_tup[ord(letter)-ord("a")]+=1
            if tuple(base_tup) in maps:
                maps[tuple(base_tup)].append(item)
            else:
                maps[tuple(base_tup)] = [item]
        return list(maps.values())
        
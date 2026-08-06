class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        maps = {}
        for i,item in enumerate(strs):
            base_tup = [0,]*26
            for letter in item:
                base_tup[ord(letter)-ord("a")]+=1
            if tuple(base_tup) in maps:
                maps[tuple(base_tup)].append(i)
            else:
                maps[tuple(base_tup)] = [i]
        out= [[] for _ in range(len(maps.keys()))]
        for p,itme in enumerate(maps.keys()):
            for ind in maps[itme]:
                out[p].append(strs[ind])
        return out



       
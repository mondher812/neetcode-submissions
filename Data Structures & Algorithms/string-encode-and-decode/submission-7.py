class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for item in strs:
            k = len(item)
            s=s+str(k)+"#"+item
        return s

    def decode(self, s: str) -> List[str]:
        o = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j+=1
            l = int(s[i:j])
            o.append(s[j+1:l+j+1])
            i = l+j+1
        return o
            



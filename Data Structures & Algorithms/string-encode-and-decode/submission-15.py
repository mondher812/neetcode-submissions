class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for item in strs:
            s+= str(len(item))
            s+="#"
            s+=item
        print(s)
        return s


    def decode(self, s: str) -> List[str]:
        r = 0
        cur_num = ""
        out = []
        while r <len(s):
            if s[r] != "#":
                cur_num += s[r]
                r+=1
            else:
                cur_s =""
                r+=1
                for i in range(int(cur_num)):
                    cur_s += s[r+i]
                out.append(cur_s)
                r+=(int(cur_num))
                cur_num = ""
        return out
                        
        


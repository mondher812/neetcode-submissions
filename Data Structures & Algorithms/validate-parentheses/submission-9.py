class Solution:
    def isValid(self, s: str) -> bool:
        st1 = []
        most_r = []

        for p in s:
            if p == "(":
                st1.append(p)
                most_r.append(p)
            if p == ")":
                if len(st1) == 0 or most_r[-1] != "(":
                    return False
                else: 
                    st1.pop()
                    most_r.pop()
            if p == "{":
                st1.append(p)
                most_r.append(p)

            if p == "}":
                if len(st1) == 0 or most_r[-1] != "{":
                    return False
                else: 
                    st1.pop()
                    most_r.pop()
            if p == "[":
                st1.append(p)
                most_r.append(p)
            if p == "]":
                if len(st1) == 0 or most_r[-1] != "[":
                    return False
                else: 
                    st1.pop()
                    most_r.pop()
       
        return len(st1) == 0 
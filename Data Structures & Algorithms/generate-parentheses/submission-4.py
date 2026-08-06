class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        s = []
        r = []
        def rec(o,c):
            if o == c ==n:
                r.append("".join(s))
                return
            if o<n:
                s.append("(")
                rec(o+1,c)
                s.pop()
            if c<o:
                s.append(")")
                rec(o ,c+1)
                s.pop()
        rec(0,0)
        return r


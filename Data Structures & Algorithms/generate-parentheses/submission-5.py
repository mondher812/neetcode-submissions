class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        o =[]
        
        def backtrack(op,total,cur):
            if total ==n:
                o.append(cur)
                return
            else:
                c = cur +"("
                if op==0:
                    c = cur +"("
                    backtrack(op+1,total,c)
                else:
                    if op+total <n:
                        backtrack(op+1,total,c)
                    c = cur +")"
                    backtrack(op-1,total+1,c)
        backtrack(0,0,"")
        return o

                    



                

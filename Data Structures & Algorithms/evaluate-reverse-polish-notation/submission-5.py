class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        o = []
        check = ["+","-","*","/"]
        for item in tokens:
            if item not in check:
                o.append(int(item))
            else:
                b = o.pop()
                if item == "+":
                    a = o.pop()
                    b = a+b
                    o.append(b)
                elif item == "-":
                    a = o.pop()
                    b = a-b
                    o.append(b)
                elif item == "*":
                    a = o.pop()
                    b = a*b
                    o.append(b)
                elif item =="/":
                    a = o.pop()
                    b = int(float(a)/b)
                    o.append(b)
                
        return o[0]
                


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        for token in tokens:
            if token not in set(["*","-","+","/"]):
                s.append(int(token))
            else:
                num1 = s.pop()
                num2 = s.pop()
                if token == "*":
                    s.append(num2 * num1)
                elif token == "+":
                    s.append(num2 + num1)
                elif token == "-":
                    s.append(num2 - num1)
                elif token == "/":
                    s.append(int(num2 / num1))
                
        return s[-1]



        
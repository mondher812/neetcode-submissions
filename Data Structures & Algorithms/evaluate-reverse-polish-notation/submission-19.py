class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums = []
        oper = set(["+","-","*","/"])
        for char in tokens:
            if char not in oper:
                nums.append(int(char))
            else:
                i = nums.pop()
                j = nums.pop()
                if char == "-":
                    nums.append((j) - int(i))
                elif char == "+":
                    nums.append(int(j) + int(i))
                elif char == "*":
                    nums.append(int(j) * int(i))
                elif char == "/":
                    nums.append(int(int(j) / int(i)))
        return int(nums[-1])



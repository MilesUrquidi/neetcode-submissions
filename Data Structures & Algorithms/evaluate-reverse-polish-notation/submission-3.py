class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i == "+":
                res = stack.pop() + stack.pop()
                stack.append(res)
            elif i == "*":
                res = stack.pop() * stack.pop()
                stack.append(res)
            elif i == "-":
                a = stack.pop()
                b = stack.pop()
                res = b - a
                stack.append(res)
            elif i == "/":
                a = stack.pop()
                b = stack.pop()
                res = int(float(b) / a)
                stack.append(res)
            else:
                stack.append(int(i))
        return stack[0]


        
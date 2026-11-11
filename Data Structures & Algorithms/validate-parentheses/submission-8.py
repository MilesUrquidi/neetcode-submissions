class Solution:
    def isValid(self, s: str) -> bool:
        #([])
        table = {"}":"{","]":"[",")":"("}
        stack = []
        if len(s) % 2 != 0:
            return False

        for i in s:
            if i in table:
                if not stack or stack.pop() != table[i]:
                    return False
            else:
                stack.append(i)
        return not stack



        
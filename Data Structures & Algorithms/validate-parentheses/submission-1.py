class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        table = {"}":"{","]":"[",")":"("}

 
        for ch in s:
            if ch in table:
                if not stack or stack.pop() != table[ch]:
                    return False
            else:
                stack.append(ch)
        return not stack

        
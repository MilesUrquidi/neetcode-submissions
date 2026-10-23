class Solution:
    def isValid(self, s: str) -> bool:
        table = {"]":"[","}":"{",')':'('}
        stack = []

        for c in s:
            if c in table:
                if not stack or stack.pop() != table[c]:
                    return False
            else:
                stack.append(c)
        return not stack
        
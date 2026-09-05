class Solution:
    def isValid(self, s: str) -> bool:
        open_parantheses = ( '(', '[', '{')
        close_parantheses = (')', ']', '}')
        parantheses_map = {')': '(', ']': '[', '}': '{'}
        stack = []
        seen_open = []

        for char in s:
            # print("stack: ", stack)
            if char in open_parantheses:
                stack.append(char)
                seen_open.append(char)
            elif char in close_parantheses:
                # print("char: ", char, "seen_open: ", seen_open)
                if stack and parantheses_map[char] == seen_open[-1]:
                    stack.pop()
                    seen_open.pop()
                else:
                    return False
        if stack:
            return False
        return True
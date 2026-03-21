class Solution:
    def isValid(self, s: str) -> bool:
        open_bracket = ['(', '{', '[']
        close_bracket = [')', '}', ']']
        
        d = dict(zip(close_bracket, open_bracket))
        stack = []

        for char in s:
            if char in open_bracket:
                stack.append(char)
            elif char in close_bracket:
                if not stack or stack[-1] != d[char]:
                    return False
                stack.pop()

        return len(stack) == 0  
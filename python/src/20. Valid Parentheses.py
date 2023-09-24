class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for c in s:
            try:
                if c == "(" or c == "{" or c == "[":
                    stack.append(c)
                elif c == ")":
                    if stack.pop() != "(":
                        return False
                elif c == "}":
                    if stack.pop() != "{":
                        return False
                elif c == "]":
                    if stack.pop() != "[":
                        return False
            except IndexError:
                return False

        return len(stack) == 0


class Solution:
    def isValid(self, s: str) -> bool:
        di = {")" : "(", "]" : "[", "}":"{"}
        stack = []
        for ch in s:
            if ch not in di:
                stack.append(ch)
            else:
                if not stack or stack[-1] != di[ch]:
                    return False
                stack.pop()
        return len(stack) == 0


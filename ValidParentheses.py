class Solution:
    def isValid(self, s: str) -> bool:
        open_bracket = {"(", "[", "{"}
        pairs = {")": "(", "]": "[", "}": "{"}
        stack = []

        for char in s:
            if char in open_bracket:
                stack.append(char)

            else:
                if not stack or stack[-1] != pairs[char]:
                    return False
                stack.pop()
        return not stack


soluttion = Solution()

print(soluttion.isValid("()"))

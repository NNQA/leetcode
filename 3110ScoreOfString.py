class Solution:
    def scoreOfString(self, s: str, i: int = 1) -> int:
        return (
            abs(ord(s[i]) - ord(s[i - 1])) + self.scoreOfString(s, i + 1)
            if i != len(s)
            else 0
        )

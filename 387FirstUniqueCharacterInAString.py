class Solution:
    def firstUniqChar(self, s: str) -> int:

        fre = [0] * 26

        for c in s:
            fre[ord(c) - ord("a")] += 1

        for c in s:
            if fre[ord(c) - ord("a")] == 1:
                return s.index(c)
        return -1

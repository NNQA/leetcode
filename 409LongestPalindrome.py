class Solution:
    def longestPalindrome(self, s: str) -> int:

        count = {}
        for c in s:
            count[c] = count.get(c, 0) + 1

        length = 0
        odd_found = False
        for v in count.values():
            if v % 2 == 0:
                length += v
            else:
                length += v - 1
                odd_found = True

        if odd_found:
            length += 1

        return length

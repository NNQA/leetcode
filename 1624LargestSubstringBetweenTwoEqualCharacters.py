class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:

        max_length = -1
        last_seen = {}
        for i, v in enumerate(s):
            if v in last_seen:
                max_length = max(max_length, i - last_seen[v] - 1)
            else:
                last_seen[v] = i
        return max_length

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        dp = [] * len(s)
        for i in range(len(s)):
            dp.append(s[i])

        j = 0
        for i in range(len(t)):
            if j < len(s) and t[i] == dp[j]:
                j += 1

        return j == len(s)

class Solution:
    def maxScore(self, s: str) -> int:
        prefixSum = [0] * len(s)
        suffixSum = [0] * len(s)

        prefixSum[0] = s[0]
        for i in range(1, len(s)):
            prefixSum[i] = prefixSum[i - 1] + s[i]

        suffixSum[-1] = s[-1]
        maxScore = 0
        for i in range(len(s) - 2, -1, -1):
            suffixSum[i] = suffixSum[i + 1] + s[i]
        maxScore = 0
        for i in range(1, len(s)):
            score = prefixSum[i - 1].count("0") + suffixSum[i].count("1")
            maxScore = max(maxScore, score)
        return maxScore


print(Solution().maxScore("011101"))

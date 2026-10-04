class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        s = "aeuio"
        n = len(words)
        pre = [0] * (n + 1)
        for i in range(n):
            pre[i + 1] = pre[i] + (words[i][0] in s and words[i][-1] in s)
        ans = []
        for l, r in queries:
            ans.append(pre[r + 1] - pre[l])
        return ans


print(
    Solution().vowelStrings(["aba", "bcb", "ece", "aa", "e"], [[0, 2], [1, 4], [1, 1]])
)

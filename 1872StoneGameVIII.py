import itertools


class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        n = len(stones)

        pref = stones.copy()
        for i in range(1, n):
            pref[i] += pref[i - 1]

        dp = pref[n - 1]

        for i in range(n - 2, 0, -1):
            dp = max(dp, pref[i] - dp)

        return dp

    def stoneGameVIII2(self, stones: List[int]) -> int:
        n = len(stones)
        s = list(itertools.accumulate(stones))

        def maxDiff(i):
            if i == n - 1:
                return s[n - 1]
            return max(maxDiff(i + 1), s[i] - maxDiff(i + 1))

        return maxDiff(1)


sol = Solution()
print(sol.stoneGameVIII([-1, 2, -3, 4, -5]))
print(sol.stoneGameVIII2([7, -6, 5, 10, 5, -2, -6]))

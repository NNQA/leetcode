from collections import Counter


class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        c = Counter(nums)
        ans = 0
        for val in c.values():
            ans += val * (val - 1) // 2
        return ans


print(Solution().numIdenticalPairs([1, 2, 3, 1, 1, 3]))

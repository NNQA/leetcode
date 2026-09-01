class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        l = 0
        total = 0
        ans = 0
        for r in range(len(nums)):

            total += nums[r]

            while (r - l + 1) * nums[r] - total > k:
                total -= nums[l]
                l += 1

            ans = max(ans, r - l + 1)
        return ans


sol = Solution()
print(sol.maxFrequency([1, 2, 4], 5))
print(sol.maxFrequency([1, 4, 8, 13], 5))
print(sol.maxFrequency([3, 9, 6], 2))

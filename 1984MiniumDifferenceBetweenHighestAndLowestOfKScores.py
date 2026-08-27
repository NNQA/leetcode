class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:

        if k == 1:
            return 0
        min_score = float("inf")
        nums.sort()
        i = 0
        while i <= len(nums) - k:
            min_score = min(min_score, nums[i + k - 1] - nums[i])
            i += 1
        return min_score


sol = Solution()
print(sol.minimumDifference([9, 4, 1, 7], 2))
# 1 4 7 9
# 4 - 2

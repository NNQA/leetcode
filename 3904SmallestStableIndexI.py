class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:

        right = [nums[-1]] * len(nums)
        for i in range(len(nums) - 2, -1, -1):
            right[i] = min(right[i + 1], nums[i])
        max_val = 0
        for i, x in enumerate(nums):
            max_val = max(max_val, x)
            if max_val - right[i] <= k:
                return i
        return -1


solution = Solution()
print(solution.firstStableIndex([5, 0, 1, 4], 3))
print(solution.firstStableIndex([3, 2, 1], 1))

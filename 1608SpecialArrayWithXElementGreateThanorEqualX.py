class Solution:
    def specialArray(self, nums: list[int]) -> int:
        nums.sort(reverse=True)
        i = 0
        while i < len(nums) and i < nums[i]:
            i += 1

        return -1 if i < len(nums) and i == nums[i] else i


Solution().specialArray([3, 6, 7, 7, 0])  # Output: 5

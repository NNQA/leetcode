class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        maxx = 0
        increase = 0
        decrease = 0

        for i in range(1, len(nums)):
            if nums[i - 1] < nums[i]:
                increase += 1
                maxx = max(maxx, increase + 1)
                decrease = 0
            elif nums[i - 1] > nums[i]:
                decrease += 1
                maxx = max(maxx, decrease + 1)
                increase = 0
        return maxx

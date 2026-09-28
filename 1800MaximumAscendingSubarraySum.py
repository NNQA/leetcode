class Solution:
    def maxAscendingSum(self, nums: list[int]) -> int:

        sum = nums[0]
        ans = max(0, sum)
        pre = nums[0]

        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                sum = nums[i]
                continue
            sum += nums[i]
            ans = max(sum, ans)
        return ans


print(Solution().maxAscendingSum([3, 6, 10, 1, 8, 9, 9, 8, 9]))

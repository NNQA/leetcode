


class Solution(object):
    def minimumDifference(self, nums, k):
        nums.sort()
        return min(nums[i + k - 1] - nums[i] for i in range(len(nums) - k  + 1))

solution = Solution()
print(solution.minimumDifference([9,4,1,7], 2))
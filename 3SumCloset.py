class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:

        nums.sort()
        closet_sum = float('inf')
        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                closet = nums[i] + nums[left] + nums[right]

                if closet == target:
                    return closet
                if abs(closet - target) < abs(closet_sum - target):
                    closet_sum = closet

                if closet < target:
                    left += 1
                else:
                    right -= 1

        return closet_sum


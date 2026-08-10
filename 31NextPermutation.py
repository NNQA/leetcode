class Solution:
    def nextPermutation(self, nums: List[int]) -> None:

        i = len(nums) - 1

        while i > 0 and nums[i - 1] >= nums[i]:
            i -= 1

        if i == 0:
            nums.reverse(),
            return

        j = len(nums) - 1

        while j >= i and nums[j] <= nums[i - 1]:
            j -= 1
        nums[i - 1], nums[j] = nums[j], nums[i - 1]
        nums[i:] = reversed(nums[i:])
        print(nums)


sol = Solution()
sol.nextPermutation([1, 2, 3, 4, 2])
sol.nextPermutation([3, 2, 1])
sol.nextPermutation([1, 1, 5])

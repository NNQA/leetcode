class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True

        prev = nums[0] % 2 == 0
        for i in range(1, len(nums)):
            if prev == (nums[i] % 2 == 0):
                return False
            prev = nums[i] % 2 == 0
        return True

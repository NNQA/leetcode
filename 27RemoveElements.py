class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        if not nums:
            return 0

        length = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[length] = nums[i]
                length += 1

        return length


sol = Solution()
print(sol.removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2))

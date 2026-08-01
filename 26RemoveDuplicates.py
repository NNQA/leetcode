class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        # length = len(nums)
        # unique_sets = set(nums)
        # unique_list = list(unique_sets)
        # unique_list.sort()
        # for i in range(length - len(unique_list), length):
        #     unique_list.append("_")

        # return unique_list

        if not nums:
            return 0
        length = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[length - 1]:
                nums[length] = nums[i]
                length += 1
        print(nums)
        unique_sets = set(nums)
        print(len(unique_sets))
        return length


sol = Solution()
print(sol.removeDuplicates([1, 1, 2, 3, 3, 4, 5, 5]))

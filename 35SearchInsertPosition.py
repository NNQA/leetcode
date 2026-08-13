class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        res = 0
        check = False
        for i in range(len(nums)):
            if nums[i] == target:
                res = i
                check = True
                break
        if res == 0 and check == False:
            for i in range(len(nums)):
                if nums[i] > target:
                    return i
                if i == len(nums) - 1:
                    return i + 1

        return res


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + (right - left) / 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left


sol = Solution()
print(sol.searchInsert([1], 1))

from collections import Counter


class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        nums.sort()
        count = Counter(nums)
        duplicate = next(num for num, freq in count.items() if freq == 2)
        n = len(nums)
        missing = next(num for num in range(1, n + 1) if num not in count)
        return [duplicate, missing]

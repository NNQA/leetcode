class Solution:
    def frequencySort(self, nums: list[int]) -> list[int]:
        counter = {}
        for num in nums:
            counter[num] = counter.get(num, 0) + 1
        return sorted(nums, key=lambda x: (counter[x], -x))

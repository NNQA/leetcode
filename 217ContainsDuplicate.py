class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        n = len(set(nums))
        if n == len(nums):
            return False
        return True

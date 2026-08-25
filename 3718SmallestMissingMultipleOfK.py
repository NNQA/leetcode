class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        nums_set = set(nums)
        n = k
        while n in nums_set:
            n += k

        return n


solution = Solution()
print(solution.missingMultiple([8, 2, 3, 4, 6], 2))

class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        mn = min((x for x in nums1 if x & 1), default=None)
        return mn is None or all(x >= mn for x in nums1 if x & 1 == 0)


solution = Solution()
print(solution.uniformArray([1, 4, 7]))
print(solution.uniformArray([13, 10]))

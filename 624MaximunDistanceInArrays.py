class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        max_val = arrays[0][-1]
        min_val = arrays[0][0]
        ans = 0
        for i in range(1, len(arrays)):
            ans = max(ans, abs(arrays[i][-1] - min_val), abs(max_val - arrays[i][0]))
            max_val = max(max_val, arrays[i][-1])
            min_val = min(min_val, arrays[i][0])

        return ans


solution = Solution()
print(solution.maxDistance([[1, 2, 3], [4, 5], [1, 2, 3]]))

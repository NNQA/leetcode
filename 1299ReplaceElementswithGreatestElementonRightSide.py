class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        if len(arr) == 1:
            return [-1]
        ans = [-1] * len(arr)

        max_val = -1
        for i in range(len(arr) - 1, -1, -1):
            max_val = max(max_val, arr[i])
            ans[i] = max_val
        return ans[1:] + [-1]


solution = Solution()
print(solution.replaceElements([17, 18, 5, 4, 6, 1]))

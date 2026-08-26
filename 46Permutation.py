class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums[:]]

        def backtrack(ans, sol):

            if len(sol) == len(nums):
                return ans.append(sol[:])

            for x in nums:
                if x not in sol:
                    sol.append(x)
                    backtrack(ans, sol)
                    sol.pop()

        ans = []
        sol = []
        backtrack(ans, sol)
        return ans


solution = Solution()
print(solution.permute([1, 2, 3]))

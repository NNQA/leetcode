import math


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = []
        visit = [False] * len(nums)
        if len(nums) == 1:
            return [nums[:]]

        def backtrack(ans, path):

            if len(path) == len(nums):
                return ans.append(path[:])

            for i in range(len(nums)):
                if visit[i]:
                    continue

                if i > 0 and nums[i] == nums[i - 1] and not visit[i - 1]:
                    continue

                visit[i] = True
                path.append(nums[i])

                backtrack(ans, path)

                path.pop()
                visit[i] = False

        nums.sort()
        backtrack(ans, [])
        return ans


solution = Solution()
print(solution.permuteUnique([1, 1, 2]))

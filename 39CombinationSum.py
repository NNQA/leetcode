class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        res = []

        def backtrack(arr: List[int], start: int, target):
            if target == 0:
                res.append(arr[:])
                return

            for i in range(start, len(candidates)):
                if candidates[i] > target:
                    continue
                arr.append(candidates[i])
                backtrack(arr, i, target - candidates[i])
                arr.pop()

        candidates.sort()
        backtrack([], 0, target)
        return res


sol = Solution()
print(sol.combinationSum([2, 3, 5], 8))

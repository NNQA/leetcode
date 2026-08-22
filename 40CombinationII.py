class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        res = []

        def backtrack(arr, start, target):
            if target == 0:
                res.append(arr[:])
                return
            for i in range(start, len(candidates)):
                if candidates[i] > target:
                    continue
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                arr.append(candidates[i])
                backtrack(arr, i + 1, target - candidates[i])
                arr.pop()

        candidates.sort()
        backtrack([], 0, target)
        return res


sol = Solution()
print(sol.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))

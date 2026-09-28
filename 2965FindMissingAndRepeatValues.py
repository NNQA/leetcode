from collections import defaultdict


class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:

        n = len(grid)
        mapG = defaultdict(int)
        repeat = 0
        missing = 0
        for i in range(n):
            for j in range(len(grid[i])):
                mapG[grid[i][j]] += 1
        for i in range(1, n * n + 1):
            if mapG[i] == 2:
                repeat = i
            if mapG[i] == 0:
                missing = i
        return [repeat, missing]


print(Solution().findMissingAndRepeatedValues([[1, 3], [2, 2]]))

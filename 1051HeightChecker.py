class Solution:
    def heightChecker(self, heights: list[int]) -> int:
        a = heights[:]

        count = 0
        for i in range(len(heights)):
            if a[i] != heights[i]:
                count += 1
        return count

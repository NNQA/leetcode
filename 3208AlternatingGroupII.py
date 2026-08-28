class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        colors.extend(colors[: (k - 1)])

        l = 0
        count = 0
        for r in range(len(colors)):

            if r > 0 and colors[r] == colors[r - 1]:
                l = r

            if r - l + 1 >= k:
                count += 1

        return count


sol = Solution()
print(sol.numberOfAlternatingGroups([0, 1, 0, 1, 0], 3))

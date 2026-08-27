class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:

        count = 0

        for i in range(k):
            if blocks[i] == "W":
                count += 1
        ans = count
        for i in range(k, len(blocks)):
            if blocks[i] == "W":
                count += 1
            if blocks[i - k] == "W":
                count -= 1
            ans = min(ans, count)
        return ans


sol = Solution()
print(sol.minimumRecolors("BWWWBB", 6))
# print(sol.maxProfitTwoDP([7, 1, 5, 3, 6, 4]))
# print(sol.maxProfitTwoDP([2, 1, 4]))

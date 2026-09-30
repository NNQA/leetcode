class Solution:
    # 0ms
    def getRow(self, rowIndex: int) -> list[int]:

        dp = [[1] * (i + 1) for i in range(rowIndex + 1)]
        if rowIndex < 2:
            return dp[rowIndex]
        for i in range(2, rowIndex + 1):
            for j in range(1, i):
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]

        return dp[rowIndex]

    def getRow2(self, rowIndex: int) -> list[int]:
        row = [1]
        for j in range(1, rowIndex + 1):
            row.append(row[-1] * (rowIndex - j + 1) // j)
        return row


print(Solution().getRow(3))

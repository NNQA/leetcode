class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        arrCop = [row[:] for row in matrix]
        for i in range(n):
            for j in range(n):
                matrix[i][j] = arrCop[n - 1 - j][i]


Solution().rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# 1 2 3
# 4 5 6
# 7 8 9

# 7 4 1

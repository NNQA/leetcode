class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_col_tups = []

        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    row_col_tups += [
                        (i, board[i][j]),
                        (board[i][j], j),
                        (i // 3, j // 3, board[i][j]),
                    ]
        return len(row_col_tups) == len(set(row_col_tups))

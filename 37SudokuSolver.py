class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:

        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                if board[r][c] != ".":
                    num = board[r][c]
                    box = (r // 3) * 3 + c // 3

                    rows[r].add(num)
                    cols[c].add(num)
                    boxes[box].add(num)

        def solve():
            best_row = -1
            best_col = -1
            best_candidates = None
            for r in range(9):
                for c in range(9):
                    if board[r][c] != ".":
                        continue
                    box = (r // 3) * 3 + c // 3

                    candidates = []

                    for num in "123456789":
                        if (
                            num not in rows[r]
                            and num not in cols[c]
                            and num not in boxes[box]
                        ):
                            candidates.append(num)
                    if not candidates:
                        return False
                    if best_candidates is None or len(candidates) < len(
                        best_candidates
                    ):
                        best_row = r
                        best_col = c
                        best_candidates = candidates

                        if len(candidates) == 1:
                            break

                if best_candidates is not None and len(best_candidates) == 1:
                    break

            if best_candidates is None:
                return True

            box = (best_row // 3) * 3 + best_col // 3

            for num in best_candidates:

                board[best_row][best_col] = num
                rows[best_row].add(num)
                cols[best_col].add(num)
                boxes[box].add(num)

                if solve():
                    return True

                board[best_row][best_col] = "."
                rows[best_row].remove(num)
                cols[best_col].remove(num)
                boxes[box].remove(num)

            return False

        solve()


Solution().solveSudoku(
    [
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", "9", ".", ".", "1", ".", ".", "3", "."],
        [".", ".", "6", ".", "2", ".", "7", ".", "."],
        [".", ".", ".", "3", ".", "4", ".", ".", "."],
        ["2", "1", ".", ".", ".", ".", ".", "9", "8"],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", "2", "5", ".", "6", "4", ".", "."],
        [".", "8", ".", ".", ".", ".", ".", "1", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
    ]
)

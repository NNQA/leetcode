
class Solution:
    # def convert(self, s: str, numRows: int) -> str:
    #     substrings = [''] * numRows
    #     if len(s) == 0 or numRows == 1 or numRows == len(s):
    #         return s
    #     for i in range(numRows):
    #         for j in range(i, len(s), 2 * numRows - 2):
    #             substrings[i] += s[j]
    #             if i != 0 and i != numRows - 1 and j + 2 * numRows - 2 - 2 * i < len(s):
    #                 substrings[i] += s[j + 2 * numRows - 2 - 2 * i]
    #     return substrings[0] + ''.join(substrings[1:])
    def convert(self, s: str, numRows: int) -> str:
        if len(s) == 0 or numRows == 1 or numRows == len(s):
            return s
        result = [''] * numRows
        index = 0 
        step = 1

        for char in s:
            result[index] += char
            if index == 0:
                step = 1
            elif index == numRows - 1:
                step = -1
            index += step
        return ''.join(result)
solution = Solution()
print(solution.convert("PAYPALISHIRING", 4))  # Output: "PAHNAPLSIIGYIR"
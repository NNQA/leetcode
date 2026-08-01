class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        res = []
        recurse(res, 0, 0, "", n)
        return res


def recurse(res: List[int], left: int, right: int, s: str, n: int):
    if len(s) == n * 2:
        res.append(s)
        return
    if left < n:
        recurse(res, left + 1, right, s + "(", n)
    if right < left:
        recurse(res, left, right + 1, s + ")", n)


solution = Solution()
print(solution.generateParenthesis(1))

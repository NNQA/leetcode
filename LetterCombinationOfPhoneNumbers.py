class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if not digits:
            return []

        map_value = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        result = []

        backtrack("", digits, map_value, result)
        return result


def backtrack(
    combination: str, next_digits: str, map_value: dict[str, str], result: list
):
    if len(next_digits) == 0:
        return result.append(combination)
    else:
        for letter in map_value[next_digits[0]]:
            backtrack(combination + letter, next_digits[1:], map_value, result)

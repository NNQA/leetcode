from collections import Counter


class Solution:
    def divideArray(self, nums: list[int]) -> bool:

        c = Counter(nums)
        for val in c.values():
            if val % 2 != 0:
                return False
        return True


print(
    Solution().divideArray(
        [
            9,
            4,
            18,
            3,
            2,
            6,
            18,
            15,
            7,
            15,
            6,
            4,
            15,
            14,
            7,
            4,
            15,
            4,
            3,
            17,
            9,
            13,
            13,
            12,
            2,
            14,
            12,
            17,
        ]
    )
)

class NumArray:

    def __init__(self, nums: list[int]):
        self.prefix = nums
        for i in range(1, len(self.prefix)):
            self.prefix[i] += self.prefix[i - 1]

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.prefix[right]
        return self.prefix[right] - self.prefix[left - 1]


print(NumArray.__init__([[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]))

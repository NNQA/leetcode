class Solution:
    def maxSatisfied(
        self, customers: List[int], grumpy: List[int], minutes: int
    ) -> int:
        base_satisfied = 0
        for i in range(len(customers)):
            if grumpy[i] == 0:
                base_satisfied += customers[i]

        current_extra = 0
        max_extra = 0

        for i in range(len(customers)):
            if grumpy[i] == 1:
                current_extra += customers[i]

            if i >= minutes:
                if grumpy[i - minutes] == 1:
                    current_extra -= customers[i - minutes]

            max_extra = max(max_extra, current_extra)

        return base_satisfied + max_extra


sol = Solution()
print(sol.maxSatisfied([1, 0, 1, 2, 1, 1, 7, 5], [0, 1, 0, 1, 0, 1, 0, 1], 3))

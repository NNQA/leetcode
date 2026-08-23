class Solution:
    def checkDivisibility(self, n: int) -> bool:
        original = n
        digit_sum = 0
        digit_product = 1

        while n > 0:
            digit = n % 10
            digit_sum += digit
            digit_product *= digit
            n = n // 10

        total = digit_product + digit_sum
        return original % total == 0


sol = Solution()
print(sol.checkDivisibility(99))

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:

        if dividend == divisor:
            return 1
        if divisor == 1:
            return dividend
        if dividend == -1:
            return -dividend
        negative = (dividend < 0) ^ (divisor < 0)
        quotient = 0
        dividend, divisor = abs(dividend), abs(divisor)

        while dividend >= divisor:
            temp_divisor, multiple = divisor, 1

            while dividend >= (temp_divisor << 1):
                temp_divisor <<= 1
                multiple <<= 1
            dividend -= temp_divisor
            quotient += multiple
        if negative:
            quotient = -quotient
        return max(min(quotient, 2**31 - 1), -(2**31))


sol = Solution()
print(sol.divide(100, 3))

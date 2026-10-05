from decimal import Decimal


class Solution:
    def myPow(self, x: float, n: int) -> float:

        if n < 0:
            n = -n
            x = Decimal(1) / Decimal(str(x))
        else:
            x = Decimal(str(x))
        ans = Decimal(1)
        while n > 0:
            if n % 2 == 1:
                ans *= x
            x *= x
            n //= 2

        return float(ans)


print(Solution().myPow(2.000, 11))

class Solution:
    def maxProfitTwoPointer(self, prices: List[int]) -> int:

        left = 0
        right = 1
        ans = 0
        while right < len(prices):
            if prices[right] > prices[left]:
                ans = max(ans, prices[right] - prices[left])
            else:
                left = right
            right += 1
        return ans

    def maxProfitTwoDP(self, prices: List[int]) -> int:

        min_prices = prices[0]
        max_prices = 0
        for sell in prices:
            max_prices = max(max_prices, sell - min_prices)
            min_prices = min(min_prices, sell)
        return max_prices


sol = Solution()
print(sol.maxProfitTwoDP([7, 6, 4, 3, 1]))
print(sol.maxProfitTwoDP([7, 1, 5, 3, 6, 4]))
print(sol.maxProfitTwoDP([2, 1, 4]))

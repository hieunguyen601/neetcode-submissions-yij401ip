class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        max_value = 0
        for right in range(1, len(prices)):
            profit = prices[right] - prices[left]
            if profit > 0:
                max_value = max(max_value, profit)
            else:
                left = right
        return max_value
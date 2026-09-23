class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        running_count = 0
        max_count = 0

        for r in range(len(prices)):
            if prices[l] > prices[r]:
                l = r
            running_count = prices[r] - prices[l]
            max_count = max(running_count, max_count)
        return max_count
class Solution:
    def maxProfit(self, prices):
        if prices == sorted(prices, reverse=True):
            return 0
        max_profit, min_price = 0, 1000001
        for i in range(len(prices)):
            min_price = prices[i] if min_price>prices[i] else min_price
            max_profit = prices[i] - min_price if max_profit < prices[i] - min_price else max_profit
        return max_profit


if __name__ == '__main__':
    sol = Solution()
    print(sol.maxProfit([7, 1, 5, 3, 6, 4]))

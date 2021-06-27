def maxProfit(prices) -> int:
    start, end = 0, len(prices)
    min_left, max_profit = prices[0], 0
    for i in range(end):
        max_profit = max(max_profit, prices[i] - min_left)
        min_left = min(min_left, prices[i])
    return max_profit


if __name__ == '__main__':
    print(maxProfit([7, 1, 5, 3, 6, 4]))
    print(maxProfit([7, 6, 4, 3, 1]))

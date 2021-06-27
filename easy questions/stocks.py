def maxProfit(prices) -> int:
    valley = 0
    peak = 0
    profit = 0
    while (valley < len(prices) and peak < len(prices)):
        while (peak < len(prices) - 1 and prices[peak] < prices[peak + 1]):
            peak += 1
        profit = profit + prices[peak] - prices[valley]
        valley = peak + 1
        peak += 1
    return profit


if __name__ == '__main__':
    prices = [7, 1, 5, 3, 6, 4]
    print(maxProfit(prices))

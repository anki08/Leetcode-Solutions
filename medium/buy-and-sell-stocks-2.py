def maxProfit(prices) -> int:
    max_profit = 0
    hill, valley = -1, -1
    if (len(prices) <= 1):
        return 0
    for i in range(len(prices)):
        if ((i == 0 and prices[i + 1] > prices[i]) or (
                i < len(prices) - 1 and prices[i - 1] >= prices[i] < prices[i + 1])):
            valley = prices[i]
        elif (i == len(prices) - 1 or (i > 0 and prices[i - 1] < prices[i] >= prices[i + 1])):
            hill = prices[i]
        if (hill > -1 and valley > -1):
            max_profit += abs(hill - valley)
            hill, valley = -1, -1
    return max_profit


if __name__ == '__main__':
    # print(maxProfit([7,1,5,3,6,4]))
    # print(maxProfit([1,2,3,4,5]))
    # print(maxProfit([2,2,5]))
    print(maxProfit([2, 1, 2, 0, 1]))

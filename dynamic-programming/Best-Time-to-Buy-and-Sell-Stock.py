def maxProfit(prices) -> int:
    max_profit, min_value = 0, 10000000
    for i in  range(len(prices)):
        min_value = min(min_value, prices[i])
        max_profit = max(max_profit, prices[i]-min_value)

    return max_profit

if __name__ == '__main__':
    print(maxProfit([7,1,5,3,6,4]))
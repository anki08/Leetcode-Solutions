items = [2, 3, 1, 2, 4, 2]

def finalPrice(prices):
    stack = []
    res = 0
    for i in range(len(prices)):
        while stack and prices[i] <= prices[stack[-1]]:
            priceI = stack.pop()
            res += prices[priceI] - prices[i]
        stack.append(i)
    res += sum(prices[i] for i in stack)
    return stack, res

print(finalPrice([2, 3, 1, 2, 4, 2]))
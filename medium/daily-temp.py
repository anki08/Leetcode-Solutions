def dailyTemperatures(temperatures):
    stack = []
    res = [0] * len(temperatures)
    for x in range(len(temperatures) - 1, -1, -1):
        while (stack and stack[-1][0] <= temperatures[x]):
            stack.pop()
        if stack:
            res[x] = stack[-1][1] - x
        stack.append((temperatures[x], x))
    return res


if __name__ == '__main__':
    temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
    # temperatures = [73]
    print(dailyTemperatures(temperatures))

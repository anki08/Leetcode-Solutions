def trap(height):
    units, max_left, max_right = 0, 0, 0

    for i in range(1, len(height) - 1):
        max_left = max(height[0:i])
        max_right = max(height[i + 1:])
        sum = min(max_left, max_right) - height[i]
        units += sum if sum > 0 else 0

    return units


def trap_dp(height):
    if (len(height) == 0):
        return 0

    left_max = [height[0]]
    for i in range(1, len(height)):
        left_max.append(max(height[:i]))

    right_max = []
    for i in range(len(height) - 1):
        right_max.append(max(height[i + 1:]))
    right_max.append(height[-1])

    units = 0
    for i in range(len(height)):
        sum = min(left_max[i], right_max[i]) - height[i]
        units += sum if sum > 0 else 0
    return units


if __name__ == '__main__':
    print(trap_dp([4, 2, 0, 3, 2, 5]))
    # print(trap([3,2,1,2,1]))
    print(trap_dp([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
    print(trap_dp([4, 2, 3]))

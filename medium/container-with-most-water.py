def maxArea(height) -> int:
    max_area = 0
    start, end = 0, len(height) - 1
    while start < end:
        max_area = max(max_area, (end - start) * min(height[start], height[end]))
        if (height[start] < height[end]):
            start += 1
        else:
            end -= 1
    return max_area


if __name__ == '__main__':
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print(maxArea(height))

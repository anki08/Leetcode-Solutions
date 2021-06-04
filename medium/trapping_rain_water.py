def trap(height):
    units, max_left, max_right = 0, 0, 0

    for i in range(1, len(height)-1):
        max_left = max(height[0:i])
        max_right = max(height[i+1:])
        sum = min(max_left, max_right) - height[i]
        units += sum if sum>0 else 0


    return units



if __name__ == '__main__':
    print(trap([4,2,0,3,2,5]))
    # print(trap([3,2,1,2,1]))
    print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))
    print(trap([4,2,3]))


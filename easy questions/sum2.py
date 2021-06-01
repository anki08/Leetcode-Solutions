def twoSum( numbers, target):
    # numbers = [x for x in numbers if x <= target]
    hash = {}
    res = []
    for i in range(len(numbers)):
        no = target-numbers[i]
        if no in hash:
            res.append(hash[no]+1)
            res.append(i+1)
        else:
            hash[numbers[i]] = i

    return res

if __name__ == '__main__':
    print(twoSum([-1,0], -1))
    print(twoSum([2,3,4], 6))
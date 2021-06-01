def removeDuplicates(nums) -> int:
    i = 0  # slow-run pointer
    for j in range(1, len(nums)):
        if nums[j] == nums[i]:
            continue
            # capture the result
        i += 1
        if i != j:
            nums[i] = nums[j]

if __name__ == '__main__':
    print(removeDuplicates([1,1,2]))
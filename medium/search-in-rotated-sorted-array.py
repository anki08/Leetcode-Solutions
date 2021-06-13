def search(nums, target: int) -> int:
    start = 0
    end = len(nums)-1
    while start <= end:
        pivot = start + (end-start)//2
        if(nums[pivot] == target):
            return pivot
        if nums[start] <= nums[pivot]:
            if (nums[start] <= target < nums[pivot]):
                end = pivot-1
            else:
                start = pivot+1
        else:
            if (nums[pivot] < target<=nums[end]):
                start = pivot+1
            else:
                end = pivot-1
    return -1


if __name__ == '__main__':
    print(search([0,1,2,3,4,5,6,7], 0))
    print(search([7,0,1,2,3,4,5,6], 0))
    print(search([6,7,0,1,2,3,4,5], 0))
    print(search([5,6,7,0,1,2,3,4], 0))
    print(search([4,5,6,7,0,1,2,3], 0))
    print(search([3,4,5,6,7,0,1,2], 0))
    print(search([2,3,4,5,6,7,0,1], 0))
    print(search([1,2,3,4,5,6,7,0], 0))
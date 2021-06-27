import heapq


def findKthLargest(nums, k: int) -> int:
    max_heap = heapq.nlargest(k, nums)[-1]
    print(max_heap)


if __name__ == '__main__':
    findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4)

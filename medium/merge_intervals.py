def merge(intervals):
    intervals = sorted(intervals, key=lambda x: x[0])
    res = []
    for i in range(len(intervals)):
        if (len(res) == 0 or intervals[i][0] > res[-1][1]):
            res.append(intervals[i])
        else:
            start = min(intervals[i][0] , res[-1][0])
            end = max(intervals[i][1] , res[-1][1])
            res[-1] = [start, end]
    return res

if __name__ == '__main__':
    print(merge([[1,5],[2,4],[3,6],[4,8], [5,10], [11,12]])) # [1,10][11,12]
    print(merge([[1,3],[2,6],[8,10],[15,18]])) #[1,6], [8,10], [15, 18]
    print(merge([[1,4],[2,3]])) #[1,4]
    print(merge([[1,4],[4,5]])) #[1,5]
    print(merge([[1,10], [2,3],[4,5],[6,7],[8,9]])) #[1,10]


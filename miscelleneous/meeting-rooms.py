import heapq

class Solution:
    def minMeetingRooms(self, intervals):
        count = 1
        intervals = sorted(intervals, key = lambda x:x[0])
        priority_heap = []
        heapq.heappush(priority_heap, intervals[0][1])
        for i in range(1, len(intervals)):
            temp = heapq.heappop(priority_heap)
            if (temp <= intervals[i][0]):
                heapq.heappush(priority_heap, intervals[i][1])
            else:
                count +=1
                heapq.heappush(priority_heap, intervals[i][1])
                heapq.heappush(priority_heap, temp)
        return count


if __name__ == '__main__':
    sol = Solution()
    # print(sol.minMeetingRooms([[0,30],[5,10],[15,20]]))
    # print(sol.minMeetingRooms([[1,10],[2,7],[3,19], [8,12], [10,20], [11,30]]))
    print(sol.minMeetingRooms([[13,15],[1,13]]))
import heapq
class Solution:
    def minMeetingRooms(self, intervals):
        intervals = sorted(intervals,key=lambda x:x[0])
        free_rooms = []
        heapq.heappush(free_rooms, intervals[0][1])
        for interval in intervals[1:]:
            if interval[0] > free_rooms[0]:
                heapq.heappushpop(free_rooms, interval[1])
            else:
                heapq.heappush(free_rooms, interval[1])
        return len(free_rooms)




if __name__ == '__main__':
    sol  = Solution()
    print(sol.minMeetingRooms( intervals = [[0,30],[5,10],[15,20]]))
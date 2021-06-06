import heapq
def minMeetingRooms(intervals):
    if(len(intervals) == 1):
        return 1

    #intervals array is sorted by start time
    intervals = sorted(intervals, key = lambda x : x[0])
    meet_room = []
    #heapq is sorted by endtime
    heapq.heappush(meet_room, intervals[0][1])
    for i in range(1, len(intervals)):
        # min_el = heapq.heappop(meet_room)
        if(meet_room[0] <= intervals[i][0]):
            heapq.heappop(meet_room)

        heapq.heappush(meet_room, intervals[i][1])


    return len(meet_room)






if __name__ == '__main__':
    print(minMeetingRooms(intervals=[[0,30],[5,10],[15,20]]))
    print(minMeetingRooms(intervals=[[7,10],[2,4]]))
    print(minMeetingRooms(intervals=[[1,5],[8,9],[8,9]]))
    print(minMeetingRooms(intervals=[[9,14],[5,6],[3,5],[12,19]]))
    print(minMeetingRooms(intervals=[[15,16],[10,15],[16,25]]))


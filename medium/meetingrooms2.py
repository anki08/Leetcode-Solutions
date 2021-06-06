def minMeetingRooms(intervals):
    if(len(intervals) == 1):
        return 1
    count = 1
    intervals = sorted(intervals, key = lambda x : x[0])
    # res = []
    i = 1
    while(i < len(intervals)):
        alloc = False
        for k in intervals[:i]:
            if(intervals[i][0]>= k[1]):
                alloc = True
                k[1] = intervals[i][1]
                intervals.remove(intervals[i])
                i -=1
                break
        i+=1
        if(alloc == False):
            count += 1
    return count






if __name__ == '__main__':
    print(minMeetingRooms(intervals=[[0,30],[5,10],[15,20]]))
    print(minMeetingRooms(intervals=[[7,10],[2,4]]))
    print(minMeetingRooms(intervals=[[1,5],[8,9],[8,9]]))
    print(minMeetingRooms(intervals=[[9,14],[5,6],[3,5],[12,19]]))
    print(minMeetingRooms(intervals=[[15,16],[10,15],[16,25]]))


class Solution:
    def isRobotBounded(self, instructions):
        directions_offset = [(0,1), (1,0),(0,-1),(-1,0)]
        x = y = 0
        idx = 0

        for i in instructions:
            if i == 'L':
                idx = (idx + 3)%4
            if i == 'R':
                idx = (idx + 1) % 4
            if i == 'G':
                x += directions_offset[idx][0]
                y += directions_offset[idx][1]
        return (x==0 and y==0) or idx!= 0

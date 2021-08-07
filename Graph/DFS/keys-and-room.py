import numpy as np
def canVisitAllRooms(rooms) -> bool:
    R = len(rooms)
    visited = np.full(R, False)

    def dfs(rooms, visited, room):
        if(len(rooms) ==0  or room<0 or room>len(rooms)-1 or visited[room] == True):
            return

        if len(rooms) >0  and room>0 and room<len(rooms) and visited[room]!= True:
            visited[room] = True
        for i in rooms[room]:
            dfs(rooms, visited, i)

    for i in rooms[0]:
        dfs(rooms, visited, i)
    print(visited[1:])
    return False if False in visited[1:] else  True


if __name__ == '__main__':
    print(canVisitAllRooms([[1],[2],[3],[]]))
    print(canVisitAllRooms([[1,3],[3,0,1],[2],[0]]))
from collections import deque
def minKnightMoves(x: int, y: int) -> int:
    offsets = [(2,1),(2,-1),(-2,1),(-2,-1), (-1,2),(1,2),(1,-2), (-1,-2)]

    def bfs():
        queue = deque([(0,0)])
        count = 0
        visited = set()
        while(len(queue)>0):
            count+=1
            for i in range(len(queue)):
                rcurr, ccurr = queue.popleft()
                if((rcurr, ccurr) == (x,y)):
                    return count
                for roffset, coffset in offsets:
                    if (rcurr+roffset, ccurr+coffset) not in visited:
                        visited.add((rcurr+roffset, ccurr+coffset))
                        queue.append((rcurr+roffset, ccurr+coffset))

    return bfs()

if __name__ == '__main__':
    print(minKnightMoves(x = 5, y = 5))
import collections
def eventualSafeNodes(graph):
    WHITE, GRAY, BLACK = 0,1,2
    color = collections.defaultdict(int)

    def dfs(node):
        if(color[node] != WHITE):
            return color[node] == BLACK

        color[node] = GRAY
        for i in graph[node]:
            if(color[i] == BLACK):
                continue
            elif(color[i] == GRAY or not dfs(i)):
                return False

        color[node] = BLACK
        return  True

    for i in range(len(graph)):
        dfs(i)
    return [i for i in range(len(graph)) if color[i] == 2]



if __name__ == '__main__':
    print(eventualSafeNodes([[1,2],[2,3],[5],[0],[5],[],[]]))
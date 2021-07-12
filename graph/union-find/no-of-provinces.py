import numpy as np
def findCircleNum(isConnected) -> int:
    n = len(isConnected)
    parent = {x:x for x in range(n)}
    print(parent)

    def find(node):
        if (parent[node] == node):
            return node
        root = find(parent[node])
        parent[node] = root
        return root

    def union(node1, node2):
        if find(node1) == find(node2):
            return
        parent[find(node1)] = find(node2)

    for i in range(n):
        for j in range(i,n):
            if(i!=j and isConnected[i][j] == 1):
                union(i,j)
    print(parent)
    return sum(1 for k,v in parent.items() if k==v)



if __name__ == '__main__':
    print(findCircleNum(isConnected = [[1,1,0],[1,1,0],[0,0,1]]))
class Solution:
    def findCircleNum(self, isConnected):
        parent = {x:x  for x in range(len(isConnected))}
        def find(node):
            if parent[node] == node:
                return node
            parent[node] = find(parent[node])
            return parent[node]

        def union(x,y):
            if find(x) == find(y):
                return
            parent[find(x)] = find(y)

        for i in range(len(isConnected)):
            for j in range(i+1, len(isConnected)):
                if isConnected[i][j] == 1:
                    union(i,j)

        print(parent)
        return sum(1 for k, v in parent.items() if k == v)



if __name__ == '__main__':
    sol = Solution()
    print(sol.findCircleNum( [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
    print(sol.findCircleNum(  [[1,0,0],[0,1,0],[0,0,1]]))
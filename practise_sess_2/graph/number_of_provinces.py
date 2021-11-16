class Solution:
    def findCircleNum(self, isConnected):
        n = len(isConnected)
        parent = {x:x for x in range(n)}
        count = 0
        def find(node):
            if parent[node] == node:
                return node
            parent[node] = find(parent[node])
            return parent[node]

        def union(node1, node2):
            if find(node1) == find(node2):
                return
            parent[find(node1)] = find(node2)

        for i in range(n):
            for j in range(i, n):
                if i != j and isConnected[i][j] == 1:
                    union(i, j)

        print(parent)
        for x,y in parent.items():
            if x == y:
                count += 1
        return count

if __name__ == '__main__':
    sol = Solution()
    print(sol.findCircleNum(isConnected = [[1,1,0],[1,1,0],[0,0,1]]))
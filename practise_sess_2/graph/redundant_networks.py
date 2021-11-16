class Solution:
    def findRedundantConnection(self, edges):
        n = len(edges)
        parent = {x:x for x in range(1, n+1)}
        def find(node):
            if node == parent[node]:
                return parent[node]
            parent[node] = find(parent[node])
            return parent[node]
        ans = []
        for x,y in edges:
            if find(x) == find(y):
                ans.append((x,y))
            else:
                parent[find(x)] = find(y)
        print(parent)
        return (ans)


if __name__ == '__main__':
    sol = Solution()
    sol.findRedundantConnection(edges = [[1,2],[1,3],[2,3]])
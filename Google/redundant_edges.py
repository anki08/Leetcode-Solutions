class Solution:
    def findRedundantConnection(self, edges):
        parent = {x:x for x in range(len(edges)+1)}
        def find(node):
            if parent[node]==node:
                return node
            parent[node] = find(parent[node])
            return parent[node]
        ans = []
        for i in range(len(edges)):
            x, y = edges[i]
            if find(x) != find(y):
                parent[find(x)] = find(y)
            else:
                ans.append([x,y])

        return ans


if __name__ == '__main__':
    sol = Solution()
    print(sol.findRedundantConnection([[1,2],[1,3],[2,3]]))
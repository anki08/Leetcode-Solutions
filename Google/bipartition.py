class Solution:
    def possibleBipartition(self, n: int, dislikes):
        parent = {x+1:x+1 for x in range(n)}
        def find(node):
            if parent[node] == node:
                return node
            parent[node] = find(parent[node])
            return parent[node]

        for p1,p2 in dislikes:
            x = find(p1)
            y = find(p2)
            if x != y:
                parent[x] = y

        print(parent)


if __name__ == '__main__':
    sol = Solution()
    print(sol.possibleBipartition(n = 4, dislikes = [[1,2],[1,3],[2,4]]))

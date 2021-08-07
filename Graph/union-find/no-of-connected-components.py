def countComponents(n, edges) -> int:
    parent = {x:x for x in range(n)}

    def find(node):
        if(parent[node] == node):
            return node
        parent[node] = find(parent[node])
        return node

    for i,j in edges:
        x = find(i)
        y = find(j)
        if(x != y):
            parent[x] = y

    print(parent)
    count  = sum([1 for x, y in parent.items() if x == y])
    print(count)

if __name__ == '__main__':
    countComponents(n = 5, edges = [[0,1],[1,2],[3,4]])
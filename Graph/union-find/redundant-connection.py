def findRedundantConnection(edges):

    def find(node):
        if(parent[node] == node):
            return node
        root = find(parent[node])
        parent[node] = root
        return root
    # edges = sorted(edges, key= lambda x:x[0])
    parent = {x:x for x in range(len(edges)+1)}
    ans = []
    for i in edges:
        x = i[0]
        y = i[1]
        if find(x)!= find(y):
            parent[find(y)] = find(x)
        else:
            ans.append(x)
            ans.append(y)
    return ans



if __name__ == '__main__':
    # print(findRedundantConnection([[1,2],[1,3],[2,3]]))
    print(findRedundantConnection([[1,4],[3,4],[1,3],[1,2],[4,5]]))
    print(findRedundantConnection([[1,2],[1,3],[2,3]]))
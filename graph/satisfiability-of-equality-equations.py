def equationsPossible(equations) -> bool:
    set1 = {x[0] for x in equations}
    set2 = {x[3] for x in equations}
    final = set1.union(set2)
    parent = {x:x for x in final}

    def find(node):
        if parent[node] == node:
            return node
        root = find(parent[node])
        parent[node] = root
        return root

    for i in range(len(equations)):
        x = find(equations[i][0])
        y = find(equations[i][3])
        sign = equations[i][1]
        if(sign == "="):
            parent[y] = x

    print(parent)
    return not any(e == "!" and find(a) == find(b) for a, e, _, b in equations)


if __name__ == '__main__':
    print(equationsPossible(["a==b","b!=a"]))
    print(equationsPossible(["b==a","a==b"]))
    print(equationsPossible(["a==b","b==c","a==c"]))
    print(equationsPossible(["a==b","b!=c","c==a"]))
    print(equationsPossible(["c==c","b==d","x!=z"]))
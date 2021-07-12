def removeStones(stones) -> int:
    uf = {}

    def find(x):
        if x != uf.setdefault(x, x):
            uf[x] = find(uf[x])
        return uf[x]

    for i, j in stones:
        uf[find(i)] = find(~j)
    return len(stones) - len({find(x) for x in uf})


if __name__ == '__main__':
    print(removeStones([[0, 0], [0, 1], [1, 0], [1, 2], [2, 1], [2, 2]]))

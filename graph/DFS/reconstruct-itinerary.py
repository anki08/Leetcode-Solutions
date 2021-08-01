from collections import defaultdict


def findItinerary(tickets):
    graph1 = defaultdict(list)
    visitedMap = defaultdict(list)

    for i in tickets:
        graph1[i[0]].append(i[1])
        visitedMap[i[0]].append(False)

    graph = defaultdict(list)
    for key, values in graph1.items():
        values = sorted(values)
        graph[key].extend(values)
    res = []

    print(graph)
    print(visitedMap)
    def dfs(graph, node):
        if (len(res) == len(tickets) + 1):
            print(len(res))
            return True
        res.append(node)
        for index, val in enumerate(graph[node]):
            if(visitedMap[node][index] == False):
                visitedMap[node][index] = True
                dfs(graph, val)

    dfs(graph, "JFK")
    return (res)


if __name__ == '__main__':
    # findItinerary([["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]])
    findItinerary([["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]])

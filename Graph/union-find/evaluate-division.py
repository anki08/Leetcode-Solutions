def calcEquation(equations, values, queries):
    gid_weight = {}
    def find(node):
        if node not in gid_weight:
            gid_weight[node] = (node, 1)

        group_id, node_weight = gid_weight[node]

        if group_id != node:
            new_group_id, new_group_weight = find(group_id)
            gid_weight[node] = (new_group_id, node_weight * new_group_weight)
        return gid_weight[node]

    def union(dividend, divisor, quotient):
        dividend_group_id, dividend_weight = find(dividend)
        divisor_group_id, divisor_weight = find(divisor)
        if(dividend_group_id != divisor_group_id):
            gid_weight[dividend_group_id] = (divisor_group_id,  divisor_weight * quotient/ dividend_weight)

    for (dividend, divisor), quotient in zip(equations, values):
        union(dividend, divisor, quotient)
    res = []
    for dividend, divisor in queries:
        if dividend not in gid_weight or divisor not in gid_weight:
            res.append(-1.0)
        else:
            dividend_group_id, dividend_weight = find(dividend)
            divisor_group_id, divisor_weight = find(divisor)
            if(divisor_group_id !=  dividend_group_id):
                res.append(-1.0)
            else:
                res.append(dividend_weight/divisor_weight)
    return res



if __name__ == '__main__':
    # print(calcEquation(equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]))
    # print(calcEquation( equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]))
    print(calcEquation( [["a","b"],["e","f"],["b","e"]], [3.4,1.4,2.3],[["b","a"],["a","f"],["f","f"],["e","e"],["c","c"],["a","c"],["f","e"]]))
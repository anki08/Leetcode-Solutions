from collections import defaultdict
def accountsMerge(accounts):
    parents = {}
    emails_to_name = {}
    def find(node):
        if parents[node] == node:
            return node
        parents[node] = find(parents[node])
        return parents[node]

    def union(node1, node2):
        parents[find(node1)] = find(node2)

    for entry in accounts:
        name = entry[0]
        for email in entry[1:]:
            if email not in parents:
                parents[email] = email
            emails_to_name[email] = name
            union(email, entry[1])
    print("email  to name", emails_to_name)
    print("parents", parents)

    trees = defaultdict(list)
    for email in parents.keys():
        trees[find(email)].append(email)
    print("trees", trees)
    return [[emails_to_name[root]] + sorted(emails) for (root, emails) in trees.items()]



if __name__ == '__main__':
    accountsMerge([["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]])
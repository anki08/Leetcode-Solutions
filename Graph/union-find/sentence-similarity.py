def areSentencesSimilarTwo(sentence1,sentence2, similarPairs) -> bool:
    if(len(sentence1) != len(sentence2)):
        return False
    set1 = {x[0] for x in similarPairs}
    set2 = {x[1] for x in similarPairs}
    final = set1.union(set2)
    parent = {x: x for x in final}

    def find(node):
        if (parent[node] == node):
            return node
        parent[node] = find(parent[node])
        return parent[node]

    for i in range(len(similarPairs)):
        # print(similarPairs[i])
        x = find(similarPairs[i][0])
        y = find(similarPairs[i][1])
        if(x!=y):
            parent[x] = y

    for i in range(len(sentence1)):
        if(sentence1[i] != sentence2[i]):
            if(sentence1[i] not in parent or sentence2[i] not in parent or find(sentence1[i])!= find(sentence2[i])):
                return False
    return True
    # print(parent)

if __name__ == '__main__':
    print(areSentencesSimilarTwo(sentence1 = ["great","acting","skills"], sentence2 = ["fine","drama","talent"], similarPairs = [["great","good"],["fine","good"],["drama","acting"],["skills","talent"]]))
    print(areSentencesSimilarTwo(sentence1 = ["I","love","leetcode"], sentence2 = ["I","love","onepiece"], similarPairs = [["manga","onepiece"],["platform","anime"],["leetcode","platform"],["anime","manga"]]))
    print(areSentencesSimilarTwo(sentence1 = ["I","love","leetcode"], sentence2 = ["I","love","onepiece"], similarPairs = [["manga","hunterXhunter"],["platform","anime"],["leetcode","platform"],["anime","manga"]]))
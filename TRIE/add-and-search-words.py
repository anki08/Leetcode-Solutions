class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}

    def addWord(self, word: str) -> None:
        node = self.trie
        for ch in word:
            if not ch in node:
                node[ch] = {}
            else:
                node = node[ch]
        node['$'] = True

    def search(self, word: str) -> bool:

        def search_util(word, node):
            for i, ch in enumerate(word):
                if ch not in node:
                    if ch == '.':
                        for x in node:
                            if x!='$' and search_util(word[i+1:], node[x]):
                                return True
                    return False
                else:
                    node = node[ch]
            return '$' in node

        return search_util(word, self.trie)



if __name__ == '__main__':
    obj = WordDictionary()
    obj.addWord("bad")
    obj.addWord("dad")
    obj.addWord("mad")
    print(obj.search("pad"))
    print(obj.search("bad"))
    print(obj.search(".ad"))
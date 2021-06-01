import collections

_end = '_end_'
def make_trie(words):
    root = dict()
    for word in words:
        current_dict = root
        for letter in word:
            current_dict = current_dict.setdefault(letter, {})
    current_dict[_end] = _end
    return root


def longestWord(words):
    Trie = lambda: collections.defaultdict(Trie)
    trie = Trie()
    END = True
    trie = make_trie(words)
    print(trie)

    # for i, word in enumerate(words):
    #     reduce(dict.__getitem__, word, trie)[END] = i

    stack = trie.values()
    ans = ""
    while stack:
        cur = stack.pop()
        if END in cur:
            word = words[cur[END]]
            if len(word) > len(ans) or len(word) == len(ans) and word < ans:
                ans = word
            stack.extend([cur[letter] for letter in cur if letter != END])

    return ans

# print(make_trie('foo', 'bar', 'baz', 'barz'))
if __name__ == '__main__':
    print(longestWord(words=["a","banana","app","appl","ap","apply","apple"]))

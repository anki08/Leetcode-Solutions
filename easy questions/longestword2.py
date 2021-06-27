import collections
from functools import reduce


def longestWord(words):
    Trie = lambda: collections.defaultdict(Trie)
    trie = Trie()
    END = True

    for i, word in enumerate(words):
        reduce(dict.__getitem__, word, trie)[END] = i

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


if __name__ == '__main__':
    words = ["k", "lg", "it", "oidd", "oid", "oiddm", "kfk", "y", "mw", "kf", "l", "o", "mwaqz", "oi", "ych", "m",
             "mwa"]
    print(longestWord(words))

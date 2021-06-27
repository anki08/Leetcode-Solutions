from collections import defaultdict


def longestStrChain(words) -> int:
    dp = defaultdict(int)
    words = sorted(words, key=lambda x: len(x))
    wordset = set(words)
    for word in words:
        max_length = 1
        for i in range(len(word)):
            new_word = word[:i] + word[i + 1:]
            if (new_word in wordset and new_word in dp):
                max_length = max(max_length, dp[new_word] + 1)
        dp[word] = max_length
    return max(dp.values())
    # print(dp)


if __name__ == '__main__':
    words = ["a", "b", "ba", "bca", "bda", "bdca"]
    print(longestStrChain(words))
    print(longestStrChain(["xbc", "pcxbcf", "xb", "cxbc", "pcxbc"]))
    print(longestStrChain(["abcd", "dbqca"]))

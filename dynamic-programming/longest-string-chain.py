def longestStrChain(words) -> int:
    wordset = set(words)
    wordhash = {}
    ans = 0
    for word in words:
        ans = max(ans, dfs(wordset, wordhash, word))
    return ans

def dfs(wordset, wordhash, word):
    max_length = 1
    if word in wordhash:
        return wordhash[word]

    for i in range(len(word)):
        new_word = word[:i] + word[i+1:]
        if(new_word in wordset):
            current_length = 1 + dfs(wordset, wordhash, new_word)
            max_length = max(max_length, current_length)

    wordhash[word] = max_length
    print(wordhash)
    return max_length


if __name__ == '__main__':
    print(longestStrChain(["a","b","ba","bca","bda","bdca"]))
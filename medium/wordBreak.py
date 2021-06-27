def wordBreak(s, wordDict) -> bool:
    def wordBreakUtil(s, wordDict, start):
        if (start == len(s)):
            return True
        for end in range(start + 1, len(s) + 1):
            if (s[start:end] in wordDict and wordBreakUtil(s, wordDict, end)):
                return True
        return False

    return wordBreakUtil(s, wordDict, 0)


if __name__ == '__main__':
    print(wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))
    print(wordBreak(s="leetcode", wordDict=["leet", "code"]))
    print(wordBreak(s="applepenapple", wordDict=["apple", "pen"]))

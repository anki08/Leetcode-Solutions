from collections import deque
import numpy as np
def wordBreak_bfs(s, wordDict) -> bool:
    word_set = set(wordDict)
    q = deque()
    visited = set()
    q.append(0)
    while q:
        start = q.popleft()
        if(start in visited):
            continue
        for end in range(start+1, len(s)+1):
            if(s[start:end] in word_set):
                q.append(start)
                if(end == len(s)):
                    return True
        visited.add(start)
    return False

def wordBreak_dp(s, wordDict) -> bool:
    dp = np.zeros(len(s)+1)
    dp[0] = True
    word_set = set(wordDict)
    for i in range(1, len(s)):
        for j in range(i):
            if(dp[j] == 1 and s[j:i] in word_set):
                dp[i] = True
                break
    if(dp[-1] == 0):
        return False
    return True


if __name__ == '__main__':
    print(wordBreak_bfs(s = "leetcode", wordDict = ["leet","code"]))
    print(wordBreak_dp(s = "leetcode", wordDict = ["leet","code"]))
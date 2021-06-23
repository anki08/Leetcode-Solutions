import numpy as np
def removeDuplicates(s: str, k: int) -> str:
    i = 0
    count = np.zeros(len(s))
    while (i < len(s)):
        if(i == 0 or s[i-1] != s[i]):
            count[i]  = 1
        else:
            count[i] = count[i-1] + 1
            if(count[i] == k):
                s = s[:i-k+1] + s[i+1:]
                i = i-k
        i +=1
    return s

def removeDuplicatesStack(s: str, k: int) -> str:
    stack = []
    i = 0
    while (i < len(s)):
        if (i == 0 or s[i - 1] != s[i]):
            stack.append(1)
        else:
            count = stack.pop()+1
            if(count == k):
                s = s[:i - k + 1] + s[i + 1:]
                i = i - k
            else:
                stack.append(count)
        i += 1
    return s

def removeDuplicatesTwoPointers(s:str, k:int):
    stack = []
    i, j = 0, 0
    res = np.zeros(len(s), dtype=str)
    while (i < len(s)):
        res[j] = s[i]
        if (j == 0 or res[j - 1] != res[j]):
            stack.append(1)
        else:
            count = stack.pop() + 1
            if (count == k):
                # s = s[:i - k + 1] + s[i + 1:]
                j = j - k
            else:
                stack.append(count)
        i += 1
        j += 1
    return "".join(res[:j])

if __name__ == '__main__':
    s = "deeedbbcccbdaa"
    k = 3
    print(removeDuplicatesTwoPointers(s, k))
